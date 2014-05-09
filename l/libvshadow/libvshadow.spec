#
# spec file for package libvshadow
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

Name: libvshadow
Version: 20131003
Release: alt1

Summary: Library to access the Volume Shadow Snapshot (VSS) format
License: LGPLv3+ and GFDL-1.3+
Group: File tools

Url: http://code.google.com/p/libvshadow/
#DL-URL:         https://googledrive.com/host/0B3fBvzttpiiSZDZXRFVMdnZCeHc/libvshadow-alpha-20131003.tar.gz
Source: libvshadow-alpha-%version.tar.gz
Source1: Paper_-_Windowless_Shadow_Snapshots.pdf
Source2: Slides_-_Windowless_Shadow_Snapshots.pdf
Source3: Volume_Shadow_Snapshot_(VSS)_format.pdf
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: libfuse-devel
BuildRequires: pkg-config
BuildRequires: python-dev

BuildRequires: pkgconfig(libcdata) >= 20130407
BuildRequires: pkgconfig(libcdata) >= 20130407
BuildRequires: pkgconfig(libcfile) >= 20130609
BuildRequires: pkgconfig(libclocale) >= 20130609
BuildRequires: pkgconfig(libcnotify) >= 20130609
BuildRequires: pkgconfig(libcpath) >= 20130609
BuildRequires: pkgconfig(libuna) >= 20130609
BuildRequires: pkgconfig(libbfio) >= 20130908
BuildRequires: pkgconfig(libcthreads) >= 20130723

# These packages from factory cause build failures, use the internal version
# verified 10/1/2013
#BuildRequires:  pkgconfig(libcerror) > 20130904
#BuildRequires:  pkgconfig(libcsplit) > 20130904
# These packages are not released as separate packages by upstream.  Internal only
#BuildRequires:  pkgconfig(libcstring)
#BuildRequires:  pkgconfig(libcsystem)
#BuildRequires:  pkgconfig(libcmulti)
#BuildRequires:  pkgconfig(libfdatetime)
#BuildRequires:  pkgconfig(libfguid)

%description
Library and tools to access the Volume Shadow Snapshot (VSS) format.
The VSS format is used by Windows, as of Vista, to maintain copies
of data on a storage media volume.

The devel package contains:

    OSDFC 2012: Paper - Windowless Shadow Snapshots
    OSDFC 2012: Slides - Windowless Shadow Snapshots
    Volume_Shadow_Snapshot_(VSS)_format.pdf

%package tools
Summary: Tools to access the Volume Shadow Snapshot (VSS) format
License: LGPLv3+
Group: File tools

%description tools
Library and tools to access the Volume Shadow Snapshot (VSS) format.
The VSS format is used by Windows, as of Vista, to maintain copies
of data on a storage media volume.

%package devel
Summary: Development files for %name
License: LGPLv3+ and GFDL-1.3+
Group: Development/C
Requires: %name = %version

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n python-module-%name
Summary: Python binding for libvshadow
License: LGPLv3+
Group: Development/Python
Requires: %name = %version
Requires: python-base

%description -n python-module-%name
Python binding for libvshadow.  libvshadow can read windows event files.

%prep
%setup
mkdir doc
cp -a %SOURCE1 .
cp -a %SOURCE2 .
cp -a "%SOURCE3" .

%build
export CFLAGS="%optflags -fno-strict-aliasing"
export CXXFLAGS="%optflags"

%configure \
	--disable-static \
	--enable-wide-character-type \
	--enable-python

%make_build

%install
%makeinstall_std

%files
%doc doc
%_libdir/*.so.*

%files tools
%_bindir/vshadow*
%_man1dir/*.gz

%files devel
%doc AUTHORS ChangeLog ABOUT-NLS
%doc Paper_-_Windowless_Shadow_Snapshots.pdf
%doc Slides_-_Windowless_Shadow_Snapshots.pdf
%doc Volume_Shadow_Snapshot_*.pdf
%_includedir/*
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_man3dir/*

%files -n python-module-%name
%doc AUTHORS README
%python_sitelibdir/*.so

%changelog
* Fri May 09 2014 Michael Shigorin <mike@altlinux.org> 20131003-alt1
- initial build for ALT Linux Sisyphus

* Thu Oct  3 2013 Greg.Freemyer@gmail.com
- update to 20131003
  * Primarily Windows related improvements
- add libcthread as a standalone BuildRequires
- update BuildRequires for post 13.1 builds
* Fri Aug  2 2013 Greg.Freemyer@gmail.com
- add version levels to BuildRequires to due to a build failure with older libyal packages
* Sat Jul 27 2013 Greg.Freemyer@gmail.com
- update to 20130723
  * Changes for stand-alone libbfio build
  * remove unnecessary restriction in library include headers
  * updated dependencies
  * worked on multi-threading support
  * added libvshadow_volume_get_store_identifier function
  * added libcthreads
  * changes to read block descriptors on demand improves vshadowinfo preformance
  * fixes for multiple open/close on the same volume object
  * fixed issue in read buffer due to recent changes
  * added store read from file IO handle function
  * vshadowmount small changes
  * worked on tests
  * worked on vshadowmount Dokan support
- Added buildrequires for gcc
- Use factory libyal packages if possible
- Add BuildRequires for fuse-devel.  Required for vshadowmount in libvshadow-tools to work correctly.
* Wed Apr 17 2013 Greg.Freemyer@gmail.com
- update to 20130413
- make specfile more consistent with the other Joachim Metz packages in openSUSE
  * change version from 0.0.%%{timestamp} to %%{timestamp}
  * move developer docs to devel package
  * add BuildRequires for the internally provided libs
- add Volume_Shadow_Snapshot_(VSS)_format.pdf to devel package
* Wed Mar 27 2013 Greg.Freemyer@gmail.com
- initial package 20130304
