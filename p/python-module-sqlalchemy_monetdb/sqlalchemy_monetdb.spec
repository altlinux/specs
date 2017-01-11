%define _unpackaged_files_terminate_build 1
%define oname sqlalchemy_monetdb

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.9.3
Release: alt1
Summary: SQLAlchemy dialect for MonetDB
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/sqlalchemy_monetdb/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/b0/68/a5ab95d99b50895ea37dec364d41b85afbeeff97b455c48510aaa62608b2/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-monetdb python-module-SQLAlchemy-tests
#BuildPreReq: python-module-nose python-module-mock
#BuildPreReq: python-module-coverage
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-monetdb python3-module-SQLAlchemy-tests
#BuildPreReq: python3-module-nose python3-module-mock
#BuildPreReq: python3-module-coverage
%endif

%py_provides %oname
%py_requires monetdb sqlalchemy

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-unittest python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-ntlm python3-module-pip python3-module-pycparser python3-module-setuptools
BuildRequires: python-module-coverage python-module-monetdb python-module-nose python-module-pbr python-module-pytest python-module-unittest2 python3-module-coverage python3-module-html5lib python3-module-monetdb python3-module-nose python3-module-pbr python3-module-pytest python3-module-unittest2 rpm-build-python3

%description
MonetDB dialect for SQLAlchemy.

%package -n python3-module-%oname
Summary: SQLAlchemy dialect for MonetDB
Group: Development/Python3
%py3_provides %oname
%py3_requires monetdb sqlalchemy

%description -n python3-module-%oname
MonetDB dialect for SQLAlchemy.

%prep
%setup -q -n %{oname}-%{version}

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
python setup.py test
python run_tests.py
%if_with python3
pushd ../python3
python3 setup.py test
python3 run_tests.py
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9-alt1.1
- NMU: Use buildreq for BR.

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1
- Initial build for Sisyphus

