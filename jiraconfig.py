token = '' # Your JIRA token goes here!
apiBase = 'https://jira.YOURDOMAIN.com/rest/api/2' # You'll need to put your company's JIRA domain.

headersGetJira = {
    'Cookie': 'auth-openid=' + token
}

headersPostJira = {
    'Cookie': 'auth-openid=' + token,
    'Content-Type' : 'application/json',
    'X-Atlassian-Token': 'no-check'
}