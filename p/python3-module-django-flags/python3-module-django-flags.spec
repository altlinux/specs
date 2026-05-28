%define modname django-flags
%define oname flags
%def_without check

Name: python3-module-%modname
Version: 5.2.0
Release: alt1

Summary: Feature flags allow you to toggle functionality in Django code
License: CC0-1.0
Group:   Development/Python3
URL: https://github.com/cfpb/django-flags
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-django
BuildRequires: python3-module-django-debug-toolbar
%endif

%description
Feature flags allow you to toggle functionality in both Django code and the 
Django templates based on configurable conditions. Flags can be useful for 
staging feature deployments, for A/B testing, or for any time you need an 
on/off switch for blocks of code. The toggle can be by date, user, URL 
value, or a number of other conditions, editable in the admin or in 
definable in settings.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
export DJANGO_SETTINGS_MODULE=flags.tests.settings
%pyproject_run_pytest -v

%files
%doc README.*
%python3_sitelibdir/%oname/
%python3_sitelibdir/%{pyproject_distinfo %modname}

%changelog
* Wed May 06 2026 Nikita Panov <nexxy@altlinux.org> 5.2.0-alt1
- Initial build for Sisyphus.


