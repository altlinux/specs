%define oname cvxopt

%def_with python3

Name: python-module-%oname
Version: 1.1.5
Release: alt1
Summary: Python Software for Convex Optimization
License: GPL v3 or higher/GPL v2 of higher
Group: Development/Python
Url: http://abel.ee.ucla.edu/cvxopt/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
Source: %oname-%version.tar.gz
%setup_python_module %oname
# disable requirements on commertial software
%add_python_req_skip mosekarr pymosek mosek

BuildRequires(pre): rpm-build-python
BuildPreReq: python-devel liblapack-devel libgsl-devel
BuildPreReq: libfftw3-devel libglpk4-devel libdsdp-devel
BuildPreReq: python-module-sphinx-devel texlive-latex-recommended dvipng
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
%endif

Conflicts: %name-pickles < %version-%release

%description
CVXOPT is a free software package for convex optimization based on the
Python programming language. It can be used with the interactive Python
interpreter, on the command line by executing Python scripts, or
integrated in other software via Python extension modules. Its main
purpose is to make the development of software for convex optimization
applications straightforward by building on Python's extensive standard
library and on the strengths of Python as a high-level programming
language.

%if_with python3
%package -n python3-module-%oname
Summary: Python 3 Software for Convex Optimization
Group: Development/Python3
%add_python3_req_skip mosekarr pymosek mosek

%description -n python3-module-%oname
CVXOPT is a free software package for convex optimization based on the
Python programming language. It can be used with the interactive Python
interpreter, on the command line by executing Python scripts, or
integrated in other software via Python extension modules. Its main
purpose is to make the development of software for convex optimization
applications straightforward by building on Python's extensive standard
library and on the strengths of Python as a high-level programming
language.
%endif

%package doc
Summary: Documentation for CVXOPT
Group: Documentation
BuildArch: noarch

%description doc
CVXOPT is a free software package for convex optimization based on the
Python programming language. It can be used with the interactive Python
interpreter, on the command line by executing Python scripts, or
integrated in other software via Python extension modules. Its main
purpose is to make the development of software for convex optimization
applications straightforward by building on Python's extensive standard
library and on the strengths of Python as a high-level programming
language.

This package contains documentation for CVXOPT.

%package examples
Summary: Examples for CVXOPT
Group: Documentation
BuildArch: noarch

%description examples
CVXOPT is a free software package for convex optimization based on the
Python programming language. It can be used with the interactive Python
interpreter, on the command line by executing Python scripts, or
integrated in other software via Python extension modules. Its main
purpose is to make the development of software for convex optimization
applications straightforward by building on Python's extensive standard
library and on the strengths of Python as a high-level programming
language.

This package contains examples for CVXOPT.

%package pickles
Summary: Pickles for CVXOPT
Group: Development/Python

%description pickles
CVXOPT is a free software package for convex optimization based on the
Python programming language. It can be used with the interactive Python
interpreter, on the command line by executing Python scripts, or
integrated in other software via Python extension modules. Its main
purpose is to make the development of software for convex optimization
applications straightforward by building on Python's extensive standard
library and on the strengths of Python as a high-level programming
language.

This package contains pickles for CVXOPT.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%prepare_sphinx doc/source

%build
pushd src
%ifarch x86_64
sed -i 's|@64@|64|g' setup.py
%else
sed -i 's|@64@||g' setup.py
%endif
%add_optflags -fno-strict-aliasing
%python_build_debug
popd

%if_with python3
pushd ../python3/src
%ifarch x86_64
sed -i 's|@64@|64|g' setup.py
%else
sed -i 's|@64@||g' setup.py
%endif
%add_optflags -fno-strict-aliasing
%python3_build_debug
popd
%endif

%make -C doc html

%install
%if_with python3
pushd ../python3/src
%python3_install
popd
%endif

pushd src
%python_install
popd

install -d %buildroot%_docdir/%name
cp -fR doc/build/html examples %buildroot%_docdir/%name/

install -d %buildroot%python_sitelibdir/%oname
cp -fR doc/build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc LICENSE
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/pickle

%files doc
%doc %dir %_docdir/%name
%doc %_docdir/%name/html

%files examples
%doc %dir %_docdir/%name
%doc %_docdir/%name/examples

%files pickles
%dir %python_sitelibdir/%oname
%python_sitelibdir/%oname/pickle

%if_with python3
%files -n python3-module-%oname
%doc LICENSE
%python3_sitelibdir/*
%endif

%changelog
* Wed May 23 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.5-alt1
- Version 1.1.5
- Added module for Python 3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.4-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.4-alt1
- Version 1.1.4

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.3-alt5.1
- Rebuild with Python-2.7

* Sat Apr 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt5
- Built with GotoBLAS2 instead of ATLAS

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt4
- Rebuilt with python-module-sphinx-devel

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt3
- Rebuilt for debuginfo

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt2
- Fixed underlinking

* Tue Sep 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1
- Version 1.1.3
- Enabled pickles package

* Fri Sep 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt3
- Added explicit conflict with old pickles package (ALT #24051)

* Mon Aug 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt2
- Rebuilt with Sphinx 1.0.1

* Tue Jul 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1
- Version 1.1.2
- Added pickles

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt3
- Rebuilt with python 2.6

* Fri Sep 04 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt2
- Rebuilt with shared library of DSDP

* Mon Aug 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1
- Initial build for Sisyphus
