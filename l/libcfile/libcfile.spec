#
# spec file for package libcfile
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

Name: libcfile
Version: 20130809
Release: alt1

Summary: Library for cross-platform C file functions
License: LGPLv3+
Group: Development/C

Url: http://code.google.com/p/libcfile/
#Git-Clone: http://code.google.com/p/libcfile
#DL-URL: https://googledrive.com/host/0B3fBvzttpiiSem41RXpvQkIyZlU/libcfile-alpha-20130809.tar.gz
Source: %name-alpha-%version.tar.gz
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: pkg-config
BuildRequires: pkgconfig(libcerror) >= 20130609
BuildRequires: pkgconfig(libclocale) >= 20130609
BuildRequires: pkgconfig(libcnotify) >= 20130103
# This can cause a build loop.  The internal version should be used.
#BuildRequires:  pkgconfig(libuna) >= 20120425
# The below have not been released as standalone packages by upstream
#BuildRequires:  pkgconfig(libcstring)

%description
A library for cross-platform C file functions.

%package devel
Summary: Development files for libcfile, a cross-platform C file library
Group: Development/C
Requires: %name = %version

%description devel
A library for cross-platform C file functions.

This subpackage contains libraries and header files for developing
applications that want to make use of libcfile.

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

* Tue Dec  3 2013 coolo@suse.com
- don't buildrequire ourselves
* Wed Oct 23 2013 Greg.Freemyer@gmail.com
- update to v20130809
  * bug fix for file access behavior
- update BuildRequires to use factory versions of packages when possible
* Mon Jul 29 2013 Greg.Freemyer@gmail.com
- update to v20130609
  * fix in .pc.in file
  * updated dependencies
  * removed WINAPI CRT function fallbacks
  * changes to ioctl detection in configure
  * textual changes
- change to gz compression to simplyfy download/convert step
* Mon Apr 22 2013 Greg.Freemyer@gmail.com
- add BuildRequires: libcnotify
- run spec-cleaner
* Wed Apr  3 2013 jengelh@inai.de
- Initial package (version 20130329) for build.opensuse.org
