Name:		libSDL-sge
Version:	030809
Release:	alt1
Summary:	A graphic extension for Simple DirectMedia Layer (SDL) library
Group:		System/Libraries
License:	GPLv2
URL:		http://www.digitalfanatics.org/cal/sge/

Source:		sge%version.tar.gz
Patch001: 001_makefile_fixes.diff
Patch004: 004_legacy_functions.diff
Patch005: 005_freetype_support.diff
Patch006: 006_freetype2_fixes.diff
Patch010: 010_examples.diff
Patch015: 015_overflow.diff
Patch100: 100_font.diff

# Automatically added by buildreq on Tue Mar 05 2013
# optimized out: libSDL-devel libstdc++-devel pkg-config
BuildRequires: gcc-c++ libSDL_image-devel libfreetype-devel

%description
SGE is a graphic library for the excellent Simple DirectMedia Layer
(SDL) library (mainly) written by Sam Lantinga.

Some of SGE features are:
    Pixel operations
    Clipping
    Lines, circles and other figures (with antialiasing and alpha blending)
    Rotation and scaling of surfaces
    Palette functions
    TrueType/Bitmap/SFont font functions
    Basic 2D collision detection
    Sprite classes
    Basic texture mapping
    Filled and gourand shaded polygons (with antialiasing or alpha blending)

%package devel
Group:	Development/C++
Summary: Development environment for %name, %summary
%description devel
%summary

%prep
%setup -n sge%version
%patch001 -p1
%patch004 -p1
%patch005 -p1
%patch006 -p1
%patch100 -p1

sed -i 's@/lib@/%_lib@' Makefile

%build
%make_build shared

%install
%makeinstall PREFIX=%buildroot%_prefix PREFIX_H=%buildroot%_prefix/include/SDL

%files
%doc README Todo WhatsNew
%_libdir/*.so.*
%exclude %_libdir/*.a

%files devel
%doc docs examples
%_libdir/*.so
%_includedir/SDL/*

%changelog
* Tue Mar 05 2013 Fr. Br. George <george@altlinux.ru> 030809-alt1
- Initial build from GNU/Debian

