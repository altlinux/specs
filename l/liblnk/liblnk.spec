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
Version: 20240120
Release: alt1

Summary: Library and tools to access the Windows Shortcut File (LNK) format
License: LGPLv3+ and GFDL-1.3+
Group: File tools

Url: https://github.com/libyal/liblnk.git
#DL-URL: https://github.com/libyal/%name/releases/download/%version/%name-alpha-%version.tar.gz
Source: %name-alpha-%version.tar.gz
Source1: Windows_Shortcut_File_(LNK)_format.pdf
Source2: %name.watch
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: python3-dev
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

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

%package -n python3-module-%name
Summary: Python bindings for liblnk, a Windows Shortcut Link parser
License: LGPLv3+
Group: Development/Python

%description -n python3-module-%name
Python binding for liblnk, which can read Windows Shortcut Link files.

%prep
%setup
cp -a "%SOURCE1" .

%build
%autoreconf

%configure \
	--disable-static \
	--enable-wide-character-type \
	--enable-python \
	--with-pythondir=%python3_sitelibdir
%make_build

%install
%makeinstall_std
%pyproject_build

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

%files -n python3-module-%name
%doc AUTHORS README
%python3_sitelibdir/pylnk.so

%changelog
* Tue Feb 13 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 20240120-alt1
- new version 20240120
- build and pack pylnk as module

* Tue Feb 13 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 20140323-alt4
- watch file and url update

* Sat May 02 2020 Michael Shigorin <mike@altlinux.org> 20140323-alt3
- minor spec cleanup (thx ldv@)

* Sat May 02 2020 Michael Shigorin <mike@altlinux.org> 20140323-alt2
- avoid forbidden R: python-base

* Sat May 10 2014 Michael Shigorin <mike@altlinux.org> 20140323-alt1
- new version (watch file uupdate)

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
