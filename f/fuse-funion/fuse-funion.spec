%define distname funionfs

Name: fuse-funion
Version: 0.4.3
Release: alt1

Summary: FunionFS - An union filesystem for FUSE

Group: System/Kernel and hardware
License: GPL
Url: http://funionfs.apiou.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://funionfs.apiou.org/file/%distname-%version.tar.bz2

%{echo Requires: `rpmquery --queryformat "%NAME = %VERSION" fuse`}

# Automatically added by buildreq on Sat Dec 31 2005
BuildRequires: libfuse-devel

%description
Funionfs is a filesystem which concatenate two or more directories. These
directories are hierarchised by Funionfs. Typically, you could use a
mounted filesystem wich is in read-only where you only read files and
an upper filesystem (empty at the start of the system) where you write
modifications.  Funionfs is very useful for embedded linux (the system
must resist powerfail) and for live-cd Linux.

%prep
%setup -q -n %distname-%version

%build
%configure
%make_build

%install
install -d %buildroot%_bindir

install %distname -m755 %buildroot%_bindir


%files
%doc AUTHORS ChangeLog NEWS README TODO
%_bindir/*

%changelog
* Tue Aug 07 2007 Vitaly Lipatov <lav@altlinux.ru> 0.4.3-alt1
- new version 0.4.3 (with rpmrb script)

* Wed Sep 13 2006 Vitaly Lipatov <lav@altlinux.ru> 0.4.2-alt0.1
- new version 0.4.2 (with rpmrb script)

* Sun Feb 26 2006 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt0.1
- new version 0.3 (with rpmrb script)
- remove COPYING

* Sat Dec 31 2005 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt0.1
- initial build for ALT Linu Sisyphus
