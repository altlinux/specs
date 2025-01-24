#
# spec file for package libcdata
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

Name: libcdata
Version: 20240414
Release: alt1

Summary: Library for cross-platform C generic data functions
License: LGPLv3+
Group: Development/C

Url: https://github.com/libyal/libcdata
#DL-URL: https://github.com/libyal/libcdata/releases/download/20240414/libcdata-alpha-20240414.tar.gz
Source: %name-alpha-%version.tar.gz

BuildRequires: pkg-config
BuildRequires: pkgconfig(libcerror) >= 20240101
#not (yet) released as a standalone package by upstream
#BuildRequires:  pkgconfig(libcstring) >= 20120425

%description
A library for cross-platform C generic data functions.

This package is part of the libyal library collection
and is used by other libraries in the collection.

%package devel
Summary: Development files for libcdata, a cross-platform C generic data library
Group: Development/C
Requires: %name = %version

%description devel
A library for cross-platform C generic data functions.

This subpackage contains libraries and header files for developing
applications that want to make use of libcdata.

%prep
%setup

%build
%autoreconf

%configure \
	--disable-static \
	--enable-wide-character-type
%make_build

%install
%makeinstall_std

%check
%make check

%files
%doc AUTHORS ChangeLog
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_man3dir/*

%changelog
* Thu Jan 16 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 20240414-alt1
- New version 20240103.

* Fri May 09 2014 Michael Shigorin <mike@altlinux.org> 20130904-alt1
- initial build for ALT Linux Sisyphus

* Thu Oct  3 2013 Greg.Freemyer@gmail.com
- update to v20130904
  * added fail safe check in array
  * bug fix in array clone function
  * fix in .pc.in file
  * updated dependencies
  * bug fixes for recent changes
  * worked on multi-threading support
  * worked on tests
  * added libcthreads
  * updated msvscpp files
  * bug fix in range list
* Mon Jul 29 2013 Greg.Freemyer@gmail.com
- update to v20130407
  * small changes to range list
  * moved range list value to separate source files
  * added value support to range list
  * improved range list remove function to multiple ranges
  * textual updates
  * updated include header
  * added error functions
  * updated dependencies
  * added array prepend entry
  * added array reverse
  * 2013 update
- change from xz to gz to simplyfy download/convert step
* Mon Apr 22 2013 Greg.Freemyer@gmail.com
- run spec-cleaner
* Wed Apr  3 2013 jengelh@inai.de
- Initial package (version 20121224) for build.opensuse.org
