%set_automake_version 1.11

%define rname getfem
Name: getfemxx
Version: 5.0
Release: alt1
%setup_python_module getfem

Group: Development/C++
Summary: Generic and efficient C++ library for finite element methods
Url: http://home.gna.org/getfem/
License: LGPLv2+

Requires: lib%name = %version-%release
Provides: %rname = %version-%release
Obsoletes: %rname < %version-%release

Source0: http://download.gna.org/getfem/stable/getfem-%version.tar.gz
Patch1: getfemxx-alt-qhull-2011.2.patch

BuildRequires: boost-devel gcc-c++ gcc-fortran glibc-devel-static libnumpy-devel
BuildRequires: python-module-scipy-devel python-module-mpi4py-devel
BuildRequires: scilab

BuildPreReq: libqhull-devel libmuparser-devel libmumps-devel
BuildPreReq: liblapack-devel 
#libsuperlu-devel

%description
The Getfem++ project focuses on the development of a generic and
efficient C++ library for finite element methods. The goal is to provide
a library allowing the computation of any elementary matrix (even for
mixed finite element methods) on the largest class of methods and
elements, and for arbitrary dimension (i.e. not only 2D and 3D
problems).

%package -n lib%name
Group: System/Libraries
Summary: %rname library
%description -n lib%name
%rname library

%package -n python-module-getfem
Summary: Python bindings to %name
Group: Development/Python
Requires: lib%name = %version-%release
%description -n python-module-getfem
Python bindings to %name


%prep
%setup -q -n %rname-%version
%patch1 -p2
%autoreconf

%build
%add_optflags -fno-strict-aliasing -fpermissive -I%_includedir/metis0
export CFLAGS="%optflags" CXXFLAGS="%optflags"
%undefine _configure_gettext
%configure \
	--disable-static \
	--enable-shared \
	--enable-boost \
	--enable-mumps \
	--with-mumps="dmumps zmumps smumps cmumps mumps_common pord" \
	--enable-qhull \
	--enable-scilab \
	--with-blas=openblas \
	--with-pic \
	--with-matlab-toolbox-dir=%_datadir/getfem_toolbox
CUT_CFLAGS=`grep "^CXXFLAGS" Makefile | head -n 1| sed "s|^CXXFLAGS[[:space:]][[:space:]]*=||"`
%make CFLAGS="$CUT_CFLAGS"

%install
%makeinstall_std

%ifarch x86_64
mv %buildroot%python_sitelibdir_noarch/getfem/* \
	%buildroot%python_sitelibdir/getfem/
%endif

%files
%doc NEWS AUTHORS
%_datadir/getfem_toolbox
%_bindir/getfem-config
%_includedir/getfem
%_includedir/getfem_boost
%_includedir/gmm
%_libdir/*.so

%files -n lib%name
%_libdir/*.so.*

%files -n python-module-getfem
%python_sitelibdir/getfem

%changelog
* Tue Jan 19 2016 Andrey Cherepanov <cas@altlinux.org> 5.0-alt1
- New version
- Use bundled libsuperlu
- Enable scilab support

* Thu Nov 07 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2-alt2
- Fixed build

* Tue Oct 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2-alt1
- Version 4.2

* Sat Aug 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt2
- Built with OpenBLAS instead of GotoBLAS2

* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 4.1.1-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Dec 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1
- Version 4.1.1

* Wed Dec 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1-alt1.3
- Rebuilt with qhull 2011.2

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.1-alt1.2.1
- Rebuild with Python-2.7

* Thu May 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1-alt1.2
- Rebuilt with qhull 2011.1

* Wed Apr 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1-alt1.1
- Built with GotoBLAS2 instead of ATLAS

* Thu Aug 26 2010 Sergey V Turchin <zerg@altlinux.org> 4.1-alt1
- new version

* Fri Jul 16 2010 Sergey V Turchin <zerg@altlinux.org> 4.0.0-alt0.M51.1
- built for M51

* Mon Jan 18 2010 Sergey V Turchin <zerg@altlinux.org> 4.0.0-alt1
- new version

* Wed Aug 26 2009 Sergey V Turchin <zerg@altlinux.org> 3.1-alt2
- fix compile with gcc-4.4

* Thu Oct 16 2008 Sergey V Turchin <zerg at altlinux dot org> 3.1-alt1
- initial specfile

