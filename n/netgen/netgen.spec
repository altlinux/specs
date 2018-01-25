%define mpiimpl openmpi-compat
%define mpidir %_libdir/%mpiimpl

%set_automake_version 1.11
%def_with python2
%def_without python3

%define oname netgen
Name: %oname
Version: 6.1
Release: alt1.dev.git20150306.qa4
Summary: Automatic 3d tetrahedral mesh generator
License: LGPL
Group: Graphics
Url: http://www.hpfem.jku.at/netgen/

# svn://svn.code.sf.net/p/netgen-mesher/code/netgen
Source: %name-%version.tar
#Source1: demoapp.tar
#Source2: dropsexport.tar

Requires: lib%oname = %version-%release tcl-tix
BuildRequires(pre): rpm-build-tcl
BuildRequires: %mpiimpl-devel libjpeg-devel libavcodec-devel tcl-devel tk-devel
BuildRequires: tcl-togl-devel libGL-devel libGLU-devel libparmetis-devel
BuildRequires: libavformat-devel libswscale-devel bzlib-devel zlib-devel
BuildRequires: libopencascade-devel
BuildRequires: libXmu-devel chrpath
%if_with python2
BuildRequires: python-devel boost-python-devel
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel boost-python3-devel
%endif

Conflicts: %oname-py3

%add_findreq_skiplist %_datadir/%oname/*

%description
NETGEN is an automatic 3d tetrahedral mesh generator. It accepts input
from constructive solid geometry (CSG) or boundary representation (BRep)
from STL file format. The connection to a geometry kernel allows the
handling of IGES and STEP files. NETGEN contains modules for mesh
optimization and hierarchical mesh refinement.

%package -n lib%oname
Summary: Shared library of NETGEN
Group: System/Libraries
Conflicts: lib%oname-py3

%description -n lib%oname
NETGEN is an automatic 3d tetrahedral mesh generator. It accepts input
from constructive solid geometry (CSG) or boundary representation (BRep)
from STL file format. The connection to a geometry kernel allows the
handling of IGES and STEP files. NETGEN contains modules for mesh
optimization and hierarchical mesh refinement.

This package contains shared library of NETGEN.

%package -n python-module-%oname
Summary: Python bindings of NETGEN
Group: Development/Python
Requires: lib%oname = %version-%release
Conflicts: python3-module-%oname

%description -n python-module-%oname
NETGEN is an automatic 3d tetrahedral mesh generator. It accepts input
from constructive solid geometry (CSG) or boundary representation (BRep)
from STL file format. The connection to a geometry kernel allows the
handling of IGES and STEP files. NETGEN contains modules for mesh
optimization and hierarchical mesh refinement.

This package contains Python bindings of NETGEN.

%if_with python3
%package %oname-py3
Summary: Automatic 3d tetrahedral mesh generator
Group: Graphics
Conflicts: %oname

%description %oname-py3
NETGEN is an automatic 3d tetrahedral mesh generator. It accepts input
from constructive solid geometry (CSG) or boundary representation (BRep)
from STL file format. The connection to a geometry kernel allows the
handling of IGES and STEP files. NETGEN contains modules for mesh
optimization and hierarchical mesh refinement.

%package -n python3-module-%oname
Summary: Python bindings of NETGEN
Group: Development/Python3
Requires: lib%oname-py3 = %version-%release
Conflicts: python-module-%oname

%description -n python3-module-%oname
NETGEN is an automatic 3d tetrahedral mesh generator. It accepts input
from constructive solid geometry (CSG) or boundary representation (BRep)
from STL file format. The connection to a geometry kernel allows the
handling of IGES and STEP files. NETGEN contains modules for mesh
optimization and hierarchical mesh refinement.

This package contains Python bindings of NETGEN.

%package -n lib%oname-py3
Summary: Shared library of NETGEN
Group: System/Libraries
Conflicts: lib%oname

%description -n lib%oname-py3
NETGEN is an automatic 3d tetrahedral mesh generator. It accepts input
from constructive solid geometry (CSG) or boundary representation (BRep)
from STL file format. The connection to a geometry kernel allows the
handling of IGES and STEP files. NETGEN contains modules for mesh
optimization and hierarchical mesh refinement.

This package contains shared library of NETGEN.

%package -n lib%oname-py3-devel
Summary: Development files of NETGEN
Group: Development/C++
BuildArch: noarch
Requires: lib%oname-py3 = %version-%release
Conflicts: lib%oname-devel

%description -n lib%oname-py3-devel
NETGEN is an automatic 3d tetrahedral mesh generator. It accepts input
from constructive solid geometry (CSG) or boundary representation (BRep)
from STL file format. The connection to a geometry kernel allows the
handling of IGES and STEP files. NETGEN contains modules for mesh
optimization and hierarchical mesh refinement.

This package contains development files of NETGEN.
%endif

%package -n lib%oname-devel
Summary: Development files of NETGEN
Group: Development/C++
BuildArch: noarch
Requires: lib%oname = %version-%release
Conflicts: lib%oname-py3-devel

%description -n lib%oname-devel
NETGEN is an automatic 3d tetrahedral mesh generator. It accepts input
from constructive solid geometry (CSG) or boundary representation (BRep)
from STL file format. The connection to a geometry kernel allows the
handling of IGES and STEP files. NETGEN contains modules for mesh
optimization and hierarchical mesh refinement.

This package contains development files of NETGEN.

%package doc
Summary: Documentation for NETGEN
Group: Documentation
BuildArch: noarch

%description doc
NETGEN is an automatic 3d tetrahedral mesh generator. It accepts input
from constructive solid geometry (CSG) or boundary representation (BRep)
from STL file format. The connection to a geometry kernel allows the
handling of IGES and STEP files. NETGEN contains modules for mesh
optimization and hierarchical mesh refinement.

This package contains documentation for NETGEN.

%package tutorials
Summary: Tutorials for NETGEN
Group: Documentation
BuildArch: noarch

%description tutorials
NETGEN is an automatic 3d tetrahedral mesh generator. It accepts input
from constructive solid geometry (CSG) or boundary representation (BRep)
from STL file format. The connection to a geometry kernel allows the
handling of IGES and STEP files. NETGEN contains modules for mesh
optimization and hierarchical mesh refinement.

This package contains tutorials for NETGEN.

%package demo
Summary: Demo for NETGEN
Group: Graphics
BuildArch: noarch
Requires: %name = %version-%release

%description demo
NETGEN is an automatic 3d tetrahedral mesh generator. It accepts input
from constructive solid geometry (CSG) or boundary representation (BRep)
from STL file format. The connection to a geometry kernel allows the
handling of IGES and STEP files. NETGEN contains modules for mesh
optimization and hierarchical mesh refinement.

This package contains demo for NETGEN.

%prep
%setup
%ifarch x86_64
sed -i "s|@UINT64_C@|UL|" ng/ngpkg.cpp
%else
sed -i "s|@UINT64_C@|ULL|" ng/ngpkg.cpp
%endif

sed -i 's|@MPIDIR@|%mpidir|g' configure.ac

%if_with python3
cp -fR . ../python3
sed -i 's|@PYVER@|%_python3_version%_python3_abiflags|' \
	../python3/ng/Makefile.am
sed -i 's|@IF3@|3|' ../python3/ng/Makefile.am
sed -i 's|@PYVER@|%_python3_version|' ../python3/configure.ac
sed -i 's|boost_python|boost_python3|g' ../python3/m4/ax_boost_python.m4
%endif

sed -i 's|@PYVER@|%_python_version|' ng/Makefile.am
sed -i 's|@IF3@||' ng/Makefile.am
sed -i 's|@PYVER@|%_python_version|' configure.ac

#tar -xf %SOURCE1
#tar -xf %SOURCE2

%build
%add_optflags $(pkg-config --cflags parmetis)
mpi-selector --set %mpiimpl
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"
source %mpidir/bin/mpivars.sh
export MPIDIR=%mpidir

PARS="-DPARALLEL -DOMPI_IGNORE_CXX_SEEK -DMETIS -DHAVE_IOMANIP"
PARS="$PARS -DGLX_GLXEXT_PROTOTYPES -I%mpidir/include"
%add_optflags $PARS -DJPEGLIB -DFFMPEG -DHAVE_IOSTREAM -DHAVE_LIMITS

%if_with python2
%autoreconf
%configure \
	--enable-occ \
	--enable-nglib \
	--enable-parallel \
	--enable-jpeglib \
	--enable-ffmpeg \
	--enable-python \
	--with-tcl=%_libdir \
	--with-togl=%_tcllibdir \
	--with-tk=%_libdir \
	--with-metis=%prefix \
	--with-boost=yes
%make -C libsrc/linalg
%make -C libsrc/gprim
%make -C libsrc/general
%make -C libsrc/meshing
%make -C libsrc/interface
%make -C libsrc/visualization
%make -C libsrc/interface clean
%make -C libsrc/interface \
	LIBVISUAL="-Wl,--no-as-needed $PWD/libsrc/visualization/libvisual.la -Wl,--as-needed"
%make_build TCLLIBDIR=%_tcllibdir
# for complete linking of libraries
for i in csg stlgeom meshing interface geom2d
do
	pushd libsrc/$i
	%make clean
	popd
	if [ "$i" == "csg" ]; then
		%make_build TCLLIBDIR=%_tcllibdir \
			NGLIB=$PWD/nglib/libnglib.la LIBNETGEN=$PWD/nglib/libnetgen.la \
			LIBVISUAL=$PWD/libsrc/visualization/libvisual.la TOPDIR=$PWD
	elif [ "$i" == "interface" ]; then
		%make_build TCLLIBDIR=%_tcllibdir \
			NGLIB=$PWD/nglib/libnglib.la \
			LIBNETGEN="-Wl,--no-as-needed $PWD/nglib/libnetgen.la -Wl,--as-needed" \
			LIBVISUAL="-Wl,--no-as-needed $PWD/libsrc/visualization/libvisual.la -Wl,--as-needed" \
			LIBCSG="-Wl,--no-as-needed $PWD/libsrc/csg/libcsg.la -Wl,--as-needed" \
			TOPDIR=$PWD
	else
		%make_build TCLLIBDIR=%_tcllibdir \
			NGLIB=$PWD/nglib/libnglib.la \
			LIBNETGEN="-Wl,--no-as-needed $PWD/nglib/libnetgen.la -Wl,--as-needed" \
			LIBCSG="-Wl,--no-as-needed $PWD/libsrc/csg/libcsg.la -Wl,--as-needed" \
			LIBVISUAL=$PWD/libsrc/visualization/libvisual.la \
			TOPDIR=$PWD
	fi
done
%endif

%if_with python3
pushd ../python3
%autoreconf
%configure \
	--enable-occ \
	--enable-nglib \
	--enable-parallel \
	--enable-jpeglib \
	--enable-ffmpeg \
	--enable-python \
	--with-tcl=%_libdir \
	--with-togl=%_tcllibdir \
	--with-tk=%_libdir \
	--with-metis=%prefix \
	--with-boost=yes
%make -C libsrc/linalg
%make -C libsrc/gprim
%make -C libsrc/general
%make -C libsrc/meshing
%make -C libsrc/interface
%make -C libsrc/visualization
%make -C libsrc/interface clean
%make -C libsrc/interface \
	LIBVISUAL="-Wl,--no-as-needed $PWD/libsrc/visualization/libvisual.la -Wl,--as-needed"
%make_build TCLLIBDIR=%_tcllibdir
# for complete linking of libraries
for i in csg stlgeom meshing interface geom2d
do
	pushd libsrc/$i
	%make clean
	popd
	if [ "$i" == "csg" ]; then
		%make_build TCLLIBDIR=%_tcllibdir \
			NGLIB=$PWD/nglib/libnglib.la LIBNETGEN=$PWD/nglib/libnetgen.la \
			LIBVISUAL=$PWD/libsrc/visualization/libvisual.la TOPDIR=$PWD
	elif [ "$i" == "interface" ]; then
		%make_build TCLLIBDIR=%_tcllibdir \
			NGLIB=$PWD/nglib/libnglib.la \
			LIBNETGEN="-Wl,--no-as-needed $PWD/nglib/libnetgen.la -Wl,--as-needed" \
			LIBVISUAL="-Wl,--no-as-needed $PWD/libsrc/visualization/libvisual.la -Wl,--as-needed" \
			LIBCSG="-Wl,--no-as-needed $PWD/libsrc/csg/libcsg.la -Wl,--as-needed" \
			TOPDIR=$PWD
	else
		%make_build TCLLIBDIR=%_tcllibdir \
			NGLIB=$PWD/nglib/libnglib.la \
			LIBNETGEN="-Wl,--no-as-needed $PWD/nglib/libnetgen.la -Wl,--as-needed" \
			LIBCSG="-Wl,--no-as-needed $PWD/libsrc/csg/libcsg.la -Wl,--as-needed" \
			LIBVISUAL=$PWD/libsrc/visualization/libvisual.la \
			TOPDIR=$PWD
	fi
done
popd
%endif

%install
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"
export MPIDIR=%mpidir

%if_with python2
install -d %buildroot%_libdir
cp -P nglib/.libs/*.so* libsrc/csg/.libs/*.so* \
	libsrc/visualization/.libs/*.so* \
	%buildroot%_libdir/

%makeinstall_std TCLLIBDIR=%_tcllibdir TOPDIR=$PWD
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* %buildroot%python_sitelibdir
%endif

pushd %buildroot%_libdir
for i in *.so.?; do
	lib=$(echo $i |sed 's|\.so.*||')
	ln -s ../../$i %buildroot%python_sitelibdir/$lib.so
done
popd

#pushd dropsexport
#autoreconf
#configure \
#	--enable-static=no \
#	--with-netgen=%buildroot \
#	--with-netgensrc=$PWD/..
#make_build
#makeinstall_std
#popd

for i in %buildroot%_libdir/*.so %buildroot%_bindir/*; do
	chrpath -r %mpidir/lib:%_tcllibdir $i ||:
done
%endif

%if_with python3
pushd ../python3
install -d %buildroot%_libdir
cp -P nglib/.libs/*.so* libsrc/csg/.libs/*.so* \
	libsrc/visualization/.libs/*.so* \
	%buildroot%_libdir/

%makeinstall_std TCLLIBDIR=%_tcllibdir TOPDIR=$PWD

%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* %buildroot%python3_sitelibdir
%endif
popd

pushd %buildroot%_libdir
for i in *.so.?; do
	lib=$(echo $i |sed 's|\.so.*||')
	ln -s ../../$i %buildroot%python3_sitelibdir/$lib.so
done
popd

for i in %buildroot%_libdir/*.so %buildroot%_bindir/*; do
	chrpath -r %mpidir/lib:%_tcllibdir $i ||:
done
%endif

%if_with python2
%files
%doc AUTHORS
%_bindir/*

%files -n lib%oname
%_libdir/*.so*

%files -n lib%oname-devel
%_includedir/*

%files doc
%_docdir/%name

%files tutorials
%_datadir/%name

#files demo
#doc demoapp

%files -n python-module-%oname
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*

%files %oname-py3
%doc AUTHORS
%_bindir/*

%files -n lib%oname-py3
%_libdir/*.so*

%files -n lib%oname-py3-devel
%_includedir/*
%endif

%changelog
* Thu Jan 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 6.1-alt1.dev.git20150306.qa4
- Fixed build.

* Fri Jul 07 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 6.1-alt1.dev.git20150306.qa3
- Fixed build with new ffmpeg

* Thu Mar 23 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 6.1-alt1.dev.git20150306.qa2
- NMU: fixed build and rebuilt against Tcl/Tk 8.6.

* Thu Apr 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 6.1-alt1.dev.git20150306.qa1
- NMU: rebuilt with boost 1.57.0 -> 1.58.0.

* Mon Mar 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.1-alt1.dev.git20150306
- Version 6.1-dev

* Mon Jul 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3-alt1.svn20140625
- New snapshot

* Thu Jun 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3-alt1.svn20140428
- Version 5.3

* Wed Nov 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.2-alt3.svn20130902
- Fixed build

* Wed Sep 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.2-alt2.svn20130902
- Fixed build

* Thu Sep 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.2-alt1.svn20130902
- Version 5.2

* Fri Jul 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1-alt1.svn20130527
- New snapshot

* Wed Feb 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1-alt1.svn20130203
- Version 5.1

* Tue Aug 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0-alt1.svn20120820
- Version 5.0

* Tue Jun 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.14-alt4.svn20120215
- Rebuilt with OpenMPI 1.6

* Mon May 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.14-alt3.svn20120215
- Fixed build

* Thu Mar 01 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.14-alt2.svn20120215
- New snapshot
- Built with OpenCASCADE

* Tue Dec 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.14-alt2.svn20111201
- New snapshot
- Rebuilt with libparmetis instead of libparmetis0

* Fri Nov 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.14-alt2.svn20111103
- New snapshot

* Wed Sep 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.14-alt2.svn20110725.1
- Rebuilt with libparmetis0 instead of libparmetis

* Mon Aug 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.14-alt2.svn20110725
- Version 4.9.14

* Sun May 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.13-alt2.svn20101017.4
- Built without OpenCASCADE (awaiting fix from upstream)

* Thu Mar 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.13-alt2.svn20101017.3
- Rebuilt for debuginfo

* Sat Feb 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.13-alt2.svn20101017.2
- Rebuilt with parmetis 3.1.1-alt10

* Mon Nov 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.13-alt2.svn20101017.1
- Rebuilt for soname set-versions

* Wed Oct 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.13-alt2.svn20101017
- New snapshot

* Tue Jul 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.13-alt2
- Rebuilt with reformed ParMetis

* Mon Jun 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.13-alt1
- Version 4.9.13
- Added demo

* Mon Mar 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.9-alt4
- Fixed build with modified OpenCascade headers

* Tue Dec 22 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.9-alt3
- Rebuilt with OpenCascade

* Mon Aug 31 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.9-alt2
- Rebuilt without OpenCascade

* Thu Aug 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.9-alt1
- Initial build for Sisyphus

