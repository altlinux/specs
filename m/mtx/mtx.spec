%define svnrev 192
Name: mtx
Version: 1.3.12
Release: alt1

Summary: SCSI Media Changer and Backup Device Control
License: GPL
Group: Archiving/Backup
Url: http://mtx.opensource-sw.net

Source: %name-%version.tar

BuildRequires: gcc-c++

%description
mtx is a set of low level driver programs to control features of SCSI
backup related devices such as autoloaders, tape changers, media
jukeboxes, and tape drives.

%prep
%setup

%build
%configure
%make_build

%install
%make_install mandir=%buildroot%_mandir sbindir=%buildroot%_sbindir install

%files
%_sbindir/*
%_man1dir/*

%changelog
* Mon Aug 23 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1.3.12-alt1
- 1.3.12 (Closes: #23921)

* Fri Mar 21 2008 Denis Klimov <zver@altlinux.ru> 1.3.11-alt1.svn.192
- initial build for ALT Linux

