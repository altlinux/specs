Name: syfi
Version: 1.0.0
Release: alt1.bzr20120323
Summary: Symbolic Finite Elements (SyFi) and The SyFi Form Compiler (SFC)
License: GPL v2
Group: Sciences/Mathematics
Url: http://www.fenics.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# lp:fenics-syfi
Source: %name-%version.tar.gz

Requires: lib%name = %version-%release
Requires: python-module-sfc = %version-%release

BuildPreReq: python-devel
BuildPreReq: cmake swig libginac-devel python-module-swiginac ufc-devel ufl
BuildPreReq: gcc-c++ libnumpy-devel
BuildPreReq: texlive-latex-recommended texlive-pictures chrpath
BuildPreReq: ghostscript-utils doxygen python-module-epydoc graphviz

%description
SyFi is a package for defining finite element methods. In contrast to most other
finite element packages, the finite elements, the weak forms etc are defined
symbolically.

The SyFi Form Compiler (SFC) is a Python module for compiling variational forms
written using UFL to C++ code implementing the UFC interface.

%package -n lib%name
Summary: Shared library of Symbolic Finite Elements (SyFi)
Group: System/Libraries

%description -n lib%name
SyFi is a package for defining finite element methods. In contrast to most other
finite element packages, the finite elements, the weak forms etc are defined
symbolically.

This package contains shared library of SyFi.

%package -n lib%name-devel
Summary: Development files of Symbolic Finite Elements (SyFi)
Group: Development/C++
Requires: lib%name = %version-%release
Requires: python-module-numpy
# temporary provide for bootstrap
#Provides: pkgconfig(python-2)

%description -n lib%name-devel
SyFi is a package for defining finite element methods. In contrast to most other
finite element packages, the finite elements, the weak forms etc are defined
symbolically.

This package contains shared library of SyFi.

%package -n python-module-%name
Summary: Python module of Symbolic Finite Elements (SyFi)
Group: Development/Python
Requires: lib%name = %version-%release

%description -n python-module-%name
SyFi is a package for defining finite element methods. In contrast to most other
finite element packages, the finite elements, the weak forms etc are defined
symbolically.

This package contains Python module of SyFi.

%package -n sfc
Summary: The SyFi Form Compiler (SFC)
Group: Development/Python
BuildArch: noarch
Requires: python-module-sfc = %version-%release

%description -n sfc
The SyFi Form Compiler (SFC) is a Python module for compiling variational forms
written using UFL to C++ code implementing the UFC interface.

%package -n python-module-sfc
Summary: Python module of the SyFi Form Compiler (SFC)
Group: Development/Python
Requires: lib%name = %version-%release
Requires: python-module-%name = %version-%release
# skip requires for bootstrap
%add_python_req_skip dolfin_utils

%description -n python-module-sfc
The SyFi Form Compiler (SFC) is a Python module for compiling variational forms
written using UFL to C++ code implementing the UFC interface.

%package doc
Summary: Documentation for Symbolic Finite Elements and SyFi Form Compiler
Group: Development/Documentation
BuildArch: noarch

%description doc
SyFi is a package for defining finite element methods. In contrast to most other
finite element packages, the finite elements, the weak forms etc are defined
symbolically.

This package contains documentation for SyFi and SFC.

%package demo
Summary: Demo for Symbolic Finite Elements and SyFi Form Compiler
Group: Development/Documentation
BuildArch: noarch

%description demo
SyFi is a package for defining finite element methods. In contrast to most other
finite element packages, the finite elements, the weak forms etc are defined
symbolically.

This package contains demo for SyFi and SFC.

%prep
%setup

%build
cmake \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_Fortran_FLAGS:STRING="%optflags" \
	-DCMAKE_EXPORT_COMPILE_COMMANDS:BOOL=ON \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	-DSYFI_ENABLE_DOCS:BOOL=ON \
	-DSYFI_LIB_DIR:PATH=%_lib \
	-DSYFI_PYTHON_EXT_DIR:PATH=%_lib/python%_python_version/site-packages \
	-DSYFI_PYTHON_MODULE_DIR:PATH=%_lib/python%_python_version/site-packages \
	-DSYFI_PKGCONFIG_DIR:PATH=%_lib/pkgconfig \
	-DSYFI_ENABLE_TESTING:BOOL=ON \
	.
%make_build VERBOSE=1

pushd doc/reference
./makedoc.sh
mv html reference
popd

%install
%makeinstall_std

export PYTHONPATH=%buildroot%python_sitelibdir:%_libexecdir/petsc-real/python
pushd doc/sfc_reference
./makedoc.sh
mv html sfc_reference
popd

pushd doc
install -d %buildroot%_docdir/%name
cp -fR papers presentations reference/reference \
	sfc_reference/sfc_reference %buildroot%_docdir/%name/
popd

chrpath -d %buildroot%python_sitelibdir/_SyFi.so

%files
%doc README AUTHORS ChangeLog COPYING

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/%name.pc
%dir %_datadir/%name
%_datadir/%name/cmake
%_datadir/%name/%name.conf

%files -n python-module-%name
%python_sitelibdir/*SyFi*

%files doc
%doc %_docdir/%name

%files -n sfc
%_bindir/*
%_man1dir/*

%files -n python-module-sfc
%python_sitelibdir/sfc

%files demo
%dir %_datadir/%name
%_datadir/%name/demo

%changelog
* Sun May 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.bzr20120323
- New snapshot

* Tue Jan 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.bzr20111214
- Version 1.0.0

* Tue Dec 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.beta.bzr20111129
- Version 1.0.0-beta

* Thu Oct 27 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.2-alt1.bzr20110603.3
- Rebuild with Python-2.7

* Thu Oct 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1.bzr20110603.2
- Rebuilt with updated NumPy

* Tue Aug 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1.bzr20110603.1
- Rebuilt with libginac 1.6.1

* Wed Aug 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1.bzr20110603
- New snapshot

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1.bzr20100621.4
- Rebuilt

* Wed Mar 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1.bzr20100621.3
- Rebuilt for debuginfo

* Thu Dec 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1.bzr20100621.2
- Rebuilt with libcln6

* Mon Aug 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1.bzr20100621.1
- Removed paths to buildroot

* Tue Aug 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1.bzr20100621
- Version 0.6.2

* Wed Jun 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt4.bzr20100615
- New snapshot

* Tue Jun 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt4.bzr20090819.4
- Disabled requirement on dolfin_utils (preparing for CGAL 3.6)

* Thu Jun 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt4.bzr20090819.3
- Rebuilt with NumPy 2.0.0

* Wed Mar 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt4.bzr20090819.1
- Fixed build error on x86_64

* Wed Dec 09 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt4.bzr20090819
- New snapshot

* Sun Dec 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt3.hg20090831.2
- Enabled requirement on dolfin_utils

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt3.hg20090831.1
- Rebuilt with python 2.6 (bootstrap)

* Mon Aug 31 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt3.hg20090831
- Snapshot 20090831

* Tue Aug 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt3.hg20090822.2
- Disabled provides pkgconfig(python-2)
- Enabled requirement on dolfin_utils

* Sun Aug 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt3.hg20090822.1
- Changed requirement: pkgconfig(python-2) -> pkgconfig(python%%__python_version)
- Temporary porvides pkgconfig(python-2) for bootstrap

* Sat Aug 22 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt3.hg20090822
- New snapshot

* Wed Jul 15 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt2
- Added previously skipped requirement

* Thu Jul 09 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1
- Bootstrap
