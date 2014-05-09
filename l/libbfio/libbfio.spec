#
# spec file for package libbfio
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

Name: libbfio
Version: 20131003
Release: alt1

Summary: Library to provide basic file input/output abstraction
License: LGPLv3+
Group: Development/C++

Url: http://code.google.com/p/libbfio/
#DL-URL: https://googledrive.com/host/0B3fBvzttpiiSTERGV3V4bnZ3dlk/libbfio-alpha-20131003.tar.gz
Source: %name-alpha-%version.tar.gz
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: pkg-config
BuildRequires: pkgconfig(libcdata) >= 20130904
BuildRequires: pkgconfig(libcfile) >= 20120425
BuildRequires: pkgconfig(libclocale) >= 20120425
BuildRequires: pkgconfig(libcnotify) >= 20130609
BuildRequires: pkgconfig(libcpath) >= 20120425
BuildRequires: pkgconfig(libcsplit) >= 20130609
BuildRequires: pkgconfig(libcthreads) >= 20130723
BuildRequires: pkgconfig(libuna) >= 20120425
# verified July 29, 2013, builds fail with these enabled
#BuildRequires:  pkgconfig(libcerror) > 20130904
# Not released as a standalone package by upstream
#BuildRequires:  pkgconfig(libcstring)

%description
libbfio is used in multiple other libraries like libewf, libmsiecf,
libnk2, libolecf and libpff. It is used to chain I/O to support
file-in-file access.

%package devel
Summary: Development files for libbfio, a basic file input/output abstraction library
Group: Development/C
Requires: %name = %version

%description devel
libbfio is used in multiple other libraries like libewf, libmsiecf,
libnk2, libolecf and libpff. It is used to chain I/O to support
file-in-file access.

This subpackage contains libraries and header files for developing
applications that want to make use of libbfio.

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
%doc AUTHORS COPYING ChangeLog
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_man3dir/*

%changelog
* Fri May 09 2014 Michael Shigorin <mike@altlinux.org> 20131003-alt1
- initial build for ALT Linux Sisyphus

* Wed Oct 23 2013 Greg.Freemyer@gmail.com
- update to v0~20131003
* Thu Oct  3 2013 Greg.Freemyer@gmail.com
- update to v0~20130908
  * worked on tests
  * updated dependencies
- updated dependencies in specfile
* Mon Jul 29 2013 Greg.Freemyer@gmail.com
- update to v0~20130721
  * worked on multi threading support
  * removed open on demand code from seek offset
  * refactored pool to use a cdata array
  * worked on tests
  * updated dependencies
  * fix for compiling with stand-alone version of libcdata
  * fix in .pc.in file
  * worked on git release
  * moved examples to project page
  * removed codegear files
  * remove libbfio_legacy.[ch]
  * 2013 update
- change to gz compression to simplyfy download/convert step
* Mon Apr 22 2013 Greg.Freemyer@gmail.com
- run spec-cleaner, update comment
* Wed Apr  3 2013 jengelh@inai.de
- Initial package (version 0~20121225) for build.opensuse.org
