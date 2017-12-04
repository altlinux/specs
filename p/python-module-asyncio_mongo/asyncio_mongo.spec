%define _unpackaged_files_terminate_build 1
%define oname asyncio_mongo

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.2.4
Release: alt2
Summary: Asynchronous Python 3.3+ driver for MongoDB
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/asyncio_mongo/

# https://bitbucket.org/mrdon/asyncio-mongo.git
Source: %oname-%version.zip

BuildRequires: unzip
%if_with python2
BuildRequires: python-devel python-module-setuptools-tests
BuildRequires: python2.7(asyncio) python-module-nose
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires: python3(asyncio) python3-module-nose
%endif

%py_provides %oname
%py_requires asyncio

%description
An asynchronous Python driver for the Mongo database, based on Python's
asyncio. This project is based on TxMongo.

%if_with python3
%package -n python3-module-%oname
Summary: Asynchronous Python 3.3+ driver for MongoDB
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio

%description -n python3-module-%oname
An asynchronous Python driver for the Mongo database, based on Python's
asyncio. This project is based on TxMongo.
%endif

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
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%changelog
* Mon Dec 04 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.4-alt2
- Updated build dependencies.

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.4-alt1
- automated PyPI update

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.3-alt1.git20140401.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.3-alt1.git20140401.1
- NMU: Use buildreq for BR.

* Sat Jan 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.3-alt1.git20140401
- Initial build for Sisyphus

