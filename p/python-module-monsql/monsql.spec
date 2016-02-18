%define oname monsql

%def_with python3

Name: python-module-%oname
Version: 0.1.6
Release: alt1.git20141222.1
Summary: MonSQL - Mongodb-style way for using mysql
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/monsql/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/firstprayer/monsql.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-MySQLdb
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-MySQLdb
#BuildPreReq: python-tools-2to3
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python-module-setuptools-tests python3-module-setuptools-tests rpm-build-python3 time

%description
A mysql wrapper for easy interaction with MySQL using a mongodb-like
interface. It's motivated by the fact that mongodb is so easy to use,
even for a complete novince! This library is suitable for people don't
know much about SQL syntax, but they can still manipulate mysql database
through this very simple mongodb-style interface -- query, insert,
update, all very easy to understand.

%package -n python3-module-%oname
Summary: MonSQL - Mongodb-style way for using mysql
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A mysql wrapper for easy interaction with MySQL using a mongodb-like
interface. It's motivated by the fact that mongodb is so easy to use,
even for a complete novince! This library is suitable for people don't
know much about SQL syntax, but they can still manipulate mysql database
through this very simple mongodb-style interface -- query, insert,
update, all very easy to understand.

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

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md doc/source/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md doc/source/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.6-alt1.git20141222.1
- NMU: Use buildreq for BR.

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.6-alt1.git20141222
- Initial build for Sisyphus

