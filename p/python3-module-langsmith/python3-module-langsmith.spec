%define _unpackaged_files_terminate_build 1
%define pypi_name langsmith

Name: python3-module-%pypi_name
Version: 0.3.30
Release: alt1

Summary: Client library to connect to the LangSmith LLM Tracing and Evaluation Platform
License: MIT
Group: Development/Python3

Url: https://github.com/langchain-ai/langsmith-sdk
Vcs: https://github.com/langchain-ai/langsmith-sdk
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(poetry-core)

BuildArch: noarch

%description
This package contains the Python client for interacting with the LangSmith
platform (https://smith.langchain.com/).

%prep
%setup

%build
%pyproject_build python

%install
cd python
%pyproject_install

%files
%doc README.md
%python3_sitelibdir_noarch/%pypi_name
%python3_sitelibdir_noarch/%pypi_name-%version.dist-info

%changelog
* Sun Apr 13 2025 David Sultaniiazov <x1z53@altlinux.org> 0.3.30-alt1
- Initial build
