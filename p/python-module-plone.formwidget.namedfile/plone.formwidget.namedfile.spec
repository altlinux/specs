%define mname plone.formwidget
%define oname %mname.namedfile
Name: python-module-%oname
Version: 1.0.12
Release: alt2.dev0.git20141008
Summary: z3c.form widgets for file and image upload/download
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.formwidget.namedfile/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.formwidget.namedfile.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.namedfile
BuildPreReq: python-module-z3c.form-tests
BuildPreReq: python-module-plone.z3cform

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires plone.namedfile z3c.form plone.z3cform

%description
This package provides z3c.form widgets for file and image
upload/download, with the option of keeping the existing file or
replacing it with a new one.

The widgets will act as the default for any NamedFile, NamedBlobFile,
NamedImage or NamedBlobImage field from the plone.namedfile package.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
Requires: python-module-z3c.form-tests

%description tests
This package provides z3c.form widgets for file and image
upload/download, with the option of keeping the existing file or
replacing it with a new one.

The widgets will act as the default for any NamedFile, NamedBlobFile,
NamedImage or NamedBlobImage field from the plone.namedfile package.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname
%py_requires plone

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

install -p -m644 plone/formwidget/__init__.py \
	%buildroot%python_sitelibdir/plone/formwidget/

%check
python setup.py test

%files
%doc *.txt docs/*
%python_sitelibdir/plone/formwidget/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/formwidget/*/tests.*
%exclude %python_sitelibdir/plone/formwidget/__init__.py*

%files tests
%python_sitelibdir/plone/formwidget/*/tests.*

%files -n python-module-%mname
%dir %python_sitelibdir/plone/formwidget
%python_sitelibdir/plone/formwidget/__init__.py*

%changelog
* Thu Oct 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.12-alt2.dev0.git20141008
- Added necessary provides

* Mon Oct 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.12-alt1.dev0.git20141008
- Initial build for Sisyphus

