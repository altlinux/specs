#
# spec file for package libfguid
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

Name: libfguid
Version: 20130904
Release: alt1

Summary: A library for GUID/UUID data types
License: LGPLv3+
Group: Development/C

Url: http://code.google.com/p/libfguid/
#Git-Clone: http://code.google.com/p/libfguid
#DL-URL: https://googledrive.com/host/0B3fBvzttpiiSRXdGUVRlX2JQWk0/libfguid-alpha-20130904.tar.gz
Source: %name-alpha-%version.tar.gz
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: pkg-config
BuildRequires: pkgconfig(libcerror) >= 20130609
#not released by upstream
#BuildRequires:  pkgconfig(libcstring) >= 20120425

%description
A library for GUID/UUID data types.

%package devel
Summary: Development files for libfguid, a GUID/UUID data type library
Group: Development/C
Requires: %name = %version

%description devel
A library for GUID/UUID data types.

This subpackage contains libraries and header files for developing
applications that want to make use of libfguid.

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
* Sat May 10 2014 Michael Shigorin <mike@altlinux.org> 20130904-alt1
- initial build for ALT Linux Sisyphus

* Thu Nov 14 2013 Greg.Freemyer@gmail.com
-  update to 20130904
  * worked on tests
  * definitions fix
  * updated dependencies
  * textual changes
- converted to gz compression to simplify updating
- remove buildrequires xz
* Tue Jul 30 2013 Greg.Freemyer@gmail.com
- update comments in specfile
* Mon Apr 22 2013 Greg.Freemyer@gmail.com
- ran spec-cleaner
* Thu Apr  4 2013 jengelh@inai.de
- Initial package (version 20130317) for build.opensuse.org
