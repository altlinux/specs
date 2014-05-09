#
# spec file for package libclocale
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

Name: libclocale
Version: 20130609
Release: alt1

Summary: Library for cross-platform C locale functions
License: LGPLv3+
Group: Development/C

Url: http://code.google.com/p/libclocale/
#Git-Clone: http://code.google.com/p/libcerror
#DL-URL: https://googledrive.com/host/0B3fBvzttpiiSNVJabTctdi1qblE/libclocale-experimental-20130609.tar.gz
Source: %name-experimental-%version.tar.gz
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: pkg-config
BuildRequires: pkgconfig(libcerror) >= 20130609

%description
A library for cross-platform C locale functions.

%package devel
Summary: Development files for libclocale, a cross-platform C locale library
Group: Development/C
Requires: %name = %version

%description devel
A library for cross-platform C locale functions.

This subpackage contains libraries and header files for developing
applications that want to make use of libclocale.

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
* Fri May 09 2014 Michael Shigorin <mike@altlinux.org> 20130609-alt1
- initial build for ALT Linux Sisyphus

* Mon Jul 29 2013 Greg.Freemyer@gmail.com
- update to v0~20130609
  * fix in .pc.in file
  * fixes for stand-alone usage on netbsd
  * fixes for stand-alone usage
  * small changes
  * updated dependencies
  * fix for missing LOCALEDIR
  * 2013 update
- change to gz compression from xz
* Wed Apr  3 2013 jengelh@inai.de
- Initial package (version 0~20121224) for build.opensuse.org
