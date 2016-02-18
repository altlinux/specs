%define oname blosc

%def_with python3

Name: python-module-%oname
Version: 1.2.6
Release: alt1.dev.git20150415.1
Summary: A Python wrapper for the extremely fast Blosc compression library
License: MIT / BSD
Group: Development/Python
Url: http://python-blosc.blosc.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Blosc/python-blosc.git
Source: %name-%version.tar

#BuildPreReq: libblosc-devel
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-nose libnumpy-devel
#BuildPreReq: python-module-sphinx-devel python-module-numpydoc
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-nose libnumpy-py3-devel
%endif

%py_provides %oname

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: elfutils python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-docutils python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-matplotlib python-module-numpy python-module-pyparsing python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-numpy python3-module-setuptools xz
BuildRequires: libblosc-devel python-module-alabaster python-module-html5lib python-module-nose python-module-numpy-testing python-module-numpydoc python-module-objects.inv python-module-pytest python3-devel python3-module-nose python3-module-numpy-testing python3-module-pytest rpm-build-python3 time

%description
Blosc (http://blosc.org) is a high performance compressor optimized for
binary data. It has been designed to transmit data to the processor
cache faster than the traditional, non-compressed, direct memory fetch
approach via a memcpy() OS call.

Blosc works well for compressing numerical arrays that contains data
with relatively low entropy, like sparse data, time series, grids with
regular-spaced values, etc.

This is a Python package that wraps it.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Blosc (http://blosc.org) is a high performance compressor optimized for
binary data. It has been designed to transmit data to the processor
cache faster than the traditional, non-compressed, direct memory fetch
approach via a memcpy() OS call.

Blosc works well for compressing numerical arrays that contains data
with relatively low entropy, like sparse data, time series, grids with
regular-spaced values, etc.

This is a Python package that wraps it.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Blosc (http://blosc.org) is a high performance compressor optimized for
binary data. It has been designed to transmit data to the processor
cache faster than the traditional, non-compressed, direct memory fetch
approach via a memcpy() OS call.

Blosc works well for compressing numerical arrays that contains data
with relatively low entropy, like sparse data, time series, grids with
regular-spaced values, etc.

This is a Python package that wraps it.

This package contains pickles for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: A Python wrapper for the extremely fast Blosc compression library
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Blosc (http://blosc.org) is a high performance compressor optimized for
binary data. It has been designed to transmit data to the processor
cache faster than the traditional, non-compressed, direct memory fetch
approach via a memcpy() OS call.

Blosc works well for compressing numerical arrays that contains data
with relatively low entropy, like sparse data, time series, grids with
regular-spaced values, etc.

This is a Python package that wraps it.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Blosc (http://blosc.org) is a high performance compressor optimized for
binary data. It has been designed to transmit data to the processor
cache faster than the traditional, non-compressed, direct memory fetch
approach via a memcpy() OS call.

Blosc works well for compressing numerical arrays that contains data
with relatively low entropy, like sparse data, time series, grids with
regular-spaced values, etc.

This is a Python package that wraps it.

This package contains tests for %oname.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
%python_build_debug \
	--blosc=%prefix

%if_with python3
pushd ../python3
%python3_build_debug \
	--blosc=%prefix
popd
%endif

%install
%python_install \
	--blosc=%prefix

%if_with python3
pushd ../python3
%python3_install \
	--blosc=%prefix
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C doc pickle
%make -C doc html

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
cd ~
export PYTHONPATH=%buildroot%python_sitelibdir
nosetests -v --with-doctest %oname
%if_with python3
export PYTHONPATH=%buildroot%python3_sitelibdir
nosetests3 -v --with-doctest %oname
%endif

%files
%doc *.rst doc/_build/html bench
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*

%files pickles
%python_sitelibdir/*/pickle

%if_with python3
%files -n python3-module-%oname
%doc *.rst doc/_build/html bench
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.2.6-alt1.dev.git20150415.1
- NMU: Use buildreq for BR.

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.6-alt1.dev.git20150415
- Initial build for Sisyphus

