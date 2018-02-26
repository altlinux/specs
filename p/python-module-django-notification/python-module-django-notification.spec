%define module_name django-notification

Name: python-module-%module_name
Version: 0.2
Release: alt1
Group: System/Base
License: MIT License
Summary: User notification management for the Django web framework
URL: http://github.com/Star2Billing/django-notification
Packager: Viacheslav Dubrovskyi <dubrsl@altlinux.org>
Source: %name-%version.tar

BuildRequires: python-module-distribute

%description
User notification management for the Django web framework

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
%doc AUTHORS CHANGELOG LICENSE README
%python_sitelibdir/django_notification*
%python_sitelibdir/notification*

%changelog
* Mon May 07 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.2-alt1
- build for ALT
