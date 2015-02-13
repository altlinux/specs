%define oname kotti_settings
Name: python-module-%oname
Version: 0.3
Release: alt1.dev.git20150124
Summary: Settings configuration for Kotti
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/kotti_settings/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/j23d/kotti_settings.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-kotti
BuildPreReq: python-module-wsgi_intercept python-module-pyramid
BuildPreReq: python-module-pyramid_deform python-module-SQLAlchemy
BuildPreReq: python-module-zope.sqlalchemy python-module-waitress
BuildPreReq: python-module-pyramid_zcml python-module-pyramid_tm
BuildPreReq: python-module-pyramid_debugtoolbar
BuildPreReq: python-module-pyramid_chameleon python-module-kotti_tinymce
BuildPreReq: python-module-pyramid_mako

%py_provides %oname
%py_requires kotti pyramid pyramid_deform

%description
Add a settings configuration to your Kotti site.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Add a settings configuration to your Kotti site.

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
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*

%changelog
* Fri Feb 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.dev.git20150124
- Initial build for Sisyphus

