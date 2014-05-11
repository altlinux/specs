#
# spec file for package libwrc
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

Name: libwrc
Version: 20140328
Release: alt1

Summary: Library to support the Windows Resource Compiler format
License: LGPLv3+
Group: File tools

Url: http://code.google.com/p/libexe/
#DL-URL: https://googledrive.com/host/0B3fBvzttpiiSYTdIQVF0Z2hKRTA/libwrc-experimental-20131017.tar.gz
Source0: %name-experimental-%version.tar.gz
Source1: %name.watch
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: pkg-config
BuildRequires: pkgconfig(libbfio) >= 20120426
BuildRequires: pkgconfig(libcdata) >= 20120425
BuildRequires: pkgconfig(libcfile) >= 20120526
BuildRequires: pkgconfig(libclocale) >= 20130609
BuildRequires: pkgconfig(libcnotify) >= 20120425
BuildRequires: pkgconfig(libcpath) >= 20130609
BuildRequires: pkgconfig(libcsplit) >= 20130904
BuildRequires: pkgconfig(libfdatetime) >= 20130317
BuildRequires: pkgconfig(libfguid) >= 20130317
BuildRequires: pkgconfig(libuna) >= 20130728
#  The following packages cause build failures if factory version is used, verified Oct 23, 2013
#BuildRequires:  pkgconfig(libcerror) >= 20120425
#  The following packages cause build failures if the internal version is not used
#  These libraries are not yet released as standalone packages by upstream
#BuildRequires:  pkgconfig(libcstring) >= 20120425
#BuildRequires:  pkgconfig(libexe) >= 20120405
#BuildRequires:  pkgconfig(libfcache) >= 20120405
#BuildRequires:  pkgconfig(libfdata) >= 20120405
#BuildRequires:  pkgconfig(libfvalue) >= 20120428
#BuildRequires:  pkgconfig(libfwevt) >= 20120426
#BuildRequires:  pkgconfig(libfwnt) >= 20120426

%description
libwrc is a library to support the Windows Resource Compiler format.

%package devel
Summary: Development files for libwrc, a Windows Resouce Compiler format support library
Group: Development/C
Requires: %name = %version

%description devel
libwrc is a library to support the Windows Resource Compiler format.

This subpackage contains libraries and header files for developing
applications that want to make use of libwrc.

%package tools
Summary: Utilities to inspect Windows Resource Compiler files
Group: File tools

%description tools
This subpackage provides the utilities from libwrc, which allows for
reading Windows Resource Compiler files.

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

%files tools
%_bindir/*
%_man1dir/*

%changelog
* Sun May 11 2014 Michael Shigorin <mike@altlinux.org> 20140328-alt1
- new version (watch file uupdate)

* Sun May 11 2014 Michael Shigorin <mike@altlinux.org> 20131017-alt1
- initial build for ALT Linux Sisyphus

* Wed Oct 23 2013 Greg.Freemyer@gmail.com
- updated to v20131017
  * updated dependencies
  * worked on libcthreads build support
  * Worked on version resource support
  * added pywrc
  * 2013 update
  * changes for libfdata update
- converted to gz compression to eliminate conversion during update
- verified BuildRequires and used version from factory when possible
* Mon Apr 22 2013 Greg.Freemyer@gmail.com
- re-organize BuildRequires and comment why commented out
- uncomment BuildRequires (libcnotify) since the version in factory seems to work fine
- ran spec-cleaner
* Wed Apr  3 2013 jengelh@inai.de
- Initial package (version 20121225) for build.opensuse.org
