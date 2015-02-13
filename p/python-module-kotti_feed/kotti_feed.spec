%define oname kotti_feed
Name: python-module-%oname
Version: 0.2
Release: alt1.git20150124
Summary: Add RSS feed generation to your Kotti site
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/kotti_feed/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/teixas/kotti_feed.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-kotti-tests
BuildPreReq: python-module-PyRSS2Gen python-module-webtest
BuildPreReq: python-module-pytest-cov python-module-zope.testbrowser

%py_provides %oname
%py_requires kotti PyRSS2Gen pyramid

%description
This is an extension to the Kotti CMS that allows you to generate RSS
2.0 feeds from your Kotti site.

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
* Fri Feb 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20150124
- Initial build for Sisyphus

