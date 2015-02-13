%define oname kotti_link
Name: python-module-%oname
Version: 0.2
Release: alt1.dev0.git20150213
Summary: Redirects for your Kotti site
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/kotti_link/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/j23d/kotti_link.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-kotti python-module-fanstatic
BuildPreReq: python-module-pyramid-tests python-module-SQLAlchemy
BuildPreReq: python-module-zope.sqlalchemy python-module-waitress
BuildPreReq: python-module-pyramid_zcml python-module-pyramid_tm
BuildPreReq: python-module-pyramid_debugtoolbar
BuildPreReq: python-module-pyramid_chameleon python-module-kotti_tinymce
BuildPreReq: python-module-pyramid_mako

%py_provides %oname
%py_requires kotti js.jquery fanstatic pyramid sqlalchemy
# for tests:
%py_requires pyramid.config.testing

%description
Link content type for Kotti.

%prep
%setup

%build
%python_build_debug

%install
%python_install

pushd %oname
cp -fR locale static templates %buildroot%python_sitelibdir/%oname/
popd

%check
python setup.py test

%files
%doc *.txt *.rst
%python_sitelibdir/*

%changelog
* Fri Feb 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.dev0.git20150213
- Initial build for Sisyphus

