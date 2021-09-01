%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

# LTO causes errors, disable it
%global optflags_lto %nil

%define _optlevel s
%define soname 21

Name: libtorrent
Epoch: 3
Version: 0.13.8
Release: alt2
Summary: libTorrent is a BitTorrent library written in C++ for *nix
Group: System/Libraries
License: GPLv2+
Url: https://github.com/rakshasa/libtorrent

# https://github.com/rakshasa/libtorrent.git
Source: %name-%version.tar

BuildRequires: gcc-c++ libsigc++2.0-devel libssl-devel
BuildRequires: cppunit-devel
BuildRequires: zlib-devel

%def_disable static

%description
libTorrent is designed to avoid redundant copying and storing of data
that other clients and libraries suffer from. libTorrent features:

* The client has full control over the polling of sockets.
* Sigc++ signals makes it easy for the client to react to events.
* Fast resume which checks the file modification time.
* Direct reading and writing from network to mmap'ed files.
* File hash check uses the same thread; client can control the rate;
  non-blocking and preload to memory with the mincore and madvise.
* File handler: fine-grained use of file read/write permissions, allows
  seeding of read-only files; allows torrents with unlimited number of
  files; opens closed files when mapping chunks to memory, with graceful
  error handling; support for files larger than 2 GB; different download
  priorities for files in the torrent.
* Multi-tracker support.
* No dependency on any specific HTTP library, the client implements a
  wrapper class.
* Dynamic request pipe size.
* Upload and download throttle.
* And much more...

%package -n %name%soname
Summary: Development libraries and header files for libTorrent
Group: System/Libraries

%description -n %name%soname
libTorrent is designed to avoid redundant copying and storing of data
that other clients and libraries suffer from. libTorrent features:

* The client has full control over the polling of sockets.
* Sigc++ signals makes it easy for the client to react to events.
* Fast resume which checks the file modification time.
* Direct reading and writing from network to mmap'ed files.
* File hash check uses the same thread; client can control the rate;
  non-blocking and preload to memory with the mincore and madvise.
* File handler: fine-grained use of file read/write permissions, allows
  seeding of read-only files; allows torrents with unlimited number of
  files; opens closed files when mapping chunks to memory, with graceful
  error handling; support for files larger than 2 GB; different download
  priorities for files in the torrent.
* Multi-tracker support.
* No dependency on any specific HTTP library, the client implements a
  wrapper class.
* Dynamic request pipe size.
* Upload and download throttle.
* And much more...

%package devel
Summary: Development libraries and header files for libTorrent
Group: Development/C
Requires: %name%soname = %EVR
Conflicts: libtorrent-rasterbar-devel

%description devel
The libtorrent-devel package contains libraries and header files needed
to develop applications using libTorrent.

%prep
%setup

mv -f COPYING COPYING.orig
ln -s $(relative %_licensedir/GPL-2 %_docdir/%name/COPYING) COPYING

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%check
%make_build check

%files -n %name%soname
%doc AUTHORS ChangeLog NEWS README
%doc --no-dereference COPYING
%_libdir/*.so.%{soname}
%_libdir/*.so.%{soname}.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%changelog
* Wed Sep 01 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3:0.13.8-alt2
- Disabled LTO.

* Thu Jun 04 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 3:0.13.8-alt1
- Updated to upstream version 0.13.8.

* Wed Sep 26 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3:0.13.7-alt1
- Updated to upstream version 0.13.7.
- Applied patch for support of openssl-1.1.

* Wed Jan 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3:0.13.6-alt2
- Fixed build with new cppunit.
- Enabled tests.

* Mon Nov 09 2015 Afanasov Dmitry <ender@altlinux.org> 3:0.13.6-alt1
- 0.13.6

* Tue Mar 11 2014 Denis Smirnov <mithraen@altlinux.ru> 3:0.13.3-alt1
- 0.13.3
