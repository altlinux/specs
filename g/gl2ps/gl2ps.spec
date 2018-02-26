Name: gl2ps
Version: 1.3.6
Release: alt2
Summary: OpenGL to PostScript printing library
License: LGPLv2+
Group: Graphics
Url: http://geuz.org/gl2ps/#tth_sEc5
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: cmake zlib-devel libpng-devel ghostscript-utils
BuildPreReq: libGLU-devel libGLUT-devel libXi-devel libXmu-devel
BuildPreReq: libICE-devel libSM-devel libXres-devel libXext-devel
BuildPreReq: libXtst-devel libXau-devel libXcomposite-devel
BuildPreReq: libXcursor-devel libXdamage-devel libXdmcp-devel
BuildPreReq: libXfixes-devel libXft-devel libXinerama-devel
BuildPreReq: libXpm-devel libXrandr-devel libXrender-devel
BuildPreReq: libXScrnSaver-devel libXt-devel libXv-devel
BuildPreReq: libXxf86misc-devel libXxf86vm-devel libxkbfile-devel

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
Requires: lib%name = %version-%release

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

%build
cmake \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
%ifarch x86_64
	-DLIBSUFF:STRING=64 \
%endif
	.

%make_build VERBOSE=1

%install
%makeinstall_std

%files -n lib%name
%doc README.txt TODO.txt
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%files -n lib%name-devel-doc
%_docdir/%name

%changelog
* Mon May 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.6-alt2
- Fixed build

* Tue Feb 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.6-alt1
- Initial build for Sisyphus

