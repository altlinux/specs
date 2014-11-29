%define mname collective
%define oname %mname.transmogrifier
Name: python-module-%oname
Version: 1.5
Release: alt1.git20130407
Summary: A configurable pipeline, aimed at transforming content for import and export
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.transmogrifier/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mjpieters/collective.transmogrifier.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-zope.app.pagetemplate
BuildPreReq: python-module-zope.pagetemplate
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Products.CMFCore Products.CMFPlone zope.component
%py_requires zope.interface zope.app.pagetemplate zope.pagetemplate
%py_requires zope.annotation zope.configuration

%description
Transmogrifier provides support for building pipelines that turn one
thing into another. Specifically, transmogrifier pipelines are used to
convert and import legacy content into a Plone site. It provides the
tools to construct pipelines from multiple sections, where each section
processes the data flowing through the pipe.

A "transmogrifier pipeline" refers to a description of a set of pipe
sections, slotted together in a set order. The stated goal is for these
sections to transform data and ultimately add content to a Plone site
based on this data. Sections deal with tasks such as sourcing the data
(from textfiles, databases, etc.) and characterset conversion, through
to determining portal type, location and workflow state.

Note that a transmogrifier pipeline can be used to process any number of
things, and is not specific to Plone content import. However, it's
original intent is to provide a pluggable way to import legacy content.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing

%description tests
Transmogrifier provides support for building pipelines that turn one
thing into another. Specifically, transmogrifier pipelines are used to
convert and import legacy content into a Plone site. It provides the
tools to construct pipelines from multiple sections, where each section
processes the data flowing through the pipe.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
rm -fR build
py.test

%files
%doc *.rst docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests
%exclude %python_sitelibdir/%mname/*/*/tests.*

%files tests
%python_sitelibdir/%mname/*/tests
%python_sitelibdir/%mname/*/*/tests.*

%changelog
* Sat Nov 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1.git20130407
- Initial build for Sisyphus

