%define module_name yolk

Name: python-module-%module_name
Version: 0.4.3
Release: alt1
Group: System/Base
License: BSD License
Summary: Yolk is a Python tool for obtaining information about installed Python packages
URL: https://github.com/cakebread/yolk.git
Packager: Viacheslav Dubrovskyi <dubrsl@altlinux.org>
Source: %name-%version.tar

BuildRequires: python-module-distribute

%description
Yolk is a Python tool for obtaining information about installed Python packages
and querying packages avilable on PyPI (Python Package Index).

You can see which packages are active, non-active or in development mode
and show you which have newer versions available by querying PyPI.

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
%doc AUTHORS COPYING FAQ README.rst THANKS ChangeLog CREDITS NEWS README TODO
%_bindir/*
%python_sitelibdir/yolk*

%changelog
* Fri May 04 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.3-alt1
- build for ALT
