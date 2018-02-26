%define oname casuarius

%def_with python3

Name: python-module-%oname
Version: 1.0
Release: alt1.b1.git20120424
Summary: Cython bindings for the Cassowary Constraint Solving Toolkit
License: LGPLv2.1+
Group: Development/Python
Url: https://github.com/enthought/casuarius
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/enthought/casuarius.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-Cython gcc-c++
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-Cython
%endif

%description
A Cython wrapper for the Cassowary incremental constraint solver.

The solver source code is derived from the 0.6 release. It has been
modified by Svilen Dobrev to remove memory leaks. His work can be found
separately as SWIG
bindings:

    http://pypi.python.org/pypi/cassowarypy

%if_with python3
%package -n python3-module-%oname
Summary: Cython bindings for the Cassowary Constraint Solving Toolkit (Python 3)
Group: Development/Python3

%description -n python3-module-%oname 
A Cython wrapper for the Cassowary incremental constraint solver.

The solver source code is derived from the 0.6 release. It has been
modified by Svilen Dobrev to remove memory leaks. His work can be found
separately as SWIG
bindings:

    http://pypi.python.org/pypi/cassowarypy
%endif

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

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

%files
%doc COPYING.LGPL LICENSE README.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc COPYING.LGPL LICENSE README.rst
%python3_sitelibdir/*
%endif

%changelog
* Thu May 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.b1.git20120424
- Version 1.0b1
- Added module for Python 3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.1-alt1.git20111123.1
- Rebuild to remove redundant libpython2.7 dependency

* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20111123
- Initial build for Sisyphus

