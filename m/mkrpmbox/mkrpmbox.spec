# -*- mode: RPM-SPEC; tab-width: 8; fill-column: 70; -*- 
# $Id: mkrpmbox.spec,v 0.0.1 2006/06/05 14:50:27 legion Exp $ 

Name: mkrpmbox
Version: 0.0.1
Release: alt4

Summary: Utility to create RPM box to build and install RPM packages
License: GPL
Group: Development/Other
BuildArch: noarch

Requires: sh
Source: %name-%version.tar.bz2

# Automatically added by buildreq on Mon Jun 05 2006 (-bi)
BuildRequires: sh help2man

%description
This package provides %name utility that creates RPM environment: rpm, rpm database (so called RPM box).
RPM box allows to install and builds RPM packages in an isolated RPM database. This utility doesn't create chroot.

%prep
%setup -q

%build
%make

%install
%__mkdir_p %buildroot%_bindir %buildroot%_man1dir

%__install -p -m755 %name %buildroot%_bindir/
%__install -p -m644 %name.1 %buildroot%_man1dir/

%files
%_bindir/*
%_man1dir/*

%changelog
* Wed Aug 09 2006 Alexey Gladkov <legion@altlinux.ru> 0.0.1-alt4
- new build
- The transferable container is created; You may move rpmbox at the filesystem.
- You may add custom wrappers at the rpmbox creation stage.
- Added new script 'retarget' to change initialization target.

* Mon Jul 03 2006 Alexey Gladkov <legion@altlinux.ru> 0.0.1-alt3
- quoting bugfix

* Wed Jun 14 2006 Alexey Gladkov <legion@altlinux.ru> 0.0.1-alt2
- minor bugfixes

* Mon Jun 05 2006 Alexey Gladkov <legion@altlinux.ru> 0.0.1-alt1
- Inital release for Sisyphus
