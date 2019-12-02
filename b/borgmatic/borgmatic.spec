Name: borgmatic
Version: 1.4.16
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

BuildRequires(pre): rpm-build-python3 rpm-build-intro

BuildRequires: python3-dev python3-module-setuptools

# according to setup.py
%py3_use pykwalify < 14.06
%py3_use pykwalify > 1.6.0
%py3_use ruamel-yaml > 0.15.0
%py3_use ruamel-yaml < 0.16.0


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
* Mon Dec 02 2019 Pavel Vainerman <pv@altlinux.ru> 1.4.16-alt1
- new version (1.4.16) with rpmgs script

* Fri Nov 08 2019 Pavel Vainerman <pv@altlinux.ru> 1.4.8-alt1
- new version (1.4.8) with rpmgs script

* Fri Nov 01 2019 Pavel Vainerman <pv@altlinux.ru> 1.4.1-alt1
- new version (1.4.1) with rpmgs script

* Sun Oct 20 2019 Pavel Vainerman <pv@altlinux.ru> 1.3.26-alt1
- new version (1.3.26) with rpmgs script

* Sun Sep 29 2019 Pavel Vainerman <pv@altlinux.ru> 1.3.21-alt1
- new version (1.3.21) with rpmgs script

* Mon Sep 23 2019 Pavel Vainerman <pv@altlinux.ru> 1.3.18-alt1
- new version (1.3.18) with rpmgs script

* Thu Sep 19 2019 Pavel Vainerman <pv@altlinux.ru> 1.3.16-alt1
- new version (1.3.16) with rpmgs script

* Fri Sep 13 2019 Pavel Vainerman <pv@altlinux.ru> 1.3.15-alt1
- new version (1.3.15) with rpmgs script

* Tue Jun 18 2019 Pavel Vainerman <pv@altlinux.ru> 1.3.7-alt1
- new version (1.3.7) with rpmgs script

* Fri Jun 14 2019 Pavel Vainerman <pv@altlinux.ru> 1.3.6-alt1
- new version (1.3.6) with rpmgs script

* Sun May 12 2019 Pavel Vainerman <pv@altlinux.ru> 1.3.3-alt1
- new version (1.3.3) with rpmgs script

* Tue Apr 30 2019 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt1
- new version 1.3.1 (with rpmrb script)

* Tue Apr 30 2019 Vitaly Lipatov <lav@altlinux.ru> 1.2.17-alt2
- fix (build)requires

* Sun Feb 24 2019 Pavel Vainerman <pv@altlinux.ru> 1.2.17-alt1
- new version (1.2.17) with rpmgs script

* Tue Dec 11 2018 Pavel Vainerman <pv@altlinux.ru> 1.2.12-alt1
- new version (1.2.12) with rpmgs script

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
