%define module_name django-countries

Name: python-module-%module_name
Version: 1.2
Release: alt1
Group: System/Base
License: BSD License
Summary: Provides a country field for Django models.
URL: django-countries
Packager: Viacheslav Dubrovskyi <dubrsl@altlinux.org>
Source: %name-%version.tar

BuildRequires: python-module-distribute

%description
Provides a country field for Django models.

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
%doc README
%python_sitelibdir/django_countries*

%changelog
* Mon May 07 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2-alt1
- build for ALT
