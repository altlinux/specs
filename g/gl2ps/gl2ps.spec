%define _unpackaged_files_terminate_build 1

Name: gl2ps
Version: 1.4.0
Release: alt1
Summary: OpenGL to PostScript printing library
License: LGPLv2+
Group: Graphics
Url: http://geuz.org/gl2ps/#tth_sEc5

# https://gitlab.onelab.info/gl2ps/gl2ps.git
Source: %name-%version.tar

Patch1: %name-%version-upstream.patch

BuildRequires: cmake zlib-devel libpng-devel ghostscript-utils
BuildRequires: libGLU-devel libGLUT-devel libXi-devel libXmu-devel
BuildRequires: libICE-devel libSM-devel libXres-devel libXext-devel
BuildRequires: libXtst-devel libXau-devel libXcomposite-devel
BuildRequires: libXcursor-devel libXdamage-devel libXdmcp-devel
BuildRequires: libXfixes-devel libXft-devel libXinerama-devel
BuildRequires: libXpm-devel libXrandr-devel libXrender-devel
BuildRequires: libXScrnSaver-devel libXt-devel libXv-devel
BuildRequires: libXxf86misc-devel libXxf86vm-devel libxkbfile-devel
BuildRequires: texlive-dist

%description
GL2PS is a C library providing high quality vector output for any OpenGL
application. The main difference between GL2PS and other similar
libraries is the use of sorting algorithms capable of handling
intersecting and stretched polygons, as well as non manifold objects.
GL2PS provides advanced smooth shading and text rendering, culling of
invisible primitives, mixed vector/bitmap output, and much more.

%package -n lib%name
Summary: Shared libraries of GL2PS
Group: System/Libraries

%description -n lib%name
GL2PS is a C library providing high quality vector output for any OpenGL
application. The main difference between GL2PS and other similar
libraries is the use of sorting algorithms capable of handling
intersecting and stretched polygons, as well as non manifold objects.
GL2PS provides advanced smooth shading and text rendering, culling of
invisible primitives, mixed vector/bitmap output, and much more.

This package contains shared libraries of GL2PS.

%package -n lib%name-devel
Summary: Development files of GL2PS
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
GL2PS is a C library providing high quality vector output for any OpenGL
application. The main difference between GL2PS and other similar
libraries is the use of sorting algorithms capable of handling
intersecting and stretched polygons, as well as non manifold objects.
GL2PS provides advanced smooth shading and text rendering, culling of
invisible primitives, mixed vector/bitmap output, and much more.

This package contains development files of GL2PS.

%package -n lib%name-devel-doc
Summary: Documentation for GL2PS
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
GL2PS is a C library providing high quality vector output for any OpenGL
application. The main difference between GL2PS and other similar
libraries is the use of sorting algorithms capable of handling
intersecting and stretched polygons, as well as non manifold objects.
GL2PS provides advanced smooth shading and text rendering, culling of
invisible primitives, mixed vector/bitmap output, and much more.

This package contains development documentation for GL2PS.

%prep
%setup
%patch1 -p1

%build
%cmake_insource \
	-DCMAKE_STRIP:FILEPATH="/bin/echo"

%make_build VERBOSE=1

%install
%makeinstall_std

# remove static libraries
rm -f %buildroot%_libdir/*.a

%files -n lib%name
%doc README.txt TODO.txt
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%files -n lib%name-devel-doc
%_docdir/%name

%changelog
* Wed Sep 19 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.0-alt1
- Updated to upstream version 1.4.0.

* Wed Apr 11 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.8-alt2
- fixed packaging on 64bit arches other than x86_64

* Mon Feb 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.8-alt1
- Version 1.3.8

* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.7-alt2
- Rebuilt with libpng15

* Wed Sep 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.7-alt1
- Version 1.3.7

* Mon May 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.6-alt2
- Fixed build

* Tue Feb 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.6-alt1
- Initial build for Sisyphus

