%define oname freetype

%def_with python3

Name: python-module-%oname
Version: 1.0.1
Release: alt1.git20150409
Summary: Freetype python bindings
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/freetype-py/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/rougier/freetype-py.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: lib%oname xvfb-run
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-numpy python-module-matplotlib
BuildPreReq: python-module-OpenGL python-module-pygobject3
BuildPreReq: python-module-Pillow python-module-pycairo
BuildPreReq: python-module-sphinx-devel python-module-sphinx_rtd_theme
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-numpy python3-module-matplotlib
BuildPreReq: python3-module-OpenGL python3-module-pygobject3
BuildPreReq: python3-module-Pillow python3-module-pycairo
%endif

%py_provides %oname
Requires: lib%oname
%py_requires ctypes

%description
Freetype python provides bindings for the FreeType library. Only the
high-level API is bound.

%if_with python3
%package -n python3-module-%oname
Summary: Freetype python bindings
Group: Development/Python3
%py3_provides %oname
Requires: lib%oname
%py3_requires ctypes

%description -n python3-module-%oname
Freetype python provides bindings for the FreeType library. Only the
high-level API is bound.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Freetype python provides bindings for the FreeType library. Only the
high-level API is bound.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Freetype python provides bindings for the FreeType library. Only the
high-level API is bound.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3/examples -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%endif

%make -C doc pickle
%make -C doc html

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
export PYTHONPATH=$PWD
xvfb-run py.test -vv $(find %oname/ -name '*.py')
xvfb-run py.test -vv $(find examples/ -name '*.py')
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=$PWD
xvfb-run py.test-%_python3_version -vv $(find %oname/ -name '*.py')
#xvfb-run py.test-%_python3_version -vv $(find examples/ -name '*.py')
popd
%endif

%files
%doc *.rst *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc examples doc/_build/html

%if_with python3
%files -n python3-module-%oname
%doc *.rst *.txt
%python3_sitelibdir/*
%endif

%changelog
* Wed Apr 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.git20150409
- Initial build for Sisyphus

