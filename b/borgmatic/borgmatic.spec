Name: borgmatic
Version: 1.2.11
Release: alt1

Summary: borgmatic (formerly atticmatic) is a simple Python wrapper script for the Borg

License: GPL3
Group: File tools
Url: https://github.com/witten/borgmatic
BuildArch: noarch

Packager: Pavel Vainerman <pv@altlinux.ru>

# Source-url: https://github.com/witten/borgmatic/archive/%version.tar.gz
Source: %name-%version.tar

Requires: python-module-pykwalify >= 1:1.6.1-alt1

BuildRequires(pre): rpm-build-python3

# Automatically added by buildreq on Thu Aug 16 2018
# optimized out: python-base python-modules python3 python3-base python3-dev python3-module-greenlet python3-module-pycparser python3-module-setuptools
BuildRequires: python3-dev python3-module-zmq

BuildRequires: libssl-devel python3-dev python3-module-setuptools


%description
borgmatic (formerly atticmatic) is a simple Python wrapper script for the Borg backup software 
that initiates a backup, prunes any old backups according to a retention policy, 
and validates backups for consistency. 
The script supports specifying your settings in a declarative configuration file 
rather than having to put them all on the command-line, and handles common errors.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE AUTHORS README.md
%_bindir/*
%python3_sitelibdir_noarch/*

%changelog
* Sun Nov 25 2018 Pavel Vainerman <pv@altlinux.ru> 1.2.11-alt1
- new version (1.2.11) with rpmgs script

* Sun Oct 14 2018 Pavel Vainerman <pv@altlinux.ru> 1.2.8-alt1
- new version (1.2.8) with rpmgs script

* Fri Aug 17 2018 Pavel Vainerman <pv@altlinux.ru> 1.2.2-alt2
- update requires

* Fri Aug 17 2018 Pavel Vainerman <pv@altlinux.ru> 1.2.2-alt1
- update build requires

* Thu Aug 16 2018 Pavel Vainerman <pv@altlinux.ru> 1.2.2-alt0.1
- new version (1.2.2) with rpmgs script
