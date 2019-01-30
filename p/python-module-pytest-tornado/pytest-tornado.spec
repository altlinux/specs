%define _unpackaged_files_terminate_build 1
%define oname pytest-tornado

%def_with check

Name: python-module-%oname
Version: 0.5.0
Release: alt1
Summary: Fixtures and markers to simplify testing of asynchronous tornado applications
License: ASLv2.0
Group: Development/Python
BuildArch: noarch
Url: https://pypi.org/project/pytest-tornado/

# https://github.com/eugeniy/pytest-tornado.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python2.7(pytest)
BuildRequires: python2.7(tornado)
BuildRequires: python3(pytest)
BuildRequires: python3(tornado)
%endif

%description
A py.test plugin providing fixtures and markers to simplify testing of
asynchronous tornado applications.

%package -n python3-module-%oname
Summary: Fixtures and markers to simplify testing of asynchronous tornado applications
Group: Development/Python3

%description -n python3-module-%oname
A py.test plugin providing fixtures and markers to simplify testing of
asynchronous tornado applications.

%prep
%setup

cp -fR . ../python3

%build
%python_build_debug

pushd ../python3
%python3_build_debug
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%check
PYTHONPATH=$(pwd) py.test -vv

pushd ../python3
PYTHONPATH=$(pwd) py.test3 -vv
popd

%files
%doc README.rst
%python_sitelibdir/pytest_tornado/
%python_sitelibdir/pytest_tornado-%version-py%_python_version.egg-info/

%files -n python3-module-%oname
%doc README.rst
%python3_sitelibdir/pytest_tornado/
%python3_sitelibdir/pytest_tornado-%version-py%_python3_version.egg-info/

%changelog
* Wed Jan 30 2019 Stanislav Levin <slev@altlinux.org> 0.5.0-alt1
- 0.4.5 -> 0.5.0.

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

