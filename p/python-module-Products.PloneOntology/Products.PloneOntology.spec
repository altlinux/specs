%define oname Products.PloneOntology
Name: python-module-%oname
Version: 1.0.0
Release: alt1.git20120907
Summary: Classify content with keywords from an (expandable) ontology
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.PloneOntology/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/Products.PloneOntology.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.Relations python-module-nose
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.security-tests
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.Relations

%description
Classify content with keywords from an (expandable) ontology.

Features:

* related content is displayed in a portlet, even if not classified with
  the same keyword (but with a related one...)
* import and export of keyword-ontologies via W3C's Web Ontology
  Language (OWL)
* Graphviz support visualizes the keywords and their relations within an
  ontology
* adding keywords and relations to an ontology through a special
  workflow
* javascript sarissa support for easier classification or keyword adding

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.component.testing zope.security.testing
%py_requires Products.PloneTestCase

%description tests
Classify content with keywords from an (expandable) ontology.

Features:

* related content is displayed in a portlet, even if not classified with
  the same keyword (but with a related one...)
* import and export of keyword-ontologies via W3C's Web Ontology
  Language (OWL)
* Graphviz support visualizes the keywords and their relations within an
  ontology
* adding keywords and relations to an ontology through a special
  workflow
* javascript sarissa support for easier classification or keyword adding

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

%files
%doc *.txt docs/*
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Mon Oct 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20120907
- Initial build for Sisyphus

