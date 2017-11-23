%define oname rpy2

%def_without python2
%def_with python3
%def_without docs

Name: python-module-%oname
Version: 2.9.1
Release: alt1
Summary: A simple and efficient access to R from Python, version 2
License: GPLv2
Group: Development/Python
Url: http://rpy.sourceforge.net/

Source: %oname-%version.tar
Patch1: %oname-%version-alt-ldpath.patch

BuildRequires: libpcre-devel liblzma-devel bzlib-devel zlib-devel
BuildRequires: libicu-devel
BuildRequires: R-devel libreadline-devel

%if_with python2
BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-setuptools-tests python-module-singledispatch
BuildRequires: python-modules-sqlite3
BuildRequires: python-module-pytest
BuildRequires: python-module-numpy
%if_with docs
BuildRequires(pre): python-module-sphinx-devel
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-sphinx-pickles
%endif
%endif

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests python3-module-singledispatch
BuildRequires: python3-modules-sqlite3
BuildRequires: python3-module-numpy
%if_with docs
BuildRequires(pre): python3-module-sphinx-devel
BuildRequires: python3-module-alabaster python3-module-docutils python3-module-html5lib
%endif
%endif

%setup_python_module %oname

#add_python_req_skip pandas
Requires: R-base
Requires: %oname-common = %EVR
%py_requires singledispatch sqlite3

%description
RPy is a very simple, yet robust, Python interface to the R Programming
Language. It can manage all kinds of R objects and can execute arbitrary
R functions (including the graphic functions). All errors from the R
language are converted to Python exceptions. Any module installed for
the R system can be used from within Python.

rpy2 is a redesign and rewrite of rpy. It is providing a low-level
interface to R, a proposed high-level interface, including wrappers to
graphical libraries, as well as R-like structures and functions.

%if_with python3
%package -n python3-module-%oname
Summary: A simple and efficient access to R from Python, version 2
Group: Development/Python3
Requires: %oname-common = %EVR
%py3_requires singledispatch sqlite3

%description -n python3-module-%oname
RPy is a very simple, yet robust, Python interface to the R Programming
Language. It can manage all kinds of R objects and can execute arbitrary
R functions (including the graphic functions). All errors from the R
language are converted to Python exceptions. Any module installed for
the R system can be used from within Python.

rpy2 is a redesign and rewrite of rpy. It is providing a low-level
interface to R, a proposed high-level interface, including wrappers to
graphical libraries, as well as R-like structures and functions.

%package -n python3-module-%oname-tests
Summary: Tests for RPy, version 2
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%add_python3_req_skip testRevents

%description -n python3-module-%oname-tests
RPy is a very simple, yet robust, Python interface to the R Programming
Language. It can manage all kinds of R objects and can execute arbitrary
R functions (including the graphic functions). All errors from the R
language are converted to Python exceptions. Any module installed for
the R system can be used from within Python.

rpy2 is a redesign and rewrite of rpy. It is providing a low-level
interface to R, a proposed high-level interface, including wrappers to
graphical libraries, as well as R-like structures and functions.

This package contains tests for RPy, version 2.

%if_with docs
%package -n python3-module-%oname-pickles
Summary: Pickles for RPy, version 2
Group: Development/Python3

%description -n python3-module-%oname-pickles
RPy is a very simple, yet robust, Python interface to the R Programming
Language. It can manage all kinds of R objects and can execute arbitrary
R functions (including the graphic functions). All errors from the R
language are converted to Python exceptions. Any module installed for
the R system can be used from within Python.

rpy2 is a redesign and rewrite of rpy. It is providing a low-level
interface to R, a proposed high-level interface, including wrappers to
graphical libraries, as well as R-like structures and functions.

This package contains pickles for RPy, version 2.

%package -n python3-module-%oname-doc
Summary: Documentation and demos for RPy, version 2
Group: Development/Documentation
BuildArch: noarch

%description -n python3-module-%oname-doc
RPy is a very simple, yet robust, Python interface to the R Programming
Language. It can manage all kinds of R objects and can execute arbitrary
R functions (including the graphic functions). All errors from the R
language are converted to Python exceptions. Any module installed for
the R system can be used from within Python.

rpy2 is a redesign and rewrite of rpy. It is providing a low-level
interface to R, a proposed high-level interface, including wrappers to
graphical libraries, as well as R-like structures and functions.

This package contains development documentation and demos for RPy,
version 2.
%endif
%endif

%if_with python2
%package tests
Summary: Tests for RPy, version 2
Group: Development/Python
Requires: %name = %version-%release
%add_python_req_skip testRevents

%description tests
RPy is a very simple, yet robust, Python interface to the R Programming
Language. It can manage all kinds of R objects and can execute arbitrary
R functions (including the graphic functions). All errors from the R
language are converted to Python exceptions. Any module installed for
the R system can be used from within Python.

rpy2 is a redesign and rewrite of rpy. It is providing a low-level
interface to R, a proposed high-level interface, including wrappers to
graphical libraries, as well as R-like structures and functions.

This package contains tests for RPy, version 2.

%if_with docs
%package pickles
Summary: Pickles for RPy, version 2
Group: Development/Python

%description pickles
RPy is a very simple, yet robust, Python interface to the R Programming
Language. It can manage all kinds of R objects and can execute arbitrary
R functions (including the graphic functions). All errors from the R
language are converted to Python exceptions. Any module installed for
the R system can be used from within Python.

rpy2 is a redesign and rewrite of rpy. It is providing a low-level
interface to R, a proposed high-level interface, including wrappers to
graphical libraries, as well as R-like structures and functions.

This package contains pickles for RPy, version 2.

%package doc
Summary: Documentation and demos for RPy, version 2
Group: Development/Documentation
BuildArch: noarch

%description doc
RPy is a very simple, yet robust, Python interface to the R Programming
Language. It can manage all kinds of R objects and can execute arbitrary
R functions (including the graphic functions). All errors from the R
language are converted to Python exceptions. Any module installed for
the R system can be used from within Python.

rpy2 is a redesign and rewrite of rpy. It is providing a low-level
interface to R, a proposed high-level interface, including wrappers to
graphical libraries, as well as R-like structures and functions.

This package contains development documentation and demos for RPy,
version 2.
%endif
%endif

%package -n %oname-common
Summary: Common files for Python 2 and Python 3 modules of RPy, version 2
Group: Development/Other
Conflicts: %name < %EVR

%description -n %oname-common
RPy is a very simple, yet robust, Python interface to the R Programming
Language. It can manage all kinds of R objects and can execute arbitrary
R functions (including the graphic functions). All errors from the R
language are converted to Python exceptions. Any module installed for
the R system can be used from within Python.

rpy2 is a redesign and rewrite of rpy. It is providing a low-level
interface to R, a proposed high-level interface, including wrappers to
graphical libraries, as well as R-like structures and functions.

This package contains common files for Python 2 and Python 3 modules of
RPy, version 2.

%prep
%setup
%patch1 -p2

%if_with python3
cp -fR . ../python3
pushd ../python3
%if_with docs
sed -i 's|@PYVER@|%_python3_version|g' doc/Makefile
%prepare_sphinx3 doc
%endif
popd
%endif

%if_with python2
%if_with docs
sed -i 's|@PYVER@|%_python_version|g' doc/Makefile
%prepare_sphinx doc
%endif
%endif

%build
%add_optflags -fno-strict-aliasing
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install

%if_with docs
export PYTHONPATH=%buildroot%python3_sitelibdir
py3_sphinx-apidoc -o doc -F rpy
%make -C doc pickle
%make -C doc html

install -d %buildroot%python3_sitelibdir/rpy2
cp -fR doc/_build/pickle %buildroot%python3_sitelibdir/rpy2/
popd
%endif
%endif

%if_with python2
%if_with docs
export PYTHONPATH=%buildroot%python_sitelibdir
sphinx-apidoc -o doc -F rpy
%make -C doc pickle
%make -C doc html

install -d %buildroot%python_sitelibdir/rpy2
cp -fR doc/_build/pickle %buildroot%python_sitelibdir/rpy2/
%endif
%endif

install -d %buildroot%_sysconfdir/profile.d
cat <<EOF > %buildroot%_sysconfdir/profile.d/%oname.sh
export R_HOME=%_libdir/R
EOF

%check
%if_with python2
# remove these tests since R packages dplyr and ggplot2 are missing
rm -f build/lib.linux*/rpy2/robjects/lib/test_dplyr.py
rm -f build/lib.linux*/rpy2/robjects/lib/tests/test_dplyr.py
rm -f build/lib.linux*/rpy2/robjects/lib/tests/test_ggplot2.py

export PYTHONPATH=$(readlink -e build/lib.linux*)
python -m rpy2.tests -v
python -m unittest -v rpy2.robjects.tests.testVector
python -m unittest discover -v rpy2.robjects
%endif

%if_with python3
pushd ../python3
# remove these tests since R packages dplyr and ggplot2 are missing
rm -f build/lib.linux*/rpy2/robjects/lib/test_dplyr.py
rm -f build/lib.linux*/rpy2/robjects/lib/tests/test_dplyr.py
rm -f build/lib.linux*/rpy2/robjects/lib/tests/test_ggplot2.py

export PYTHONPATH=$(readlink -e build/lib.linux*)
python3 -m rpy2.tests -v
python3 -m unittest -v rpy2.robjects.tests.testVector
python3 -m unittest discover -v rpy2.robjects
popd
%endif

%files -n %oname-common
%_sysconfdir/profile.d/*

%if_with python2
%files
%doc AUTHORS NEWS *.rst gpl*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests*
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/*/*/tests
%if_with docs
%exclude %python_sitelibdir/%oname/pickle
%endif

%files tests
%python_sitelibdir/*/tests*
%python_sitelibdir/*/*/tests
%python_sitelibdir/*/*/*/tests

%if_with docs
%files pickles
%dir %python_sitelibdir/%oname
%python_sitelibdir/%oname/pickle

%files doc
%doc doc/_build/html/*
%endif
%endif

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS NEWS *.rst gpl*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests*
%exclude %python3_sitelibdir/*/*/tests*
%exclude %python3_sitelibdir/*/*/*/tests
%if_with docs
%exclude %python3_sitelibdir/%oname/pickle
%endif

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests*
%python3_sitelibdir/*/*/tests*
%python3_sitelibdir/*/*/*/tests

%if_with docs
%files -n python3-module-%oname-pickles
%dir %python3_sitelibdir/%oname
%python3_sitelibdir/%oname/pickle

%files -n python3-module-%oname-doc
%doc ../python3/doc/_build/html/*
%endif
%endif

%changelog
* Thu Nov 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.9.1-alt1
- Updated to upstream version 2.9.1.
- Disabled python-2 build.
- Disabled docs generation.

* Mon Mar 28 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.7.8-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Fri Mar 25 2016 Denis Medvedev <nbr@altlinux.org> 2.7.8-alt1
- New version

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.6.2-alt1.1
- NMU: Use buildreq for BR.

* Thu Aug 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.2-alt1
- Version 2.6.2

* Tue Feb 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.6-alt1
- Version 2.5.6

* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.4-alt1
- Version 2.5.4

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.2-alt1
- Version 2.5.2

* Thu Nov 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1
- Version 2.5.1

* Tue Nov 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.0-alt1
- Version 2.5.0

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.2-alt1
- Version 2.4.2
- Added module for Python 3

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.8-alt1
- Version 2.3.8

* Thu Sep 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.7-alt1
- Version 2.3.7

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.4-alt1
- Version 2.3.4

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.5-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Fri Jan 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.5-alt1
- Version 2.2.5

* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.4-alt1
- Version 2.2.4

* Tue Dec 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.1-alt1
- Version 2.2.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1.9-alt1.1
- Rebuild with Python-2.7

* Thu May 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.9-alt1
- Version 2.1.9

* Thu Apr 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt5
- Built with GotoBLAS2 instead of ATLAS

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt4
- Rebuilt with python-module-sphinx-devel

* Sat Mar 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt3
- Rebuilt for debuginfo

* Mon Aug 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt2
- Fixed build of docs

* Fri Jun 11 2010 Alexey Tourbin <at@altlinux.ru> 2.1.0-alt1.1
- Rebuilt with libR-2.11.so

* Mon Mar 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1
- Version 2.1.0
- Extracted tests into separate package
- Added:
  + documentation in PDF
  + pickles package

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.6-alt1.svn20090914.1
- Rebuilt with python 2.6

* Mon Sep 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.6-alt1.svn20090914
- Initial build for Sisyphus

