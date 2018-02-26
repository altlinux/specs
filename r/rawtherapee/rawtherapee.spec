# LAST_REVISION=`hg log -b default | head -1 | sed 's|\s||g'`
# RT_CHANGESET=`hg parents --template 'Latest-tag:{latesttag},CSet:{rev}:{node|short}'`
# RT_DIST=`hg parents --template '{latesttagdistance}'`
%define rtlastrev changeset:1768:c0f0396030bf
%define rtlasttag changeset:1768:c0f0396030bf
%define rtdist 0

Name: rawtherapee
Version: 4.0.7
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
Source: rawtherapee-%version.tar.bz2
Source1: rawtherapee.desktop
Source2: http://rawtherapee.googlecode.com/files/356_RawTherapee.svg
Source3: rawtherapee48.png
Source4: rawtherapee.Ukrainian

# Automatically added by buildreq on Tue Jun 14 2011
BuildRequires: bzlib-devel cmake gcc-c++ libgomp-devel libgtkmm2-devel libiptcdata-devel libjpeg-devel liblcms2-devel libpng-devel libtiff-devel mercurial

%description
Raw Therapee is a free RAW converter and digital photo processing software.

%prep
%setup
# Do not install useless rtstart:
subst "s|install (PROGRAMS rtstart|\#install (PROGRAMS rtstart|" CMakeLists.txt

# Tell version
cat > rtgui/version.h << EOF
#ifndef _VERSION_
#define _VERSION_

#define VERSION "%{rtlastrev} %{rtlasttag}"
#define TAGDISTANCE %{rtdist}
#define CACHEFOLDERNAME "RawTherapee${CACHE_NAME_SUFFIX}"
#endif
EOF

cat > AboutThisBuild.txt << EOF
See package informations
EOF

cp %_sourcedir/rawtherapee.Ukrainian rtdata/languages/Ukrainian

%build
cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=MinSizeRel -DCMAKE_SKIP_RPATH:BOOL=yes .
%make_build VERBOSE=1

%install
%makeinstall_std
install -pDm644 %SOURCE1 %buildroot%_desktopdir/rawtherapee.desktop
install -pDm644 rtdata/images/rt-logo-large.png %buildroot%_niconsdir/rawtherapee.png
install -pDm644 rtdata/images/rt-logo.png %buildroot%_miconsdir/rawtherapee.png
install -pDm644 %_sourcedir/356_RawTherapee.svg %buildroot%_iconsdir/hicolor/scalable/apps/rawtherapee.svg
install -pDm644 %_sourcedir/rawtherapee48.png %buildroot%_liconsdir/rawtherapee.png

rm -f %buildroot/%_datadir/doc/rawtherapee/*.txt

%files
%_bindir/*
%_datadir/rawtherapee
%_desktopdir/*
#%_miconsdir/*
#%_niconsdir/*
#%_liconsdir/*
%_iconsdir/hicolor/*/apps/*

%changelog
* Mon Mar 26 2012 Victor Forsiuk <force@altlinux.org> 4.0.7-alt1
- 4.0.7

* Fri Dec 16 2011 Victor Forsiuk <force@altlinux.org> 4.0.5-alt1
- 4.0.5

* Tue Jun 14 2011 Victor Forsiuk <force@altlinux.org> 3.0-alt2.20110614
- Mercurial repository snapshot from 2011-06-14.

* Mon Feb 15 2010 Victor Forsiuk <force@altlinux.org> 3.0-alt1.alpha1
- Initial build.
