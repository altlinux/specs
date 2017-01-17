%define _unpackaged_files_terminate_build 1
BuildRequires: unzip
%define oname asyncio_mongo

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.2.4
Release: alt1
Summary: Asynchronous Python 3.3+ driver for MongoDB
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/asyncio_mongo/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://bitbucket.org/mrdon/asyncio-mongo.git
Source0: https://pypi.python.org/packages/55/d5/b49346cb293f03d26dfe4074e11d0b6cd59cf346b6ed6d4fe5dd7ee55be1/%{oname}-%{version}.zip

%if_with python2
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-asyncio python-module-nose
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-asyncio python3-module-nose
%endif

%py_provides %oname
%py_requires asyncio

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: elfutils python-base python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python3-devel python3-module-asyncio python3-module-nose python3-module-setuptools-tests rpm-build-python3

%description
An asynchronous Python driver for the Mongo database, based on Python's
asyncio. This project is based on TxMongo.

%package -n python3-module-%oname
Summary: Asynchronous Python 3.3+ driver for MongoDB
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio

%description -n python3-module-%oname
An asynchronous Python driver for the Mongo database, based on Python's
asyncio. This project is based on TxMongo.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
%endif

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
%if_with python2
python setup.py test
%endif
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%if_with python2
%files
%doc PKG-INFO
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%python3_sitelibdir/*
%endif

%changelog
* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.4-alt1
- automated PyPI update

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.3-alt1.git20140401.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.3-alt1.git20140401.1
- NMU: Use buildreq for BR.

* Sat Jan 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.3-alt1.git20140401
- Initial build for Sisyphus

