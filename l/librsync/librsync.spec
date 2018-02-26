Name: librsync
Version: 0.9.7
Release: alt3

Summary: rsync remote network-delta algorithm library
Group: System/Libraries
License: LGPLv2+
Url: http://librsync.sourceforge.net/
Packager: Vitaly Lipatov <lav@altlinux.ru>
Source: http://download.sourceforge.net/%name/%name-%version.tar.bz2
Patch1: librsync-debian-manpage.patch
Patch2: librsync-debian-4gb.patch
Patch3: librsync-debian-getopt.patch

# Automatically added by buildreq on Thu Dec 08 2011
BuildRequires: bzlib-devel libpopt-devel zlib-devel

%description
librsync is a free software library that implements the rsync remote-delta
algorithm.  This algorithm allows efficient remote updates of a file,
without requiring the old and new versions to both be present at the
sending end.  The library uses a "streaming" design similar to that of
zlib with the aim of allowing it to be embedded into many different
applications.

librsync is not wire-compatible with rsync, and is not likely to be in
the future.

%package devel
Summary: Files for development of %name-based applications
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains files for development of applications
which will use %name.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%autoreconf
%configure --disable-static --enable-shared
%make_build

%install
%makeinstall_std
%set_verify_elf_method strict
%define _unpackaged_files_terminate_build 1

%files
%_libdir/*.so.*
%_bindir/*
%_man1dir/*
%doc AUTHORS README

%files devel
%_libdir/*.so
%_includedir/*
%_man3dir/*

%changelog
* Fri Dec 09 2011 Dmitry V. Levin <ldv@altlinux.org> 0.9.7-alt3
- Synced with Debian librsync-0.9.7-8.

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 0.9.7-alt2.qa1
- rebuild using girar-nmu to require/provide setversion
  by request of mithraen@

* Wed Nov 18 2009 Vitaly Lipatov <lav@altlinux.ru> 0.9.7-alt2
- cleanup spec

* Tue Jul 01 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9.7-alt1
- cleanup spec, update spec
- add patches from Debian (fixes transfer from 32bit to 64bit host)

* Mon Nov 28 2005 Vitaly Lipatov <lav@altlinux.ru> 0.9.7-alt0.1
- initial build for ALT Linux Sisyphus
