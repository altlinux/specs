%def_disable snapshot
%if_enabled snapshot
%define git_distance 1175
%endif

Name: rawtherapee
Version: 5.0%{?_enable_snapshot:.%git_distance}
Release: alt1

Summary: THe Experimental RAw Photo Editor
License: GPLv3+
Group: Graphics
URL: http://www.rawtherapee.com/

%if_enabled snapshot
# use full archive not git-archive to avoid dancing around version
Source: rawtherapee-%version.tar
%else
Source: http://rawtherapee.com/shared/source/%name-%version-gtk3.tar.xz
%endif

Requires: %name-data = %version-%release

%{?_enable_snapshot:BuildRequires: git}
BuildRequires: bzlib-devel cmake gcc-c++ libgomp-devel libgtkmm3-devel libiptcdata-devel
BuildRequires: libjpeg-devel liblcms2-devel libpng-devel libtiff-devel libfftw3-devel
BuildRequires: libexpat-devel libpixman-devel libcanberra-gtk3-devel
BuildRequires: libXdmcp-devel libXdamage-devel libXxf86vm-devel
BuildRequires: libexiv2-devel libharfbuzz-devel

%description
Raw Therapee is a free RAW converter and digital photo processing software.

%package data
Summary: Arch independent files for Raw Therapee
Group: Graphics
BuildArch: noarch

%description data
This package provides noarch data needed for Raw Therapee to work.

%prep
%setup -n %name-%version-gtk3
# Do not install useless rtstart:
subst "s|install (PROGRAMS rtstart|\#install (PROGRAMS rtstart|" CMakeLists.txt

%build
%cmake -DCMAKE_BUILD_TYPE:STRING="Release" \
	-DCMAKE_CXX_FLAGS="-std=c++11" \
	-DCACHE_NAME_SUFFIX=""
%cmake_build VERBOSE=1

%install
%cmakeinstall_std

rm -f %buildroot/%_datadir/doc/rawtherapee/*.txt

%files
%_bindir/%name
%doc AUTHORS.txt LICENSE.txt RELEASE_NOTES.txt

%files data
%_desktopdir/%name.desktop
%_datadir/%name/
%_iconsdir/hicolor/*/apps/*
%_man1dir/%name.1.*
%_datadir/appdata/%name.appdata.xml

%changelog
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
