%define _unpackaged_files_terminate_build 1
%define oname SQLAlchemy-FullText-Search

%def_with python3

Name: python-module-%oname
Version: 0.2.3
Release: alt1
Summary: Offering FullText Search of MySQL in SQLAlchemy
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/SQLAlchemy-FullText-Search/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mengzhuo/sqlalchemy-fulltext-search.git
Source0: https://pypi.python.org/packages/05/bc/efed1d829e4902bfc207fed42c36707e09683e0c44b14e5423ea68b5f877/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-SQLAlchemy python-module-pymysql
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-SQLAlchemy python3-module-pymysql
%endif

%py_provides sqlalchemy_fulltext

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python-module-setuptools-tests python3-module-setuptools-tests rpm-build-python3

%description
Provide FullText for MYSQL & SQLAlchemy model.

%package -n python3-module-%oname
Summary: Offering FullText Search of MySQL in SQLAlchemy
Group: Development/Python3
%py3_provides sqlalchemy_fulltext

%description -n python3-module-%oname
Provide FullText for MYSQL & SQLAlchemy model.

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
%if_with python3
pushd ../python3
python3 setup.py test
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
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.2-alt1.git20150109.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 0.2.2-alt1.git20150109.1
- NMU: Use buildreq for BR.

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1.git20150109
- Version 0.2.2

* Tue Oct 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20141028
- Initial build for Sisyphus

