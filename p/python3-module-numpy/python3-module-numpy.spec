%define _unpackaged_files_terminate_build 1

%define oname numpy
%def_without latex
%def_without doc
%def_without tests

Name: python3-module-%oname
Epoch: 1
Version: 1.19.5
Release: alt1

Summary: NumPy: array processing for numbers, strings, records, and objects
License: BSD-3-Clause
Group: Development/Python3
Url: https://www.numpy.org/

# https://github.com/numpy/numpy.git
Source: %name-%version.tar
Source2: site.cfg
Patch0: %oname-%version-Remove-strict-dependency-on-testing-package.patch

BuildRequires(pre): rpm-macros-sphinx3
BuildRequires(pre): rpm-build-python3
BuildRequires: /proc
BuildRequires: doxygen gcc-c++ gcc-fortran liblapack-devel
BuildRequires: swig
BuildRequires: python3-devel
BuildRequires: python3-module-Cython
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-alabaster python3-module-html5lib python3-module-matplotlib-sphinxext python3-module-notebook python3-module-numpydoc python3-module-objects.inv
%if_with doc
BuildRequires: tex(preview.sty)
%endif

# https://bugzilla.altlinux.org/show_bug.cgi?id=18379
%add_python3_req_skip Scons setuptools distutils nose number code_generators
# See bug 35103
%add_python3_req_skip setuptools.command.develop setuptools.command.egg_info
%add_python3_req_skip code_generators.genapi code_generators.numpy_api genapi numpy._build_utils.apple_accelerate numpy_api

%add_findprov_skiplist %python3_sitelibdir/%oname/random/_examples/*
%add_findreq_skiplist  %python3_sitelibdir/%oname/random/_examples/*

%py3_provides %oname.addons
Provides: python3-module-numpy-addons = %EVR

%description
NumPy is a general-purpose array-processing package designed to
efficiently manipulate large multi-dimensional arrays of arbitrary
records without sacrificing too much speed for small multi-dimensional
arrays.  NumPy is built on the Numeric code base and adds features
introduced by numarray as well as an extended C-API and the ability to
create arrays of arbitrary type.

There are also basic facilities for discrete fourier transform,
basic linear algebra and random number generation.

%package testing
Summary: Testing part of NumPy (Python 3)
Group: Development/Python3
Requires: %name = %EVR
%add_python3_req_skip setuptools

%description testing
NumPy is a general-purpose array-processing package designed to
efficiently manipulate large multi-dimensional arrays of arbitrary
records without sacrificing too much speed for small multi-dimensional
arrays.  NumPy is built on the Numeric code base and adds features
introduced by numarray as well as an extended C-API and the ability to
create arrays of arbitrary type.

This package contains testing part of NumPy.

%package tests
Summary: Tests for NumPy (Python 3)
Group: Development/Python3
Requires: %name = %EVR
%add_python3_req_skip core scipy

%description tests
NumPy is a general-purpose array-processing package designed to
efficiently manipulate large multi-dimensional arrays of arbitrary
records without sacrificing too much speed for small multi-dimensional
arrays.  NumPy is built on the Numeric code base and adds features
introduced by numarray as well as an extended C-API and the ability to
create arrays of arbitrary type.

This package contains tests NumPy.

%package -n lib%oname-py3-devel
Summary: Development files of NumPy (Python 3)
Group: Development/Python3
Requires: %name = %EVR
Requires: python3-devel

%description -n lib%oname-py3-devel
NumPy is a general-purpose array-processing package designed to
efficiently manipulate large multi-dimensional arrays of arbitrary
records without sacrificing too much speed for small multi-dimensional
arrays.  NumPy is built on the Numeric code base and adds features
introduced by numarray as well as an extended C-API and the ability to
create arrays of arbitrary type.

This package contains development files of NumPy.

%package pickles
Summary: Pickles for NumPy
Group: Development/Python3

%description pickles
NumPy is a general-purpose array-processing package designed to
efficiently manipulate large multi-dimensional arrays of arbitrary
records without sacrificing too much speed for small multi-dimensional
arrays.  NumPy is built on the Numeric code base and adds features
introduced by numarray as well as an extended C-API and the ability to
create arrays of arbitrary type.

This package contains pickles for NumPy.

%if_with doc
%package doc
Summary: Documentation modules of NumPy
Group: Development/Python3
Requires: %name = %EVR
Conflicts: %name < %EVR
%add_python3_req_skip Numeric

%description doc
NumPy is a general-purpose array-processing package designed to
efficiently manipulate large multi-dimensional arrays of arbitrary
records without sacrificing too much speed for small multi-dimensional
arrays.  NumPy is built on the Numeric code base and adds features
introduced by numarray as well as an extended C-API and the ability to
create arrays of arbitrary type.

This package contains documentation modules of NumPy.

%package doc-html
Summary: Documentation in HTML for NumPy
Group: Development/Documentation
BuildArch: noarch

%description doc-html
NumPy is a general-purpose array-processing package designed to
efficiently manipulate large multi-dimensional arrays of arbitrary
records without sacrificing too much speed for small multi-dimensional
arrays.  NumPy is built on the Numeric code base and adds features
introduced by numarray as well as an extended C-API and the ability to
create arrays of arbitrary type.

This package contains documentation for NumPy in HTML format.

%package doc-pdf
Summary: Documentation in PDF for NumPy
Group: Development/Documentation
BuildArch: noarch

%description doc-pdf
NumPy is a general-purpose array-processing package designed to
efficiently manipulate large multi-dimensional arrays of arbitrary
records without sacrificing too much speed for small multi-dimensional
arrays.  NumPy is built on the Numeric code base and adds features
introduced by numarray as well as an extended C-API and the ability to
create arrays of arbitrary type.

This package contains documentation for NumPy in PDF format.
%endif

%prep
%setup
%patch0 -p1

install -m644 %SOURCE2 .
sed -i 's|@LIBDIR@|%_libdir|g' site.cfg
sed -i 's|@PYVER@|%_python3_version|g' site.cfg doc/Makefile
sed -i 's|@PYSUFF@|3|' site.cfg

# headers
sed -i 's|^prefix.*|prefix=%python3_sitelibdir/%oname/core|' \
	%oname/core/npymath.ini.in
sed -i 's|^includedir.*|includedir=%_includedir/python%_python3_version/%oname|' \
	%oname/core/npymath.ini.in

%if_with doc
# Sphinx
sed -i "s|@TOP@|$PWD|" \
	doc/source/conf.py
%prepare_sphinx3 doc
ln -s ../objects.inv doc/source/objects.inv
%endif

%build
INCS="-I%_includedir/suitesparse -I$PWD/numpy/core/include/numpy"
INCS="$INCS -I$PWD/numpy/core/include -I%buildroot%_includedir/python%_python3_version/%oname"
INCS="$INCS -I%buildroot%_includedir"
DEFS="-DHAVE_FREXPF -DHAVE_FREXPL -DHAVE_FREXP -DHAVE_LDEXP -DHAVE_LDEXPL"
DEFS="$DEFS -DHAVE_EXPM1 -DHAVE_LOG1P -DHAVE_LDEXPF"
DEFS="$DEFS -UNPY_CPU_AMD64 -UNPY_CPU_X86"
%add_optflags -fno-strict-aliasing $DEFS $INCS %optflags_shared

%python3_build_debug --fcompiler=gnu95

%install
INCS="-I%_includedir/suitesparse -I$PWD/numpy/core/include/numpy"
INCS="$INCS -I$PWD/numpy/core/include -I%buildroot%_includedir/python%_python3_version/%oname"
INCS="$INCS -I%buildroot%_includedir"
DEFS="-DHAVE_FREXPF -DHAVE_FREXPL -DHAVE_FREXP -DHAVE_LDEXP -DHAVE_LDEXPL"
DEFS="$DEFS -DHAVE_EXPM1 -DHAVE_LOG1P -DHAVE_LDEXPF"
DEFS="$DEFS -UNPY_CPU_AMD64 -UNPY_CPU_X86"
DEFS="$DEFS -DNPY_ENABLE_SEPARATE_COMPILATION"
%add_optflags -fno-strict-aliasing $DEFS $INCS %optflags_shared

%python3_build_install

# private headers

install -d %buildroot%_includedir/python%_python3_version
mv %buildroot%python3_sitelibdir/%oname/core/include/%oname \
	%buildroot%_includedir/python%_python3_version/%oname

install -d %buildroot%python3_sitelibdir/%oname/core/include
ln -s %_includedir/python%_python3_version/%oname \
	%buildroot%python3_sitelibdir/%oname/core/include/
cp build/src.*/%oname/core/include/%oname/{*.h,*.c} \
	%buildroot%_includedir/python%_python3_version/%oname/
install -d %buildroot%python3_sitelibdir/%oname/core/lib/npy-pkg-config
cp -fR build/src.*/%oname/core/lib/npy-pkg-config/* \
	%buildroot%python3_sitelibdir/%oname/core/lib/npy-pkg-config/

# docs, tests and addons need build with installed NumPy
export PYTHONPATH=%buildroot%python3_sitelibdir

# docs
%if_with doc

%if_with latex
%make -C doc
%else
%make -C doc html
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
pushd doc
install -p -m644 conf.py %buildroot%python3_sitelibdir
#generate_pickles %buildroot%python_sitelibdir $PWD %oname
%make html
%make pickle
popd
rm -f %buildroot%python3_sitelibdir/conf.py
cp -fR doc/build/pickle %buildroot%python3_sitelibdir/%oname/

pushd doc/cdoc
%make
popd

install -d %buildroot%_docdir/%name/pdf/reference
install -d %buildroot%_docdir/%name/cdoc
cp -fR doc/build/html %buildroot%_docdir/%name/
cp -fR doc/cdoc/build/html %buildroot%_docdir/%name/cdoc/
%if_with latex
cp -u $(find doc -name '*.pdf' |egrep -v plot_directive) \
	%buildroot%_docdir/%name/pdf/
cp -fR doc/build/plot_directive/reference/generated/*.pdf \
	%buildroot%_docdir/%name/pdf/reference/
%endif

%endif

# tests

%if_with tests
cp %oname/fft/*.c %oname/fft/*.h \
	%buildroot%python3_sitelibdir/%oname/fft/
cp %oname/linalg/*.c \
	%buildroot%python3_sitelibdir/%oname/linalg/
cp -fR %oname/core/src \
	%buildroot%python3_sitelibdir/%oname/core/
cp -fR %oname/random/mtrand \
	%buildroot%python3_sitelibdir/%oname/random/

export PYTHONPATH=%buildroot%python3_sitelibdir

%if_with doc
#export PYTHONPATH=%buildroot%python3_sitelibdir
pushd doc
for i in newdtype_example; do
pushd $i
%python3_build_debug
%python3_install
popd
done
popd

%endif
%endif

%files
%doc LICENSE.txt
%doc README.md THANKS.txt
%_bindir/f2py*
%python3_sitelibdir/%oname
%exclude %python3_sitelibdir/%oname/conftest.py
%exclude %python3_sitelibdir/%oname/_pytesttester.py
%exclude %python3_sitelibdir/%oname/__pycache__/conftest.*
%exclude %python3_sitelibdir/%oname/__pycache__/_pytesttester.*
%exclude %python3_sitelibdir/%oname/f2py/f2py_testing.py
%exclude %python3_sitelibdir/%oname/f2py/__pycache__/f2py_testing.*
%exclude %python3_sitelibdir/%oname/lib/recfunctions.py
%exclude %python3_sitelibdir/%oname/lib/__pycache__/recfunctions.*
%exclude %python3_sitelibdir/%oname/ma/timer_comparison.py
%exclude %python3_sitelibdir/%oname/ma/__pycache__/timer_comparison.*
%exclude %python3_sitelibdir/%oname/testing
%exclude %python3_sitelibdir/%oname/tests
%exclude %python3_sitelibdir/%oname/*/test*
%exclude %python3_sitelibdir/%oname/*/*/test*
%exclude %python3_sitelibdir/%oname/f2py/src/fortranobject.h
%exclude %python3_sitelibdir/%oname/core/lib/npy-pkg-config
%exclude %python3_sitelibdir/%oname/doc
%exclude %python3_sitelibdir/%oname/core/include
%exclude %python3_sitelibdir/%oname/distutils/mingw
%exclude %python3_sitelibdir/%oname/f2py/src
%if_with tests
%exclude %python3_sitelibdir/%oname/random/mtrand/*.h
%exclude %python3_sitelibdir/%oname/random/mtrand/*.c
%exclude %python3_sitelibdir/%oname/random/mtrand/*.pxi
%exclude %python3_sitelibdir/%oname/random/mtrand/*.pyx
%exclude %python3_sitelibdir/%oname/core/src/multiarray/*.h
%exclude %python3_sitelibdir/%oname/core/src/multiarray/*.c*
%exclude %python3_sitelibdir/%oname/core/src/npymath
%exclude %python3_sitelibdir/%oname/core/src/private
%exclude %python3_sitelibdir/%oname/core/src/*.c*
%exclude %python3_sitelibdir/%oname/core/src/umath
%exclude %python3_sitelibdir/%oname/fft/*.c
%exclude %python3_sitelibdir/%oname/fft/*.h
%exclude %python3_sitelibdir/%oname/linalg/*.c
%endif #if_with tests
%exclude %python3_sitelibdir/%oname/core/lib/libnpymath.a
%exclude %python3_sitelibdir/%oname/random/lib/libnpyrandom.a
%python3_sitelibdir/%oname-%version-*.egg-info

%files testing
%python3_sitelibdir/%oname/testing
%python3_sitelibdir/%oname/conftest.py
%python3_sitelibdir/%oname/_pytesttester.py
%python3_sitelibdir/%oname/__pycache__/conftest.*
%python3_sitelibdir/%oname/__pycache__/_pytesttester.*

%files tests
%python3_sitelibdir/%oname/tests
%python3_sitelibdir/%oname/*/test*
%python3_sitelibdir/%oname/*/*/test*
%exclude %python3_sitelibdir/%oname/testing/tests
%python3_sitelibdir/%oname/f2py/tests/src/array_from_pyobj
%python3_sitelibdir/%oname/lib/recfunctions.py
%python3_sitelibdir/%oname/lib/__pycache__/recfunctions.*
%if_with tests
%python3_sitelibdir/%oname/f2py/f2py_testing.py
%python3_sitelibdir/%oname/f2py/__pycache__/f2py_testing.*
%python3_sitelibdir/%oname/ma/timer_comparison.py
%python3_sitelibdir/%oname/ma/__pycache__/timer_comparison.*
%python3_sitelibdir/f2py_ext*
%python3_sitelibdir/gen_ext*
%python3_sitelibdir/swig_ext*
%python3_sitelibdir/testnumpydistutils*
%endif

%files -n lib%oname-py3-devel
%_includedir/python%_python3_version/%oname
%if_with tests
%python3_sitelibdir/%oname/random/mtrand/*.h
%python3_sitelibdir/%oname/random/mtrand/*.c
%python3_sitelibdir/%oname/random/mtrand/*.pxi
%python3_sitelibdir/%oname/random/mtrand/*.pyx
%python3_sitelibdir/%oname/core/src/multiarray/*.h
%python3_sitelibdir/%oname/core/src/multiarray/*.c*
%python3_sitelibdir/%oname/fft/*.c
%python3_sitelibdir/%oname/fft/*.h
%python3_sitelibdir/%oname/core/src/npymath
%python3_sitelibdir/%oname/core/src/private
%python3_sitelibdir/%oname/core/src/*.c*
%python3_sitelibdir/%oname/core/src/umath
%python3_sitelibdir/%oname/linalg/*.c
%endif
%python3_sitelibdir/%oname/core/include
%python3_sitelibdir/%oname/distutils/mingw
%exclude %python3_sitelibdir/%oname/distutils/tests
%python3_sitelibdir/%oname/f2py/src
%python3_sitelibdir/%oname/core/lib/npy-pkg-config
%python3_sitelibdir/%oname/core/lib/libnpymath.a
%python3_sitelibdir/%oname/random/lib/libnpyrandom.a

%if_with doc
%files doc
%python3_sitelibdir/%oname/doc

%files doc-html
%dir %_docdir/%name
%_docdir/%name/html
%_docdir/%name/cdoc

%if_with latex
%files doc-pdf
%dir %_docdir/%name
%_docdir/%name/pdf
%endif

%files pickles
%dir %python_sitelibdir/%oname
%python3_sitelibdir/%oname/pickle
%endif

%changelog
* Fri Jan 15 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.19.5-alt1
- Updated to upstream version 1.19.5.

* Thu Aug 20 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.19.1-alt1
- Updated to upstream version 1.19.1
- Disabled build for python-2.
- Cleaned up spec.

* Wed Mar 11 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.15.4-alt5
- Moved include directories (Closes: #38013).

* Tue Feb 11 2020 Andrey Bychkov <mrdrew@altlinux.org> 1:1.15.4-alt4
- Fixed build requires.

* Fri Sep 13 2019 Vladimir Didenko <cow@altlinux.org> 1:1.15.4-alt3
- Remove dependency on scons (it is not required anymore)

* Tue Jun 11 2019 Stanislav Levin <slev@altlinux.org> 1:1.15.4-alt2
- Dropped dependency on testing/test packages in the main one.

* Tue Dec 25 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1:1.15.4-alt1
- Update to upstream version 1.15.4
- Remove runnig 2to3 on generators

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.13.3-alt2.2.qa1
- NMU: applied repocop patch

* Fri Jun 29 2018 Anton Midyukov <antohami@altlinux.org> 1:1.13.3-alt2.2
- Skip requires from python3-module numpy (Closes:35103) to:
  - python3(setuptools.command.develop)
  - python3(setuptools.command.egg_info)

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.13.3-alt2.1.1
- (NMU) Rebuilt with python-3.6.4.

* Tue Mar 06 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.13.3-alt2.1
- NMU: corrected BR: for new texlive

* Mon Jan 22 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.13.3-alt2
- added optional Provides: python-module-numpy-doc for autoimports

* Wed Nov 29 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.13.3-alt1
- Updated to upstream version 1.13.3.
- Removed git from build dependencies.
- Cleaned up spec.
- Disabled generation of docs.

* Mon Apr 17 2017 Anton Midyukov <antohami@altlinux.org> 1:1.12.1-alt1
- New version 1.12.1
- Remove __svn_version__.py
- Disable tests
- Disable convert python 2 to python3 script

* Thu Mar 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt15.git20150829.2.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Wed Mar 23 2016 Denis Medvedev <nbr@altlinux.org> 2.0.0-alt15.git20150829.2
- NMU: reorganized dependencies.

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.0.0-alt15.git20150829.1
- NMU: Use buildreq for BR.

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt15.git20150829
- New snapshot

* Fri May 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt14.git20150424
- Added dgetrf into lapack_lite

* Sat Apr 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt13.git20150424
- New snapshot

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt13.git20141102
- Fixed numpy.distutils.misc_util.get_num_build_jobs for cases when
  --jobs command line argument doesn't recognized by setup.py

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt12.git20141102
- New snapshot

* Tue May 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt12.git20140505
- New snapshot

* Mon May 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt12.git20131021
- Avoid requirement on python-devel for %name (ALT #29862)

* Wed Jan 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt11.git20131021
- Enabled docs

* Wed Jan 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt10.git20131021
- Removed dependency on devel subpackage (ALT #29723)

* Tue Jan 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt9.git20131021
- Disabled docs

* Tue Oct 22 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt8.git20131021
- New snapshot

* Fri Jun 14 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt8.git20130613
- New snapshot

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt8.git20121009
- Use 'find... -exec...' instead of 'for ... $(find...'

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 2.0.0-alt7.git20121009.1
- Rebuild with Python-3.3

* Sun Oct 14 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt7.git20121009
- Fixed upgrading of numpydoc
- Extracted tests for numpydoc into separate package

* Fri Oct 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt6.git20121009
- New snapshot

* Sun Aug 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt6.git20120502
- Built with OpenBLAS instead of GotoBLAS2

* Sun May 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt5.git20120502
- Fixed headers for libnumpy-py3-devel

* Fri May 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt4.git20120502
- New snapshot
- Added modules for Python 3
- Moved numpy.lib.polynomial into main package (ALT #27314)

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.0-alt3.git20111023.1
- Rebuild to remove redundant libpython2.7 dependency

* Sat Nov 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt3.git20111023
- Rebuilt with docs (except pdf) and tests

* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.0-alt2.git20111023.1
- Rebuild with Python-2.7

* Mon Oct 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2.git20111023
- New snapshot

* Mon Jul 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2.git20110715.1
- Built with docs and tests

* Sun Jul 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2.git20110715
- New snapshot (without docs and tests for bootstrap)

* Sat Apr 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2.git20110422
- New snapshot
- Changed type promotion tables from char to signed char (thanks to
  manowar@ and charris)

* Sat Apr 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2.git20110405.4
- Built with docs

* Fri Apr 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2.git20110405.3
- Built with OpenMP
- Bootstrap with GotoBLAS2 1.13-alt3 (without docs)

* Thu Apr 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2.git20110405.2
- Built with docs
- Don't set fake ATLAS_VERSION (it's problem somewhere)

* Thu Apr 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2.git20110405.1
- Set fake ATLAS_VERSION for client software

* Wed Apr 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2.git20110405
- New snapshot (from github)
- Built with GotoBLAS2 instead of ATLAS
- Bootstrap (without docs now)

* Wed Apr 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.svn20100607.11
- linalg: avoid raising LinAlgError exception

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.svn20100607.10
- Rebuilt with ATLAS 3.9.35

* Mon Mar 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.svn20100607.9
- Fixed linking with ATLAS

* Mon Mar 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.svn20100607.8
- Rebuilt with lapack 3.3.0-alt4

* Fri Mar 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.svn20100607.7
- Restored %_bindir/f2py

* Tue Mar 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.svn20100607.6
- Added -g into compiler flags
- Moved all headers into libnumpy-devel

* Fri Feb 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.svn20100607.5
- Rebuilt for debuginfo

* Fri Dec 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.svn20100607.4
- Fixed inner headers' directory (ALT #24817)

* Tue Oct 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.svn20100607.3
- Rebuilt for soname set-versions

* Wed Oct 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.svn20100607.2
- Fixed linking

* Thu Jul 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.svn20100607.1
- Avoid requirement on python-module-Numeric for doc

* Wed Jun 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.svn20100607
- Version 2.0.0

* Thu Apr 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.svn20100120.3
- Added addons packages

* Mon Feb 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.svn20100120.2
- Fixed building of PDFs
- Rebuilt with updated macro %%prepare_sphinx

* Mon Feb 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.svn20100120.1
- Added modules: numpyx, floatint, (numpydoc & pickles - in separate
  packages) files
- Built additional documentation
- Made building of docs by one command `make'

* Sun Jan 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.svn20100120
- New snapshot
- Added param `-std=f95' for NAG Fortran compiler
- Added docs packages
- Extracted tests and addons into separate package
- Generate additional submodules
- Some another minor fixes

* Mon Jan 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.svn20091231.2
- Added link to libnpymath.so into %_libdir

* Mon Jan 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.svn20091231.1
- Added __svn_version__.py and site.cfg

* Thu Dec 31 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.svn20091231
- Version 1.5.0

* Sat Dec 19 2009 Ivan Fedorov <ns@altlinux.org> 1.4.0-alt4.svn20090913
- Remove dependency to Numeric
- Update homepage URL

* Mon Dec 14 2009 Dmitry V. Levin <ldv@altlinux.org> 1.4.0-alt3.svn20090913
- Updated build dependencies.

* Fri Nov 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt2.svn20090913.1
- Rebuilt with python 2.6

* Sun Sep 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt2.svn20090913
- New snapshot

* Tue Sep 08 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt2.svn20090902.1
- Added preinstall deletion of old include directory (ALT #21473)

* Wed Sep 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt2.svn20090902
- Rebuilt with shared libraries of SuiteSparse

* Thu Aug 27 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt2.svn20090827
- New snapshot

* Tue Aug 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.svn20090822.2
- Enabled conflict with old syfi

* Tue Aug 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.svn20090822.1
- Bootstrap for syfi

* Sat Aug 22 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.svn20090822
- New snapshot
- Added pkg-config file

* Fri Jul 31 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.svn20090731.1
- Version 1.4.0
- Made %_bindir/f2py as symbolic link

* Thu Apr 23 2009 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- new version 1.3.0 (with rpmrb script)

* Sun Dec 28 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt2
- remove unneeded buildreqs
- disable scons requires (fix bug #18379)

* Mon Dec 01 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- new version 1.2.1 (with rpmrb script)
- update buildreqs

* Mon Jul 07 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt2
- fix unmets

* Sat Jul 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- new version 1.1.0 (with rpmrb script)
- add rpm-build-compat requires due build_python macros

* Sat Apr 07 2007 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt1
- new version 1.0.2 (with rpmrb script)

* Sat Nov 11 2006 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt0.1
- initial build for ALT Linux Sisyphus

