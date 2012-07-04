Name:           gdcm
Version:        2.2.0
Release:        alt1
Summary:        DiCoM is a C++ library for DICOM medical files
Group:          System/Libraries
License:        BSD
URL:            http://sourceforge.net/projects/gdcm/
Source:         %name-%version.tar

Patch6: gdcm-2.0.17-install2libarch.patch
Patch10: gdcm-2.0.17-no_versioned_dir.patch

BuildRequires: doxygen tetex-latex wget gnuplot cmake gcc-c++ vtk-python libvtk-devel libvtk-python-devel libexpat-devel zlib-devel libuuid-devel libopenjpeg-devel libssl-devel libCharLS-devel libpoppler-devel
BuildRequires: /proc java-1.6.0-sun-devel swig mono-mcs mono-devel libwxGTK-devel libgtk+2-devel libpixman-devel libXdmcp-devel libXdamage-devel libXxf86vm-devel xorg-dri2proto-devel xorg-glproto-devel
BuildRequires: python-devel perl-devel libpq-devel libmysqlclient-devel

%description
Grassroots DiCoM is a C++ library for DICOM medical files. It is wrapped to Python,
C#, Java and PHP. It supports RAW, JPEG, J2K, JPEG-LS, RLE and deflated.
It supports SCU network operations (C-ECHO, C-FIND, C-STORE, C-MOVE).
Part 3/6 are XML files.

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

%package -n	lib%name-vtk
Summary:        Grassroots DICOM vtk bindings
Group:          System/Libraries

%description -n	lib%name-vtk
Grassroots DiCoM is a C++ library for DICOM medical files. It is
automatically wrapped to python/C#/Java (using swig). It supports
RAW,JPEG (lossy/lossless),J2K,JPEG-LS, RLE and deflated.

VTK bindings to the GDCM DICOM library.

%package -n	lib%name-sharp
Summary:        Grassroots DICOM vtk bindings
Group:          Development/Other

%description -n	lib%name-sharp
Grassroots DiCoM is a C++ library for DICOM medical files. It is
automatically wrapped to python/C#/Java (using swig). It supports
RAW,JPEG (lossy/lossless),J2K,JPEG-LS, RLE and deflated.

.NET bindings to the GDCM DICOM library.

%package -n	lib%name-java
Summary:        Grassroots DICOM Java bindings
Group:          System/Libraries

%description -n	lib%name-java
Grassroots DiCoM is a C++ library for DICOM medical files. It is
automatically wrapped to python/C#/Java (using swig). It supports
RAW,JPEG (lossy/lossless),J2K,JPEG-LS, RLE and deflated.

Java bindings to the GDCM DICOM library. It allows developers to use
GDCM from Java environment.

%package -n	perl-%name
Summary:        Grassroots DICOM perl bindings
Group:          Development/Perl

%description -n	perl-%name
Grassroots DiCoM is a C++ library for DICOM medical files. It is
automatically wrapped to python/C#/Java (using swig). It supports
RAW,JPEG (lossy/lossless),J2K,JPEG-LS, RLE and deflated.

Perl bindings to the GDCM DICOM library.

%package -n	python-module-%name
Summary:        Grassroots DICOM python bindings
Group:          Development/Python

%description -n	python-module-%name
Grassroots DiCoM is a C++ library for DICOM medical files. It is
automatically wrapped to python/C#/Java (using swig). It supports
RAW,JPEG (lossy/lossless),J2K,JPEG-LS, RLE and deflated.

Python bindings to the GDCM DICOM library.

%package -n	wxGDCM
Summary:        Viewer for %name
Group:          Graphics

%description -n	wxGDCM
The wx%name is GDCM DICOM viewer

%prep
%setup -q
%patch6 -p 1
%patch10 -p 1

sed -i '28,36d' CMakeLists.txt
#Fix DSO link error
sed -i 's/vtkRendering/vtkRendering vtkIO/g' Utilities/wxWidgets/CMakeLists.txt
#Fix link
sed -i '/SWIG_LINK_LIBRARIES/s/gdcmMSFF/gdcmMSFF ${PERL_POSSIBLE_LIBRARY_NAMES}/g' Wrapping/Perl/CMakeLists.txt

%build
%cmake \
	-DCMAKE_VERBOSE_MAKEFILE=ON \
	-DCMAKE_SKIP_RPATH:BOOL=YES \
	-DGDCM_BUILD_APPLICATIONS:BOOL=ON \
	-DGDCM_BUILD_SHARED_LIBS:BOOL=ON \
	-DBUILD_DOCUMENTATION:BOOL=ON \
	-DGDCM_DOCUMENTATION:BOOL=ON \
	-DGDCM_PDF_DOCUMENTATION:BOOL=OFF \
	-DGDCM_BUILD_TESTING:BOOL=OFF \
	-DCMAKE_BUILD_TYPE:STRING="Release" \
	-DGDCM_BUILD_EXAMPLES:BOOL=OFF \
	-DGDCM_WRAP_PYTHON:BOOL=ON \
	-DGDCM_WRAP_PERL:BOOL=ON \
	-DGDCM_WRAP_CSHARP:BOOL=ON \
	-DGDCM_WRAP_JAVA:BOOL=ON \
	-DGDCM_WRAP_PHP:BOOL=OFF \
	-DGDCM_USE_PARAVIEW:BOOL=OFF \
	-DGDCM_USE_WXWIDGETS:BOOL=ON \
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

mkdir -p %buildroot%perl_vendor_archlib
mkdir -p %buildroot%python_sitelibdir

mv %buildroot%_libdir/*.pm %buildroot%perl_vendor_archlib/
mv %buildroot%_libdir/*.py* %buildroot%python_sitelibdir/

%files
%doc AUTHORS AUTHORS README.*
%_bindir/*
%_datadir/%name
%_man1dir/*

%exclude %_bindir/wxGDCM

%files -n lib%name
%_libdir/lib%{name}*.so.*
%_libdir/libsocketxx.so.*

%files -n lib%name-devel
%_libdir/*.so
%_libdir/%name
%_includedir/%name

%exclude %_libdir/lib%{name}jni.so
%exclude %_libdir/libgdcmsharpglue.so
%exclude %_libdir/libvtkgdcmsharpglue.so
%exclude %_libdir/libvtkgdcmPythonD.so
%exclude %_libdir/gdcm.so
%exclude %_libdir/_gdcmswig.so

%files -n lib%name-vtk
%_libdir/libvtkgdcm*.so.*
%exclude %_libdir/libvtkgdcmPython*.so*

%files -n lib%name-sharp
%_libdir/libgdcmsharpglue.so
%_libdir/libvtkgdcmsharpglue.so
%_libdir/%{name}*.dll
%_libdir/vtk%{name}*.dll

%files -n lib%name-java
%_libdir/_gdcmswig.so
%_libdir/lib%{name}jni.so
%_libdir/gdcm.jar

%files -n python-module-%name
%_libdir/libvtkgdcmPython.so.*
%_libdir/libvtkgdcmPythonD.so
%python_sitelibdir/*

%files -n perl-%name
%_libdir/gdcm.so
%perl_vendor_archlib/*

%files -n wxGDCM
%_bindir/wxGDCM

%changelog
* Sat Jun 23 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.2.0-alt1
- 2.2.0

* Mon Nov 07 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0.18-alt1
- first build for ALT Linux
