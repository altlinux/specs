%define oname pytest_twisted
%def_with check

Name: python3-module-pytest-twisted
Version: 1.14.3
Release: alt1

Summary: Test twisted code with pytest
License: BSD-3-Clause
Group: Development/Python3

Url: https://pypi.org/project/pytest-twisted
Vcs: https://github.com/pytest-dev/pytest-twisted

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-decorator python3-module-greenlet
BuildRequires: python3-module-twisted-core python3-module-service_identity
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
Pytest-twisted is a plugin for pytest, which allows to test code,
which uses the twisted framework. test functions can return Deferred
objects and pytest will wait for their completion with this plugin.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest testing

%files
%doc LICENSE *.rst
%python3_sitelibdir/%oname/
%python3_sitelibdir/%{pyproject_distinfo %oname}/

%changelog
* Sun Dec 07 2025 Aleksandr Shamaraev <shad@altlinux.org> 1.14.3-alt1
- Initial build for ALT Linux.
