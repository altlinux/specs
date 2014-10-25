%define mname ploneintranet
%define oname %mname.workspace
Name: python-module-%oname
Version: 1.2
Release: alt1.dev0.git20141015
Summary: A Workspace implementation for ploneintranet
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/ploneintranet.workspace/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ploneintranet/ploneintranet.workspace.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-collective.workspace
BuildPreReq: python-module-plone.api
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-plone.namedfile
BuildPreReq: python-module-Products.CMFPlacefulWorkflow
BuildPreReq: python-module-ploneintranet.invitations
BuildPreReq: python-module-zest.releaser
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.app.robotframework
BuildPreReq: python-module-sphinx-devel
BuildPreReq: python-module-openid

%py_provides %oname
%py_requires %mname collective.workspace plone.api plone.app.dexterity
%py_requires plone.namedfile Products.CMFPlacefulWorkflow
%py_requires ploneintranet.invitations zest.releaser

%description
This package provides a 'workspace' container and content workflow
working in conjunction to provide flexible levels of content access in a
Plone site.

It aims to provide a flexible team/community workspace solution, allow
teams of users to communicate and collaborate effectively within their
own area of an intranet. Plone's extensive permissions are distilled
into a set of distinct policies that control who can access a workspace,
who can join a workspace, and what users can do once they are part of a
workspace.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing plone.app.robotframework

%description tests
This package provides a 'workspace' container and content workflow
working in conjunction to provide flexible levels of content access in a
Plone site.

It aims to provide a flexible team/community workspace solution, allow
teams of users to communicate and collaborate effectively within their
own area of an intranet. Plone's extensive permissions are distilled
into a set of distinct policies that control who can access a workspace,
who can join a workspace, and what users can do once they are part of a
workspace.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
This package provides a 'workspace' container and content workflow
working in conjunction to provide flexible levels of content access in a
Plone site.

It aims to provide a flexible team/community workspace solution, allow
teams of users to communicate and collaborate effectively within their
own area of an intranet. Plone's extensive permissions are distilled
into a set of distinct policies that control who can access a workspace,
who can join a workspace, and what users can do once they are part of a
workspace.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
This package provides a 'workspace' container and content workflow
working in conjunction to provide flexible levels of content access in a
Plone site.

It aims to provide a flexible team/community workspace solution, allow
teams of users to communicate and collaborate effectively within their
own area of an intranet. Plone's extensive permissions are distilled
into a set of distinct policies that control who can access a workspace,
who can join a workspace, and what users can do once they are part of a
workspace.

This package contains documentation for %oname.

%prep
%setup

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

export PYTHONPATH=$PWD/src
pushd docs
sphinx-build -b pickle -d build/doctrees . build/pickle
sphinx-build -b html -d build/doctrees . build/html
popd

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test

%files
%doc *.txt *.rst
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%files pickles
%python_sitelibdir/%oname

%files docs
%doc docs/build/html/*

%changelog
* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.dev0.git20141015
- Initial build for Sisyphus

