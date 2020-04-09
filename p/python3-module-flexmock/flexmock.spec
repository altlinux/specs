%define _unpackaged_files_terminate_build 1
%define oname flexmock

%def_with check

Name: python3-module-%oname
Version: 0.10.4
Release: alt2

Summary: Mock/Stub/Spy library for Python
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/flexmock/

BuildArch: noarch

# https://github.com/has207/flexmock.git
Source: %name-%version.tar.gz

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(nose)
BuildRequires: python3(pytest)
BuildRequires: python3(twisted)
%endif

%description
flexmock is a testing library for Python that makes it easy to create
mocks, stubs and fakes.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
export PYTHON_VERSIONS='%_python3_version'
tests/run_tests.sh

%files
%doc CHANGELOG README.rst docs
%python3_sitelibdir/flexmock.py
%python3_sitelibdir/__pycache__/flexmock.cpython-*
%python3_sitelibdir/flexmock-%version-py%_python3_version.egg-info/

%changelog
* Thu Apr 09 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.10.4-alt2
- Build for python2 disabled.

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

