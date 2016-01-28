%define oname pytest-httpbin

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.0.6
Release: alt1.git20150215.1
Summary: Easily test your HTTP library against a local copy of httpbin
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-httpbin/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/kevin1024/pytest-httpbin.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-flask python-module-decorator
#BuildPreReq: python-module-httpbin python-module-six
#BuildPreReq: python-module-requests python-modules-wsgiref
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-flask python3-module-decorator
#BuildPreReq: python3-module-httpbin python3-module-six
#BuildPreReq: python3-module-requests
%endif

%py_provides pytest_httpbin

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-cryptography python-module-enum34 python-module-jinja2 python-module-pyasn1 python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-cffi python3-module-cryptography python3-module-enum34 python3-module-jinja2 python3-module-ndg-httpsclient python3-module-ntlm python3-module-pycparser python3-module-setuptools
BuildRequires: python-module-chardet python-module-ndg-httpsclient python-module-ntlm python-module-pytest python-modules-wsgiref python3-module-chardet python3-module-pytest python3-module-urllib3 rpm-build-python3

%description
httpbin is an amazing web service for testing HTTP libraries. It has
several great endpoints that can test pretty much everything you need in
a HTTP library. The only problem is: maybe you don't want to wait for
your tests to travel across the Internet and back to make assertions
against a remote web service.

Enter pytest-httpbin. Pytest-httpbin creates a pytest "fixture" that is
dependency-injected into your tests. It automatically starts up a HTTP
server in a separate thread running httpbin and provides your test with
the URL in the fixture.

%package -n python3-module-%oname
Summary: Easily test your HTTP library against a local copy of httpbin
Group: Development/Python3
%py3_provides pytest_httpbin

%description -n python3-module-%oname
httpbin is an amazing web service for testing HTTP libraries. It has
several great endpoints that can test pretty much everything you need in
a HTTP library. The only problem is: maybe you don't want to wait for
your tests to travel across the Internet and back to make assertions
against a remote web service.

Enter pytest-httpbin. Pytest-httpbin creates a pytest "fixture" that is
dependency-injected into your tests. It automatically starts up a HTTP
server in a separate thread running httpbin and provides your test with
the URL in the fixture.

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
export PYTHONPATH=$PWD
python setup.py test
./runtests.sh
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
python3 setup.py test
sed -i 's|python|python3|' runtests.sh
./runtests.sh
popd
%endif

%files
%doc *.rst *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst *.md
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.6-alt1.git20150215.1
- NMU: Use buildreq for BR.

* Mon Feb 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.6-alt1.git20150215
- Version 0.0.6

* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt1.git20140914
- Initial build for Sisyphus

