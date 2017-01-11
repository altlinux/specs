%define _unpackaged_files_terminate_build 1
%define oname pytest-cov

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 2.4.0
Release: alt1
Summary: py.test plugin for coverage reporting with support for centralised and distributed testing
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-cov/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/schlamar/pytest-cov.git
Source0: https://pypi.python.org/packages/00/c0/2bfd1fcdb9d407b8ac8185b1cb5ff458105c6b207a9a7f0e13032de9828f/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-coverage python-module-cov-core
#BuildPreReq: python-module-virtualenv python-module-pytest-xdist
#BuildPreReq: python-module-process-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-coverage python3-module-cov-core
#BuildPreReq: python3-module-virtualenv python3-module-pytest-xdist
#BuildPreReq: python3-module-process-tests
%endif

%py_provides pytest_cov
%py_requires pytest cov_core

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-chardet python-module-cryptography python-module-enum34 python-module-ndg-httpsclient python-module-ntlm python-module-pyasn1 python-module-pytest python-module-rlcompleter2 python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-chardet python3-module-pytest python3-module-setuptools python3-module-yieldfrom.http.client python3-module-yieldfrom.requests python3-module-yieldfrom.urllib3
BuildRequires: python-module-coverage python-module-pytest-xdist python-module-virtualenv python3-module-coverage python3-module-pytest-xdist python3-module-virtualenv rpm-build-python3

%description
This plugin produces coverage reports. It supports centralised testing
and distributed testing in both load and each modes. It also supports
coverage of subprocesses.

All features offered by the coverage package should be available, either
through pytest-cov or through coverage's config file.

%package -n python3-module-%oname
Summary: py.test plugin for coverage reporting with support for centralised and distributed testing
Group: Development/Python3
%py3_provides pytest_cov
%py3_requires pytest cov_core

%description -n python3-module-%oname
This plugin produces coverage reports. It supports centralised testing
and distributed testing in both load and each modes. It also supports
coverage of subprocesses.

All features offered by the coverage package should be available, either
through pytest-cov or through coverage's config file.

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
export PYTHONPATH=%buildroot%python_sitelibdir
py.test -vv
python setup.py test
%if_with python3
pushd ../python3
export PYTHONPATH=%buildroot%python3_sitelibdir
python3 setup.py test
py.test-%_python3_version -vv
popd
%endif
exit 1

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.4.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1.0-alt1.git20150823.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.1.0-alt1.git20150823.1
- NMU: Use buildreq for BR.

* Mon Aug 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1.git20150823
- Version 2.1.0

* Sun Aug 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.git20150801
- New snapshot

* Wed Jul 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.git20150728
- Version 2.0.0

* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.1-alt1.git20141125
- New snapshot

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.1-alt1.git20141106
- Version 1.8.1

* Fri Oct 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt1.git20140822
- Initial build for Sisyphus

