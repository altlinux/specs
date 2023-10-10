%define vrs	3.1
%define tstamp 	20230828

Name: libedit3
Version: %vrs.%tstamp
Release: alt1

Summary: The BSD editline library
License: BSD-3-Clause
Group: System/Libraries
Url: https://www.thrysoee.dk/editline/

# Repacked https://www.thrysoee.dk/editline/libedit-%tstamp-%vrs.tar.gz
Source: libedit-%tstamp-%vrs.tar

Patch0: libedit-alt-use-OpenBSD-soname.patch
Patch1: libedit-alt-configure-AC_SYS_LARGEFILE.patch

# Automatically added by buildreq on Tue Feb 15 2011
BuildRequires: groff-base libtinfo-devel

%description
This is an autotool- and libtoolized port of the NetBSD Editline
library (libedit). This Berkeley-style licensed command line
editor library provides generic line editing, history, and
tokenization functions, similar to those found in GNU Readline.

%package -n libedit-devel
Summary: Files needed to develop programs which use the %name library
Group: Development/C
Requires: %name = %EVR

%description -n libedit-devel
This package contains the files needed to develop programs which use
the %name library to provide an easy to use and more intuitive
command line interface for users.

%prep
%setup -q -n libedit-%tstamp-%vrs
%patch0 -p2
%patch1 -p2
rm aclocal.m4 m4/*.m4

%build
%add_optflags %optflags_warnings -Wunused-function -Wunused-label -Wunused-variable -Wunused-value
%autoreconf
%configure \
	--disable-examples \
	--disable-static \
#
%make_build

%install
%makeinstall_std

# In 20160618-3.1 some manpages dropped prefix for some reason.
cd %buildroot%_man3dir
	for m in tok_*.3 history*.3 ; do
		mv -v "$m" el_"$m"
	done
cd -

%set_verify_elf_method strict
%define _stripped_files_terminate_build 1
%define _unpackaged_files_terminate_build 1

%files
%_libdir/*.so.*
%_man5dir/*
%_man7dir/*

%files -n libedit-devel
%_libdir/*.so
%_pkgconfigdir/libedit.pc
%_includedir/*
%_man3dir/*

%changelog
* Tue Oct 03 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.1.20230828-alt1
- Updated to 20230828-3.1.

* Fri Jul 28 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.1.20221030-alt1
- Updated to 20221030-3.1.

* Sun Dec 06 2020 Dmitry V. Levin <ldv@altlinux.org> 3.1.20191231-alt1
- 20190324-3.1 -> 20191231-3.1.
- libedit-devel: removed libedit.a.
- Moved user manpages from libedit-devel to libedit3.

* Fri Aug 23 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.1.20190324-alt1
- Updated to 20190324-3.1.

* Mon Mar 11 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.1.20181209-alt1
- Updated to 20181209-3.1.

* Thu Oct 30 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.1.20141030-alt1
- Built new version.
- Made use of OpenBSD soname for library.

* Sat Mar 23 2013 Alexey Gladkov <legion@altlinux.ru> 3.0.20121213-alt1
- New version.
- SONAME change: libedit.so.0.0.35 -> libedit.so.0.0.42

* Tue Feb 15 2011 Alexey Tourbin <at@altlinux.ru> 3.0.20100424-alt2
- rebuilt for debuginfo

* Mon Oct 18 2010 Alexey Gladkov <legion@altlinux.ru> 3.0.20100424-alt1
- New version.
- Add UTF-8 support.
- SONAME change: libedit.so.0.0.29 -> libedit.so.0.0.35

* Thu Apr 16 2009 Alexey Gladkov <legion@altlinux.ru> 3.0.20090405-alt1
- new major version.
- Move libedit.so to devel (ALT#19244).
- SONAME change: libedit.so.0.0.23 -> libedit.so.0.0.29

* Fri Feb 29 2008 Alexey Gladkov <legion@altlinux.ru> 2.10.20070831-alt1
- new version.
- add libedit.pc in libedit-devel.

* Sat Jan 13 2007 Alexey Gladkov <legion@altlinux.ru> 2.10.20061228-alt1
- new version
- sync with upstream source. More readline functions.
- SONAME change: libedit.so.0.0.19 -> libedit.so.0.0.23

* Mon Jun 19 2006 Alexey Gladkov <legion@altlinux.ru> 2.9.20060603-alt1
- sync with upstream source.
- SONAME change: libedit.so.0.0.18 -> libedit.so.0.0.19

* Tue Mar 07 2006 Alexey Gladkov <legion@altlinux.ru> 2.9.20060213-alt2
- ncurses support fix.

* Sun Feb 26 2006 Alexey Gladkov <legion@altlinux.ru> 2.9.20060213-alt1
- sync with upstream source.

* Wed Nov 30 2005 Alexey Gladkov <legion@altlinux.ru> 2.9-alt1
- first build for ALT Linux.
