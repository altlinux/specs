%define oname oauth2client

%def_with python3

Name: python-module-%oname
Version: 4.1.2
Release: alt2.1
Summary: OAuth 2.0 client library
License: Apache Software License
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/oauth2client/

# https://github.com/google/oauth2client.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python
BuildRequires: python-module-docutils python-module-html5lib python-module-httplib2 python-module-keyring python-module-mox python-module-objects.inv python-module-pyasn1-modules python-module-rsa python-module-setuptools 
BuildRequires: python-module-sphinx-devel
BuildRequires: python-module-mock python-module-fasteners python-module-flask
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-httplib2 python3-module-keyring python3-module-mox python3-module-pyasn1-modules python3-module-rsa python3-module-setuptools
BuildRequires: python3-module-mock python3-module-fasteners python3-module-flask
BuildRequires: python3(sqlalchemy)
BuildRequires: python3-module-pytest
%endif

%setup_python_module %oname
%add_python_req_skip google webapp2

%add_python_req_skip google.appengine.api google.appengine.ext google.appengine.ext.webapp.util
%if_with python3
%add_python3_req_skip google.appengine.api google.appengine.ext google.appengine.ext.webapp.util
%endif

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

%package -n python-module-django-%oname
Summary:        Django extension
Group: Development/Python
PreReq: %name = %version-%release

%description -n python-module-django-%oname
OAuth 2.0 utilities for Django.

Utilities for using OAuth 2.0 in conjunction with
the Django datastore.

%package flask
Summary: Flask extension
Group: Development/Python
PreReq: %name = %version-%release

%description flask
Provides a Flask extension that makes using OAuth2 web server flow easier.
The extension includes views that handle the entire auth flow and a
``@required`` decorator to automatically ensure that user credentials are
available.

%package gce
Summary: GCE extension
Group: Development/Python
PreReq: %name = %version-%release

%description gce
Utilities for Google Compute Engine

Utilities for making it easier to use OAuth 2.0 on Google Compute Engine.

%if_with python3
%package -n python3-module-%oname
Summary: OAuth 2.0 client library
Group: Development/Python3
%add_python3_req_skip google webapp2

%description -n python3-module-%oname
The oauth2client is a client library for OAuth 2.0.

%package -n python3-module-django-%oname
Summary:        Django extension
Group: Development/Python3
PreReq: python3-module-%oname = %version-%release

%description -n python3-module-django-%oname
OAuth 2.0 utilities for Django.

Utilities for using OAuth 2.0 in conjunction with
the Django datastore.

%package -n python3-module-%oname-flask
Summary: Flask extension
Group: Development/Python3
PreReq: python3-module-%oname = %version-%release

%description -n python3-module-%oname-flask
Provides a Flask extension that makes using OAuth2 web server flow easier.
The extension includes views that handle the entire auth flow and a
``@required`` decorator to automatically ensure that user credentials are
available.

%package -n python3-module-%oname-gce
Summary: GCE extension
Group: Development/Python3
PreReq: python3-module-%oname = %version-%release

%description -n python3-module-%oname-gce
Utilities for Google Compute Engine

Utilities for making it easier to use OAuth 2.0 on Google Compute Engine.

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
#%make -C docs pickle
#%make -C docs html
#cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
rm -rf tests/contrib/{django_util,appengine}
py.test
%if_with python3
pushd ../python3
rm -rf tests/contrib/{django_util,appengine}
py.test3
popd
%endif

%files
%doc *.md
%python_sitelibdir/*
#%exclude %python_sitelibdir/*/pickle

%exclude %python_sitelibdir/oauth2client/contrib/flask*
%exclude %python_sitelibdir/oauth2client/contrib/django*
%exclude %python_sitelibdir/oauth2client/contrib/gce*

#%files pickles
#%python_sitelibdir/*/pickle

#%files docs
#%doc docs/_build/html/*

%files flask
%python_sitelibdir/oauth2client/contrib/flask*

%files -n python-module-django-%oname
%python_sitelibdir/oauth2client/contrib/django*

%files gce
%python_sitelibdir/oauth2client/contrib/gce*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/oauth2client/contrib/flask*
%exclude %python3_sitelibdir/oauth2client/contrib/django*
%exclude %python3_sitelibdir/oauth2client/contrib/gce*

%files -n python3-module-%oname-flask
%python3_sitelibdir/oauth2client/contrib/flask*

%files -n python3-module-django-%oname
%python3_sitelibdir/oauth2client/contrib/django*

%files -n python3-module-%oname-gce
%python3_sitelibdir/oauth2client/contrib/gce*

%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.1.2-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.1.2-alt2
- Fixed build.

* Fri Aug 04 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.1.2-alt1
- Updated to upstream release 4.1.2.

* Wed Apr 13 2016 Alexey Shabalin <shaba@altlinux.ru> 1.5.2-alt1
- 1.5.2
- split flask, django, gce packages

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.4.12-alt2.git20150814.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 03 2016 Sergey Alembekov <rt@altlinux.ru> 1.4.12-alt2.git20150814
- cleanup buildreq

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

