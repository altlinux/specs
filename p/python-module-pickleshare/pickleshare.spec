%define oname pickleshare

%def_with python3
# because slow
%def_disable check

Name: python-module-%oname
Version: 0.5
Release: alt1.git20150422.1
Summary: File system based database that uses python pickles
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pickleshare
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pickleshare/pickleshare.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-path
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-path
%endif

%py_provides %oname
%py_requires path

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-setuptools
BuildRequires: python-module-pytest python3-module-pytest rpm-build-python3

%description
PickleShare - a small 'shelve' like datastore with concurrency support

Like shelve, a PickleShareDB object acts like a normal dictionary.
Unlike shelve, many processes can access the database simultaneously.
Changing a value in database is immediately visible to other processes
accessing the same database.

Concurrency is possible because the values are stored in separate files.
Hence the 'database' is a directory where all files are governed by
PickleShare.

%if_with python3
%package -n python3-module-%oname
Summary: File system based database that uses python pickles
Group: Development/Python3
%py3_provides %oname
%py3_requires path

%description -n python3-module-%oname
PickleShare - a small 'shelve' like datastore with concurrency support

Like shelve, a PickleShareDB object acts like a normal dictionary.
Unlike shelve, many processes can access the database simultaneously.
Changing a value in database is immediately visible to other processes
accessing the same database.

Concurrency is possible because the values are stored in separate files.
Hence the 'database' is a directory where all files are governed by
PickleShare.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

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

%check
python setup.py test -v
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test -v
py.test-%_python3_version -vv
popd
%endif

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5-alt1.git20150422.1
- NMU: Use buildreq for BR.

* Thu Aug 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20150422
- Initial build for Sisyphus

