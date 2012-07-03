Name: coin3d
Version: 3.1.3
Release: alt7
Summary: OpenGL-based, 3D graphics library
License: GPL
Group: Development/Tools
Url: http://www.coin3d.org
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://ftp.coin3d.org/coin/src/all/Coin-%version.tar.gz

Requires: lib%name = %version-%release
Requires: %name-common = %version-%release

BuildPreReq: libGL-devel libGLU-devel doxygen gcc-c++ fontconfig
BuildPreReq: libopenal-devel zlib-devel bzlib-devel
BuildPreReq: gcc-fortran libdirectfb-devel libX11-devel libXt-devel
BuildPreReq: libexpat-devel

%description
Coin is an OpenGL-based, 3D graphics library that has its roots in the
Open Inventor 2.1 API, which Coin still is compatible with.

If you are not familiar with Open Inventor, it is a scene-graph based,
retain-mode, rendering and model manipulation, C++ class library,
originally designed by SGI.  It quickly became the de facto standard
graphics library for 3D visualization and visual simulation software
in the scientific and engineering community after its release.  It
also became the basis for the VRML1 file format standard.

%package -n lib%name
Summary: Shared libraries of Coin3D
Group: System/Libraries
Conflicts: %name < %version-%release

%description -n lib%name
Coin is an OpenGL-based, 3D graphics library that has its roots in the
Open Inventor 2.1 API, which Coin still is compatible with.

If you are not familiar with Open Inventor, it is a scene-graph based,
retain-mode, rendering and model manipulation, C++ class library,
originally designed by SGI.  It quickly became the de facto standard
graphics library for 3D visualization and visual simulation software
in the scientific and engineering community after its release.  It
also became the basis for the VRML1 file format standard.

This package contains shared libraries of Coin3D.

%package -n lib%name-devel
Summary: Development files for Coin3D
Group: Development/C++
Requires: lib%name = %version-%release
Requires: %name-common = %version-%release
Conflicts: %name < %version-%release
Conflicts: libInventor-devel

%description -n lib%name-devel
Coin is an OpenGL-based, 3D graphics library that has its roots in the
Open Inventor 2.1 API, which Coin still is compatible with.

If you are not familiar with Open Inventor, it is a scene-graph based,
retain-mode, rendering and model manipulation, C++ class library,
originally designed by SGI.  It quickly became the de facto standard
graphics library for 3D visualization and visual simulation software
in the scientific and engineering community after its release.  It
also became the basis for the VRML1 file format standard.

This package contains development files for Coin3D.

%package -n lib%name-devel-doc
Summary: Documentation for Coin3D
Group: Development/Documentation
BuildArch: noarch
Conflicts: lib%name-devel < %version-%release

%description -n lib%name-devel-doc
Coin is an OpenGL-based, 3D graphics library that has its roots in the
Open Inventor 2.1 API, which Coin still is compatible with.

If you are not familiar with Open Inventor, it is a scene-graph based,
retain-mode, rendering and model manipulation, C++ class library,
originally designed by SGI.  It quickly became the de facto standard
graphics library for 3D visualization and visual simulation software
in the scientific and engineering community after its release.  It
also became the basis for the VRML1 file format standard.

This package contains development documentation for Coin3D.

%package common
Summary: Architecture independent files of Coin3D
Group: Development/Documentation
BuildArch: noarch

%description common
Coin is an OpenGL-based, 3D graphics library that has its roots in the
Open Inventor 2.1 API, which Coin still is compatible with.

If you are not familiar with Open Inventor, it is a scene-graph based,
retain-mode, rendering and model manipulation, C++ class library,
originally designed by SGI.  It quickly became the de facto standard
graphics library for 3D visualization and visual simulation software
in the scientific and engineering community after its release.  It
also became the basis for the VRML1 file format standard.

This package contains architecture independent files of Coin3D.

%prep
%setup

%build
#sed -i 's|^libdir.*|libdir=%_libdir|' Coin.pc.in
%add_optflags -I%_includedir/directfb
%configure \
	--enable-3ds-import \
	--enable-threadsafe \
	--enable-html \
	--enable-man \
	--enable-dl-simage \
	--enable-dl-openal \
	--enable-dl-glu \
	--with-pthread \
	--with-doxygen \
	--with-dl \
	--with-simage \
	--with-openal \
	--with-fontconfig \
	--with-freetype \
	--with-zlib \
	--with-bzip2 \
	--with-x \
	--with-opengl \
	--with-mesa \
	--enable-system-expat
%make_build

%install
%makeinstall_std

install -d %buildroot%_docdir/%name
#mv %buildroot%_datadir/Coin/html %buildroot%_docdir/%name/
%ifarch x86_64
sed -i 's|/lib64|/lib|g' %buildroot%_bindir/coin-config
sed -i 's|/lib|/lib64|g' %buildroot%_bindir/coin-config
sed -i 's|/lib64|/lib|g' %buildroot%_datadir/Coin/conf/coin-default.cfg
sed -i 's|/lib|/lib64|g' %buildroot%_datadir/Coin/conf/coin-default.cfg
%endif
sed -i 's|^\(htmldir\).*|\1=%_docdir/%name/html|g' \
	%buildroot%_datadir/Coin/conf/coin-default.cfg

mv %buildroot%_datadir/aclocal/coin.m4 \
	%buildroot%_datadir/aclocal/%name.m4

%files -n lib%name
%doc AUTHORS COPYING FAQ* LICENSE.GPL NEWS README README.UNIX RELNOTES
%doc THANKS
%_libdir/*.so.*

%files -n lib%name-devel
%_bindir/*
%_man1dir/*
%_datadir/Coin/conf/coin-default.cfg
%_libdir/*.so
%_pkgconfigdir/*
%_includedir/*
%_datadir/aclocal/*

%files -n lib%name-devel-doc
%doc docs/*
%doc %_docdir/coin
%_man3dir/*
%exclude %_man3dir/deprecated.3*
%exclude %_man3dir/details.3*

%files common
%_datadir/Coin
%exclude %_datadir/Coin/conf/coin-default.cfg

%changelog
* Sun Feb 19 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.3-alt7
- libcoin3d-devel-doc: avoid conflict with libtrilinos10-devel-doc

* Fri Feb 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.3-alt6
- Built without OSMesa

* Thu Apr 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.3-alt5
- Removed %name package (ALT #25523)

* Sat Feb 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.3-alt4
- Rebuilt for debuginfo

* Mon Jan 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.3-alt3
- Moved devel man pages into devel-doc package

* Tue Oct 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.3-alt2
- Rebuilt for soname set-versions

* Wed Mar 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.3-alt1
- Version 3.1.3

* Wed Feb 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.2-alt3
- Renamed coin.m4 -> coin3d.m4

* Mon Jan 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.2-alt2
- Removed %_man3dir/deprecated.3*

* Fri Jan 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.2-alt1
- Version 3.1.2

* Tue May 05 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt3
- lib%name-devel: explicit conflict with libInventor-devel

* Sun May 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt1.M50.1
- Port for Branch 5.0

* Sun May 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt2.2
- Move default config file into package %name

* Sat May 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt2.1
- Fix pkgconfig file for x86_64

* Sat May 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt2
- Fix for x86_64

* Sat May 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt0.M50.1
- Port for Branch 5.0

* Sat May 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt1
- Initial build for Sisyphus

