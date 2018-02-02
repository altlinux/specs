%define oname linkedin

%def_with python3

Name: python-module-%oname
Version: 4.2
Release: alt1.git20150625.1.1.1
Summary: Python Interface to the LinkedIn API
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/python-linkedin/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ozgur/python-linkedin.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-requests python-module-requests-oauthlib
#BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-requests python3-module-requests-oauthlib
%endif

%py_provides %oname
%py_requires requests requests_oauthlib json

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-chardet python-module-cryptography python-module-enum34 python-module-ndg-httpsclient python-module-ntlm python-module-oauthlib python-module-pyasn1 python-module-pycrypto python-module-pytest python-module-requests python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-enum34 python3-module-ndg-httpsclient python3-module-ntlm python3-module-oauthlib python3-module-pycparser python3-module-pycrypto python3-module-pytest python3-module-requests python3-module-setuptools python3-module-urllib3
BuildRequires: python-module-requests-oauthlib python-module-setuptools python3-module-requests-oauthlib python3-module-setuptools rpm-build-python3 time

%description
This library provides a pure Python interface to the LinkedIn Profile,
Group, Company, Jobs, Search, Share, Network and Invitation REST APIs.

%if_with python3
%package -n python3-module-%oname
Summary: Python Interface to the LinkedIn API
Group: Development/Python3
%py3_provides %oname
%py3_requires requests requests_oauthlib json

%description -n python3-module-%oname
This library provides a pure Python interface to the LinkedIn Profile,
Group, Company, Jobs, Search, Share, Network and Invitation REST APIs.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%doc *.md *.rst examples
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md *.rst ../python3/examples
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.2-alt1.git20150625.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.2-alt1.git20150625.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.2-alt1.git20150625.1
- NMU: Use buildreq for BR.

* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2-alt1.git20150625
- New snapshot

* Thu Apr 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2-alt1.git20150214
- Initial build for Sisyphus

