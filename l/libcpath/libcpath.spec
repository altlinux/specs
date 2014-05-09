#
# spec file for package libcpath
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

Name: libcpath
Version: 20130809
Release: alt1

Summary: Library for cross-platform C path functions
License: LGPLv3+
Group: Development/C

Url: http://code.google.com/p/libcpath/
#Git-Clone: http://code.google.com/p/libcpath
#DL-URL: https://googledrive.com/host/0B3fBvzttpiiSOGFVQUwtOHlEWjQ/libcpath-alpha-20130809.tar.gz
Source: %name-alpha-%version.tar.gz
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: pkg-config
BuildRequires: pkgconfig(libcerror)  >= 20120425
BuildRequires: pkgconfig(libclocale) >= 20120425
BuildRequires: pkgconfig(libcsplit)  >= 20120701
BuildRequires: pkgconfig(libuna)     >= 20130609
# fails to build with these from factory, so use internal version
# none!!!!
# not (yet) in factory
#BuildRequires:  pkgconfig(libcstring)

%description
A library for cross-platform C path functions.

%package devel
Summary: Development files for libcpath, a cross-platform C path library
Group: Development/C
Requires: %name = %version

%description devel
A library for cross-platform C path functions.

This subpackage contains libraries and header files for developing
applications that want to make use of libcpath.

%prep
%setup

%build
%configure \
	--disable-static \
	--enable-wide-character-type
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_man3dir/*

%changelog
* Fri May 09 2014 Michael Shigorin <mike@altlinux.org> 20130809-alt1
- initial build for ALT Linux Sisyphus

* Thu Nov 14 2013 Greg.Freemyer@gmail.com
- update to v20130809
  * updated dependencies
- remove xz buildrequires, not needed
* Tue Jul 30 2013 Greg.Freemyer@gmail.com
- update to v20130609
  * fix in .pc.in file
  * removed CRT functions
  * updated dependencies
  * textual changes
  * small updates
  * 2013 update
- use gz compression to simplyfy download/convert
* Wed Apr  3 2013 jengelh@inai.de
- Initial package (version 20121225) for build.opensuse.org
