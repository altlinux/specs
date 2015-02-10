%define oname rpy2

%def_with python3

Name: python-module-%oname
Version: 2.5.6
Release: alt1
Summary: A simple and efficient access to R from Python, version 2
License: MPL/GPL/LGPL
Group: Development/Python
Url: http://rpy.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %oname-%version.tar.gz

Requires: R-base

BuildRequires(pre): rpm-build-python
BuildPreReq: libpcre-devel liblzma-devel bzlib-devel zlib-devel
BuildPreReq: libicu-devel
BuildPreReq: python-devel R-devel liblapack-devel libreadline-devel
BuildPreReq: python-module-setuptools-tests python-module-singledispatch
BuildPreReq: python-module-six
#BuildPreReq: python-module-sphinx-devel python-module-Pygments
#BuildPreReq: graphviz
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-singledispatch
BuildPreReq: python3-module-six
%endif
%setup_python_module %oname

#add_python_req_skip pandas
Requires: %oname-common = %EVR
%py_requires singledispatch

%description
RPy is a very simple, yet robust, Python interface to the R Programming
Language. It can manage all kinds of R objects and can execute arbitrary
R functions (including the graphic functions). All errors from the R
language are converted to Python exceptions. Any module installed for
the R system can be used from within Python.

rpy2 is a redesign and rewrite of rpy. It is providing a low-level
interface to R, a proposed high-level interface, including wrappers to
graphical libraries, as well as R-like structures and functions.

%package -n python3-module-%oname
Summary: A simple and efficient access to R from Python, version 2
Group: Development/Python3
Requires: %oname-common = %EVR
%py3_requires singledispatch

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

%if_with python3
cp -fR . ../python3
%endif

sed -i 's|@PYVER@|%_python_version|g' doc/Makefile
#prepare_sphinx doc

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

#export PYTHONPATH=%buildroot%python_sitelibdir
#pushd doc
#make html
#popd

#install -d %buildroot%_docdir/%oname/demos
#cp -fR doc/build/html %buildroot%_docdir/%oname/
#cp -fR doc/build/latex/*.pdf %buildroot%_docdir/%oname/
#install -p -m644 demos/*.py %buildroot%_docdir/%oname/demos

#install -d %buildroot%python_sitelibdir/rpy2
#cp -fR doc/build/pickle %buildroot%python_sitelibdir/rpy2/

install -d %buildroot%_sysconfdir/profile.d
cat <<EOF > %buildroot%_sysconfdir/profile.d/%oname.sh
export R_HOME=%_libdir/R
EOF

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc AUTHORS NEWS *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests*
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/*/*/tests
#exclude %python_sitelibdir/%oname/pickle

%files -n %oname-common
%_sysconfdir/profile.d/*

%files tests
%python_sitelibdir/*/tests*
%python_sitelibdir/*/*/tests
%python_sitelibdir/*/*/*/tests

#files pickles
#dir %python_sitelibdir/%oname
#python_sitelibdir/%oname/pickle

#files doc
#_docdir/%oname

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS NEWS *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests*
%exclude %python3_sitelibdir/*/*/tests*
%exclude %python3_sitelibdir/*/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests*
%python3_sitelibdir/*/*/tests*
%python3_sitelibdir/*/*/*/tests
%endif

%changelog
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

