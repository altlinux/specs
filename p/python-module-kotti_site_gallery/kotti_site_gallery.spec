%define oname kotti_site_gallery
Name: python-module-%oname
Version: 0.3.0
Release: alt1.dev.git20150121
Summary: Site gallery for Kotti sites
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/kotti_site_gallery/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Kotti/kotti_site_gallery.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-kotti-tests
BuildPreReq: python-module-minify python-module-fanstatic
BuildPreReq: python-module-pyramid python-module-SQLAlchemy

%py_provides %oname
%py_requires kotti fanstatic pyramid sqlalchemy

%description
This is an extension to Kotti that allows to add a site gallery to your
site.

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

%changelog
* Fri Feb 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.dev.git20150121
- Initial build for Sisyphus

