%define mname archetypes
%define oname %mname.schemaextender
Name: python-module-%oname
Version: 2.1.5
Release: alt1.dev0.git20140908
Summary: Dynamically extend Archetypes schemas with named adapters
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/archetypes.schemaextender/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/archetypes.schemaextender.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-plone.uuid

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires plone.uuid

%description
This package allows you to modify an Archetypes schema, using simple
adapters. This can be used to add new fields, reorder fields and
fieldsets or make other changes.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package allows you to modify an Archetypes schema, using simple
adapters. This can be used to add new fields, reorder fields and
fieldsets or make other changes.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files for %mname
Group: Development/Python

%description -n python-module-%mname
Core files for %mname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 %mname/__init__.py \
	%buildroot%python_sitelibdir/%mname/

%check
python setup.py test

%files
%doc *.txt docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests
%exclude %python_sitelibdir/%mname/__init__.py*

%files tests
%python_sitelibdir/%mname/*/tests

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%changelog
* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.5-alt1.dev0.git20140908
- Initial build for Sisyphus

