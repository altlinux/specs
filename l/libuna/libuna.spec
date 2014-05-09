#
# spec file for package libuna
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name: libuna
Version: 20130728
Release: alt1

Summary: Library to support Unicode and ASCII (byte string) conversions
License: LGPLv3+
Group: Development/C

Url: http://code.google.com/p/libuna/
#DL-URL: https://googledrive.com/host/0B3fBvzttpiiSaXBjN1ZJVzVsbjQ/libuna-alpha-20130728.tar.gz
Source: %name-alpha-%version.tar.gz
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: pkg-config
BuildRequires: pkgconfig(libcfile) >= 20120526
BuildRequires: pkgconfig(libclocale) >= 20120425
BuildRequires: pkgconfig(libcnotify) >= 20121224
# these fail to build with factory version, so use internal version.  Verified 10/20/13
#BuildRequires:  pkgconfig(libcerror) > 20130904

%description
libuna is a library to support Unicode and ASCII (byte string)
conversions. It currently supports: 7-bit ASCII, ISO 8859-{1..15},
Windows 874, 932, 936, 949, 950, 1250, 1251, 1252, 1253, 1254, 1255,
1256, 1257, 1258, KOI8-R, KOI8-U, UTF-7, UTF-8, UTF-16, UTF-32.

%package tools
Summary: Utilities from libuna for Unicode/ASCII Byte Stream conversions
Group: Text tools

%description tools
Several tools for converting Unicode and ASCII (byte stream) based text.

%package devel
Summary: Development files for libuna, a library to support Unicode/ASCII conversions
Group: Development/C
Requires: %name = %version

%description devel
libuna is a library to support Unicode and ASCII (byte string)
conversions.

This subpackage contains libraries and header files for developing
applications that want to make use of libuna.

%prep
%setup

%build
%configure \
	--disable-static \
	--enable-wide-character-type \
	--enable-python
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog ABOUT-NLS
%_libdir/*.so.*

%files tools
%_bindir/*
%_man1dir/*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_man3dir/*

%changelog
* Fri May 09 2014 Michael Shigorin <mike@altlinux.org> 20130728-alt1
- initial build for ALT Linux Sisyphus

* Wed Oct 23 2013 Greg.Freemyer@gmail.com
- update to v20130728
  * fixes for some stream functions being too strict
- fix version numbers on dependancies to not have  in them
* Sat Jul 27 2013 Greg.Freemyer@gmail.com
- update to v20130609
  * fix in .pc.in file
  * updated dependencies
  * fixes issues for building with stand-alone version of libcnotify
  * removed date time functionality from libcsystem
- change to gz compression for tarball to eliminate conversion from download
- use libyal libraries from factory where posible, not internal versions
* Mon Apr 22 2013 Greg.Freemyer@gmail.com
- run spec-cleaner
- add comments about why internal libraries are being used
* Wed Apr  3 2013 jengelh@inai.de
- Initial package (version 20130103) for build.opensuse.org
