# vim: set ft=spec: -*- rpm-spec -*-

%define modulename rest_framework

Name: python-module-django-rest-framework
Version: 2.2.1
Release: alt1.1

%setup_python_module %modulename

Summary: Django REST framework
License: %bsd
Group: Development/Python

Url: http://django-rest-framework.org
Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

# https://github.com/tomchristie/django-rest-framework
Source: %name-%version.tar

# see tox.ini
Requires: Django >= 1.3

BuildPreReq: rpm-build-licenses
BuildPreReq: %py_dependencies setuptools
BuildPreReq: Django >= 1.3
BuildPreReq: python-module-django-tests
BuildPreReq: python-module-django-dbbackend-sqlite3
# for docs
BuildPreReq: %py_dependencies markdown

%description
Django REST framework is a lightweight library that makes it easy to
build Web APIs. It is designed as a modular and easy to customize
architecture, based on Django's class based views.

%package tests
Summary: Tests for Django REST framework
Group: Development/Python
BuildArch: noarch
Requires: %name = %EVR

%description tests
This package contains tests for Django REST framework.

%prep
%setup

%build
%python_build

# for docs
./mkdocs.py

%install
%python_install

%check
./rest_framework/runtests/runtests.py

%files
%doc README.md optionals.txt html
%python_sitelibdir/%modulename/
%exclude %python_sitelibdir/%modulename/tests
%exclude %python_sitelibdir/%modulename/runtests
%python_sitelibdir/*.egg-info

%files tests
%python_sitelibdir/%modulename/tests
%python_sitelibdir/%modulename/runtests

%changelog
* Fri Oct 04 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.2.1-alt1.1
- Fixed build requires.

* Thu Feb 28 2013 Aleksey Avdeev <solo@altlinux.ru> 2.2.1-alt1
- Initial build for ALT Linux Sisyphus
