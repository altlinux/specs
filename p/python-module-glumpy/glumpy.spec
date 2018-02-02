%define oname glumpy

%def_without python3
%def_disable check

Name: python-module-%oname
Version: 1.0.3
Release: alt1.git20150322.1
Summary: Fast, scalable & beautiful scientific visualisation
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/glumpy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/glumpy/glumpy.git
Source: %name-%version.tar

BuildPreReq: libfreetype-devel libtriangle-devel libglfw3-devel
BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-Cython libnumpy-devel
BuildPreReq: python-module-triangle python-module-OpenGL
BuildPreReq: python-module-Pillow python-module-nose
BuildPreReq: python-module-sphinx-devel python-module-sphinx_rtd_theme
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-Cython libnumpy-py3-devel
BuildPreReq: python3-module-triangle python3-module-OpenGL
BuildPreReq: python3-module-Pillow python3-module-nose
%endif

%py_provides %oname
%py_requires numpy triangle OpenGL PIL

%description
Glumpy is a python library for scientific visualization that is both
fast, scalable and beautiful. Glumpy offers an intuitive interface
between numpy and modern OpenGL.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Glumpy is a python library for scientific visualization that is both
fast, scalable and beautiful. Glumpy offers an intuitive interface
between numpy and modern OpenGL.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Fast, scalable & beautiful scientific visualisation
Group: Development/Python3
%py3_provides %oname
%py3_requires numpy triangle OpenGL PIL

%description -n python3-module-%oname
Glumpy is a python library for scientific visualization that is both
fast, scalable and beautiful. Glumpy offers an intuitive interface
between numpy and modern OpenGL.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Glumpy is a python library for scientific visualization that is both
fast, scalable and beautiful. Glumpy offers an intuitive interface
between numpy and modern OpenGL.

This package contains tests for %oname.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Glumpy is a python library for scientific visualization that is both
fast, scalable and beautiful. Glumpy offers an intuitive interface
between numpy and modern OpenGL.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Glumpy is a python library for scientific visualization that is both
fast, scalable and beautiful. Glumpy offers an intuitive interface
between numpy and modern OpenGL.

This package contains documentation for %oname.

%prep
%setup

rm -f %oname/ext/sdf/_sdf.c

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

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
sed -i 's|\t|        |g' \
	%buildroot%python3_sitelibdir/%oname/app/window/backends/backend_pyglet.py
%endif

%make -C doc pickle
%make -C doc html

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
python setup.py build_ext -i
export PYTHONPATH=$PWD
nosetests -v
%if_with python3
pushd ../python3
python3 setup.py test
python3 setup.py build_ext -i
export PYTHONPATH=$PWD
nosetests3 -v
popd
%endif

%files
%doc *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/*/*/test*

%files tests
%python_sitelibdir/*/*/*/test*

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/_build/html examples

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/*/test*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.3-alt1.git20150322.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Mar 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.git20150322
- Initial build for Sisyphus

