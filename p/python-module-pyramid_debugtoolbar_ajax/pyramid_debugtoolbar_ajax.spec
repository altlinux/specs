%define oname pyramid_debugtoolbar_ajax
Name: python-module-%oname
Version: 0.0.3
Release: alt1.git20141025
Summary: Ajax support for pyramid_debugtoolbar
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pyramid_debugtoolbar_ajax/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jvanasco/pyramid_debugtoolbar_ajax.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-nose
BuildPreReq: python-module-pyramid_debugtoolbar-tests
BuildPreReq: python-module-repoze.lru
BuildPreReq: python-module-Pygments
BuildPreReq: python-module-pyramid_mako
BuildPreReq: python-module-mako
BuildPreReq: python-module-PasteDeploy
BuildPreReq: python-module-zope.deprecation
BuildPreReq: python-module-markupsafe
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-pyramid-tests

%py_provides %oname
%py_requires pyramid_debugtoolbar
# for tests:
%py_requires repoze.lru paste.deploy zope.deprecation
%py_requires pyramid_debugtoolbar.tests zope.component
%py_requires pyramid.config.testing

%description
This adds an "Ajax" panel to the pyramid_debugtoolbar

This panel contains a button to replay the request in a new window --
allowing you to spawn a debugger window for errors encountered on
background ajax requests.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
nosetests

%files
%doc *.txt *.md
%python_sitelibdir/*

%changelog
* Sun Oct 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt1.git20141025
- Initial build for Sisyphus

