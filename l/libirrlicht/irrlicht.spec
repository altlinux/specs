%define _unpackaged_files_terminate_build 1

%def_disable static
%define realname irrlicht
%define major 1
%define irrxml_major 1
%define libname %name%major

Name: libirrlicht
Version: 1.8.4
Release: alt4

Summary: Fast Open-source 3D engine
License: zlib
Group: System/Libraries

Url: http://irrlicht.sourceforge.net/
Source: %realname-%version.tar

# Patches from Fedora

# Various fixes, optflags, system libraries/headers
# http://irrlicht.sourceforge.net/phpBB2/viewtopic.php?t=24076&highlight=
Patch0: irrlicht-1.8-optflags.patch

# Get the code compiling
Patch1: irrlicht-1.8-glext.patch

# Use system libaesgm
Patch2: irrlicht18-libaesgm.patch

# Make libIrrXML.so
Patch4: irrlicht-1.8-irrXML-shared-library.patch

# Fix issue with definition of LOCALE_DECIMAL_POINTS
Patch5: irrlicht-1.8-fix-locale-decimal-points.patch

# Fix build with Mesa 10
Patch6: irrlicht-1.8.1-mesa10.patch

# Use RPM_LD_FLAGS
Patch7: irrlicht-1.8.4-ldflags.patch

# sysctl.h was removed from glibc in f33.
# it is only actually used on OSX, so we just conditionalize the include to match the call
Patch8: irrlicht-1.8.4-no-sysctl-on-linux.patch

BuildRequires: pkg-config unzip gcc-c++ zlib-devel
BuildRequires: ImageMagick
BuildRequires: zlib-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libGLU-devel
BuildRequires: pkgconfig(x11)
BuildRequires: libXext-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libXft-devel
BuildRequires: bzlib-devel
BuildRequires: fontconfig-devel
BuildRequires: libXcursor-devel
BuildRequires: libaesgm-devel

%description
The Irrlicht Engine is a cross-platform high performance realtime 3D
engine written in C++. It is a powerful high level API for creating
complete 3D and 2D applications like games or scientific visualizations.
It comes with an excellent documentation and integrates all the
state-of-the-art features for visual representation like dynamic
shadows, particle systems, character animation, indoor and outdoor
technology, and collision detection. All this is accessible through
a well designed C++ interface, which is extremely easy to use.

%package devel
Summary: Headers for %name
Group: Development/C
Requires: %name = %EVR
#Requires: irrXML-devel = %EVR

%description devel
Headers for building software that uses %name

%package -n %libname
Summary: Shared libraries for Irrlicht 3D engine
Group: System/Libraries

Provides: liblibirrlicht1 = %EVR
Obsoletes: liblibirrlicht1 < %EVR
Provides: libirrlicht = %EVR
Obsoletes: libirrlicht < %EVR

%description -n %libname
Shared libraries for Irrlicht 3D engine.

The Irrlicht Engine is a cross-platform high performance realtime 3D
engine written in C++. It is a powerful high level API for creating
complete 3D and 2D applications like games or scientific visualizations.
It comes with an excellent documentation and integrates all the
state-of-the-art features for visual representation like dynamic
shadows, particle systems, character animation, indoor and outdoor
technology, and collision detection. All this is accessible through
a well designed C++ interface, which is extremely easy to use.

%package -n libirrXML%{irrxml_major}
Summary: Simple and fast XML parser for C++
Group: System/Libraries

%description -n libirrXML%{irrxml_major}
irrXML is a simple and fast open source xml parser for C++.

%package -n irrXML-devel
Summary: Development headers and libraries for irrXML
Group: Development/C
Requires: libirrXML%{irrxml_major} = %EVR

%description -n irrXML-devel
Development headers and libraries for irrXML.

%package examples
Summary: Examples for %name
Group: Development/C
Requires: %name = %EVR

%description examples
Examples that uses %name

%if_enabled static
%package devel-static
Summary: Static libraries for %name
Group: Development/C
Requires: %name-devel = %EVR

%description devel-static
Static libs for building statically linked software that uses %name
%endif

%prep
%setup -n %realname-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1
# TODO: separate libIrrXML.so
#patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

# make readme.txt and changes.txt utf8 with LF line endings
sed -i 's/\r//' readme.txt changes.txt
iconv -o readme.txt.utf8 -f iso88591 -t utf8 readme.txt
mv readme.txt.utf8 readme.txt

# use system wide libs
rm -rf source/Irrlicht/{jpeglib,zlib,libpng,bzip2,aesGladman}
# FIXME: Unbundle lzmadec if possible

# https://bugzilla.redhat.com/show_bug.cgi?id=1035757
sed -i -e '/_IRR_MATERIAL_MAX_TEXTURES_/s/4/8/' include/IrrCompileConfig.h

%build
%make_build -C source/Irrlicht sharedlib NDEBUG=1

%install
#makeinstall
mkdir -p %buildroot%_libdir
make -C source/Irrlicht INSTALL_DIR=%buildroot%_libdir install
ln -s libIrrlicht.so.%version %buildroot%_libdir/libIrrlicht.so.%major

mkdir -p %buildroot%_includedir/%realname
cp -a include/*.h %buildroot%_includedir/%realname/

%files -n %libname
%_libdir/libIrrlicht.so.%{major}
%_libdir/libIrrlicht.so.%{major}.*

%files devel
%_libdir/libIrrlicht.so
%_includedir/%realname
#exclude %_includedir/%realname/fast_atof.h
#exclude %_includedir/%realname/heapsort.h
#exclude %_includedir/%realname/irrArray.h
#exclude %_includedir/%realname/irrString.h
#exclude %_includedir/%realname/irrTypes.h
#exclude %_includedir/%realname/irrXML.h

#doc doc/html doc/index.html
%doc doc/upgrade-guide.txt
%doc readme.txt changes.txt

#files -n libirrXML%{irrxml_major}
#_libdir/libIrrXML.so.%{irrxml_major}
#_libdir/libIrrXML.so.%{irrxml_major}.*

#files -n irrXML-devel
#_libdir/libIrrXML.so
#dir %_includedir/%realname
#_includedir/%realname/fast_atof.h
#_includedir/%realname/heapsort.h
#_includedir/%realname/irrArray.h
#_includedir/%realname/irrString.h
#_includedir/%realname/irrTypes.h
#_includedir/%realname/irrXML.h

#%files examples
#%_bindir/*
#%_datadir/irrlicht

%if_enabled static
%files -n lib%name-devel-static
%_libdir/lib%name.a
%endif

%changelog
* Tue Jan 12 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.8.4-alt4
- Fixed build with new glibc.
- Applied patches from Fedora.
- Updated license tag.

* Wed Nov 11 2020 Michael Shigorin <mike@altlinux.org> 1.8.4-alt3
- minor deps/spec cleanup (thx ldv@)

* Tue Jun 11 2019 Michael Shigorin <mike@altlinux.org> 1.8.4-alt2
- Added P: libirrlicht = %%version-%%release for -devel

* Tue Nov 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.8.4-alt1
- Updated to upstream version 1.8.4.

* Tue Jun 14 2016 Igor Vlasenko <viy@altlinux.ru> 1.8.3-alt1
- NMU update

* Thu Dec 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.1-alt2.1
- Fixed build with libpng15

* Sat Jan 22 2011 Damir Shayhutdinov <damir@altlinux.ru> 1.7.1-alt2
- Rebuilt with set-provides.

* Tue Mar 30 2010 Damir Shayhutdinov <damir@altlinux.ru> 1.7.1-alt1
- New version.

* Sat Nov 22 2008 Damir Shayhutdinov <damir@altlinux.ru> 1.4.2-alt1
- New version.

* Fri Apr 13 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.3-alt4
- Moved docs to devel subpackage. Now libirrlicht is ready for biarch.

* Thu Apr 12 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.3-alt3
- Fix license tag (#11483).

* Thu Mar 22 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.3-alt2
- Packaged readme.txt and changes.txt.
- Added documentation to -devel package.

* Sat Mar 17 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.3-alt1
- New version. 

* Fri Mar 02 2007 Damir Shayhutdinov <damir@altlinux.ru> 1.2.0-alt1
- Initial build for ALT Linux.
