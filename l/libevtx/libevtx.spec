#
# spec file for package libevtx
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

Name: libevtx
Version: 20140323
Release: alt1

Summary: Library and tools to access the Windows XML Event Log (EVTX) format
License: LGPLv3+ and GFDLv1.3
Group: File tools

Url: http://code.google.com/p/libevtx/
#DL-URL: https://googledrive.com/host/0B3fBvzttpiiSRnQ0SExzX3JjdFE/libevtx-alpha-20131013.tar.gz
Source0: %name-alpha-%version.tar.gz
Source1: Windows_XML_Event_Log_(EVTX).pdf
Source2: %name.watch
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: pkg-config
BuildRequires: python-dev
BuildRequires: pkgconfig(libbfio) >= 20121003
BuildRequires: pkgconfig(libcdata) >= 20130407
BuildRequires: pkgconfig(libcfile) >= 20130609
BuildRequires: pkgconfig(libclocale) >= 20130609
BuildRequires: pkgconfig(libcnotify) >= 20130609
BuildRequires: pkgconfig(libcpath) >= 20130609
BuildRequires: pkgconfig(libcsplit) >= 20130609
BuildRequires: pkgconfig(libfdatetime) >= 20130317
BuildRequires: pkgconfig(libfguid) >= 20130317
BuildRequires: pkgconfig(libuna) >= 20130609
#build fails if the factory package is used, use the internal version
#verified 11/25/2013
#BuildRequires:  pkgconfig(libwrc) >= 20131017
#BuildRequires:  pkgconfig(libregf) >= 20130716
#BuildRequires:  pkgconfig(libcerror) >= 20120425
#packages not yet released by upstream
#BuildRequires:  pkgconfig(libcstring) >= 20120425
#BuildRequires:  pkgconfig(libcsystem) >= 20120425
#BuildRequires:  pkgconfig(libcdirectory) >= 20120425
#BuildRequires:  pkgconfig(libfvalue) >= 20120428
#BuildRequires:  pkgconfig(libfwevt) >= 20120426
#BuildRequires:  pkgconfig(libfwnt) >= 20120426
#BuildRequires:  pkgconfig(libexe) >= 20120405
#BuildRequires:  pkgconfig(libfcache) >= 20120405
#BuildRequires:  pkgconfig(libfdata) >= 20120405

%description
Library and tools to access the Windows XML Event Log (EVTX) format.
For the Windows pre-XML Event Log (EVT) format, see libevt.

%package tools
Summary: Utilities to export events from Windows XML event files (EVTX)
License: LGPLv3+
Group: File tools

%description tools
Tools for parsing EVTX files. These include evtxinfo and evtxexport.

%package devel
Summary: Development files for libevtx, a Windows XML Event file parser
License: LGPLv3+ and GFDLv1.3
Group: Development/C
Requires: %name = %version

%description devel
libevtx is a library to access the Windows XML Event log format.

This subpackage contains libraries and header files for developing
applications that want to make use of %name.

%package -n python-module-%name
Summary: Python bindings for libevtx
License: LGPLv3+
Group: Development/Python
Requires: python-base

%description -n python-module-%name
Python bindings for libevtx, which can read Windows XML Event files.

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
%_libdir/libevtx.so.*

%files tools
%_bindir/evtx*
%_man1dir/evt*.1*

%files devel
%doc Windows_XML_Event_Log*.pdf
%_includedir/*
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_man3dir/*

%files -n python-module-%name
%doc AUTHORS README
%python_sitelibdir/pyevtx.so

%changelog
* Sun May 11 2014 Michael Shigorin <mike@altlinux.org> 20140323-alt1
- new version (watch file uupdate)

* Sun May 11 2014 Michael Shigorin <mike@altlinux.org> 20131013-alt1
- initial build for ALT Linux Sisyphus

* Tue Nov 26 2013 Greg.Freemyer@gmail.com
- using internal libregf, latest factory update broke libevtx
* Mon Nov  4 2013 Greg.Freemyer@gmail.com
- update to 20131013
  * updated dependencies
- using internal libwrc, latest factory update broke libevtx
- removed  from buildrequires dependencies
* Wed Oct  2 2013 Greg.Freemyer@gmail.com
-  update to 20130923
  * updated dependencies
  * worked on libcthreads build support
* Wed Jul 31 2013 Greg.Freemyer@gmail.com
- update to 20130727
  * updated dependencies
  * pyevtx
  - changed event identifier to an unsigned long
  - fixes for >2G file objects in BFIO glue code
  - other updates and bug fixes
  * removed unnecessary restriction in library include headers
  * worked on tests
  * improved reading from dirty files with an incorrect number of chunks
  * fix for encoding special characters in XML output
  * added support for parsing ProcessingErrorData
  * worked on improving corruption detection for recovered records
  * textual changes
  * fixed codepage 1255 restriction
  * improvements to message string support
- changed to gz compression to simplyfy donwload/convert
- used factory version of libyal libraries if possible
* Mon Apr  8 2013 Greg.Freemyer@gmail.com
- update to 20130329
  * bug fix for recent libfdata changes
* Thu Apr  4 2013 jengelh@inai.de
- Cleanups: Set RPM group, license, summary and description
  metadata; remove unused %%py_requires; do not bloat shlib package
  with documentation
- Use system libraries instead of bundled ones where possible
- Name the tools package according to upstream's recommendation
- Drop unnecessary -fno-strict-aliasing
* Wed Mar 27 2013 Greg.Freemyer@gmail.com
- initial package (version 20130319) for build.opensuse.org
