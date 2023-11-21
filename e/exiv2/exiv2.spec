%def_enable snapshot
%define beta %nil

%def_enable video
%def_enable curl
%def_enable webready
%def_disable ssh
%def_enable tests
%ifarch armh aarch64
%def_disable check
%else
%def_disable check
%endif

Name: exiv2
Version: 0.28.1
Release: alt1%beta

Summary: Command line tool to access EXIF data in image files
License: GPL-2.0-or-later
Group: Graphics
Url: http://www.exiv2.org

%if_disabled snapshot
Source: https://github.com/Exiv2/%name/archive/v%version/%name-%version.tar.gz
%else
Vcs: https://github.com/Exiv2/exiv2.git
Source: %name-%version.tar
%endif
Requires: lib%name = %EVR

BuildRequires(pre): rpm-macros-cmake
BuildRequires: /proc cmake gcc-c++ python3
BuildRequires: libexpat-devel zlib-devel
BuildRequires: libbrotli-devel libinih-devel
BuildRequires: doxygen xsltproc graphviz
%{?_enable_tests:BuildRequires: libgtest-devel}
%{?_enable_curl:BuildRequires: libcurl-devel}
%{?_enable_webready:BuildRequires: libcurl-devel libssh-devel libgcrypt-devel}
%{?_enable_check:BuildRequires: ctest}

%description
Exiv2 comprises of a C++ library and a command line utility to access
image metadata. Exiv2 supports full read and write access to the EXIF and
IPTC metadata, EXIF MakerNote support, extract and delete methods for
EXIF thumbnails, classes to access IFD and so on.

%package -n libexiv2
Summary: EXIF and IPTC metadata manipulation library
Group: Graphics

%description -n libexiv2
libexiv2 is a C++ library to access image metadata.

%package -n libexiv2-devel
Summary: Headers and links to compile against the exiv2 library
Group: Development/C
Requires: libexiv2 = %EVR

%description -n libexiv2-devel
This package contains all files which one needs to compile programs using the
exiv2 library.

%prep
%setup -n %name-%version

%build
%add_optflags -Wno-deprecated-declarations %(getconf LFS_CFLAGS)
%cmake \
	-DEXIV2_ENABLE_NLS:BOOL=ON \
	-DEXIV2_BUILD_SAMPLES:BOOL=OFF \
	-DEXIV2_ENABLE_BMFF:BOOL=ON \
	%{?_enable_video:-DEXIV2_ENABLE_VIDEO:BOOL=ON} \
	%{?_enable_curl:-DEXIV2_ENABLE_CURL:BOOL=ON} \
	%{?_enable_webready:-DEXIV2_ENABLE_WEBREADY:BOOL=ON} \
	%{?_enable_ssh:-DEXIV2_ENABLE_SSH:BOOL=ON} \
	%{?_enable_tests:-DEXIV2_BUILD_UNIT_TESTS:BOOL=ON}
%nil
%cmake_build

%install
%cmake_install
%find_lang exiv2

%check
%ctest

%files
%_bindir/%name
%_man1dir/*
%doc README* doc/ChangeLog

%files -n libexiv2 -f exiv2.lang
%_libdir/lib%name.so.*

%files -n libexiv2-devel
%_libdir/lib%name.so
%_includedir/%name/
%_pkgconfigdir/%name.pc
%_libdir/cmake/%name/


%changelog
* Wed Nov 08 2023 Yuri N. Sedunov <aris@altlinux.org> 0.28.1-alt1
- v0.28.1-1-gc351c7cce

* Mon Oct 23 2023 Yuri N. Sedunov <aris@altlinux.org> 0.28.0-alt1
- v0.28.0-79-g42e2f62a2
- built with current gcc

* Tue Jul 04 2023 Yuri N. Sedunov <aris@altlinux.org> 0.27.7-alt1.1
- enabled BMFF support (ALT #46748)

* Tue May 16 2023 Yuri N. Sedunov <aris@altlinux.org> 0.27.7-alt1
- 0.27.7

* Fri Jan 20 2023 Yuri N. Sedunov <aris@altlinux.org> 0.27.6-alt1
- 0.27.6

* Mon Oct 25 2021 Yuri N. Sedunov <aris@altlinux.org> 0.27.5-alt1
- 0.27.5 (https://github.com/Exiv2/exiv2/issues/1018#issuecomment-948573657)

* Fri Aug 27 2021 Yuri N. Sedunov <aris@altlinux.org> 0.27.4-alt1.2
- set optflags_lto to %%nil while we use gcc-9 to build

* Fri Jun 18 2021 Yuri N. Sedunov <aris@altlinux.org> 0.27.4-alt1.1
- fixed build on %%e2k

* Tue Jun 15 2021 Yuri N. Sedunov <aris@altlinux.org> 0.27.4-alt1
- 0.27.4 (fixed CVE-2021-3482, CVE-2021-29457,
  CVE-2021-29458, CVE-2021-29470, CVE-2021-29473,
  CVE-2021-29623, CVE-2021-32617)
- adapted to new cmake macros
- enabled NLS support
- used gcc-9 to avoid mass rebuild
- disabled tests broken with googletest-1.11.0-alt1

* Wed Jul 01 2020 Yuri N. Sedunov <aris@altlinux.org> 0.27.3-alt1
- 0.27.3

* Sat Aug 10 2019 Yuri N. Sedunov <aris@altlinux.org> 0.27.2-alt1
- 0.27.2

* Mon Apr 01 2019 Michael Shigorin <mike@altlinux.org> 0.26-alt3
- E2K: tweaked CVE-2017-17725 patch to fix ftbfs with lcc-1.23

* Tue Aug 07 2018 Yuri N. Sedunov <aris@altlinux.org> 0.26-alt2
- applied set of fc/upstream patches (fixed CVE-2017-11683,
  CVE-2017-14859, CVE-2017-14860, CVE-2017-14862,
  CVE-2017-14864, CVE-2017-17669, CVE-2017-17723,
  CVE-2017-17725, CVE-2018-10958, CVE-2018-10998,
  CVE-2018-11531, CVE-2018-12264, CVE-2018-12265,
  CVE-2018-14046, CVE-2018-5772, CVE-2018-8976,
  CVE-2018-8977)

* Sun May 07 2017 Yuri N. Sedunov <aris@altlinux.org> 0.26-alt1
- 0.26

* Sun Jun 28 2015 Yuri N. Sedunov <aris@altlinux.org> 0.25-alt1
- 0.25
- explicitly enabled video files and WebReady support

* Mon Jun 15 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.24-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Mon Dec 02 2013 Yuri N. Sedunov <aris@altlinux.org> 0.24-alt1
- 0.24

* Sun May 13 2012 Yuri N. Sedunov <aris@altlinux.org> 0.23-alt1
- 0.23
- fixed interpackage dependencies
- enabled LFS support

* Thu Feb 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.22-alt1.1
- Removed bad RPATH

* Thu Sep 22 2011 Yuri N. Sedunov <aris@altlinux.org> 0.22-alt1
- 0.22

* Wed Sep 14 2011 Yuri N. Sedunov <aris@altlinux.org> 0.21.1-alt1
- 0.21.1

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.20-alt2.1
- Rebuilt for debuginfo

* Sun Oct 31 2010 Victor Forsiuk <force@altlinux.org> 0.20-alt2
- Rebuilt for soname set-versions.

* Mon May 31 2010 Victor Forsiuk <force@altlinux.org> 0.20-alt1
- 0.20

* Mon Jan 04 2010 Victor Forsyuk <force@altlinux.org> 0.19-alt1
- 0.19

* Mon Jul 20 2009 Victor Forsyuk <force@altlinux.org> 0.18.2-alt1
- 0.18.2

* Mon Dec 15 2008 Victor Forsyuk <force@altlinux.org> 0.17.1-alt2
- Remove obsolete ldconfig calls.

* Mon Jun 23 2008 Victor Forsyuk <force@altlinux.org> 0.17.1-alt1
- 0.17.1

* Mon Jun 09 2008 Victor Forsyuk <force@altlinux.org> 0.17-alt1
- 0.17

* Sat Mar 29 2008 Victor Forsyuk <force@altlinux.org> 0.16-alt1
- 0.16

* Thu Dec 27 2007 Victor Forsyuk <force@altlinux.org> 0.12-alt3
- Library itself was included by mistake in both library and devel subpackages.
  Now we package in -devel only library symlink, as it should be. This in fact
  fixes ALT#13805.

* Mon Dec 24 2007 Victor Forsyuk <force@altlinux.org> 0.12-alt2
- Security fix: CVE-2007-6353.

* Mon Nov 27 2006 Victor Forsyuk <force@altlinux.org> 0.12-alt1
- Initial build.

