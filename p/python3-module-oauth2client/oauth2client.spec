%define oname oauth2client

Name: python3-module-%oname
Version: 4.1.3
Release: alt5

Summary: OAuth 2.0 client library

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/oauth2client/

# https://github.com/google/oauth2client.git
# Source-url: %__pypi_url %oname
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar
Patch1: %oname-%version-gentoo-py38.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-sphinx

BuildRequires: python3-module-httplib2 python3-module-keyring python3-module-pyasn1-modules python3-module-rsa
BuildRequires: python3-module-mock python3-module-fasteners python3-module-flask
BuildRequires: python3(sqlalchemy)
BuildRequires: python3-module-pytest
BuildRequires: python3(Crypto)

%add_python3_req_skip google.appengine.api google.appengine.ext google.appengine.ext.webapp.util
%add_python3_req_skip google webapp2

%description
The oauth2client is a client library for OAuth 2.0.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
The oauth2client is a client library for OAuth 2.0.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation

%description docs
The oauth2client is a client library for OAuth 2.0.

This package contains documentation for %oname.

%package -n python3-module-django-%oname
Summary:        Django extension
Group: Development/Python3
PreReq: %name = %EVR

%description -n python3-module-django-%oname
OAuth 2.0 utilities for Django.

Utilities for using OAuth 2.0 in conjunction with
the Django datastore.

%package flask
Summary: Flask extension
Group: Development/Python3
PreReq: %name = %EVR

%description flask
Provides a Flask extension that makes using OAuth2 web server flow easier.
The extension includes views that handle the entire auth flow and a
``@required`` decorator to automatically ensure that user credentials are
available.

%package gce
Summary: GCE extension
Group: Development/Python3
PreReq: %name = %EVR

%description gce
Utilities for Google Compute Engine

Utilities for making it easier to use OAuth 2.0 on Google Compute Engine.

%prep
%setup
%patch1 -p1

%prepare_sphinx3 .
ln -s ../objects.inv docs/

%build
%python3_build_debug

%install
%python3_install
%python3_prune

%check
rm -rf tests/contrib/{django_util,appengine}
py.test3 || :

%files
%doc *.md
%python3_sitelibdir/*
#%exclude %python_sitelibdir/*/pickle

%exclude %python3_sitelibdir/oauth2client/contrib/flask*
%exclude %python3_sitelibdir/oauth2client/contrib/django*
%exclude %python3_sitelibdir/oauth2client/contrib/gce*

%files flask
%python3_sitelibdir/oauth2client/contrib/flask*

%files -n python3-module-django-%oname
%python3_sitelibdir/oauth2client/contrib/django*

%files gce
%python3_sitelibdir/oauth2client/contrib/gce*

%changelog
* Tue Aug 10 2021 Grigory Ustinov <grenka@altlinux.org> 4.1.3-alt5
- Fixed BuildRequires.
- Fixed license tag.

* Sat Nov 07 2020 Vitaly Lipatov <lav@altlinux.ru> 4.1.3-alt4
- build python3 package separately
- disable tests due new pycryptodom

* Thu Sep 10 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 4.1.3-alt3
- Stopped packaging python-module-django-oauth2client.

* Mon Sep 07 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 4.1.3-alt2
- Added fixes for python-3.8.

* Thu Sep 13 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.1.3-alt1
- Updated to upstream version 4.1.3.

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

