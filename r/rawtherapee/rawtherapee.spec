%def_disable hg

# LAST_REVISION=`hg log -b default | head -1 | sed 's|\s||g'`
# RT_CHANGESET=`hg parents --template 'Latest-tag:{latesttag},CSet:{rev}:{node|short}'`
# RT_DIST=`hg parents --template '{latesttagdistance}'`
%if_enabled hg
%define rtlastrev changeset:1768:c0f0396030bf
%define rtlasttag changeset:1768:c0f0396030bf
%define rtdist 0
%endif

Name: rawtherapee
Version: 4.0.11
Release: alt1

Summary: THe Experimental RAw Photo Editor
License: GPLv3+
Group: Graphics
URL: http://www.rawtherapee.com/

# Tarfile created from Mercurial repository
# hg clone https://rawtherapee.googlecode.com/hg/ %name-%version
# cd %name-%version
# rm -rf .hg*
# rm -rf doc/
# rm -rf rawzor*
# rm -rf tools/createicon.exe
# tar -cjvf ~/%name-%version.tar.bz2 ../%name-%version
%if_enabled hg
Source: rawtherapee-%version.tar.bz2
%else
Source: http://rawtherapee.googlecode.com/files/%name-%version.tar.xz
%endif
Source4: rawtherapee.Ukrainian

Requires: %name-data = %version-%release

BuildRequires: bzlib-devel cmake gcc-c++ libgomp-devel libgtkmm2-devel libiptcdata-devel
BuildRequires: libjpeg-devel liblcms2-devel libpng-devel libtiff-devel libfftw3-devel
BuildRequires: libexpat-devel libpixman-devel libcanberra-gtk2-devel
BuildRequires: libXdmcp-devel libXdamage-devel libXxf86vm-devel
BuildRequires: libexiv2-devel libharfbuzz-devel
%{?_enable_hg:BuildRequires: mercurial}

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

%if_enabled hg
# Tell version
cat > rtgui/version.h << EOF
#ifndef _VERSION_
#define _VERSION_

#define VERSION "%{rtlastrev} %{rtlasttag}"
#define TAGDISTANCE %{rtdist}
#define CACHEFOLDERNAME "RawTherapee${CACHE_NAME_SUFFIX}"
#endif
EOF
%endif

cat > AboutThisBuild.txt << EOF
See package informations
EOF

cp %_sourcedir/rawtherapee.Ukrainian rtdata/languages/Ukrainian

%build
%cmake -DCMAKE_BUILD_TYPE=MinSizeRel
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

%changelog
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
