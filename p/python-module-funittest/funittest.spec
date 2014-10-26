%define oname funittest
Name: python-module-%oname
Version: 1.0
Release: alt1.beta2.svn20100131
Summary: Making it easy to go from use case to functional test
License: GPL
Group: Development/Python
Url: http://www.coactivate.org/projects/funittest/project-home
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://svn.plone.org/svn/collective/funittest/funittest/trunk/
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-nose
BuildPreReq: python-module-martian python-module-simplejson
BuildPreReq: python-module-transaction
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.pagetemplate
BuildPreReq: python-module-docutils python-module-configobj
BuildPreReq: python-module-selenium python-module-lxml

%py_provides %oname
%py_requires zope.interface zope.component zope.pagetemplate

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
%doc *.txt doc/*
%_bindir/*
%python_sitelibdir/*

%changelog
* Sun Oct 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.beta2.svn20100131
- Initial build for Sisyphus

