%define oname oauth2client

%def_with python3

Name: python-module-%oname
Version: 1.4.12
Release: alt1.git20150814

Summary: OAuth 2.0 client library
License: Apache Software License
Group: Development/Python

Url: https://pypi.python.org/pypi/oauth2client/

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python
BuildPreReq: python-module-setuptools-tests python-modules-json
BuildPreReq: python-module-httplib2 python-module-pyasn1
BuildPreReq: python-module-pyasn1-modules python-module-rsa
BuildPreReq: python-module-keyring python-module-mox
BuildPreReq: python-module-webapp2 python-module-google-appengine
BuildPreReq: python-module-flask
BuildPreReq: python-module-sphinx-devel python-module-django
BuildPreReq: python-module-sphinx_rtd_theme
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-httplib2 python3-module-pyasn1
BuildPreReq: python3-module-pyasn1-modules python3-module-rsa
BuildPreReq: python3-module-keyring python3-module-mox
BuildPreReq: python3-module-webapp2 python3-module-google-appengine
BuildPreReq: python3-module-flask
BuildPreReq: python-tools-2to3
%endif

%setup_python_module %oname
%py_requires httplib2 pyasn1 pyasn1_modules rsa six
%add_python_req_skip google webapp2

%description
The oauth2client is a client library for OAuth 2.0.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
The oauth2client is a client library for OAuth 2.0.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation

%description docs
The oauth2client is a client library for OAuth 2.0.

This package contains documentation for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: OAuth 2.0 client library
Group: Development/Python3
%py3_requires httplib2 pyasn1 pyasn1_modules rsa six
%add_python3_req_skip google webapp2

%description -n python3-module-%oname
The oauth2client is a client library for OAuth 2.0.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
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

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Thu Aug 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.12-alt1.git20150814
- Version 1.4.12

* Tue Nov 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.2-alt1.git20141124
- Version 1.4.2

* Sun Nov 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1.git20141115
- Version 1.4.1

* Tue Nov 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt1.git20141031
- Version 1.3.2

* Tue Oct 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1.git20141027
- Version 1.3.1

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2
- Added module for Python 3

* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1
- Version 1.2

* Wed Apr 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

