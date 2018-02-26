Name: extundelete
Version: 0.2.0
Release: alt2.1

Summary: An ext3 and ext4 file undeletion utility
License: GPLv2+
Group: File tools
URL: http://extundelete.sourceforge.net/
Packager: Victor Forsiuk <force@altlinux.org>
Source: http://downloads.sourceforge.net/extundelete/extundelete-%version.tar.bz2
Patch: extundelete-0.2.0-alt-group_desc.patch
Patch1: extundelete-0.2.0-alt-e2fsprogs-1.42.patch

# Automatically added by buildreq on Tue Oct 06 2009
BuildRequires: gcc-c++ libe2fs-devel

%description
extundelete is a utility that can recover deleted files from an ext3 or ext4 partition.

%prep
%setup
%patch -p1
%patch1 -p2

%build
%configure
%define _optlevel 3
subst 's/-O./%optflags/g' src/Makefile
%make_build -C src nodebug

%install
install -pDm 755 src/extundelete %buildroot%_bindir/extundelete

%files
%_bindir/*

%changelog
* Thu Feb 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt2.1
- Fixed build with e2fsprogs 1.42

* Thu Apr 21 2011 Dmitry V. Levin <ldv@altlinux.org> 0.2.0-alt2
- Fixed build due to e2fsprogs-v1.41.12-107-gefe0b40 API change.

* Thu Jun 17 2010 Victor Forsiuk <force@altlinux.org> 0.2.0-alt1
- 0.2.0

* Fri Nov 06 2009 Victor Forsyuk <force@altlinux.org> 0.1.8-alt1
- 0.1.8

* Tue Oct 06 2009 Victor Forsyuk <force@altlinux.org> 0.1.7-alt1
- 0.1.7

* Mon Sep 21 2009 Victor Forsyuk <force@altlinux.org> 0.1.6-alt1
- Initial build.
