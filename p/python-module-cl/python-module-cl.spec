%define module_name cl

Name: python-module-%module_name
Version: 0.0.3
Release: alt1
Group: System/Base
License: BSD License
Summary: Actor framework for Kombu
URL: http://github.com/ask/cl/
Packager: Viacheslav Dubrovskyi <dubrsl@altlinux.org>
Source: %name-%version.tar

BuildRequires: python-module-distribute

%description
cl is an actor framework for Kombu

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
%doc AUTHORS Changelog README.rst
%_bindir/*
%python_sitelibdir/cl*

%changelog
* Sat May 05 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.0.3-alt1
- build for ALT
