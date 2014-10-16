%define oname Plone
Name: python-module-%oname
Version: 5.0a3
Release: alt1.dev0.git20140718
Summary: The Plone Content Management System
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/Plone/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/Plone.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.CMFPlacefulWorkflow
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-plone.app.caching
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-plone.app.iterate
BuildPreReq: python-module-plone.app.openid
BuildPreReq: python-module-plone.app.upgrade
BuildPreReq: python-module-openid python-module-unittest2

%py_provides %oname
%py_requires Products.Archetypes Products.ATContentTypes
%py_requires Products.CMFPlacefulWorkflow Products.CMFPlone
%py_requires plone.app.caching plone.app.dexterity plone.app.iterate
%py_requires plone.app.openid plone.app.upgrade

%description
Plone is a user friendly Content Management System running on top of
Python, Zope and the CMF.

It benefits from all features of Zope/CMF such as: RDBMS integration,
Python extensions, Object Oriented Database, Web configurable workflow,
pluggable membership and authentication, Undos, Form validation, amongst
many many other features. Available protocols: FTP, XMLRPC, HTTP and
WEBDAV Turn it into a distributed application system by installing ZEO.

Plone shares some of the qualities of Livelink, Interwoven and
Documentum. It aims to be the open source out-of-the-box publishing
system.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.rst docs/*
%python_sitelibdir/*

%changelog
* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0a3-alt1.dev0.git20140718
- Initial build for Sisyphus

