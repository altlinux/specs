%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%global optflags_lto %nil

Name: dhcdrop
Version: 0.5
Release: alt3
Summary: Drop dhcp offers from illegitimate dhcp server.
Group: System/Servers
License: GPL-2.0
Url: http://www.netpatch.ru/projects/dhcdrop/

# http://www.netpatch.ru/projects/dhcdrop/%name-%version.tar.bz2
Source: %name-%version.tar

# Automatically added by buildreq on Tue Jul 14 2009 (-bi)
BuildRequires: libpcap-devel

%description
Drop dhcp offers from illegitimate dhcp server

%prep
%setup

%build
%configure --bindir=%_sbindir --enable-static=no
%make_build

%install
%makeinstall_std

%find_lang %name

%files
%doc AUTHORS COPYING ChangeLog NEWS README INSTALL
%_sbindir/%name
%_man8dir/*
%_mandir/ru/man8/*

%changelog
* Mon Sep 13 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5-alt3
- Disabled LTO.

* Wed Apr 17 2013 Andrew Clark <andyc@altlinux.org> 0.5-alt2
- rebuilt for debuginfo

* Wed Aug 19 2009 Andrew Clark <andyc@altlinux.org> 0.5-alt1
- initial build for ALT.

