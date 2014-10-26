%define oname funittest.plone
Name: python-module-%oname
Version: 1.0
Release: alt1.beta1.svn20100110
Summary: Plone test using funittest
License: GPL
Group: Development/Python
Url: http://www.coactivate.org/projects/funittest/project-home
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://svn.plone.org/svn/collective/funittest/funittest.plone/trunk/
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-funittest
BuildPreReq: python-module-simplejson
BuildPreReq: python-module-transaction

%py_provides %oname
%py_requires funittest

%description
Funittest is a functional test tool based on Selenium Remote Control.
It proposes a way of creating a model stack for different levels of
abstraction, helping the developer sketch out their functional tests in
a modular and reusable way, as can be seen from the existing models for
Plone and Silva, that can be integrated or taken as an example for your
custom tests.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%python_sitelibdir/*

%changelog
* Sun Oct 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.beta1.svn20100110
- Initial build for Sisyphus

