%define _unpackaged_files_terminate_build 1
%def_with check
%define mod_name td_watson

Name: python3-module-watson
Version: 2.1.0
Release: alt1

Summary: A wonderful CLI to track your time
License: MIT
Group: Office
Url: https://pypi.org/project/td-watson/
Vcs: https://github.com/jazzband/Watson

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-requests
BuildRequires: python3-module-arrow
BuildRequires: python3-module-click
BuildRequires: python3-module-click-didyoumean
%if_with check
BuildRequires: python3-module-flake8
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-datafiles
BuildRequires: python3-module-pytest-mock
BuildRequires: python3-module-mock
BuildRequires: python3-module-tox
%endif

%description
Watson is here to help you manage your time.
You want to know how much time you are spending on your projects?
You want to generate a nice report for your client?
Watson is here for you.

%prep
%setup -q

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.rst LICENSE
%_bindir/watson
%python3_sitelibdir/watson/
%python3_sitelibdir/%{pyproject_distinfo %mod_name}

%changelog
* Thu Jun 25 2026 Alexander Kuznetsov <kuznetsovam@altlinux.org> 2.1.0-alt1
- Initial build.
