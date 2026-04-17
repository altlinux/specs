%define _unpackaged_files_terminate_build 1
%define pypi_name python-backoff
%define module_name backoff
%def_with check

Name: python3-module-%module_name
Version: 2.3.1
Release: alt1
Summary: Python library providing function decorators for configurable backoff and retry
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/python-backoff
VCS: https://github.com/python-backoff/backoff

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(hatchling)

%if_with check
BuildRequires: python3(requests)
BuildRequires: python3(responses)
BuildRequires: python3(pytest)
BuildRequires: python3(pytest-asyncio)
%endif

%description
This module provides function decorators which can be used to wrap
a function such that it will be retried until some condition is met.
It is meant to be of use when accessing unreliable resources with
the potential for intermittent failures i.e. network resources and
external APIs. Somewhat more generally, it may also be of use for
dynamically polling resources for externally generated content.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir/%module_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%doc LICENSE

%changelog
* Fri Apr 17 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 2.3.1-alt1
- Updated to version 2.3.1.
- Switched upstream to maintained fork.

* Sun Sep 14 2025 Alexander Makeenkov <amakeenk@altlinux.org> 2.2.1-alt2
- Fixed FTBFS.

* Sun Dec 15 2024 Alexander Makeenkov <amakeenk@altlinux.org> 2.2.1-alt1
- Initial build for ALT.
