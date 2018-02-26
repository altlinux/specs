Name: pax
Version: 3.4
Release: alt2

Packager: Victor Forsyuk <force@altlinux.org>

Summary: POSIX File System Archiver
License: BSD
Group: Archiving/Backup

URL: http://ftp.suse.com/pub/people/kukuk/pax
Source: %url/pax-%version.tar.bz2
Patch1: pax-3.4-rdtruncate.patch
Patch2: pax-3.4-abs100.patch
Patch3: pax-3.4-PATHMAX.patch

%description
'pax' is the POSIX standard archive tool. It supports the two most
common forms of standard Unix archive (backup) files - CPIO and TAR.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%_bindir/*
%_man1dir/*

%changelog
* Wed Dec 24 2008 Victor Forsyuk <force@altlinux.org> 3.4-alt2
- Add patches from Fedora.

* Thu Oct 27 2005 Victor Forsyuk <force@altlinux.ru> 3.4-alt1
- 3.4 (LFS supported in this version).

* Tue Oct 05 2004 Stanislav Ievlev <inger@altlinux.org> 3.2-alt1
- 3.2

* Fri Feb 28 2003 Stanislav Ievlev <inger@altlinux.ru> 3.1-alt1
- Inital release
