%define _unpackaged_files_terminate_build 1
%define oname WebGrid
Name: python-module-%oname
Version: 0.1.31
Release: alt1
Summary: A library for rendering HTML tables and Excel files from SQLAlchemy models
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/WebGrid/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/72/20/ab20cbb0ff098d5ea7854bc779fbd63d7b1521a7227c858011a745593ddc/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-BlazeUtils python-module-FormEncode
BuildPreReq: python-module-jinja2 python-module-SQLAlchemy
BuildPreReq: python-module-webhelpers python-module-dateutil
BuildPreReq: python-module-werkzeug python-module-BlazeWeb-tests
BuildPreReq: python-module-SQLAlchemyBWC python-module-mock
BuildPreReq: python-module-nose python-module-flask
BuildPreReq: python-module-nose python-module-Flask-Bootstrap
BuildPreReq: python-module-flask_sqlalchemy python-module-Flask-WebTest
BuildPreReq: python-module-wrapt python-module-xlrd
BuildPreReq: python-module-xlwt python-module-PasteDeploy

%py_provides webgrid
%py_requires formencode blazeutils jinja2 sqlalchemy webhelpers wrapt
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
%setup -q -n %{oname}-%{version}

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
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.31-alt1
- automated PyPI update

* Mon Jan 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.12-alt1
- Initial build for Sisyphus

