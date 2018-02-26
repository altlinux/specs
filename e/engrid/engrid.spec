%define vtk_ver 5.10

Name: engrid
Version: 1.3
Release: alt2.git20120322
Summary: Mesh generation software with CFD applications in mind
License: GPL v3 or later
Group: Sciences/Physics
Url: http://sourceforge.net/projects/engrid/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# git://engrid.git.sourceforge.net/gitroot/engrid/engrid
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: libvtk-devel libcgns-mpi-devel
BuildPreReq: libqt4-devel gcc-c++ libnetgen-devel
BuildPreReq: python-tools-2to3

%add_python3_req_skip BPyAddMesh bpy_extras mathutils
%add_python3_path %_datadir/blender/scripts/blender

%description
ENGRID is a mesh generation software with CFD applications in mind. It
supports automatic prismatic boundary layer grids for Navier-Stokes
simulations and has a Qt based GUI.

%package docs
Summary: Documentation for ENGRID
Group: Documentation
BuildArch: noarch

%description docs
ENGRID is a mesh generation software with CFD applications in mind. It
supports automatic prismatic boundary layer grids for Navier-Stokes
simulations and has a Qt based GUI.

This package contains documentation for ENGRID.

%prep
%setup

for i in $(find ./ -name '*.py'); do
	2to3 -w $i
done

%build
pushd src

%add_optflags -I%_includedir/vtk-%vtk_ver
qmake-qt4 QMAKE_CFLAGS_RELEASE="%optflags" \
	QMAKE_CXXFLAGS_RELEASE="%optflags" engrid.pro
%make_build

popd

%install
#makeinstall_std -C src INSTALL_ROOT=%buildroot

install -d %buildroot%_bindir
install -m755 src/%name %buildroot%_bindir

install -d %buildroot%_libdir
cp -P src/libengrid/libengrid.so.* %buildroot%_libdir/

install -d %buildroot%_man1dir
install -p -m644 debian/%name.1 %buildroot%_man1dir

install -d %buildroot%_niconsdir
install -d %buildroot%_miconsdir
install -d %buildroot%_liconsdir
install -p -m644 src/libengrid/resources/icons/engrid.xpm \
	%buildroot%_niconsdir
ln -s %_niconsdir/engrid.xpm %buildroot%_miconsdir/
ln -s %_niconsdir/engrid.xpm %buildroot%_liconsdir/

install -d %buildroot%_desktopdir
install -p -m644 debian/%name.desktop %buildroot%_desktopdir
install -d %buildroot%_datadir/blender/scripts/blender
install -p -m644 src/blender_scripts/* \
	%buildroot%_datadir/blender/scripts/blender

%files
%doc *.txt
%_bindir/*
%_libdir/*.so.*
%_man1dir/*
%_niconsdir/*
%_miconsdir/*
%_liconsdir/*
%_desktopdir/*
%_datadir/blender/scripts/blender/*

%files docs
%doc manual tutorials

%changelog
* Sat Jun 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt2.git20120322
- Rebuilt with VTK 5.10.0

* Mon Apr 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.git20120322
- New snapshot
- Rebuilt with Blender 2.62

* Fri Jan 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.git20120127
- Version 1.3

* Mon Nov 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.0-alt5.1
- Rebuild with Python-2.7

* Fri Sep 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt5
- Rebuilt with VTK 5.8.0

* Mon May 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt4
- Rebuilt with cgns 3.1.3

* Fri Apr 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt3
- Rebuilt with VTK 5.6.1

* Wed Mar 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt2
- Rebuilt for debuginfo

* Fri Dec 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus

