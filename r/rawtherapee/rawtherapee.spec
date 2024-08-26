%def_disable snapshot

%define rev %nil
%if_enabled snapshot
%define git_distance 1175
%endif

%define xdg_name com.rawtherapee.RawTherapee

Name: rawtherapee
Version: 5.11%{?_enable_snapshot:.%git_distance}
Release: alt1

Summary: THe Experimental RAw Photo Editor
License: GPLv3+
Group: Graphics
URL: https://www.rawtherapee.com

%if_enabled snapshot
Vcs: https://github.com/Beep6581/RawTherapee
Source: rawtherapee-%version.tar
%else
# use full archive not git-archive to avoid dancing around version
#Source: https://rawtherapee.com/shared/source/%name-%version.tar.xz
Source: https://github.com/Beep6581/RawTherapee/releases/download/%version/%name-%version.tar.xz
%endif

%define gtk_ver 3.24.3
%define tiff_ver 4.0.4
%define rsvg_ver 2.52

Requires: %name-data = %version-%release
Requires: libgtk+3 >= %gtk_ver

BuildRequires(pre): rpm-macros-cmake >= 2.8.8
BuildRequires: cmake >= 2.8.8 gcc-c++ libgomp-devel
%{?_enable_snapshot:BuildRequires: git}
BuildRequires: libgtkmm3-devel >= %gtk_ver librsvg-devel >= %rsvg_ver
BuildRequires: libtiff-devel >= %tiff_ver
BuildRequires: bzlib-devel libiptcdata-devel
BuildRequires: libjpeg-devel liblcms2-devel libpng-devel libfftw3-devel
BuildRequires: libexpat-devel libpixman-devel libcanberra-gtk3-devel
BuildRequires: libexiv2-devel libharfbuzz-devel
BuildRequires: liblensfun-devel
# since 5.11
BuildRequires: libraw-devel libjxl-devel

%description
Raw Therapee is a free RAW converter and digital photo processing software.

%package data
Summary: Arch independent files for Raw Therapee
Group: Graphics
BuildArch: noarch

%description data
This package provides noarch data needed for Raw Therapee to work.

%prep
%setup

# Do not install useless rtstart:
subst "s|install (PROGRAMS rtstart|\#install (PROGRAMS rtstart|" CMakeLists.txt

%build
%define _optlevel 3
%define optflags -O%_optlevel -g
%add_optflags %(getconf LFS_CFLAGS)
%cmake -DCMAKE_BUILD_TYPE:STRING="Release" \
	%{?_disable_snapshot:-DCACHE_NAME_SUFFIX=""} \
	%{?_enable_snapshot:-DCACHE_NAME_SUFFIX="5-dev"}
%cmake_build

%install
%cmake_install

rm -f %buildroot/%_datadir/doc/rawtherapee/*.txt

%files
%_bindir/%name
%_bindir/%name-cli
%doc AUTHORS.txt LICENSE RELEASE_NOTES.txt

%files data
%_desktopdir/%name.desktop
%_datadir/%name/
%_iconsdir/hicolor/*/apps/*
%_man1dir/%name.1.*
%_datadir/metainfo/%xdg_name.appdata.xml

%changelog
* Mon Aug 26 2024 Yuri N. Sedunov <aris@altlinux.org> 5.11-alt1
- 5.11

* Sat Feb 17 2024 Yuri N. Sedunov <aris@altlinux.org> 5.10-alt1
- 5.10

* Sat Jun 24 2023 Yuri N. Sedunov <aris@altlinux.org> 5.9-alt1.1
- fixed build with gcc-13

* Mon Nov 28 2022 Yuri N. Sedunov <aris@altlinux.org> 5.9-alt1
- 5.9

* Thu Oct 14 2021 Yuri N. Sedunov <aris@altlinux.org> 5.8-alt2
- fixed build with glibc-2.34

* Mon May 31 2021 Yuri N. Sedunov <aris@altlinux.org> 5.8-alt1.1
- adapted to new cmake macros

* Wed Feb 05 2020 Yuri N. Sedunov <aris@altlinux.org> 5.8-alt1
- 5.8

* Wed Sep 11 2019 Yuri N. Sedunov <aris@altlinux.org> 5.7-alt1
- 5.7

* Sun Apr 21 2019 Yuri N. Sedunov <aris@altlinux.org> 5.6-alt1
- 5.6

* Wed Dec 19 2018 Yuri N. Sedunov <aris@altlinux.org> 5.5-alt1
- 5.5

* Wed Mar 21 2018 Yuri N. Sedunov <aris@altlinux.org> 5.4-alt1
- 5.4

* Mon Oct 02 2017 Yuri N. Sedunov <aris@altlinux.org> 5.3-alt1
- 5.3

* Thu Jul 27 2017 Yuri N. Sedunov <aris@altlinux.org> 5.2-alt1
- 5.2

* Wed May 17 2017 Yuri N. Sedunov <aris@altlinux.org> 5.1-alt1
- 5.1

* Wed Feb 08 2017 Yuri N. Sedunov <aris@altlinux.org> 5.0-alt1.r1
- 5.0-r1

* Thu Jan 26 2017 Yuri N. Sedunov <aris@altlinux.org> 5.0-alt1
- 5.0 (gtk3)

* Fri Jun 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.2-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Tue Mar 31 2015 Yuri N. Sedunov <aris@altlinux.org> 4.2-alt1
- 4.2

* Mon Jan 13 2014 Yuri N. Sedunov <aris@altlinux.org> 4.0.12-alt1
- 4.0.12

* Wed Dec 18 2013 Yuri N. Sedunov <aris@altlinux.org> 4.0.11-alt1
- 4.0.11

* Mon Oct 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.7-alt1.1
- Rebuilt with libpng15

* Mon Mar 26 2012 Victor Forsiuk <force@altlinux.org> 4.0.7-alt1
- 4.0.7

* Fri Dec 16 2011 Victor Forsiuk <force@altlinux.org> 4.0.5-alt1
- 4.0.5

* Tue Jun 14 2011 Victor Forsiuk <force@altlinux.org> 3.0-alt2.20110614
- Mercurial repository snapshot from 2011-06-14.

* Mon Feb 15 2010 Victor Forsiuk <force@altlinux.org> 3.0-alt1.alpha1
- Initial build.
