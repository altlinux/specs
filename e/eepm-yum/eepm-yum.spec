Name: eepm-yum
Version: 3.52.6
Release: alt1

Summary: Yum like frontend via Etersoft EPM package manager

License: AGPL-3.0+
Group: System/Configuration/Packaging
Url: http://wiki.etersoft.ru/EPM

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/Etersoft/eepm-yum/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildArchitectures: noarch

BuildRequires: eepm >= 3.52.5
Requires: eepm >= 3.52.5

AutoProv:no
AutoReq:no

Conflicts: yum

Requires: grep

%description
This package contains yum like frontend for Etersoft EPM package manager.

Etersoft EPM is the package manager for any platform
and any platform version. It provides
universal interface to any package manager.
Can be useful for system administrators working
with various distros.

See detailed description here: http://wiki.etersoft.ru/EPM

%prep
%setup

%install
# install to datadir and so on
# do not use uncommon makeinstall_std here
%make_install install DESTDIR=%buildroot \
	datadir=%_datadir bindir=%_bindir mandir=%_mandir \
	sysconfdir=%_sysconfdir version=%version-%release

%files
# not for yum based system
%_bindir/yum

%changelog
* Mon Sep 22 2025 Vitaly Lipatov <lav@altlinux.ru> 3.52.6-alt1
- yum: update env

* Sat Apr 22 2023 Vitaly Lipatov <lav@altlinux.ru> 3.52.5-alt1
- separate build eepm-yum
