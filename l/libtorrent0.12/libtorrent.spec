%define _optlevel s
%define abiversion 0.12

Name: libtorrent%{abiversion}
Version: 0.12.7
Release: alt1

Summary: libTorrent is a BitTorrent library written in C++ for *nix
Group: System/Libraries
License: GPLv2+
Url: http://libtorrent.rakshasa.no/
Packager: Alexey Morsov <swi@altlinux.ru>

%define full_version %version
Source0: %name-%version.tar

BuildRequires: gcc-c++ libsigc++2.0-devel libssl-devel
BuildRequires: cppunit-devel
Obsoletes: librtorrent <= 0.12.2-alt1

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

%package -n libtorrent-devel
Summary: Development libraries and header files for libTorrent
Group: Development/C
Requires: %name = %version-%release
Conflicts: libtorrent-rasterbar0.13-devel

%description -n libtorrent-devel
The libtorrent-devel package contains libraries and header files needed
to develop applications using libTorrent.

%prep
%setup -q -n %name-%full_version
mv -f COPYING COPYING.orig
ln -s $(relative %_licensedir/GPL-2 %_docdir/%name/COPYING) COPYING

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
rm %buildroot%_libdir/*.la

%files
%doc AUTHORS ChangeLog NEWS README
%doc --no-dereference COPYING

%_libdir/*.so.*

%files -n libtorrent-devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*

%changelog
* Sat Nov 13 2010 Alexey Morsov <swi@altlinux.ru> 0.12.7-alt1
- new version
- reformatted description
- add cppunit-devel

* Fri Oct 01 2010 Dmitry V. Levin <ldv@altlinux.org> 0.12.6-alt2
- Cleaned up specfile a bit.
- Rebuilt with libcrypto.so.10.

* Fri Jan 15 2010 Alexey Morsov <swi@altlinux.ru> 0.12.6-alt1
- new version

* Wed Jul 15 2009 Alexey Morsov <swi@altlinux.ru> 0.12.5-alt1
- new version

* Mon May 11 2009 Alexey Morsov <swi@altlinux.ru> 0.12.4-alt2
- fix build with gcc4.4

* Mon Feb 16 2009 Alexey Morsov <swi@altlinux.ru> 0.12.4-alt1.1
- fix -devel name (remove abi version)

* Wed Nov 26 2008 Alexey Morsov <swi@altlinux.ru> 0.12.4-alt1
- new version

* Thu Nov 06 2008 Alexey Morsov <swi@altlinux.ru> 0.12.3-alt2
- new version

* Fri Jul 25 2008 Alexey Morsov <swi@altlinux.ru> 0.12.2-alt2
[ Alexey Morsov ]
- rename library
  + upsream name fixed
  + dso compliance
- spec change
  + compliance to RPMChangleLog policy
  + remove static

* Sat May 17 2008 Alexey Morsov <swi@altlinux.ru> 0.12.2-alt1
- new version

* Wed Jan 30 2008 Alexey Morsov <swi@altlinux.ru> 0.12.0-alt1
- v0.12.0
- add DHT support

* Tue Dec 11 2007 Alexey Morsov <swi@altlinux.ru> 0.11.9-alt1
- Improved detection of unnecessary handshakes to decrease the load
- Fixed several bugs in PEX
- Print to the log when close_on_diskspace gets triggered

* Sun Oct 14 2007 Alexey Morsov <swi@altlinux.ru> 0.11.8-alt1
- version 0.11.8

* Tue Aug 07 2007 Alexey Morsov <swi@altlinux.ru> 0.11.5-alt1
- new version 0.11.5

* Mon Apr 09 2007 Alexey Morsov <swi@altlinux.ru> 0.11.4-alt1
- new version (new features, encryption support, bug fixes)

* Mon Nov 13 2006 Andrei Bulava <abulava@altlinux.ru> 0.10.4-alt1
- 0.10.4
- built with "-Os" instead of "-O2" as suggested by upstream

* Mon Sep 11 2006 Andrei Bulava <abulava@altlinux.ru> 0.9.3-alt1
- 0.9.3

* Thu May 04 2006 Andrei Bulava <abulava@altlinux.ru> 0.8.5-alt1
- 0.8.5
- referenced everywhere in spec as libTorrent instead of LibTorrent
  though upstream mixes the above names here and where :)
- dropped gcc_warnings_comparison and gcc_warnings patches (fixed
  upstream)
- replaced COPYING with a symlink to the system-wide GPL-2 text

* Fri Nov 18 2005 Andrei Bulava <abulava@altlinux.ru> 0.7.6-alt1
- 0.7.6

* Fri Oct 28 2005 Andrei Bulava <abulava@altlinux.ru> 0.7.5-alt1
- 0.7.5
- minor spec fixes regarding build process
- applied patches to fix obvious GCC warnings

* Mon Sep 26 2005 Andrei Bulava <abulava@altlinux.ru> 0.7.0-alt1
- 0.7.0-1
- updated BuildRequires
- minor fix to handle versioning of stable releases

* Mon Jun 13 2005 Andrei Bulava <abulava@altlinux.ru> 0.6.4-alt1
- initial build for ALT Linux
