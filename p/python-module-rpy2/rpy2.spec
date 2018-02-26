%define oname rpy2
Name: python-module-%oname
Version: 2.2.5
Release: alt1.1
Summary: A simple and efficient access to R from Python, version 2
License: MPL/GPL/LGPL
Group: Development/Python
Url: http://rpy.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %oname-%version.tar.gz

Requires: R-base

BuildRequires(pre): rpm-build-python
BuildPreReq: python-devel R-devel liblapack-devel libreadline-devel
#BuildPreReq: python-module-sphinx-devel python-module-Pygments
#BuildPreReq: graphviz texlive-latex-recommended
%setup_python_module %oname

%description
RPy is a very simple, yet robust, Python interface to the R Programming
Language. It can manage all kinds of R objects and can execute arbitrary
R functions (including the graphic functions). All errors from the R
language are converted to Python exceptions. Any module installed for
the R system can be used from within Python.

rpy2 is a redesign and rewrite of rpy. It is providing a low-level
interface to R, a proposed high-level interface, including wrappers to
graphical libraries, as well as R-like structures and functions.

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

%prep
%setup

sed -i 's|@PYVER@|%_python_version|g' doc/Makefile
#prepare_sphinx .

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%install
%python_install

#export PYTHONPATH=%buildroot%python_sitelibdir
#pushd doc
#make latex
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

%files
%doc AUTHORS GPL_LICENSE LGPL_LICENSE MPL_LICENSE NEWS README
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests*
%exclude %python_sitelibdir/*/*/tests
#exclude %python_sitelibdir/%oname/pickle
%_sysconfdir/profile.d/*

%files tests
%python_sitelibdir/*/tests*
%python_sitelibdir/*/*/tests

#files pickles
#dir %python_sitelibdir/%oname
#python_sitelibdir/%oname/pickle

#files doc
#_docdir/%oname

%changelog
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

