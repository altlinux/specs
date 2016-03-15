%define oname jsonapi

%def_with python3

Name: python-module-%oname
Version: 0.7.0
Release: alt1.git20150227.1.1
Summary: JSON API realisation
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/jsonapi/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pavlov99/jsonapi.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-django-tests python-module-mixer
#BuildPreReq: python-module-django-command-extensions
#BuildPreReq: python-module-django-debug-toolbar
#BuildPreReq: python-module-django-nose python-module-coverage
#BuildPreReq: python-module-mock ipython python-module-ipdb
#BuildPreReq: python-module-django-dbbackend-sqlite3
#BuildPreReq: python-module-oauth2_provider python-module-testfixtures
#BuildPreReq: python-modules-sqlite3
#BuildPreReq: python-modules-multiprocessing
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-django-tests python3-module-mixer
#BuildPreReq: python3-module-django-command-extensions
#BuildPreReq: python3-module-django-debug-toolbar
#BuildPreReq: python3-module-django-nose python3-module-coverage
#BuildPreReq: python3-module-mock ipython3 python3-module-ipdb
#BuildPreReq: python3-module-django-dbbackend-sqlite3
#BuildPreReq: python3-module-oauth2_provider python3-module-testfixtures
#BuildPreReq: python3-modules-sqlite3
%endif

%py_provides %oname
%py_requires django oauth2_provider

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: ipython ipython3 python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-django python-module-docutils python-module-enum34 python-module-functools32 python-module-future python-module-genshi python-module-greenlet python-module-ipykernel python-module-ipyparallel python-module-ipython_genutils python-module-jinja2 python-module-jsonschema python-module-jupyter_client python-module-jupyter_core python-module-matplotlib python-module-nbconvert python-module-nbformat python-module-ndg-httpsclient python-module-ntlm python-module-numpy python-module-pexpect python-module-pip python-module-psycopg2 python-module-ptyprocess python-module-pyasn1 python-module-pycares python-module-pycurl python-module-pygobject3 python-module-pyparsing python-module-pytest python-module-pytz python-module-setuptools python-module-snowballstemmer python-module-sphinx python-module-terminado python-module-tornado_xstatic python-module-traitlets python-module-wx3.0 python-module-xstatic python-module-xstatic-term.js python-module-yaml python-module-zmq python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-multiprocessing python-modules-unittest python-modules-wsgiref python3 python3-base python3-module-Pygments python3-module-babel python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-cssselect python3-module-docutils python3-module-enum34 python3-module-future python3-module-genshi python3-module-greenlet python3-module-ipykernel python3-module-ipyparallel python3-module-ipython_genutils python3-module-jinja2 python3-module-jsonschema python3-module-jupyter_client python3-module-jupyter_core python3-module-matplotlib python3-module-nbconvert python3-module-nbformat python3-module-ntlm python3-module-numpy python3-module-pexpect python3-module-pip python3-module-psycopg2 python3-module-ptyprocess python3-module-pycares python3-module-pycparser python3-module-pygobject3 python3-module-pyparsing python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-snowballstemmer python3-module-sphinx python3-module-terminado python3-module-tornado_xstatic python3-module-traitlets python3-module-xstatic python3-module-xstatic-term.js python3-module-yaml python3-module-yieldfrom.http.client python3-module-yieldfrom.requests python3-module-yieldfrom.urllib3 python3-module-zmq python3-module-zope python3-module-zope.event python3-module-zope.interface
BuildRequires: python-module-coverage python-module-django-command-extensions python-module-html5lib python-module-ipdb python-module-nose python-module-notebook python-module-pbr python-module-setuptools-tests python-module-unittest2 python3-module-coverage python3-module-django python3-module-html5lib python3-module-ipdb python3-module-nose python3-module-notebook python3-module-pbr python3-module-setuptools-tests python3-module-unittest2 python3-module-zope.component rpm-build-python3

%description
jsonapi protocol implementation for Django.

%package -n python3-module-%oname
Summary: JSON API realisation
Group: Development/Python3
%py3_provides %oname
%py3_requires django oauth2_provider

%description -n python3-module-%oname
jsonapi protocol implementation for Django.

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
#make test
%if_with python3
pushd ../python3
python3 setup.py test
sed -i 's|django-admin.py|django-admin.py3|' Makefile
#make test
popd
%endif

%files
%doc *.rst docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.0-alt1.git20150227.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1.git20150227.1
- NMU: Use buildreq for BR.

* Tue Mar 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1.git20150227
- Version 0.7.0

* Thu Feb 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.11-alt1.git20150226
- Version 0.6.11

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.9-alt1.git20150225
- Version 0.6.9

* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.5-alt1.git20150211
- Version 0.6.5

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.9-alt1.git20150114
- Initial build for Sisyphus

