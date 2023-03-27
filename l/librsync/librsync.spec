%define _unpackaged_files_terminate_build 1

%def_with check
%def_with doc

Name: librsync
Version: 2.3.4
Release: alt1

Summary: remote delta-compression library
License: LGPL-2.1
Group: System/Libraries

#https://github.com/librsync/librsync
Url: https://librsync.github.io/
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires: cmake
BuildRequires: zlib-devel
BuildRequires: bzlib-devel
BuildRequires: libb2-devel
BuildRequires: libpopt-devel

%if_with check
BuildRequires: ctest
%endif

%if_with doc
BuildRequires: doxygen
BuildRequires: graphviz
%endif

%description
librsync is a library for calculating and applying network deltas, with an
interface designed to ease integration into diverse network applications.

librsync encapsulates the core algorithms of the rsync protocol, which help
with efficient calculation of the differences between two files. The rsync
algorithm is different from most differencing algorithms because it does
not require the presence of the two files to calculate the delta. Instead,
it requires a set of checksums of each block of one file, which together
form a signature for that file. Blocks at any position in the other file
which have the same checksum are likely to be identical, and whatever
remains is the difference.

This algorithm transfers the differences between two files without needing
both files on the same system.

librsync is for building other programs that transfer files as efficiently
as rsync. You can use librsync in a program you write to do backups,
distribute binary patches to programs, or sync directories to a server or
between peers.

This tree also produces the rdiff command that exposes the key operations
of librsync: generating file signatures, generating the delta from a
signature to a new file, and applying the delta to regenerate the new file
given the old file.

librsync was originally written for the rproxy experiment in
delta-compression for HTTP. librsync is used by: Dropbox, rdiff-backup,
Duplicity, and others. (If you would like to be listed here, let me know.)

%package devel
Summary: Headers and development libraries for librsync
Group: Development/C
Requires: %name = %EVR

%description devel
The librsync-devel package contains header files and library necessary for
developing programs based on librsync.

%if_with doc
%package doc
Summary: Documentation for librsync
Group: Development/Documentation
BuildArch: noarch

%description doc
This package contains the API documentation for developing applications that
use librsync.
%endif

%prep
%setup
%patch0 -p1

%build
%cmake -DENABLE_TRACE=1
%cmake_build
%if_with doc
%cmake_build --target doc
%endif

%install
%cmakeinstall_std

%check
%cmake_build --target check

%files
%doc AUTHORS README.md NEWS.md COPYING
%_bindir/*
%_libdir/*.so.*
%_man1dir/*

%files devel
%_libdir/*.so
%_includedir/*
%_man3dir/*

%if_with doc
%files doc
%doc %_cmake__builddir/html
%endif

%changelog
* Mon Mar 27 2023 Egor Ignatov <egori@altlinux.org> 2.3.4-alt1
- New version 2.3.4.

* Wed Apr 20 2022 Egor Ignatov <egori@altlinux.org> 2.3.2-alt2
- enable trace (closes: #42493)

* Tue Jan 11 2022 Egor Ignatov <egori@altlinux.org> 2.3.2-alt1
- update to 2.3.2 (closes: #41679)
- gear: change package build scheme
  + merge with upstream git
  + build from release tag

* Mon Apr 20 2020 Michael Shigorin <mike@altlinux.org> 0.9.7-alt5
- fix build with lcc (and clang: upstream issue #41)

* Fri Feb 15 2019 Ivan A. Melnikov <iv@altlinux.org> 0.9.7-alt4
- synced with Debian librsync-0.9.7-10.
- %%check added.

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
