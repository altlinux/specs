%define oname mf2py

%def_with python3

Name: python-module-%oname
Version: 0.2.2
Release: alt1.git20150205.1.1
Summary: Python Microformats2 parser
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/mf2py/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/tommorris/mf2py.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-html5lib python-module-requests
#BuildPreReq: python-module-BeautifulSoup4 python-module-nose
#BuildPreReq: python-module-flask python-module-gunicorn
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-html5lib python3-module-requests
#BuildPreReq: python3-module-BeautifulSoup4 python3-module-nose
#BuildPreReq: python3-module-flask python3-module-gunicorn
#BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires html5lib requests bs4 flask gunicorn

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-django python-module-dns python-module-enum34 python-module-genshi python-module-greenlet python-module-html5lib python-module-jinja2 python-module-ndg-httpsclient python-module-ntlm python-module-paste python-module-psycopg2 python-module-pyasn1 python-module-pycares python-module-pycurl python-module-pytest python-module-setuptools python-module-yaml python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-modules-wsgiref python-tools-2to3 python3 python3-base python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-cssselect python3-module-django python3-module-dns python3-module-enum34 python3-module-genshi python3-module-greenlet python3-module-gunicorn python3-module-html5lib python3-module-jinja2 python3-module-ndg-httpsclient python3-module-ntlm python3-module-paste python3-module-psycopg2 python3-module-pycares python3-module-pycparser python3-module-pytest python3-module-setuptools python3-module-urllib3 python3-module-yaml python3-module-zope python3-module-zope.interface
BuildRequires: python-module-BeautifulSoup4 python-module-gunicorn python-module-nose python-module-requests python-module-setuptools-tests python3-module-BeautifulSoup4 python3-module-nose python3-module-requests python3-module-setuptools-tests rpm-build-python3 time

%description
Python parser for microformats 2. Full-featured and mostly stable.
Implements the full mf2 spec, including backward compatibility with
microformats1.

%package -n python3-module-%oname
Summary: Python Microformats2 parser
Group: Development/Python3
%py3_provides %oname
%py3_requires html5lib requests bs4 flask gunicorn

%description -n python3-module-%oname
Python parser for microformats 2. Full-featured and mostly stable.
Implements the full mf2 spec, including backward compatibility with
microformats1.

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
#nosetests -v
%if_with python3
pushd ../python3
python3 setup.py test
#nosetests3 -v
popd
%endif

%files
%doc AUTHORS *.md doc/source/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.md doc/source/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.2-alt1.git20150205.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.2-alt1.git20150205.1
- NMU: Use buildreq for BR.

* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1.git20150205
- Initial build for Sisyphus

