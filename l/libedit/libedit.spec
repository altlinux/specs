%define vrs	3.0
%define tstamp 	20100424
#def_enable Werror

Name: libedit
Version: %vrs.%tstamp
Release: alt2

Summary: libedit is a replacement or alternative to the GNU readline commandline editing functionality.
License: BSD
Group: System/Libraries
Url: http://www.thrysoee.dk/editline/

Source: http://www.thrysoee.dk/editline/%name-%tstamp-%vrs.tar.gz

Patch0: libedit-alt-examples-disable.patch
Patch1: libedit-alt-configure-fix.patch
Patch2: libedit-alt-fix-warnings.patch

# Automatically added by buildreq on Tue Feb 15 2011
BuildRequires: groff-base libncurses-devel

%description
This is an autotool- and libtoolized port of the NetBSD Editline
library (libedit). This Berkeley-style licensed command line
editor library provides generic line editing, history, and
tokenization functions, similar to those found in GNU Readline.

%package devel
Summary: Files needed to develop programs which use the %name library
Group: Development/C
PreReq: %name = %version-%release

%description devel
This package contains the files needed to develop programs which use
the %name library to provide an easy to use and more intuitive
command line interface for users.

%prep
%setup -q -n %name-%tstamp-%vrs
%patch0 -p1 -b .fix0
%patch1 -p1 -b .fix1
%patch2 -p1 -b .fix2

%build
%add_optflags %optflags_warnings -Wunused-function -Wunused-label -Wunused-variable -Wunused-value
%autoreconf
%configure --enable-widec
%make_build

%install
%makeinstall

%files
%_libdir/*.so.*

%files devel
%_libdir/*.a
%_libdir/*.so
%_libdir/pkgconfig/libedit.pc
%_includedir/*
%_man3dir/*
%_man5dir/*

%changelog
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
