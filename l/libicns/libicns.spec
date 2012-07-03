%def_disable static

Name: libicns
Version: 0.7.1
Release: alt1.1

Summary: Library for manipulation of the Mac OS icns resource format
License: %lgpl21plus/%gpl2plus
Group: System/Libraries
URL: http://sf.net/projects/icns

BuildRequires(pre): rpm-build-licenses

# http://downloads.sourceforge.net/icns/libicns-0.7.1.tar.gz
Source: %name-%version.tar

# Automatically added by buildreq on Fri Jul 23 2010
BuildRequires: gcc-c++ libjasper-devel libpng-devel

%description
libicns is a library for manipulation of the Mac OS icns resource format, also
known as the IconFamily resource type. It can read and write files from the
Mac OS X icns format, as well as read from Mac OS resource files and macbinary
encoded Mac OS resource forks. As of release 0.5.9, it can fully manipulate
any 128x128 and smaller 32-bit icons, and has partial support for manipulating
8-bit, 4-bit, and 1-bit icons. When linked with Jasper, it also has full
support for 256x256 and 512x512 icons within the icon family.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package provides header and libraries for build programs against %name

%package utils
Summary: %name utils
Group: File tools
Requires: %name = %version-%release

%description utils
Tools to cope with ICNS (Mac OS icns resource format) files:
  icns2png - A utility for converting icns files into png images
  png2icns - A utility for converting png files into icns images
  icontainer2icns - A utility for extracting icns files from icontainer packs

%prep
%setup

%build
%configure %{subst_enable static}
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog DEVNOTES README TODO
%_libdir/*.so.*

%files devel
%doc src/apidocs.{txt,html}
%_includedir/*.h
%_libdir/*.so
%_libdir/pkgconfig/*.pc

%files utils
%_bindir/*
%_man1dir/*

%changelog
* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1.1
- Removed bad RPATH

* Fri Jul 23 2010 Artem Zolochevskiy <azol@altlinux.ru> 0.7.1-alt1
- initial build for Sisyphus
