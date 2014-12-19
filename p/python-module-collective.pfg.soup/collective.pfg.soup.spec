%define mname collective
%define oname %mname.pfg.soup
Name: python-module-%oname
Version: 1.7
Release: alt1.dev0.git20141216
Summary: PloneFormGen Adapter: store, show/search, edit, csv-export, based on souper.soup
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.pfg.soup/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.pfg.soup.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Plone python-module-openid
BuildPreReq: python-module-Products.PloneFormGen
BuildPreReq: python-module-collective.js.datatables
BuildPreReq: python-module-souper.plone
BuildPreReq: python-module-bda.calendar.base
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-zope.app.component
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-repoze.catalog

%py_provides %oname
Requires: python-module-%mname.pfg = %EVR
Requires: python-module-Zope2
%py_requires Plone Products.PloneFormGen collective.js.datatables
%py_requires souper.plone bda.calendar.base souper.soup plone.memoize
%py_requires souper.interfaces Products.ATContentTypes Products.CMFCore
%py_requires Products.Archetypes zope.component zope.app.component
%py_requires zope.interface zope.i18nmessageid repoze.catalog

%description
This PloneFormGen Storage Adapter saves and index form-data in so called
soup. A soup is an unstructured flat storage containing records with
attributes (form-data). Attributes are indexed in an repoze.catalog.
Thus complex queries on the data are possible.

It ships with an full-featured table view based on jquery.datatables.
Datatables server-side processing enables to have large datasets
processed. It provides a search over all columns and by single columns.
Each column can be sorted.

%package -n python-module-%mname.pfg
Summary: Core files of %mname.pfg
Group: Development/Python
%py_provides %mname.pfg
%py_requires %mname

%description -n python-module-%mname.pfg
Core files of %mname.pfg.

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
%doc *.rst
%python_sitelibdir/%mname/pfg/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/pfg/__init__.py*

%files -n python-module-%mname.pfg
%dir %python_sitelibdir/%mname/pfg
%python_sitelibdir/%mname/pfg/__init__.py*

%changelog
* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt1.dev0.git20141216
- Initial build for Sisyphus

