%define svnrev 192
Name: mtx
Version: 1.3.12
Release: alt2

Summary: SCSI Media Changer and Backup Device Control
License: GPL-2.0-only
Group: Archiving/Backup
URL: http://mtx.opensource-sw.net

Source: %name-%version.tar

# http://mtx.opensource-sw.net/bugs/view.php?id=9
Patch0: %name-1.3.12-destdir.patch
# http://mtx.opensource-sw.net/bugs/view.php?id=13
# https://bugzilla.redhat.com/show_bug.cgi?id=538403
Patch1: %name-1.3.12-argc.patch
# update for GCC 15 / C23
Patch2: %name-1.3.12-bool.patch

#BuildRequires: gcc-c++

%description
mtx is a set of low level driver programs to control features of SCSI
backup related devices such as autoloaders, tape changers, media
jukeboxes, and tape drives.

%prep
%setup
%patch0 -p2 -b .destdir
%patch1 -p2 -b .argc
%patch2 -p1 -b .bool

%build
%configure
%make_build

%install
%make_install mandir=%buildroot%_mandir sbindir=%buildroot%_sbindir install

%files
%_sbindir/*
%_man1dir/*

%changelog
* Sat Jun 06 2026 Anton Midyukov <antohami@altlinux.org> 1.3.12-alt2
- Fix FTBFS with gcc 15.

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.3.12-alt1.qa1
- NMU: rebuilt for debuginfo.

* Mon Aug 23 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1.3.12-alt1
- 1.3.12 (Closes: #23921)

* Fri Mar 21 2008 Denis Klimov <zver@altlinux.ru> 1.3.11-alt1.svn.192
- initial build for ALT Linux

