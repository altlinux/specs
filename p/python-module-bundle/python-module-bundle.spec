%define module_name bundle

Name: python-module-%module_name
Version: 1.1.2
Release: alt1
Group: System/Base
License: BSD License
Summary: Manages installed Bundle packages
URL: https://github.com/ask/bundle.git
Packager: Viacheslav Dubrovskyi <dubrsl@altlinux.org>
Source: %name-%version.tar

BuildRequires: python-module-distribute

%description
Manages installed Bundle packages

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
%doc AUTHORS Changelog LICENSE README.rst TODO
%python_sitelibdir/bundle*

%changelog
* Fri May 04 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1.2-alt1
- build for ALT
