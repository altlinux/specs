%define oname freetypy

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.1
Release: alt1.git20150408.1
Summary: Fast and modern Python wrappers for freetype, written in Python/C API 
License: BSD
Group: Development/Python
Url: https://github.com/matplotlib/freetypy
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/matplotlib/freetypy.git
Source: %name-%version.tar

#BuildPreReq: libfreetype-devel
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-numpy python-module-matplotlib
#BuildPreReq: python-module-nose
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-numpy python3-module-matplotlib
#BuildPreReq: python3-module-nose
%endif

%py_provides %oname

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils pkg-config python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-matplotlib python-module-numpy python-module-pyparsing python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base
BuildRequires: libfreetype-devel python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python3-devel rpm-build-python3 time

%description
Fast and modern Python wrappers for freetype, written in Python/C API.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Fast and modern Python wrappers for freetype, written in Python/C API.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Fast and modern Python wrappers for freetype, written in Python/C API
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Fast and modern Python wrappers for freetype, written in Python/C API.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Fast and modern Python wrappers for freetype, written in Python/C API.

This package contains tests for %oname.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Fast and modern Python wrappers for freetype, written in Python/C API.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Fast and modern Python wrappers for freetype, written in Python/C API.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx doc
ln -s ../objects.inv doc/source/

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%if_with python3
pushd ../python3
sed -i 's|PyInt_FromLong|PyLong_FromLong|g' src/glyph.c
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
cd ~
export PYTHONPATH=%buildroot%python_sitelibdir
nosetests -v --processes=-1 freetypy.tests
%if_with python3
export PYTHONPATH=%buildroot%python3_sitelibdir
nosetests3 -v --processes=-1 freetypy.tests
%endif

%files
%doc *.md examples
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests

%files docs
%doc doc/build/html/*

%files tests
%python_sitelibdir/*/tests

%files pickles
%python_sitelibdir/*/pickle

%if_with python3
%files -n python3-module-%oname
%doc *.md examples doc/build/html
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt1.git20150408.1
- NMU: Use buildreq for BR.

* Wed Apr 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20150408
- Initial build for Sisyphus

