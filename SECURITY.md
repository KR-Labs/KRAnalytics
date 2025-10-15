# Security Policy

## Supported Versions

We actively maintain and provide security updates for the following versions of KRAnalytics:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

We take the security of KRAnalytics seriously. If you discover a security vulnerability, please follow these steps:

### How to Report

1. **Do NOT** open a public GitHub issue for security vulnerabilities
2. Email security reports to: **security@krlabs.dev**
3. Include the following information:
   - Description of the vulnerability
   - Steps to reproduce the issue
   - Potential impact
   - Suggested fix (if available)

### What to Expect

- **Initial Response**: Within 48 hours of your report
- **Status Update**: Within 7 days with an assessment of the issue
- **Resolution Timeline**: Critical vulnerabilities will be addressed within 30 days
- **Disclosure**: We follow responsible disclosure practices and will coordinate with you on public disclosure timing

### Security Best Practices

When using KRAnalytics, please follow these security guidelines:

#### API Key Management

- **Never commit API keys** to version control
- Store API keys in environment variables or secure configuration files
- Use the `.env` file pattern and ensure `.env` is in your `.gitignore`
- Rotate API keys regularly
- Limit API key permissions to minimum required scope

```bash
# Example: Setting API keys as environment variables
export CENSUS_API_KEY="your_key_here"
export BLS_API_KEY="your_key_here"
export FRED_API_KEY="your_key_here"
```

#### Data Security

- **Sensitive Data**: Never commit personally identifiable information (PII) or sensitive data
- **Sample Data**: Use only aggregate, anonymized, or publicly available data in examples
- **Data Storage**: Store sensitive analysis results outside of version control
- **Access Control**: Implement appropriate access controls for production deployments

#### Dependency Security

- Regularly update dependencies to patch known vulnerabilities
- Review `requirements.txt` and update packages periodically
- Use virtual environments to isolate dependencies

```bash
# Check for outdated packages
pip list --outdated

# Update specific packages
pip install --upgrade <package-name>
```

#### Code Security

- Validate and sanitize all user inputs
- Avoid executing arbitrary code from untrusted sources
- Be cautious with `eval()`, `exec()`, and similar functions
- Review notebook code before execution, especially from external sources

### Known Security Considerations

#### API Rate Limits

Many data sources implement rate limiting. Excessive requests may result in:
- Temporary IP blocks
- API key suspension
- Service interruptions

Always respect API rate limits and implement appropriate throttling.

#### Data Privacy

When working with socioeconomic data:
- Ensure compliance with applicable data protection regulations (GDPR, CCPA, etc.)
- Aggregate data appropriately to prevent re-identification
- Document data sources and usage restrictions
- Obtain necessary permissions for proprietary data

### Security Features

KRAnalytics implements the following security measures:

- **No Credential Storage**: API keys are loaded from environment or external configuration
- **Input Validation**: Data inputs are validated before processing
- **Safe Defaults**: Secure configurations are applied by default
- **Minimal Permissions**: Requests only necessary data scopes from APIs

### Vulnerability Disclosure

When a security vulnerability is confirmed:

1. We will develop a fix and test it thoroughly
2. A security advisory will be published on GitHub Security Advisories
3. A new version with the fix will be released
4. Users will be notified through release notes and GitHub notifications
5. Credit will be given to the reporter (unless anonymity is requested)

### Security Updates

To stay informed about security updates:

- Watch the repository for security advisories
- Subscribe to release notifications
- Follow [@KRLabs](https://github.com/KR-Labs) for announcements
- Check the [CHANGELOG](./CHANGELOG.md) for security-related updates

### Scope

This security policy applies to:

- KRAnalytics core library code
- Example notebooks and tutorials
- Documentation and configuration files
- Build and deployment scripts

### Out of Scope

The following are generally outside the scope of this security policy:

- Issues in third-party dependencies (report to respective projects)
- Social engineering attacks
- Physical security issues
- Denial of service attacks against public APIs
- Issues requiring physical access to infrastructure

### Additional Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Python Security Best Practices](https://python.readthedocs.io/en/stable/library/security.html)
- [Jupyter Notebook Security](https://jupyter-notebook.readthedocs.io/en/stable/security.html)
- [GitHub Security Advisories](https://github.com/KR-Labs/KRAnalytics/security/advisories)

## Contact

For security-related inquiries:
- **Email**: security@krlabs.dev
- **General Contact**: info@krlabs.dev

For general questions, bug reports, or feature requests (non-security):
- Open an issue on [GitHub Issues](https://github.com/KR-Labs/KRAnalytics/issues)

---

**Thank you for helping keep KRAnalytics and our community safe!**
