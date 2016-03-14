%define oname httpbin

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.2.0
Release: alt1.git20140826.1.1
Summary: HTTP Request and Response Service
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/httpbin/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/kennethreitz/httpbin.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-flask python-module-markupsafe
#BuildPreReq: python-module-decorator python-module-itsdangerous
#BuildPreReq: python-module-six python-module-gevent
#BuildPreReq: python-module-greenlet python-module-gunicorn
#BuildPreReq: python-module-jinja2 python-module-werkzeug
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-flask python3-module-markupsafe
#BuildPreReq: python3-module-decorator python3-module-itsdangerous
#BuildPreReq: python3-module-six python3-module-gevent
#BuildPreReq: python3-module-greenlet python3-module-gunicorn
#BuildPreReq: python3-module-jinja2 python3-module-werkzeug
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-cryptography python-module-django python-module-dns python-module-enum34 python-module-greenlet python-module-jinja2 python-module-paste python-module-psycopg2 python-module-pyasn1 python-module-pycares python-module-pycurl python-module-setuptools python-module-yaml python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python-modules-wsgiref python3 python3-base python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-django python3-module-dns python3-module-enum34 python3-module-greenlet python3-module-gunicorn python3-module-jinja2 python3-module-paste python3-module-psycopg2 python3-module-pycares python3-module-pycparser python3-module-setuptools python3-module-yaml python3-module-zope python3-module-zope.interface
BuildRequires: python-module-gunicorn python-module-pytest python3-module-pytest rpm-build-python3

%description
Testing an HTTP Library can become difficult sometimes. PostBin.org is
fantastic for testing POST requests, but not much else. This exists to
cover all kinds of HTTP scenarios. Additional endpoints are being
considered.

All endpoint responses are JSON-encoded.

%package -n python3-module-%oname
Summary: HTTP Request and Response Service
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Testing an HTTP Library can become difficult sometimes. PostBin.org is
fantastic for testing POST requests, but not much else. This exists to
cover all kinds of HTTP scenarios. Additional endpoints are being
considered.

All endpoint responses are JSON-encoded.

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
python test_httpbin.py
%if_with python3
pushd ../python3
python3 setup.py test
python3 test_httpbin.py
popd
%endif

%files
%doc AUTHORS *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.md
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.git20140826.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1.git20140826.1
- NMU: Use buildreq for BR.

* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20140826
- Initial build for Sisyphus

