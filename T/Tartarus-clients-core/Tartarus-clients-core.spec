%define base_version 0.8
%define build_version 1

Version: %base_version.%build_version
Release: alt2.1.1

Summary: Tartarus clients part
Name: Tartarus-clients-core
Source: %name-%base_version.tar
License: %gpl2plus
Group: System/Configuration/Other
Url: http://www.tartarus.ru
Packager: Dmitry M. Maslennikov <rlz at altlinux.org>

BuildArch: noarch

%add_python_lib_path /usr/share/Tartarus/ClientsCore

Requires: python-module-PyQt4, Tartarus-SysDB-slice, Tartarus-Kerberos-slice

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Wed May 28 2008
BuildRequires: python-base, scons, python-module-PyQt4

%description
This package contains Tartarus client modules and administative utilities

%prep
%setup  -q -n %name-%base_version

%build
scons

%install
scons install --install-sandbox=%buildroot

%files
%_bindir/sysdb-admin
/usr/share/Tartarus/*

%changelog
* Fri Oct 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.1-alt2.1.1
- Rebuild with Python-2.7

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt2.1
- Rebuilt with python 2.6

* Fri Jan 23 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.8.1-alt2
- Build for Sisyphus
