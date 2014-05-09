#
# spec file for package libfdatetime
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

Name: libfdatetime
Version: 20130904
Release: alt1

Summary: A library for date and time data types
License: LGPL-3.0+
Group: Development/C

Url: http://code.google.com/p/libfdatetime/
#Git-Clone: http://code.google.com/p/libfdatetime
#DL-URL: https://googledrive.com/host/0B3fBvzttpiiSQlBfaUlYTmhzUjQ/libfdatetime-alpha-20130904.tar.gz
Source: %name-alpha-%version.tar.gz

BuildRequires: pkg-config
BuildRequires: pkgconfig(libcerror) >= 20130609
# not released by upstream as a standalone package
#BuildRequires:  pkgconfig(libcstring) >= 20120425

%description
A library for date and time data types.

%package devel
Summary: Development files for libfdatetime, a date and time data type library
Group: Development/C
Requires: %name = %version

%description devel
A library for date and time data types.

This subpackage contains libraries and header files for developing
applications that want to make use of libfdatetime.

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
* Fri May 09 2014 Michael Shigorin <mike@altlinux.org> 20130904-alt1
- initial build for ALT Linux Sisyphus

* Thu Nov 21 2013 Greg.Freemyer@gmail.com
- update to 20130904
  * code clean up
  * worked on tests
  * updated dependencies
  * textual changes
  * maximum string size is now only returned for invalid date time values
- change compression to gz to simplify updates
* Tue Jul 30 2013 Greg.Freemyer@gmail.com
- cleanup specfile comments
* Mon Apr 22 2013 Greg.Freemyer@gmail.com
- ran spec-cleaner
* Thu Apr  4 2013 jengelh@inai.de
- Initial package (version 20130317) for build.opensuse.org
