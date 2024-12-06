# DJ CRM - Modern Django Customer Relationship Management System

A powerful, modern, and user-friendly CRM system built with Django, featuring a beautiful dark theme UI and comprehensive agent management capabilities.

## 🌟 Features

### Agent Management
- Comprehensive agent dashboard with real-time statistics
- Detailed agent profiles with performance metrics
- Lead tracking and conversion monitoring
- 30-day activity timelines
- Conversion rate analytics

### Lead Management
- Active and converted lead tracking
- Lead assignment to agents
- Lead status monitoring
- Detailed lead information display
- Lead conversion tracking

### User Interface
- Modern, responsive dark theme design
- Mobile-first approach
- Interactive navigation with dropdown menus
- Real-time statistics and updates
- Beautiful gradient accents

### Security
- Role-based access control
- Secure authentication system
- Organizer-specific features
- Protected agent management

## 🚀 Technology Stack

### Backend
- Python 3.13.0
- Django 4.2.7
- PostgreSQL (recommended)

### Frontend
- Tailwind CSS
- Alpine.js
- HTML5
- Modern JavaScript

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/dj-crm.git
cd dj-crm
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your database and email settings
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

## 🔧 Configuration

### Required Settings
- Database configuration in settings.py
- Email settings for agent invitations
- Static files configuration
- Media files setup

### Optional Settings
- Custom email templates
- Lead status customization
- Agent role permissions
- Activity tracking duration

## 👥 User Roles

### Organizer
- Full system access
- Agent management
- Lead assignment
- Performance monitoring
- System configuration

### Agent
- Lead management
- Lead conversion
- Profile management
- Activity tracking

## 📊 Features in Detail

### Agent Dashboard
- Total leads count
- Active leads tracking
- Conversion rates
- Recent activity timeline
- Performance metrics

### Lead Management
- Lead creation and assignment
- Status tracking
- Conversion monitoring
- Contact information
- Activity history

### Performance Analytics
- Conversion rates
- 30-day performance metrics
- Lead status distribution
- Agent productivity tracking

## 🎨 UI/UX Features

### Dark Theme
- Professional dark color scheme
- Gradient accents
- High contrast text
- Accessible design

### Responsive Design
- Mobile-first approach
- Tablet optimization
- Desktop enhancement
- Flexible layouts

### Interactive Elements
- Dynamic dropdowns
- Real-time updates
- Smooth transitions
- Intuitive navigation

## 🛠 Development

### Prerequisites
- Python 3.13.0+
- Node.js and npm
- PostgreSQL
- Git

### Development Setup
1. Install development dependencies:
```bash
pip install -r requirements-dev.txt
```

2. Set up pre-commit hooks:
```bash
pre-commit install
```

3. Run tests:
```bash
python manage.py test
```

### Code Style
- Follow PEP 8 guidelines
- Use Black for formatting
- Implement type hints
- Write docstrings

## 📝 Contributing

1. Fork the repository
2. Create your feature branch:
```bash
git checkout -b feature/AmazingFeature
```
3. Commit your changes:
```bash
git commit -m 'Add some AmazingFeature'
```
4. Push to the branch:
```bash
git push origin feature/AmazingFeature
```
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Django community
- Tailwind CSS team
- Alpine.js developers
- All contributors

## 📞 Support

For support, email support@djcrm.com or create an issue in the repository.

## 🔮 Future Enhancements

- Advanced reporting
- API integration
- Mobile application
- Enhanced analytics
- Automated lead scoring
- Integration with external CRM systems
- Enhanced email marketing features
- Advanced search capabilities
