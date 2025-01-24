#
# spec file for package libcthreads
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

Name: libcthreads
Version: 20240413
Release: alt1

Summary: Library for cross-platform C threads functions
License: LGPLv3+
Group: Development/C

Url: https://github.com/libyal/libcthreads
#DL-URL: https://github.com/libyal/libcthreads/releases/download/20240413/libcthreads-alpha-20240413.tar.gz
Source: %name-experimental-%version.tar.gz

BuildRequires: pkg-config
BuildRequires: pkgconfig(libcerror) >= 20130904
# not yet released as a standalone package
#BuildRequires:  pkgconfig(libcstring) >= 20121224

%description
A library for cross-platform C threads functions.

libcthreads is part of the libyal library collection

%package devel
Summary: Development files for libcthreads, a cross-platform C thread library
Group: Development/C
Requires: %name = %version

%description devel
A library for cross-platform C thread functions.

This subpackage contains libraries and header files for developing
applications that want to make use of libcthreads.

%prep
%setup

%build
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
* Wed Jan 22 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 20240413-alt1
- New version 20240413.

* Fri May 09 2014 Michael Shigorin <mike@altlinux.org> 20130723-alt1
- initial build for ALT Linux Sisyphus

* Thu Oct  3 2013 Greg.Freemyer@gmail.com
- initial package (v20130723)
