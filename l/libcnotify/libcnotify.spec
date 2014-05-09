#
# spec file for package libcnotify
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

Name: libcnotify
Version: 20130609
Release: alt1

Summary: Library for cross-platform C notify functions
License: LGPLv3+
Group: Development/C

Url: http://code.google.com/p/libcnotify/
#Git-Clone: http://code.google.com/p/libcnotify
#DL-URL: https://googledrive.com/host/0B3fBvzttpiiSb0xsMGNocEtGUjQ/libcnotify-alpha-20130609.tar.gz
Source: %name-alpha-%version.tar.gz
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: pkg-config
BuildRequires: pkgconfig(libcerror) >= 20130609
# libcstring is not in factory (yet)
#BuildRequires:  pkgconfig(libcstring) >= 20120425

%description
A library for cross-platform C notify functions.

%package devel
Summary: Development files for libcnotify, a cross-platform C notify library
Group: Development/C
Requires: %name = %version

%description devel
A library for cross-platform C notify functions.

This subpackage contains libraries and header files for developing
applications that want to make use of libcnotify.

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

* Tue Jul 30 2013 Greg.Freemyer@gmail.com
- update to v20130609
  * fix in .pc.in file
  * updated dependencies
  * 2013 update
- change compression to gz to simplyfy download/convert step
* Wed Apr  3 2013 jengelh@inai.de
- Initial package (version 20121224) for build.opensuse.org
