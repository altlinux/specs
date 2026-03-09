%define pypi_name claude-agent-sdk
%define mod_name claude_agent_sdk

Name: python3-module-%pypi_name
Version: 0.1.46
Release: alt1

Summary: Python SDK for Claude Code
License: MIT
Group: Development/Python3

URL: https://github.com/anthropics/claude-agent-sdk-python

BuildArch: noarch

# Source-url: %__pypi_url %mod_name
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling

%description
Python SDK for Claude Code that enables programmatic interaction with Claude
through async functions and bidirectional conversations.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Mar 10 2026 Vitaly Lipatov <lav@altlinux.ru> 0.1.46-alt1
- new version 0.1.46

* Mon Jan 20 2025 Vitaly Lipatov <lav@altlinux.ru> 0.1.20-alt1
- initial build for ALT Sisyphus
