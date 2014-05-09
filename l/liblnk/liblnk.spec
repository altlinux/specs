#
# spec file for package liblnk
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

Name: liblnk
Version: 20131015
Release: alt1

Summary: Library and tools to access the Windows Shortcut File (LNK) format
License: LGPLv3+ and GFDL-1.3+
Group: File tools

Url: http://code.google.com/p/liblnk/
#DL-URL: https://googledrive.com/host/0B3fBvzttpiiSQmluVC1YeDVvZWM/liblnk-alpha-20131015.tar.gz
Source: %name-alpha-%version.tar.gz
Source1: Windows_Shortcut_File_(LNK)_format.pdf
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: pkg-config
BuildRequires: python-dev
BuildRequires: pkgconfig(libbfio) >= 20130721
BuildRequires: pkgconfig(libcdata) >= 20130904
BuildRequires: pkgconfig(libcfile) >= 20130609
BuildRequires: pkgconfig(libclocale) >= 20130609
BuildRequires: pkgconfig(libcnotify) >= 20130609
BuildRequires: pkgconfig(libcpath) >= 20130609
BuildRequires: pkgconfig(libcsplit) >= 20130609
BuildRequires: pkgconfig(libfdatetime) >= 20130317
BuildRequires: pkgconfig(libfguid) >= 20130904
BuildRequires: pkgconfig(libuna) >= 20120425
# the below failed to compile with factory version as of Nov 1, 2013
#BuildRequires:  pkgconfig(libcerror) >= 20120425
# the below are not released as standalone packages by upstream
#BuildRequires:  pkgconfig(libfwsi) >= 20120426
#BuildRequires:  pkgconfig(libcsystem) >= 20120425
#BuildRequires:  pkgconfig(libcstring) >= 20120425

%description
liblnk is a library to access Windows Shortcut File (LNK) files.

%package tools
Summary: Tools to access the Windows Shortcut File (LNK) format
License: LGPLv3+
Group: File tools

%description tools
liblnk is a library to access Windows Shortcut File (LNK) files.

%package devel
Summary: Development files for liblnk, a library to access Windows Shortcut Links
License: LGPLv3+ and GFDL-1.3+
Group: Development/C
Requires: %name = %version

%description devel
liblnk is a library to access Windows Shortcut File (LNK) files.

This subpackage contains libraries and header files for developing
applications that want to make use of %name.

%package -n python-module-%name
Summary: Python bindings for liblnk, a Windows Shortcut Link parser
License: LGPLv3+
Group: Development/Python
Requires: python-base

%description -n python-module-%name
Python binding for liblnk, which can read Windows Shortcut Link files.

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
%_libdir/liblnk.so.*

%files tools
%_bindir/lnk*
%_man1dir/lnkinfo.1*

%files devel
%doc Windows_Shortcut_File_*.pdf
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_man3dir/*

%files -n python-module-%name
%doc AUTHORS README
%python_sitelibdir/pylnk.so

%changelog
* Sat May 10 2014 Michael Shigorin <mike@altlinux.org> 20131015-alt1
- initial build for ALT Linux Sisyphus

* Thu Nov 21 2013 Greg.Freemyer@gmail.com
- update to v20131015
  * updated dependencies
  * improved pyolecf as integer functions
  * worked on setup.py, largely for MSI builds
- cleanup BuildRequires statements
* Fri Sep 20 2013 Greg.Freemyer@gmail.com
- updated to v20130829
  * change to API to expose link target identifier data
  * fixes for building with stand-alone libuna and libbfio
  * updated dependencies
  * worked on automated tests
  * bug fix in pymsiecf file object libbfio glue code
  * worked on shell items
  - detection of delegate 0x2e item
  * fix in debug output for local path
  * worked on tests
  * textual changes
* Tue Jul 30 2013 Greg.Freemyer@gmail.com
- update to v20130413
  * updated dependencies
  * moved examples to project site
  * updated lnkinfo man page
  * worked on tests
  * updates and bug fixes in pylnk
  * fixed codepage 949, 950, 1255 restriction
  * added PackageMaker files
  * added functions to retrieve drive type, drive serial number and volume label
  * fix trailing \ for local and network path when common path is an emtpy string
- use gz compression to simplify download/convert
- use factory version of sub-packages as possible
* Fri Apr  5 2013 jengelh@inai.de
- Cleanups: Set RPM group, license, summary and description
  metadata; remove unused %%py_requires; do not bloat shlib package
  with documentation
- Use system libraries instead of bundled ones where possible
- Name the tools package according to upstream's recommendation
- Drop unnecessary -fno-strict-aliasing
- Drop Windows_Shell_Item pdf, this belongs to a different package
* Wed Mar 27 2013 Greg.Freemyer@gmail.com
- initial package (version 20130304) for build.opensuse.org
