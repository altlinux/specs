%define oname kotti_contactform
Name: python-module-%oname
Version: 0.6
Release: alt1.dev.git20150122
Summary: Simple contact form for Kotti sites
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/kotti_contactform/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Kotti/kotti_contactform.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-kotti-tests
BuildPreReq: python-module-httplib2 python-module-kotti_settings
BuildPreReq: python-module-pyramid-tests python-module-SQLAlchemy
BuildPreReq: python-module-zope.sqlalchemy python-module-waitress
BuildPreReq: python-module-pyramid_zcml python-module-pyramid_tm
BuildPreReq: python-module-pyramid_debugtoolbar
BuildPreReq: python-module-pyramid_chameleon python-module-kotti_tinymce
BuildPreReq: python-module-pyramid_mako python-module-wsgi_intercept
BuildPreReq: python-module-deform-tests

%py_provides %oname
%py_requires kotti httplib2 kotti_settings pyramid sqlalchemy

%description
This is an extension to Kotti that allows to add a simple contact form
to your site.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This is an extension to Kotti that allows to add a simple contact form
to your site.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%changelog
* Fri Feb 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1.dev.git20150122
- Initial build for Sisyphus

