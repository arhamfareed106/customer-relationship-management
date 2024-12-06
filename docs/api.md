# DJ CRM API Documentation

## Authentication

All API endpoints require authentication. Use token-based authentication by including the token in the Authorization header:

```
Authorization: Token your-token-here
```

## Agents Endpoints

### List Agents
```
GET /api/agents/
```

Returns a list of all agents with their basic information and performance metrics.

### Agent Detail
```
GET /api/agents/{id}/
```

Returns detailed information about a specific agent, including:
- Personal information
- Lead statistics
- Performance metrics
- Recent activity

### Create Agent
```
POST /api/agents/
```

Create a new agent. Required fields:
- `user`: User ID
- `organization`: Organization ID

### Update Agent
```
PUT /api/agents/{id}/
```

Update an existing agent's information.

### Delete Agent
```
DELETE /api/agents/{id}/
```

Remove an agent from the system.

### Agent Performance
```
GET /api/agents/{id}/performance/
```

Returns performance metrics for the specified agent:
- Total leads
- Active leads
- Converted leads
- Conversion rate
- 30-day activity summary

## Lead Management

### List Leads
```
GET /api/leads/
```

Returns a list of all leads in the system.

### Lead Detail
```
GET /api/leads/{id}/
```

Returns detailed information about a specific lead.

### Create Lead
```
POST /api/leads/
```

Create a new lead. Required fields:
- `first_name`
- `last_name`
- `email`
- `agent`: Agent ID

### Update Lead
```
PUT /api/leads/{id}/
```

Update an existing lead's information.

### Delete Lead
```
DELETE /api/leads/{id}/
```

Remove a lead from the system.

### Convert Lead
```
POST /api/leads/{id}/convert/
```

Convert a lead to a customer.

## Statistics

### Overall Statistics
```
GET /api/statistics/
```

Returns system-wide statistics:
- Total agents
- Total leads
- Overall conversion rate
- Recent activity

### Agent Performance Rankings
```
GET /api/statistics/agent-rankings/
```

Returns performance rankings for all agents based on:
- Number of leads
- Conversion rates
- Activity levels

## Error Responses

All endpoints may return the following error responses:

- `400 Bad Request`: Invalid input data
- `401 Unauthorized`: Missing or invalid authentication
- `403 Forbidden`: Insufficient permissions
- `404 Not Found`: Requested resource not found
- `500 Internal Server Error`: Server-side error

## Rate Limiting

API requests are limited to:
- 100 requests per minute for authenticated users
- 20 requests per minute for unauthenticated users

## Pagination

List endpoints support pagination with the following query parameters:
- `page`: Page number (default: 1)
- `page_size`: Number of items per page (default: 20, max: 100)

## Filtering

List endpoints support filtering with query parameters:
- `created_after`: ISO 8601 datetime
- `created_before`: ISO 8601 datetime
- `status`: Lead status
- `agent`: Agent ID
- `organization`: Organization ID
