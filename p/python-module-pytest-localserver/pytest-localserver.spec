%define _unpackaged_files_terminate_build 1
%define oname pytest-localserver

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.3.6
Release: alt1
Summary: py.test plugin to test server connections locally
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-localserver/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/06/42/cc9e9101ddfcf9eefcc6bd0f9624f1631f385745e1f39a24ecc69201403c/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-werkzeug python-module-OpenSSL
#BuildPreReq: python-module-six python-module-requests
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-werkzeug python3-module-OpenSSL
#BuildPreReq: python3-module-six python3-module-requests
%endif

%py_provides pytest_localserver

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-cryptography python-module-enum34 python-module-pyasn1 python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-cffi python3-module-cryptography python3-module-enum34 python3-module-ndg-httpsclient python3-module-ntlm python3-module-pycparser python3-module-setuptools
BuildRequires: python-module-chardet python-module-ndg-httpsclient python-module-ntlm python-module-pytest python3-module-chardet python3-module-pytest python3-module-urllib3 rpm-build-python3

%description
pytest-localserver is a plugin for the pytest testing framework which
enables you to test server connections locally.

%package -n python3-module-%oname
Summary: py.test plugin to test server connections locally
Group: Development/Python3
%py3_provides pytest_localserver

%description -n python3-module-%oname
pytest-localserver is a plugin for the pytest testing framework which
enables you to test server connections locally.

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
py.test
%if_with python3
pushd ../python3
py.test-%_python3_version
popd
%endif

%files
%doc README
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.6-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.3-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.3-alt2.1
- NMU: Use buildreq for BR.

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3-alt2
- Fixed requirements

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3-alt1
- Initial build for Sisyphus

