from django.core.mail import send_mail
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from leads.models import Agent, Lead
from .forms import AgentModelForm
from .mixins import OrganisorAndLoginRequiredMixin
from django.db.models import Count, Q, F
import random
from django.utils import timezone
from datetime import timedelta


class AgentListView(OrganisorAndLoginRequiredMixin, generic.ListView):
    template_name = "agents/agent_list.html"
    context_object_name = "agents"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        thirty_days_ago = timezone.now() - timedelta(days=30)
        
        queryset = Agent.objects.filter(organisation=organisation).annotate(
            total_leads=Count('leads'),
            active_leads_count=Count('leads', filter=Q(leads__converted_date__isnull=True)),
            converted_leads_count=Count('leads', filter=Q(leads__converted_date__isnull=False)),
            recent_conversions=Count(
                'leads',
                filter=Q(
                    leads__converted_date__isnull=False,
                    leads__converted_date__gte=thirty_days_ago
                )
            )
        ).order_by('-total_leads')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_agents'] = context['agents'].count()
        context['total_leads'] = sum(agent.total_leads for agent in context['agents'])
        context['total_active_leads'] = sum(agent.active_leads_count for agent in context['agents'])
        return context


class AgentCreateView(OrganisorAndLoginRequiredMixin, generic.CreateView):
    template_name = "agents/agent_form.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents:agent-list")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organisor = False
        user.set_password(f"{random.randint(0, 1000000)}")
        user.save()
        Agent.objects.create(
            user=user,
            organisation=self.request.user.userprofile
        )
        send_mail(
            subject="You are invited to be an agent",
            message="You were added as an agent on DJCRM. Please come login to start working.",
            from_email="admin@test.com",
            recipient_list=[user.email]
        )
        return super(AgentCreateView, self).form_valid(form)


class AgentDetailView(OrganisorAndLoginRequiredMixin, generic.DetailView):
    template_name = "agents/agent_detail.html"
    context_object_name = "agent"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        agent = context['agent']
        thirty_days_ago = timezone.now() - timedelta(days=30)
        
        # Get all leads for this agent
        leads = Lead.objects.filter(agent=agent)
        
        # Active leads
        active_leads = leads.filter(converted_date__isnull=True)
        context['active_leads'] = active_leads.order_by('-date_added')
        
        # Converted leads
        converted_leads = leads.filter(converted_date__isnull=False)
        context['converted_leads'] = converted_leads.order_by('-converted_date')
        
        # Recent activity
        context['recent_leads'] = leads.filter(
            date_added__gte=thirty_days_ago
        ).order_by('-date_added')
        
        context['recent_conversions'] = converted_leads.filter(
            converted_date__gte=thirty_days_ago
        ).order_by('-converted_date')
        
        # Statistics
        context['total_leads'] = leads.count()
        context['active_leads_count'] = active_leads.count()
        context['converted_leads_count'] = converted_leads.count()
        context['conversion_rate'] = (
            (converted_leads.count() / leads.count() * 100)
            if leads.count() > 0 else 0
        )
        context['recent_conversion_rate'] = (
            (context['recent_conversions'].count() / context['recent_leads'].count() * 100)
            if context['recent_leads'].count() > 0 else 0
        )
        
        return context


class AgentUpdateView(OrganisorAndLoginRequiredMixin, generic.UpdateView):
    template_name = "agents/agent_form.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents:agent-list")

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)


class AgentDeleteView(OrganisorAndLoginRequiredMixin, generic.DeleteView):
    template_name = "agents/agent_delete.html"
    context_object_name = "agent"

    def get_success_url(self):
        return reverse("agents:agent-list")

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        agent = context['agent']
        context['active_leads_count'] = Lead.objects.filter(
            agent=agent,
            converted_date__isnull=True
        ).count()
        return context
