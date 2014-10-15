%define oname pas.plugins.velruse

Name: python-module-%oname
Version: 0.1.0
Release: alt1.a2.dev0.git20140514
Summary: PAS plugin for Plone. Allow users to login using social networks through Velruse
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/pas.plugins.velruse/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/RedTurtle/pas.plugins.velruse.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-modules-json python-module-requests
BuildPreReq: python-module-lxml python-module-Products.PlonePAS
BuildPreReq: python-module-plone.app.registry
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-plone.app.z3cform
BuildPreReq: python-module-Products.PluggableAuthService
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Zope2-tests
BuildPreReq: python-module-markdown
BuildPreReq: python-module-unittest2

%py_provides %oname
Requires: python-module-pas.plugins = %EVR
%py_requires plone.app.registry z3c.form plone.app.z3cform
%py_requires Products.PluggableAuthService Products.PlonePAS
%py_requires Products.CMFPlone

%description
A PAS plugin for Plone that authenticate users from social networks
through the use of Velruse.

%package -n python-module-pas.plugins
Summary: Core files of pas.plugins
Group: Development/Python
Requires: python-module-pas = %EVR

%description -n python-module-pas.plugins
Core files of pas.plugins.

%package -n python-module-pas
Summary: Core files of pas
Group: Development/Python

%description -n python-module-pas
Core files of pas.

%prep
%setup

%build
%python_build_debug

%install
%python_install
install -p -m644 pas/__init__.py %buildroot%python_sitelibdir/pas/
install -p -m644 pas/plugins/__init__.py \
	%buildroot%python_sitelibdir/pas/plugins/

%check
python setup.py test

%files
%doc *.rst docs/*
%python_sitelibdir/pas/plugins/velruse
%python_sitelibdir/*.egg-info

%files -n python-module-pas.plugins
%dir %python_sitelibdir/pas/plugins
%python_sitelibdir/pas/plugins/__init__.py*

%files -n python-module-pas
%dir %python_sitelibdir/pas
%python_sitelibdir/pas/__init__.py*

%changelog
* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.a2.dev0.git20140514
- Initial build for Sisyphus

