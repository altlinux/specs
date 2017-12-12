%define _unpackaged_files_terminate_build 1
%define oname WebGrid
Name: python-module-%oname
Version: 0.1.34
Release: alt2
Summary: A library for rendering HTML tables and Excel files from SQLAlchemy models
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/WebGrid/

Source: %oname-%version.tar

BuildRequires: python-devel python-module-setuptools-tests
BuildRequires: python-module-BlazeUtils python-module-FormEncode
BuildRequires: python-module-jinja2 python-module-SQLAlchemy
BuildRequires: python-module-webhelpers2 python-module-dateutil
BuildRequires: python-module-werkzeug python-module-BlazeWeb-tests
BuildRequires: python-module-SQLAlchemyBWC python-module-mock
BuildRequires: python-module-nose python-module-flask
BuildRequires: python-module-nose python-module-Flask-Bootstrap
BuildRequires: python-module-flask_sqlalchemy python-module-Flask-WebTest
BuildRequires: python-module-wrapt python-module-xlrd
BuildRequires: python-module-xlwt python-module-PasteDeploy
BuildRequires: python2.7(arrow) python2.7(sqlalchemy_utils)

%py_provides webgrid
%py_requires formencode blazeutils jinja2 sqlalchemy webhelpers2 wrapt
%py_requires dateutil werkzeug blazeweb sqlalchemybwc flask xlwt

%description
WebGrid is a datagrid library for Flask and other Python web frameworks
designed to work with SQLAlchemy ORM entities.

Based on the configured grid, it will output an HTML table with sorting,
filtering, and paging.

It also will export the grid to Excel.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires xlrd

%description tests
WebGrid is a datagrid library for Flask and other Python web frameworks
designed to work with SQLAlchemy ORM entities.

Based on the configured grid, it will output an HTML table with sorting,
filtering, and paging.

It also will export the grid to Excel.

This package contains tests for %oname.

%prep
%setup -n %oname-%version

%build
%python_build_debug

%install
%python_install

cp -fR webgrid_ta %buildroot%python_sitelibdir/

%check
python setup.py test

%files
%doc *.rst
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%changelog
* Tue Dec 12 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.34-alt2
- Fixed build.

* Thu Oct 12 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.34-alt1
- Updated to upstream version 0.1.34.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.31-alt1
- automated PyPI update

* Mon Jan 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.12-alt1
- Initial build for Sisyphus

