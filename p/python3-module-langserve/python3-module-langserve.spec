%define _unpackaged_files_terminate_build 1
%define pypi_name langserve

Name: python3-module-%pypi_name
Version: 0.3.1
Release: alt1

Summary: LangServe
License: MIT
Group: Development/Python3

Url: https://github.com/langchain-ai/langserve
Vcs: https://github.com/langchain-ai/langserve
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(poetry.core)

BuildArch: noarch

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md
%python3_sitelibdir_noarch/%pypi_name
%python3_sitelibdir_noarch/%pypi_name-%version.dist-info

%changelog
* Sun Apr 13 2025 David Sultaniiazov <x1z53@altlinux.org> 0.3.1-alt1
- Initial build
