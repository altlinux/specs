%define _unpackaged_files_terminate_build 1
%define oname sqlalchemy-multidb

%def_with python3

Name: python-module-%oname
Version: 1.0.2
Release: alt1
Summary: Provides methods to connect to multiple databases easily
License: ASLv2.0
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/sqlalchemy-multidb/

# https://github.com/viniciuschiele/sqlalchemy-multidb.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools-tests
BuildRequires: python-module-SQLAlchemy
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires: python3-module-SQLAlchemy
%endif

%py_provides sqlalchemy_multidb
%py_requires sqlalchemy

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
* Thu Dec 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.2-alt1
- Updated to upstream version 1.0.2.

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.2-alt1.git20150711.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.8.2-alt1.git20150711.1
- NMU: Use buildreq for BR.

* Tue Jul 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.git20150711
- Initial build for Sisyphus

