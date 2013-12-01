Name:           gdcm
Version:        2.4.0
Release:        alt3
Summary:        DiCoM is a C++ library for DICOM medical files
Group:          System/Libraries
License:        BSD
URL:            http://sourceforge.net/projects/gdcm/
Source:         %name-%version.tar
Patch0:         %name-%version-alt.patch

BuildRequires: doxygen tetex-latex cmake gcc-c++ libvtk-devel libexpat-devel zlib-devel libuuid-devel libopenjpeg-devel libssl-devel libCharLS-devel libpoppler-devel
BuildRequires: /proc java-1.6.0-sun-devel swig mono-mcs mono-devel vtk-python
#BuildRequires: php5 php5-devel python-devel

%description
Grassroots DiCoM is a C++ library for DICOM medical files. It is wrapped to Python,
C#, Java and PHP. It supports RAW, JPEG, J2K, JPEG-LS, RLE and deflated.
It supports SCU network operations (C-ECHO, C-FIND, C-STORE, C-MOVE).
Part 3/6 are XML files.

%package 	doc
Summary:        Libraries for %name
Group:          Documentation

%description	doc
The %name-doc package contains documentation for %name

%package -n	lib%name
Summary:        Libraries for %name
Group:          System/Libraries

%description -n	lib%name
The lib%name package contains libraries for %name

%package -n	lib%name-devel
Summary:        Development files for %name
Group:          System/Libraries
Requires:       lib%name = %version-%release

%description -n	lib%name-devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n	lib%name-java
Summary:        Grassroots DICOM Java bindings
Group:          System/Libraries

%description -n	lib%name-java
Grassroots DiCoM is a C++ library for DICOM medical files. It is
automatically wrapped to python/C#/Java (using swig). It supports
RAW,JPEG (lossy/lossless),J2K,JPEG-LS, RLE and deflated.

Java bindings to the GDCM DICOM library. It allows developers to use
GDCM from Java environment.

%package -n	lib%name-vtk
Summary:        Grassroots DICOM vtk bindings
Group:          System/Libraries

%description -n	lib%name-vtk
Grassroots DiCoM is a C++ library for DICOM medical files. It is
automatically wrapped to python/C#/Java (using swig). It supports
RAW,JPEG (lossy/lossless),J2K,JPEG-LS, RLE and deflated.

VTK bindings to the GDCM DICOM library.

%prep
%setup -q
%patch -p 1

%build
%cmake \
	-DCMAKE_VERBOSE_MAKEFILE=ON \
	-DCMAKE_SKIP_RPATH:BOOL=YES \
	-DGDCM_BUILD_APPLICATIONS:BOOL=ON \
	-DGDCM_BUILD_SHARED_LIBS:BOOL=ON \
	-DGDCM_DOCUMENTATION:BOOL=ON \
	-DGDCM_PDF_DOCUMENTATION:BOOL=OFF \
	-DGDCM_BUILD_TESTING:BOOL=OFF \
	-DCMAKE_BUILD_TYPE:STRING="Release" \
	-DGDCM_BUILD_EXAMPLES:BOOL=OFF \
	-DGDCM_WRAP_PYTHON:BOOL=OFF \
	-DGDCM_WRAP_CSHARP:BOOL=ON \
	-DGDCM_WRAP_JAVA:BOOL=ON \
	-DGDCM_WRAP_PHP:BOOL=OFF \
	-DPHP5_FOUND_INCLUDE_PATH=$(php-config --include-dir) \
	-DGDCM_USE_VTK:BOOL=ON \
	-DGDCM_USE_SYSTEM_EXPAT:BOOL=ON \
	-DGDCM_USE_SYSTEM_ZLIB:BOOL=ON \
	-DGDCM_USE_SYSTEM_UUID:BOOL=ON \
	-DGDCM_USE_SYSTEM_OPENJPEG:BOOL=ON \
	-DGDCM_USE_SYSTEM_OPENSSL:BOOL=ON \
	-DGDCM_USE_SYSTEM_CHARLS:BOOL=ON \
	-DGDCM_USE_SYSTEM_LJPEG=OFF \
	-DGDCM_USE_SYSTEM_POPPLER=ON \
	-DGDCM_USE_JPEGLS=ON \
	-DGMCS_EXECUTABLE=/usr/bin/gmcs

%cmake_build

%install
%cmakeinstall_std

%files
%doc AUTHORS AUTHORS README.*
%_bindir/*
%_datadir/%name
%_man1dir/*

%files doc
%_defaultdocdir/%name

%files -n lib%name
%_libdir/lib%{name}*.so.*
%_libdir/libsocketxx.so.*
%_libdir/%{name}*.dll


%files -n lib%name-devel
%_libdir/*.so
%_libdir/%name
%_includedir/%name
#_libdir/pkgconfig/*.pc

%exclude %_libdir/lib%{name}jni.so

%files -n lib%name-java
%_libdir/lib%{name}jni.so
%_libdir/gdcm.jar

%files -n lib%name-vtk
%_libdir/libvtk*.so.*
%_libdir/vtk%{name}*.dll


%changelog
* Sun Dec 01 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.4.0-alt3
- 2.4.0

* Fri Aug 30 2013 Vladimir Lettiev <crux@altlinux.ru> 2.2.3-alt3
- built for perl 5.18

* Tue Apr 23 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.2.3-alt2
- Rebuild for poppler

* Tue Apr 09 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.2.3-alt1
- 2.2.3

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 2.2.0-alt2
- rebuilt for perl-5.16

* Sat Jun 23 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.2.0-alt1
- 2.2.0

* Mon Nov 07 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0.18-alt1
- first build for ALT Linux
