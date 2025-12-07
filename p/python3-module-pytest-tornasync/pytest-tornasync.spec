%define oname pytest_tornasync
%def_with check

Name: python3-module-pytest-tornasync
Version: 0.6.0
Release: alt0.post2

Summary: A pytest plugin for testing Tornado (version 5.0 or newer) apps
License: MIT
Group: Development/Python3

Url: https://pypi.org/project/pytest-tornasync
Vcs: https://github.com/eukaryote/pytest-tornasync

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-tornado
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
A simple pytest plugin that provides some helpful fixtures for testing
Tornado (version 5.0 or newer) apps and easy handling of plain (undecoratored)
native coroutine tests (Python 3.5+).

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest test

%files
%doc LICENSE *.rst
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version.post2.dist-info/

%changelog
* Sun Dec 07 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.6.0-alt0.post2
- Initial build for ALT Linux.
