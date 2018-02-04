%define _unpackaged_files_terminate_build 1
%define oname pytest-tornado

%def_with python3

Name: python-module-%oname
Version: 0.4.5
Release: alt2.1
Summary: Fixtures and markers to simplify testing of asynchronous tornado applications
License: ASLv2.0
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/pytest-tornado/

# https://github.com/eugeniy/pytest-tornado.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-tornado
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-tornado
BuildRequires: python3-module-pytest
%endif

%py_provides pytest_tornado
%py_requires pytest tornado.testing

%description
A py.test plugin providing fixtures and markers to simplify testing of
asynchronous tornado applications.

%package -n python3-module-%oname
Summary: Fixtures and markers to simplify testing of asynchronous tornado applications
Group: Development/Python3
%py3_provides pytest_tornado
%py3_requires pytest tornado.testing

%description -n python3-module-%oname
A py.test plugin providing fixtures and markers to simplify testing of
asynchronous tornado applications.

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
python setup.py test
PYTHONPATH=$(pwd) py.test -vv

%if_with python3
pushd ../python3
python3 setup.py test
PYTHONPATH=$(pwd) py.test3 -vv
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.5-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Nov 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.5-alt2
- Fixed build.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.5-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.2-alt1.git20150219.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.git20150219
- Initial build for Sisyphus

