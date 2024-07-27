%define modname django-ansible-base

# Tests require PostgreSQL
%def_without check

Name: python3-module-%modname
Version: 2024.7.17
Release: alt1

Summary: A base for any Ansible application which will leverage Django
License: Apache-2.0
Group:   Development/Python3
URL: https://github.com/ansible/django-ansible-base
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-django
BuildRequires: python3-module-pytest-django
BuildRequires: python3-module-django-split-settings
BuildRequires: python3-module-typeguard
BuildRequires: python3-module-djangorestframework
BuildRequires: python3-module-social-app-django
BuildRequires: python3-module-django-extensions
BuildRequires: python3-module-django-debug-toolbar
BuildRequires: python3-module-drf-spectacular
BuildRequires: python3-module-django-oauth-toolkit
BuildRequires: python3-module-django-crum
BuildRequires: python3-module-django-redis
BuildRequires: python3-module-channels
BuildRequires: python3-module-ldap
BuildRequires: python3-module-pyrad
BuildRequires: python3-module-django-auth-ldap
BuildRequires: python3-module-xmlsec
BuildRequires: python3-module-lxml
BuildRequires: libxmlsec1-devel
BuildRequires: libxmlsec1-openssl
BuildRequires: libxmlsec1-openssl-devel
%endif

%description
Django-ansible-base is exactly what it says it is.
A base for any Ansible application which will leverage Django.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc README.*
%python3_sitelibdir/ansible_base/
%python3_sitelibdir/%{pyproject_distinfo %modname}

%changelog
* Sun Jul 21 2024 Anton Vyatkin <toni@altlinux.org> 2024.7.17-alt1
- Initial build for Sisyphus.
