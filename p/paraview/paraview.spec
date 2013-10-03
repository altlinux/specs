%define pv_maj 3
%define pv_min 8
%define pv_patch 0
%define pv_majmin %pv_maj.%pv_min
#set_gcc_version 4.5

Name: paraview
Version: 4.0.1
Release: alt1
Summary: Parallel visualization application
License: BSD
Group: Sciences/Other

Url: http://www.paraview.org
Source: %url/files/v%pv_majmin/ParaView-%version.tar.gz
Source1: paraview_22x22.png
%define pixfile paraview_22x22.png
Source2: paraview.xml
Source3: CMakeCache.txt
#Add needed link libraries
#http://public.kitware.com/Bug/view.php?id=10298
Patch: paraview-3.6.2-libs.patch
#Add some needed includes
Patch1: paraview-3.8.0-include.patch
#Upstream patch to fix install paths
Patch2: paraview-3.8.0-installpath.patch
#Support Python 2.7
Patch3: paraview-3.8.0-py27.patch
#Installs PointSpriteDemo into incorrect location, remove install for now
#Reported upstream: http://public.kitware.com/mantis/view.php?id=9292
Patch5: paraview-3.8.0-demo.patch
#Reported upstream: http://public.kitware.com/mantis/view.php?id=7023
Patch7: paraview-3.2.2-hdf5.patch
#Change H5_USE_16_API_DEFAULT to H5_USE_16_API
Patch8: paraview-3.8.0-hdf5-1.8.patch
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildRequires: cmake unzip
#BuildRequires: paraview-data
BuildRequires: qt4-devel, libGL-devel libGLU-devel
BuildRequires: tk-devel, libhdf5-devel
BuildRequires: libfreetype-devel, libtiff-devel, zlib-devel
BuildRequires: libexpat-devel libjpeg-devel
BuildRequires: %_bindir/desktop-file-install
BuildRequires: doxygen, graphviz
BuildRequires: libreadline-devel
BuildRequires: libssl-devel
BuildRequires: gnuplot
#BuildRequires: wget
BuildRequires: boost-devel libproj-devel phonon-devel
BuildRequires: libqt4-assistant-devel
BuildRequires: gcc-c++
BuildPreReq: libopenmotif-devel tcl-devel libhdf5-devel
BuildPreReq: libnetcdf-devel chrpath
BuildPreReq: libsilo-devel libGLU-devel python-devel libprotobuf-devel
BuildPreReq: libgl2ps-devel libxml2-devel libogg-devel libtheora-devel
BuildPreReq: libGLUT-devel python-module-sphinx-devel protobuf-compiler
BuildPreReq: libnetcdf_c++-devel
Requires: %name-doc = %version-%release

%description
ParaView is an application designed with the need to visualize large data
sets in mind. The goals of the ParaView project include the following:

    * Develop an open-source, multi-platform visualization application.
    * Support distributed computation models to process large data sets.
    * Create an open, flexible, and intuitive user interface.
    * Develop an extensible architecture based on open standards.

ParaView runs on distributed and shared memory parallel as well as single
processor systems and has been successfully tested on Windows, Linux and
various Unix workstations and clusters. Under the hood, ParaView uses the
Visualization Toolkit as the data processing and rendering engine and has a
user interface written using a unique blend of Tcl/Tk and C++.

%package devel
Summary: Development files for ParaView
Group: Development/C++
Requires: %name = %version-%release

%description devel
%summary.

%package devel-static
Summary: Static libraries of ParaView
Group: Development/C++
Requires: %name-devel = %version-%release

%description devel-static
%summary.

%package doc
Summary: Documentation files for ParaView
Group: Documentation
BuildArch: noarch

%description doc
%summary.

%prep
%setup -n ParaView-%version

#Remove included thirdparty sources just to be sure
for x in autobahn vtkmpi4py vtkprotobuf twisted zope
do
  rm -r ThirdParty/*/${x}
done
for x in expat freetype gl2ps hdf5 jpeg libxml2 netcdf oggtheora png sqlite tiff zlib
do
  rm -r VTK/ThirdParty/${x}/vtk${x}
done

%build
mkdir altlinux
pushd altlinux
install -m644 %SOURCE3 .
sed -i 's|@LIBDIR@|%_libdir|' CMakeCache.txt ../VTK/ThirdParty/hdf5/CMakeLists.txt
%ifarch x86_64
LIB64=64
%endif
sed -i "s|@64@|$LIB64|" CMakeCache.txt
sed -i 's|@CXX@|g++|' CMakeCache.txt
sed -i 's|@CC@|gcc|' CMakeCache.txt
%remove_optflags -O2
%add_optflags -O1 -I%_libdir/hdf5-seq/include/netcdf
FLAGS="%optflags -fno-strict-aliasing"
cmake .. \
				-DPARAVIEW_USE_MPI:BOOL=OFF \
        -DPV_INSTALL_BIN_DIR:PATH=bin \
        -DPV_INSTALL_LIB_DIR:PATH=%_lib \
				-DCMAKE_C_FLAGS:STRING="$FLAGS" \
				-DCMAKE_CXX_FLAGS:STRING="$FLAGS" \
				-DCMAKE_Fortran_FLAGS:STRING="$FLAGS" \
				-DVTK_PYTHON_SETUP_ARGS="--prefix=%prefix --root=%buildroot"
cmake ..
export LD_LIBRARY_PATH=$PWD/bin
%make VERBOSE=1
popd

%install
#Fix permissions
find . \( -name \*.txt -o -name \*.xml -o -name '*.[ch]' -o -name '*.[ch][px][px]' \) -print0 | xargs -0 chmod -x

# Create some needed directories
install -d %buildroot%_miconsdir
install -pm644 %SOURCE1 %buildroot%_miconsdir
install -d %buildroot%_datadir/mime/packages
install -pm644 %SOURCE2 %buildroot%_datadir/mime/packages

pushd altlinux
export LD_LIBRARY_PATH=$PWD/bin
sed -i 's|""|\\"\\"|g' $(find ./ -name cmake_install.cmake)
%makeinstall_std
popd

rm -f %buildroot%_bindir/lproj

#Create desktop file
cat > paraview.desktop <<EOF
[Desktop Entry]
Name=ParaView Viewer
GenericName=Data Viewer
Comment=ParaView allows viewing of large data sets
Type=Application
Terminal=false
Icon=paraview_22x22
MimeType=application/x-paraview;
Categories=Graphics;Viewer;
Exec=paraview %%U
EOF
install -pDm644 paraview.desktop %buildroot%_desktopdir/paraview.desktop

pushd %buildroot%_bindir
chmod +x *
#execs=$(ls)
popd

pushd %buildroot%prefix
for i in bin/* $(find %_lib -name '*.so')
do
	chrpath -d $i ||:
done
popd

# delete unnecessary files
rm -f %buildroot%_libdir/paraview/*.a

%files
%doc License_v1.2.txt
%_bindir/*
%_libdir/paraview
%_desktopdir/paraview.desktop
%_miconsdir/*
%_datadir/mime/packages/paraview.xml

#files devel
#_libdir/*.so
#_libdir/*.cmake
#_libdir/CMake
#_includedir/*
#_man3dir/*
#exclude %_man3dir/icet*

%files doc
%doc Documentation/*

%changelog
* Thu Oct 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1
- Version 4.0.1 (without MPI)

* Wed Jul 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.1-alt11
- Rebuilt with OpenMPI 1.6

* Sun Jun 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.1-alt10
- Rebuilt with VTK 5.10.0

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.8.1-alt9.1
- Rebuild with Python-2.7

* Wed Sep 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.1-alt9
- Rebuilt with libhdf5-7-mpi

* Sun Apr 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.1-alt8
- Rebuilt with libnetcdf7

* Sun Mar 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.1-alt7
- BuildRequires: replaced xorg-devel by libGL-devel and libGLU-devel
- Disabled static package

* Fri Mar 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.1-alt6
- Rebuilt with Boost 1.46.1 and for debuginfo

* Sat Dec 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.1-alt5
- Removed links to *.so.*.* of Qt4

* Fri Dec 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.1-alt4
- Replaced native Qt4 libraries by links
- Moved CMake and *.so into devel package
- Extracted *.a into devel-static package

* Thu Dec 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.1-alt3
- Avoid floating point exception (ALT #24714)

* Thu Nov 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.1-alt2
- Fixed desktop file
- Avoid conflict with icet-devel-docs

* Tue Nov 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.1-alt1
- Version 3.8.1 (with OpenMPI)

* Fri Sep 03 2010 Michael Shigorin <mike@altlinux.org> 3.8.0-alt1
- initial ALT Linux package (based on Fedora one)
  + disabled MPI subpackages build for now
  + considerable spec cleanup

* Fri Jul 30 2010 Orion Poplawski <orion@cora.nwra.com> - 3.8.0-4
- Add patch to support python 2.7

* Tue Jul 27 2010 David Malcolm <dmalcolm@redhat.com> - 3.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Jun 4 2010 Orion Poplawski <orion@cora.nwra.com> - 3.8.0-2
- Drop doc sub-package

* Tue Jun 1 2010 Orion Poplawski <orion@cora.nwra.com> - 3.8.0-1
- Update to 3.8.0
- Update demo patch
- Update hdf5 patch
- Drop old documentation patches
- Add patch to add needed include headers
- Add patch from upstream to fix install path issue

* Sat Mar 13 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.6.2-4
- BR qt-assistant-adp-devel
- Don't Require qt4-assistant, should be qt-assistant-adp now, and it (or qt-x11
  4.6.x which Provides it) gets dragged in anyway by the soname dependencies

* Fri Feb 19 2010 Orion Poplawski <orion@cora.nwra.com> - 3.6.2-3
- More MPI packaging changes

* Tue Feb 16 2010 Orion Poplawski <orion@cora.nwra.com> - 3.6.2-2
- Conform to updated MPI packaging guidelines
- Build mpich2 version

* Mon Jan 4 2010 Orion Poplawski <orion@cora.nwra.com> - 3.6.2-1
- Update to 3.6.2

* Thu Nov 19 2009 Orion Poplawski <orion@cora.nwra.com> - 3.6.1-7
- New location for openmpi (fixes FTBFS bug #539179)

* Mon Aug 31 2009 Orion Poplawski <orion@cora.nwra.com> - 3.6.1-6
- Don't ship lproj, conflicts with vtk

* Thu Aug 27 2009 Orion Poplawski <orion@cora.nwra.com> - 3.6.1-5
- Specify PV_INSTALL_LIB_DIR as relative path, drop install prefix patch
- Update assitant patch to use assistant_adp, don't ship assistant-real

* Wed Aug 26 2009 Orion Poplawski <orion@cora.nwra.com> - 3.6.1-4
- Disable building various plugins that need OverView

* Tue Aug 25 2009 Orion Poplawski <orion@cora.nwra.com> - 3.6.1-3
- Disable building OverView - not ready yet

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 3.6.1-2
- rebuilt with new openssl

* Wed Jul 22 2009 Orion Poplawski <orion@cora.nwra.com> - 3.6.1-1
- Update to 3.6.1

* Thu May 7 2009 Orion Poplawski <orion@cora.nwra.com> - 3.4.0-5
- Update doc patch to look for help file in the right place (bug #499273)

* Tue Feb 24 2009 Orion Poplawski <orion@cora.nwra.com> - 3.4.0-4
- Rebuild with hdf5 1.8.2, gcc 4.4.0
- Update hdf5-1.8 patch to work with hdf5 1.8.2
- Add patch to allow build with Qt 4.5
- Move documentation into noarch sub-package

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> - 3.4.0-3
- rebuild with new openssl

* Sun Nov 30 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 3.4.0-2
- Rebuild for Python 2.6

* Fri Oct 17 2008 Orion Poplawski <orion@cora.nwra.com> - 3.4.0-1
- Update to 3.4.0 final

* Thu Oct 2 2008 Orion Poplawski <orion@cora.nwra.com> - 3.4.0-0.20081002.1
- Update 3.4.0 CVS snapshot
- Update gcc43 patch
- Drop qt patch, upstream now allows compiling against Qt 4.4.*

* Mon Aug 11 2008 Orion Poplawski <orion@cora.nwra.com> - 3.3.1-0.20080811.1
- Update 3.3.1 CVS snapshot
- Update hdf5 patch to drop upstreamed changes
- Fix mpi build (bug #450598)
- Use rpath instead of ls.so conf files so mpi and non-mpi can be installed at
  the same time
- mpi package now just ships mpi versions of the server components
- Drop useless mpi-devel subpackage
- Update hdf5 patch to fix H5pubconf.h -> H5public.h usage

* Wed May 20 2008 - Orion Poplawski <orion@cora.nwra.com> - 3.3.0-0.20080520.1
- Update to 3.3.0 CVS snapshot
- Update qt and gcc43 patches, drop unneeded patches
- Add openssl-devel, gnuplot, and wget BRs
- Update license text filename
- Set VTK_USE_RPATH to off, needed with development versions
- Run ctest in %%check - still need to exclude more tests

* Wed Mar 5 2008 - Orion Poplawski <orion@cora.nwra.com> - 3.2.1-5
- Rebuild for hdf5 1.8.0 using compatability API define and new patch

* Mon Feb 18 2008 - Orion Poplawski <orion@cora.nwra.com> - 3.2.1-4
- Add patch to compile with gcc 4.3

* Fri Jan 18 2008 - Orion Poplawski <orion@cora.nwra.com> - 3.2.1-3
- Add patch to fix parallel make
- Obsolete demos package (bug #428528)

* Tue Dec 18 2007 - Orion Poplawski <orion@cora.nwra.com> - 3.2.1-2
- Name ld.so.conf.d file with .conf extension
- Drop parallel make for now

* Mon Dec 03 2007 - Orion Poplawski <orion@cora.nwra.com> - 3.2.1-1
- Update to 3.2.1
- Use macros for version numbers
- Add patches to fix documentation install location and use assistant-qt4,
  not install copies of Qt libraries, and not use rpath.
- Install ld.so.conf.d file
- Fixup desktop files

* Thu Aug 23 2007 - Orion Poplawski <orion@cora.nwra.com> - 3.0.2-2
- Update license tag to BSD
- Fix make %%{_smp_mflags}
- Rebuild for ppc32

* Wed Jul 11 2007 - Orion Poplawski <orion@cora.nwra.com> - 3.0.2-1
- Update to 3.0.2
- Turn mpi build back on
- Add devel packages
- Remove demo package no longer in upstream
- Use cmake macros

* Thu Mar 08 2007 - Orion Poplawski <orion@cora.nwra.com> - 2.4.4-6
- Don't build mpi version until upstream fixes the build system

* Fri Dec 22 2006 - Orion Poplawski <orion@cora.nwra.com> - 2.4.4-5
- Fix .so permissions
- Patch for const issue
- Patch for new cmake
- Build with openmpi

* Thu Dec 14 2006 - Jef Spaleta <jspaleta@gmail.com> - 2.4.4-4
- Bump and build for python 2.5

* Fri Oct  6 2006 - Orion Poplawski <orion@cora.nwra.com> - 2.4.4-3
- Install needed python libraries to get around make install bug

* Wed Oct  4 2006 - Orion Poplawski <orion@cora.nwra.com> - 2.4.4-2
- Re-enable OSMESA support for FC6
- Enable python wrapping

* Fri Sep 15 2006 - Orion Poplawski <orion@cora.nwra.com> - 2.4.4-1
- Update to 2.4.4

* Thu Jun 29 2006 - Orion Poplawski <orion@cora.nwra.com> - 2.4.3-8
- No OSMesa support in FC5
- Make data sub-package pull in main package (bug #193837)
- A patch from CVS to fix vtkXOpenRenderWindow.cxx
- Need lam-devel for FC6

* Fri Apr 21 2006 - Orion Poplawski <orion@cora.nwra.com> - 2.4.3-7
- Re-enable ppc

* Mon Apr 17 2006 - Orion Poplawski <orion@cora.nwra.com> - 2.4.3-6
- Exclude ppc due to gcc bug #189160

* Wed Apr 12 2006 - Orion Poplawski <orion@cora.nwra.com> - 2.4.3-5
- Cleanup permissions

* Mon Apr 10 2006 - Orion Poplawski <orion@cora.nwra.com> - 2.4.3-4
- Add icon and cleanup desktop file

* Mon Apr 10 2006 - Orion Poplawski <orion@cora.nwra.com> - 2.4.3-3
- Add VTK_USE_MANGLE_MESA for off screen rendering
- Cleanup source permisions
- Add an initial .desktop file
- Make requirement on -data specific to version
- Don't package Ice-T man pages and cmake files

* Thu Apr  6 2006 - Orion Poplawski <orion@cora.nwra.com> - 2.4.3-2
- Add mpi version

* Tue Apr  4 2006 - Orion Poplawski <orion@cora.nwra.com> - 2.4.3-1
- Initial Fedora Extras version
