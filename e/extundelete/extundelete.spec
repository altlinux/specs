Name: extundelete
Version: 0.2.4
Release: alt2

Summary: An ext3 and ext4 file undeletion utility
License: GPLv2+
Group: File tools
Url: http://extundelete.sourceforge.net/
Source: %name-%version.tar.bz2
Patch1: extundelete-0.2.4-fedora-i_size_high.patch

# Automatically added by buildreq on Tue Oct 06 2009
BuildRequires: gcc-c++ libe2fs-devel

%description
extundelete is a utility that can recover deleted files from an ext3 or ext4
partition. extundelete uses the information stored in the partition's journal
to attempt to recover a file that has been deleted from the partition. There is
no guarantee that any particular file will be able to be undeleted, so always
try to have a good backup system in place, or at least put one in place after
recovering your files!

%prep
%setup
%patch1 -p1

%build
%configure
%make_build

%install
%makeinstall

%files
%doc README
%_bindir/*

%changelog
* Wed Dec 26 2018 Ivan A. Melnikov <iv@altlinux.org> 0.2.4-alt2
- Add patch 1 to build with recent e2fstools

* Sat May 10 2014 Fr. Br. George <george@altlinux.ru> 0.2.4-alt1
- Autobuild version bump to 0.2.4
- Drop patches

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
