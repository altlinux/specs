%define module_name django-picklefield

Name: python-module-%module_name
Version: 0.2.1
Release: alt1
Group: System/Base
License: BSD License
Summary: django-picklefield provides an implementation of a pickled object field
URL: http://github.com/gintas/django-picklefield.git
Packager: Viacheslav Dubrovskyi <dubrsl@altlinux.org>
Source: %module_name-%version.tar.gz

BuildRequires: python-module-distribute

%description
django-picklefield provides an implementation of a pickled object field.
Such fields can contain any picklable objects.

%prep
%setup -n %module_name-%version

%build
%python_build

%install
%python_install
%ifarch x86_64
mv %buildroot%_target_libdir_noarch %buildroot%_libdir
%endif

%files
%doc README
%python_sitelibdir/django_picklefield*
%python_sitelibdir/picklefield*

%changelog
* Mon May 07 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.2.1-alt1
- build for ALT
