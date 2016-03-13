%define oname dbarray

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.1.6
Release: alt1.git20141122.1.1
Summary: NumPy array stored in database
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/dbarray/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/wanji/dbarray.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: doxygen graphviz doxypy
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-leveldb python-module-lmdb libnumpy-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-leveldb python3-module-lmdb
#BuildPreReq: libnumpy-py3-devel python-tools-2to3
%endif

%py_provides %oname

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: fontconfig fonts-bitmap-misc libwayland-client libwayland-server python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-numpy python-module-pyparsing python-module-pytz python-module-setuptools python-module-snowballstemmer python-module-sphinx python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base python3-module-numpy python3-module-setuptools
BuildRequires: doxygen doxypy graphviz python-module-docutils python-module-html5lib python-module-matplotlib python-module-pytest python3-module-pytest rpm-build-python3 time

%description
DBArray is an 2D array stored in database. The purpose of this class is
to provide a way to store and access large array which can not be loaded
into memory.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation

%description docs
DBArray is an 2D array stored in database. The purpose of this class is
to provide a way to store and access large array which can not be loaded
into memory.

This package contains documentation for %oname.

%package -n python3-module-%oname
Summary: NumPy array stored in database
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
DBArray is an 2D array stored in database. The purpose of this class is
to provide a way to store and access large array which can not be loaded
into memory.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

doxygen

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
py.test
%if_with python3
pushd ../python3
python3 setup.py test
#py.test-%_python3_version
popd
%endif

%files
%doc *.md
%python_sitelibdir/*

%files docs
%doc doc/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.6-alt1.git20141122.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.6-alt1.git20141122.1
- NMU: Use buildreq for BR.

* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.6-alt1.git20141122
- Initial build for Sisyphus

