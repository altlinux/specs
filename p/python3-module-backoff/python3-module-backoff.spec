%define _unpackaged_files_terminate_build 1
%define module_name backoff
%def_with check

Name: python3-module-%module_name
Version: 2.2.1
Release: alt1
Summary: Python library providing function decorators for configurable backoff and retry
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/backoff
VCS: https://github.com/litl/backoff

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(poetry)
BuildRequires: python3(poetry-core)

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
%python3_sitelibdir/%{pyproject_distinfo %module_name}
%doc LICENSE

%changelog
* Sun Dec 15 2024 Alexander Makeenkov <amakeenk@altlinux.org> 2.2.1-alt1
- Initial build for ALT.
