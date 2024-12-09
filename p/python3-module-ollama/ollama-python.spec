# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1

Name: python3-module-ollama
Version: 0.4.4
Release: alt1
Summary: Ollama Python library
License: MIT
Group: Sciences/Computer science
Url: https://ollama.com
Vcs: https://github.com/ollama/ollama-python
Requires: python3(anyio)

Source: %name-%version.tar
BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3(poetry-core)
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
%{?!_without_check:%{?!_disable_check:
BuildRequires: pytest3
BuildRequires: python3(anyio)
BuildRequires: python3(httpx)
BuildRequires: python3(PIL)
BuildRequires: python3(pydantic)
BuildRequires: python3(pytest_asyncio)
BuildRequires: python3(pytest_httpserver)
}}

%description
The Ollama Python library provides the easiest way to integrate Python 3.8+
projects with Ollama.

%prep
%setup
sed -Ei '/^version\s*=/s/"[0.]+"/"%version"/' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE README.md requirements.txt examples
%python3_sitelibdir/ollama
%python3_sitelibdir/ollama-%version.dist-info

%changelog
* Mon Dec 09 2024 Vitaly Chikunov <vt@altlinux.org> 0.4.4-alt1
- First import v0.4.4-1-g70dd0b7 (2024-12-07).
