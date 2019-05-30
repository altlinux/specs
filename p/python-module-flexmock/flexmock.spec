%define _unpackaged_files_terminate_build 1
%define oname flexmock

%def_with check

Name: python-module-%oname
Version: 0.10.4
Release: alt1
Summary: Mock/Stub/Spy library for Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/flexmock/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/has207/flexmock.git
Source: %name-%version.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python2.7(nose)
BuildRequires: python2.7(pytest)
BuildRequires: python2.7(twisted)
BuildRequires: python-module-twisted-core-test
BuildRequires: python3(nose)
BuildRequires: python3(pytest)
BuildRequires: python3(twisted)
%endif

%description
flexmock is a testing library for Python that makes it easy to create
mocks, stubs and fakes.

%package -n python3-module-%oname
Summary: Mock/Stub/Spy library for Python
Group: Development/Python3

%description -n python3-module-%oname
flexmock is a testing library for Python that makes it easy to create
mocks, stubs and fakes.

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
export PYTHON_IMPLEMENTATIONS=python

export PYTHON_VERSIONS='%_python_version'
tests/run_tests.sh

pushd ../python3
export PYTHON_VERSIONS='%_python3_version'
tests/run_tests.sh
popd

%files
%doc CHANGELOG README.rst docs
%python_sitelibdir/flexmock.py
%python_sitelibdir/flexmock.py[co]
%python_sitelibdir/flexmock-%version-py%_python_version.egg-info/

%files -n python3-module-%oname
%doc CHANGELOG README.rst docs
%python3_sitelibdir/flexmock.py
%python3_sitelibdir/__pycache__/flexmock.cpython-*
%python3_sitelibdir/flexmock-%version-py%_python3_version.egg-info/

%changelog
* Thu May 30 2019 Stanislav Levin <slev@altlinux.org> 0.10.4-alt1
- 0.10.2 -> 0.10.4.

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.10.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.7-alt1.git20140924.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.7-alt1.git20140924.1
- NMU: Use buildreq for BR.

* Sat Nov 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7-alt1.git20140924
- Initial build for Sisyphus

