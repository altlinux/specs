%define module_name django-socketio

Name: python-module-%module_name
Version: 0.1.4
Release: alt1
Group: System/Base
License: BSD License
Summary: Application that allow you to use WebSockets seamlessly with any Django project
URL: https://github.com/ask/bundle.git
Packager: Viacheslav Dubrovskyi <dubrsl@altlinux.org>
Source: %name-%version.tar

BuildRequires: python-module-distribute

%description
Application that brings together a variety of features that allow you to use WebSockets seamlessly with any Django project

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
%doc LICENSE README.rst
%python_sitelibdir/django_socketio*

%changelog
* Mon May 07 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.1.4-alt1
- build for ALT
