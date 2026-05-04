%define pypi_name agent-client-protocol
%define dist_name agent_client_protocol
%define mod_name acp

Name:    python3-module-%pypi_name
Version: 0.9.0
Release: alt1

Summary: Python SDK for Agent Client Protocol (ACP)

License: Apache-2.0
Group:   Development/Python3
Url:     https://agentclientprotocol.github.io/python-sdk/
VCS:     https://github.com/agentclientprotocol/python-sdk

BuildArch: noarch

# Source-url: %__pypi_url %dist_name
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pdm-backend

%description
Python SDK for Agent Client Protocol (ACP) clients and agents.
The Agent Client Protocol standardises communication between code editors
and AI coding agents, originally introduced by Zed Industries.

This package provides the acp module with primitives for building
ACP clients, agents, transports and routers using pydantic models.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md LICENSE
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %dist_name}

%changelog
* Fri May 01 2026 Vitaly Lipatov <lav@altlinux.ru> 0.9.0-alt1
- initial build for ALT Sisyphus
