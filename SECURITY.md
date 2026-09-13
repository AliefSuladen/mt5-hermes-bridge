# Security Policy

## Overview

This project connects an AI agent with MetaTrader 5 through an HTTP-based trading bridge.

Because the system can interact with trading infrastructure, security and credential management are important.

## Supported Versions

This project is experimental and does not currently maintain multiple supported release versions.

Security fixes will be applied to the latest version when appropriate.

## Reporting a Security Issue

If you discover a security vulnerability, please do not disclose sensitive details in a public GitHub issue.

Instead, contact the repository owner privately through GitHub.

When reporting a vulnerability, please include:

- A description of the issue
- Steps to reproduce the issue
- Potential impact
- Relevant logs or screenshots, if safe to share
- Any suggested mitigation

Please do not include API keys, passwords, private keys, access tokens, or other sensitive credentials in your report.

## Credential Security

Never commit real credentials to this repository.

Sensitive values such as:

- API keys
- Access tokens
- Passwords
- Private keys
- Trading account credentials

must be stored outside the repository and provided through environment variables or another secure secret-management mechanism.

## Responsible Disclosure

Please allow reasonable time for a security issue to be investigated and addressed before publicly disclosing technical details.

Thank you for helping keep this project and its users secure.
