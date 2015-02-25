%define oname pyqtgraph

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.9.10
Release: alt1.git20141224
Summary: Scientific Graphics and GUI Library for Python
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pyqtgraph/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pyqtgraph/pyqtgraph.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-numpy python-module-PySide
BuildPreReq: python-module-scipy python-module-matplotlib
BuildPreReq: python-module-nose python-module-matplotlib-qt4
BuildPreReq: python-module-OpenGL
BuildPreReq: python-modules-multiprocessing python-modules-xml
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-numpy python3-module-PySide
BuildPreReq: python3-module-scipy python3-module-matplotlib
BuildPreReq: python3-module-nose python3-module-matplotlib-qt4
BuildPreReq: python3-module-OpenGL
%endif

%py_provides %oname
%py_requires numpy PySide scipy matplotlib multiprocessing xml OpenGL.GL
%py_requires matplotlib.backends.backend_qt4agg

%description
PyQtGraph is a pure-python graphics and GUI library built on
PyQt4/PySide and numpy.

It is intended for use in mathematics / scientific / engineering
applications. Despite being written entirely in python, the library is
very fast due to its heavy leverage of numpy for number crunching, Qt's
GraphicsView framework for 2D display, and OpenGL for 3D display.

%package examples
Summary: Examples for %oname
Group: Development/Python
Requires: %name = %EVR

%description examples
PyQtGraph is a pure-python graphics and GUI library built on
PyQt4/PySide and numpy.

It is intended for use in mathematics / scientific / engineering
applications. Despite being written entirely in python, the library is
very fast due to its heavy leverage of numpy for number crunching, Qt's
GraphicsView framework for 2D display, and OpenGL for 3D display.

This package contains examples for %oname.

%package -n python3-module-%oname
Summary: Scientific Graphics and GUI Library for Python
Group: Development/Python3
%py3_provides %oname
%py3_requires numpy PySide scipy matplotlib multiprocessing xml OpenGL.GL
%py3_requires matplotlib.backends.backend_qt4agg
%add_python3_req_skip UserDict

%description -n python3-module-%oname
PyQtGraph is a pure-python graphics and GUI library built on
PyQt4/PySide and numpy.

It is intended for use in mathematics / scientific / engineering
applications. Despite being written entirely in python, the library is
very fast due to its heavy leverage of numpy for number crunching, Qt's
GraphicsView framework for 2D display, and OpenGL for 3D display.

%package -n python3-module-%oname-examples
Summary: Examples for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-examples
PyQtGraph is a pure-python graphics and GUI library built on
PyQt4/PySide and numpy.

It is intended for use in mathematics / scientific / engineering
applications. Despite being written entirely in python, the library is
very fast due to its heavy leverage of numpy for number crunching, Qt's
GraphicsView framework for 2D display, and OpenGL for 3D display.

This package contains examples for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
PyQtGraph is a pure-python graphics and GUI library built on
PyQt4/PySide and numpy.

It is intended for use in mathematics / scientific / engineering
applications. Despite being written entirely in python, the library is
very fast due to its heavy leverage of numpy for number crunching, Qt's
GraphicsView framework for 2D display, and OpenGL for 3D display.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
PyQtGraph is a pure-python graphics and GUI library built on
PyQt4/PySide and numpy.

It is intended for use in mathematics / scientific / engineering
applications. Despite being written entirely in python, the library is
very fast due to its heavy leverage of numpy for number crunching, Qt's
GraphicsView framework for 2D display, and OpenGL for 3D display.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx doc
ln -s ../objects.inv doc/source/

%build
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

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C doc pickle
%make -C doc html

cp -fR doc/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc CHANGELOG *.txt *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/examples

%files examples
%python_sitelibdir/*/examples

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/build/html examples

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG *.txt *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/examples

%files -n python3-module-%oname-examples
%python3_sitelibdir/*/examples
%endif

%changelog
* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.10-alt1.git20141224
- Initial build for Sisyphus

