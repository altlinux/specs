#
# spec file for package libregf
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

Name: libregf
Version: 20140427
Release: alt3

Summary: Library to access Windows REGF-type Registry files
License: LGPL-3.0+ and GFDL-1.3+
Group: File tools

Url: http://code.google.com/p/libregf/
#DL-URL: https://googledrive.com/host/0B3fBvzttpiiSSC1yUDZpb3l0UHM/libregf-alpha-20140427.tar.gz
Source0: %name-alpha-%version.tar.gz
Source1: Windows_NT_Registry_File_(REGF)_format.pdf
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: pkg-config
BuildRequires: python-dev
BuildRequires: pkgconfig(fuse) >= 2.6
BuildRequires: pkgconfig(libbfio) >= 20131003
BuildRequires: pkgconfig(libcdata) >= 20130904
BuildRequires: pkgconfig(libcfile) >= 20130809
BuildRequires: pkgconfig(libclocale) >= 20130609
BuildRequires: pkgconfig(libcnotify) >= 20130609
BuildRequires: pkgconfig(libcpath) >= 20130809
BuildRequires: pkgconfig(libcsplit) >= 20130609
BuildRequires: pkgconfig(libfdatetime) >= 20130317
BuildRequires: pkgconfig(libuna) >= 20130728
# Using these packages from factory causes build failures, so use the internal version instead
# Verified 11/15/2013
#BuildRequires:  pkgconfig(libfguid) >= 20120426
#BuildRequires:  pkgconfig(libcerror) >= 20120425
# These packages are not yet released by upstream as standalone packages
#BuildRequires:  pkgconfig(libcstring) >= 20120425
#BuildRequires:  pkgconfig(libcsystem) >= 20120425
#BuildRequires:  pkgconfig(libfcache) >= 20120425
#BuildRequires:  pkgconfig(libfdata) >= 20120425
#BuildRequires:  pkgconfig(libfwnt) >= 20120426
#BuildRequires:  pkgconfig(libfwsi) >= 20120426

%description
libregf is a library to access Windows Registry files of the REGF
type (a non-text representation).

%package tools
Summary: Utilities to inspect Windows REGF-type Registry files
License: LGPL-3.0+
Group: File tools

%description tools
Several tools for inspecting Windows REGF-type Registry files.
Typically used for computer forensics.

%package devel
Summary: Development files for libregf, a Windows REGF-type Registry file parser
License: LGPL-3.0+ and GFDL-1.3+
Group: Development/C
Requires: %name = %version

%description devel
libregf is a library to access Windows Registry files of the REGF
type (a non-text representation).

This subpackage contains libraries and header files for developing
applications that want to make use of %name.

%package -n python-module-%name
Summary: Python bindings for libregf, a library to access Windows REGF Registry files
License: LGPL-3.0+
Group: Development/Python

%description -n python-module-%name
libregf is a library to access Windows Registry files of the REGF
type (a non-text representation).

This subpackage contains the Python bindings for libregf.

%prep
%setup
cp -a "%SOURCE1" .

%build
%configure \
	--disable-static \
	--enable-wide-character-type \
	--enable-python
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog
%_libdir/libregf.so.*

%files tools
%_bindir/regf*
%_man1dir/regf*.1*

%files devel
%doc Windows_NT_Registry_File*.pdf
%_includedir/*
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_man3dir/*

%files -n python-module-%name
%doc AUTHORS README
%python_sitelibdir/pyregf.so

%changelog
* Fri Apr 01 2022 Grigory Ustinov <grenka@altlinux.org> 20140427-alt3
- Simple rebuild with release rising.

* Sat May 02 2020 Michael Shigorin <mike@altlinux.org> 20140427-alt2
- minor spec cleanup (thx ldv@)

* Thu May 08 2014 Michael Shigorin <mike@altlinux.org> 20140427-alt1
- initial build for ALT Linux Sisyphus (suggested by Maxim Suhanov)

* Sat Nov 23 2013 Greg.Freemyer@gmail.com
- update to v20131013
- clean up buildrequires
- use libyal packages from factory if feasible
* Wed Oct  2 2013 Greg.Freemyer@gmail.com
- update to v20130922
  * removed hardcoded codepages from value functions
  * worked on automated tests
  * updated dependencies
* Tue Aug 27 2013 Greg.Freemyer@gmail.com
- update to v20130821
  * fix in pyregf value data as integer function for bounds check being too strict
* Tue Jul 30 2013 Greg.Freemyer@gmail.com
- update to v20130716
  * updated dependencies
  * worked on tests
  * bug fix for large values
  * added support for REG_LINK as a string
  * fixed multiple open issues
  * pyregf: fix for retrieving default value by name
  * worked on tests
  * changes for strings values with trailing data
  * small update for 64-bit build
  * Textual changes
  * updates and bug fixes in pyregf
  * fixed codepage 1255 restriction
  * fixed codepage 949 and 950 restriction
  * changes for libfdata update
  * removed item flags
- changed to gz compression to simplyfy download/convert
* Mon Apr 22 2013 Greg.Freemyer@gmail.com
- organize BuildRequires to better comment why they are commented out
- ran spec-cleaner
* Wed Apr  3 2013 jengelh@inai.de
- Cleanups: Set RPM group, license, summary and description
  metadata; less greedy fileslists; remove unused %%py_requires;
  do not bloat shlib package with documentation
- Enable FUSE support
- Use system libraries instead of bundled ones where possible
- Name the tools package according to upstream's recommendation
- Drop unnecessary -fno-strict-aliasing
* Wed Mar 27 2013 Greg.Freemyer@gmail.com
- initial package (version 20130319) for build.opensuse.org
