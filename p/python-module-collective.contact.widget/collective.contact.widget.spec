%define mname collective.contact
%define oname %mname.widget
Name: python-module-%oname
Version: 1.2.3
Release: alt1.dev0.git20140925
Summary: Contact widget
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.contact.widget/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.contact.widget.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-five.grok
BuildPreReq: python-module-plone.formwidget.contenttree
BuildPreReq: python-module-plone.formwidget.autocomplete
BuildPreReq: python-module-z3c.relationfield
BuildPreReq: python-module-ecreall.helpers.testing
BuildPreReq: python-module-plone.app.testing

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires five.grok plone.formwidget.contenttree
%py_requires plone.formwidget.autocomplete z3c.relationfield

%description
Contact widget. You can add contact fields to your schema.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_requires collective

%description -n python-module-%mname
Core files of %mname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 src/collective/contact/__init__.py \
	%buildroot%python_sitelibdir/collective/contact/

%check
python setup.py test

%files
%doc *.rst docs/*
%python_sitelibdir/collective/contact/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/contact/__init__.py*

%files -n python-module-%mname
%dir %python_sitelibdir/collective/contact
%python_sitelibdir/collective/contact/__init__.py*

%changelog
* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt1.dev0.git20140925
- Initial build for Sisyphus

