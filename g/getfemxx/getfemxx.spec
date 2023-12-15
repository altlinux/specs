%define sover 5
%define libgetfem libgetfem%sover
%add_python3_req_skip _getfem

%define rname getfem
Name: getfemxx
Version: 5.3
Release: alt10

Group: Development/C++
Summary: Generic and efficient C++ library for finite element methods
Url: http://getfem.org/
License: LGPLv2+

Provides: %rname = %EVR
Obsoletes: %rname < %EVR

Source0: getfem-%version.tar
Patch1: alt-ax_boost_base.patch
Patch2: getfemxx-ax-python.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: boost-devel gcc-c++ gcc-fortran glibc-devel python3-devel
BuildRequires: libnumpy-py3-devel python3-module-scipy python3-module-mpi4py
%ifnarch %{arm} aarch64 ppc64le
#BuildRequires: scilab
%endif

BuildPreReq: libmuparser-devel libmumps-devel
BuildPreReq: liblapack-devel
#libsuperlu-devel

%description
The Getfem++ project focuses on the development of a generic and
efficient C++ library for finite element methods. The goal is to provide
a library allowing the computation of any elementary matrix (even for
mixed finite element methods) on the largest class of methods and
elements, and for arbitrary dimension (i.e. not only 2D and 3D
problems).

%package -n %libgetfem
Group: System/Libraries
Summary: %rname library
Provides: libgetfemxx = %EVR
Obsoletes: libgetfemxx < %EVR
%description -n %libgetfem
%rname library

%package -n python3-module-getfem
Summary: Python bindings to %name
Group: Development/Python
%description -n python3-module-getfem
Python bindings to %name


%prep
%setup -n %rname-%version
%patch1 -p1
%patch2 -p2
%ifarch %e2k
# broken lib64 test
sed -i 's/|sparc64|/&e2k|/' m4/ax_boost_base.m4
%endif
%autoreconf

ln -sf %__python3 bin/python

%build
export PATH=$PWD/bin:$PATH
%add_optflags -fno-strict-aliasing -fpermissive -I%_includedir/metis0 -I%_includedir/mumps
export CFLAGS="%optflags" CXXFLAGS="%optflags"
%undefine _configure_gettext
%configure \
	--disable-static \
	--enable-shared \
	--enable-boost \
	--enable-mumps \
	--with-mumps="dmumps zmumps smumps cmumps mumps_common pord" \
	--with-blas=openblas \
	--with-pic \
	--with-matlab-toolbox-dir=%_datadir/getfem_toolbox \
	--enable-python3 \
#	--enable-qhull \
	#
CUT_CFLAGS=`grep "^CXXFLAGS" Makefile | head -n 1| sed "s|^CXXFLAGS[[:space:]][[:space:]]*=||"`
%make_build CFLAGS="$CUT_CFLAGS"

%install
%makeinstall_std

%if "%python3_sitelibdir_noarch/getfem" != "%python3_sitelibdir/getfem"
mv %buildroot%python3_sitelibdir_noarch/getfem/* \
	%buildroot%python3_sitelibdir/getfem/
%endif

mkdir -p %buildroot%__python3_dynlibdir
install -m 0644 \
    interface/src/python/_getfem.cpython*.so \
    %buildroot%python3_sitelibdir/

%files
%doc NEWS AUTHORS
%_datadir/getfem_toolbox
%_bindir/getfem-config
%_includedir/getfem
%_includedir/getfem_boost
%_includedir/gmm
%_libdir/*.so

%files -n %libgetfem
%_libdir/*.so.*

%files -n python3-module-getfem
%python3_sitelibdir/getfem
%python3_sitelibdir/*getfem*.so

%changelog
* Fri Dec 15 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 5.3-alt10
- NMU: fixed FTBFS on LoongArch

* Fri Apr 28 2023 Michael Shigorin <mike@altlinux.org> 5.3-alt9
- E2K: fix broken lib64 boost test (ilyakurdyukov@)

* Tue Jan 25 2022 Grigory Ustinov <grenka@altlinux.org> 5.3-alt8
- fix build with python3.10

* Thu Aug 26 2021 Sergey V Turchin <zerg@altlinux.org> 5.3-alt7
- fix build requires

* Tue Aug 17 2021 Vitaly Lipatov <lav@altlinux.ru> 5.3-alt6
- NMU: s/libnumpy-devel/libnumpy-py3-devel
- NMU: use python3-module-scipy python3-module-mpi4py without -devel

* Mon Jul 12 2021 Sergey V Turchin <zerg@altlinux.org> 5.3-alt5
- fix to find python (closes: 40456)

* Sat May 15 2021 Grigory Ustinov <grenka@altlinux.org> 5.3-alt4
- Disable qhull support, because it doesn't build with new qhull.

* Thu Apr 22 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 5.3-alt3
- Rebuilt with new mumps.

* Mon Mar 23 2020 Sergey V Turchin <zerg@altlinux.org> 5.3-alt2
- build without scilab

* Tue Jul 09 2019 Sergey V Turchin <zerg@altlinux.org> 5.3-alt1
- new version

* Fri Jul 05 2019 Sergey V Turchin <zerg@altlinux.org> 5.2-alt2
- build with python3
- build without scilab on arm, ppc64le

* Fri Nov 03 2017 Oleg Solovyov <mcpain@altlinux.org> 5.2-alt1
- Version 5.2

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 5.0-alt1.1
- (AUTO) subst_x86_64.

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

