%define module_name django-tastypie

Name: python-module-%module_name
Version: 0.9.11
Release: alt1
Group: System/Base
License: BSD License
Summary: Creating delicious APIs for Django apps since 2010
URL: https://github.com/toastdriven/django-tastypie.git
Packager: Viacheslav Dubrovskyi <dubrsl@altlinux.org>
Source: %name-%version.tar

BuildRequires: python-module-distribute

%description
Creating delicious APIs for Django apps since 2010
There are other, better known API frameworks out there for Django. You need to
assess the options available and decide for yourself. That said, here are some
common reasons for tastypie.

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
%doc AUTHORS LICENSE README.rst TODO
%python_sitelibdir/tastypie*
%python_sitelibdir/django_tastypie*

%changelog
* Mon May 07 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.11-alt1
- build for ALT
