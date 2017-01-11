%define _unpackaged_files_terminate_build 1
%define oname bynamodb

%def_with python3

Name: python-module-%oname
Version: 0.1.7
Release: alt1
Summary: High-Level DynamoDB Interface for Pythonwrapping Low-Level Interface of boto
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/bynamodb/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/teddychoi/BynamoDB.git
Source0: https://pypi.python.org/packages/d7/1f/461f4c9b6e67980820a136fef018cc7af950bb75b12763aa3e8ee2849e09/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-boto python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-boto
%endif

%py_provides %oname
%py_requires boto

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-cryptography python-module-enum34 python-module-pyasn1 python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-chardet python3-module-pytest python3-module-setuptools python3-module-yieldfrom.http.client python3-module-yieldfrom.urllib3
BuildRequires: python-module-chardet python-module-ecdsa python-module-ndg-httpsclient python-module-ntlm python-module-pycrypto python-module-setuptools-tests python-module-yaml python3-module-ecdsa python3-module-pycrypto python3-module-setuptools-tests python3-module-yaml python3-module-yieldfrom.requests rpm-build-python3

%description
High-Level DynamoDB Interface for Python wrapping Low-Level Interface of
boto.

%package -n python3-module-%oname
Summary: High-Level DynamoDB Interface for Pythonwrapping Low-Level Interface of boto
Group: Development/Python3
%py3_provides %oname
%py3_requires boto

%description -n python3-module-%oname
High-Level DynamoDB Interface for Python wrapping Low-Level Interface of
boto.

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
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.7-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.6-alt1.git20150717.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.6-alt1.git20150717.1
- NMU: Use buildreq for BR.

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.6-alt1.git20150717
- New snapshot

* Tue Apr 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.6-alt1.git20150414
- Version 0.1.6

* Tue Mar 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20150312
- Version 0.1.2

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20141215
- Initial build for Sisyphus

