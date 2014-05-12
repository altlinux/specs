#
# spec file for package libpff
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

Name: libpff
Version: 20131028
Release: alt1

Summary: Library and tools to access Microsoft PFF and OFF format files
License: LGPLv3+ and GFDLv1.1+ and GFDLv1.3+
Group: File tools

Url: http://code.google.com/p/libpff/
#DL-URL:        https://googledrive.com/host/0B3fBvzttpiiScU9qcG5ScEZKZE0/libpff-experimental-20130722.tar.gz
Source0: %name-experimental-%version.tar.gz
Source1: %name.watch
Source2: PFF_Forensics_-_analyzing_the_horrible_reference_file_format.pdf
Source3: PFF_forensics_-_e-mail_and_appoinment_falsification_analysis.pdf
Source4: Personal_Folder_File_(PFF)_format.pdf
Source5: MAPI_definitions.pdf
Source6: libpff-libfdata.pdf
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: pkg-config
BuildRequires: python-dev
BuildRequires: pkgconfig(libcsplit) >= 20130609
BuildRequires: pkgconfig(libcfile) >= 20130609
BuildRequires: pkgconfig(libcpath) >= 20130609
BuildRequires: pkgconfig(libclocale) >= 20130609
BuildRequires: pkgconfig(libbfio) >= 20130721
# fails to build with factory package, use internal
# verified 7/31/2013
#BuildRequires:  pkgconfig(libcerror) >= 20120425
#BuildRequires:  pkgconfig(libcnotify) >= 20120425
#BuildRequires:  pkgconfig(libfguid) >= 20120426
#BuildRequires:  pkgconfig(libuna) >= 20120425
#BuildRequires:  pkgconfig(libfdatetime) >= 20120522
# not (yet) released as packages by upstream
#BuildRequires:  pkgconfig(libfmapi) >= 20120405
#BuildRequires:  pkgconfig(libfvalue) >= 20120428
#BuildRequires:  pkgconfig(libfwnt) >= 20120426
#BuildRequires:  pkgconfig(libcstring) >= 20120425
#BuildRequires:  pkgconfig(libcsystem) >= 20120425
#BuildRequires:  pkgconfig(libfcache) >= 20120405
#BuildRequires:  pkgconfig(libfdata) >= 20120405

%description
libpff is a library to access the Personal Folder File (PFF) and the
Offline Folder File (OFF) format. These are used in several file
Types: PAB (Personal Address Book), PST (Personal Storage Table) and
OST (Offline Storage Table).

%package tools
Summary: Tools to access Microsoft PST and OST files
License: LGPLv3+
Group: File tools
Requires: %name = %version

%description tools
Tools to access the Personal Folder File (PFF) and the Offline Folder
File (OFF) format. These are used in several file types: PAB
(Personal Address Book), PST (Personal Storage Table) and OST
(Offline Storage Table).

%package devel
Summary: Development files for libpff, a PFF/OFF file format library
License: LGPLv3+ and GFDL-1.1+ and GFDLv1.3+
Group: Development/C
Requires: %name = %version

%description devel
libpff is a library to access the Personal Folder File (PFF) and the
Offline Folder File (OFF) format. These are used in several file
Types: PAB (Personal Address Book), PST (Personal Storage Table) and
OST (Offline Storage Table).

This subpackage contains libraries and header files for developing
applications that want to make use of libpff.

%package -n python-module-%name
Summary: Python bindings for libpff, a PFF/OFF file format parser
License: LGPLv3+
Group: Development/Python
Requires: python-base

%description -n python-module-%name
Python bindings for libpff, which can read Personal Folder File (PFF)
and Offline Folder File (OFF) formats.

%prep
%setup
cp -a "%{S:2}" "%{S:3}" "%{S:4}" "%{S:5}" "%{S:6}" .

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
%_libdir/*.so.*

%files tools
%doc AUTHORS ChangeLog
%_bindir/*
%_man1dir/*

%files devel
%doc AUTHORS README ChangeLog
%doc MAPI_definitions.pdf
%doc PFF_Forensics_-_analyzing_the_horrible_reference_file_format.pdf
%doc PFF_forensics_-_e-mail_and_appoinment_falsification_analysis.pdf
%doc Personal_Folder_File_*.pdf
%_includedir/*
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_man3dir/*

%files -n python-module-%name
%python_sitelibdir/pypff.so

%changelog
* Mon May 12 2014 Michael Shigorin <mike@altlinux.org> 20131028-alt1
- new version (watch file uupdate)

* Mon May 12 2014 Michael Shigorin <mike@altlinux.org> 20130722-alt1
- re-initial build for ALT Linux Sisyphus
  + spec based on typical opensuse factory one
  + pre-existing changelog merged just in case

* Wed Jul 31 2013 Greg.Freemyer@gmail.com
- update to v20130722
  * major refactor of code, packaged redesignated experimental
  * Worked on compressed OST support
  * worked on pypff
  * worked on tests
  * fix for handling floating point values in item file
  * updated dependencies
  * worked on API by_utf8_name and by_utf16_name functions
  * worked on libcdata rewrite
  * worked on libfdata update
  * worked on 64-bit 4k page file format support
  * bug fixes in error path
  * improved debug output
  * pffexport:
  - worked on IPM.DistList support
  - added message flags
  - improved output of flag types
  * libfmapi
  - improved debug output
  - fixes in error code paths
  * tests:
  - added pffinfo test
  * 2013 update
- changed to gz compression to simplyfy download/convert
- use all libyal factory packages possible
* Mon Apr 29 2013 kaanozdincer@gmail.com
- Make specfile more consistent with the other Joachim Metz packages.
- Move developer docs to devel package.

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 20100510-alt1.qa1
- NMU: rebuilt for debuginfo.

* Fri Apr  5 2013 jengelh@inai.de
- Cleanups: Set RPM group, summary and description metadata
- Use system libraries instead of bundled ones where possible
- Name the tools package according to upstream's recommendation
- Drop unnecessary -fno-strict-aliasing
* Wed Apr  3 2013 Greg.Freemyer@gmail.com
- Put documentation in -devel; do not bloat the shlib package
- Set licenses in each sub-package
- Remove unused %%py_requires
* Mon Apr  1 2013 Greg.Freemyer@gmail.com
- initial package (version 0.0.20120802) - alpha quality software

* Fri Jul 09 2010 Fr. Br. George <george@altlinux.ru> 20100510-alt1
- Initial build for ALT

* Sun Mar 28 2010 Joachim Metz <jbmetz@users.sourceforge.net> 20100328-1
- Email change

* Sat Aug 29 2009 Joachim Metz <forensics@hoffmannbv.nl> 20090829-1
- Fix for empty requires and build requires

* Thu May 21 2009 Joachim Metz <forensics@hoffmannbv.nl> 20090521-1
- Corrected typo in autoconf/make macros

* Sat Mar 21 2009 Joachim Metz <forensics@hoffmannbv.nl> 20090321-1
- Changed comment

* Sat Jan 24 2009 Joachim Metz <forensics@hoffmannbv.nl> 20090124-1
- Added support for libbfio

* Tue Dec 16 2008 Joachim Metz <forensics@hoffmannbv.nl> 20081216-1
- Changed project URL

* Sat Oct 19 2008 Joachim Metz <forensics@hoffmannbv.nl> 20081018-1
- Added pffexport and pffrecover
- Added support for libuna

* Mon Sep 1 2008 Joachim Metz <forensics@hoffmannbv.nl> 20080901-1
- Small adjustments to text
- Removed old requires and build requires

* Sun May 11 2008 Joachim Metz <forensics@hoffmannbv.nl> 20080511-1
- Initial version based on libtableau spec file
