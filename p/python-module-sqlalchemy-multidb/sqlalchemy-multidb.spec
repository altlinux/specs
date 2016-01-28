%define oname sqlalchemy-multidb

%def_with python3

Name: python-module-%oname
Version: 0.8.2
Release: alt1.git20150711.1
Summary: Provides methods to connect to multiple databases easily
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/sqlalchemy-multidb/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/viniciuschiele/sqlalchemy-multidb.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-SQLAlchemy
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-SQLAlchemy
%endif

%py_provides sqlalchemy_multidb
%py_requires sqlalchemy

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python-module-setuptools-tests python3-module-setuptools-tests rpm-build-python3

%description
Provides methods to load the database configurations from a config file
and access multiple databases easily.

%if_with python3
%package -n python3-module-%oname
Summary: Provides methods to connect to multiple databases easily
Group: Development/Python3
%py3_provides sqlalchemy_multidb
%py3_requires sqlalchemy

%description -n python3-module-%oname
Provides methods to load the database configurations from a config file
and access multiple databases easily.
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
%if_with python3
pushd ../python3
python3 setup.py test -v
popd
%endif

%files
%doc *.rst examples
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst examples
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.8.2-alt1.git20150711.1
- NMU: Use buildreq for BR.

* Tue Jul 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.git20150711
- Initial build for Sisyphus

