%define module_name django-celery

Name: python-module-%module_name
Version: 2.5.3
Release: alt1
Group: System/Base
License: BSD License
Summary: django-celery provides Celery integration for Django
URL: https://github.com/ask/django-celery.git
Packager: Viacheslav Dubrovskyi <dubrsl@altlinux.org>
Source: %name-%version.tar

BuildRequires: python-module-distribute

%description
Using the Django ORM and cache backend for storing results, autodiscovery of task modules
for applications listed in INSTALLED_APPS, and more.

%prep
%setup

%build
%python_build

%install
%python_install
%ifarch x86_64
mv %buildroot%_target_libdir_noarch %buildroot%_libdir
%endif

%files
%doc AUTHORS Changelog FAQ LICENSE README.rst THANKS TODO
%_bindir/*
%python_sitelibdir/djcelery*
%python_sitelibdir/django_celery*

%changelog
* Mon May 07 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.5.3-alt1
- build for ALT
