%define _unpackaged_files_terminate_build 1
%define pypi_nname flask-appbuilder
%define pypi_name Flask-AppBuilder
%define mod_name flask_appbuilder

# off because need internet, LDAP, and DB server.
%def_without check

Name: python3-module-%pypi_nname
Version: 5.2.1
Release: alt1
Summary: Simple and rapid application development framework, built on top of Flask
License: BSD-3-Clause
Group: Development/Python
Url: https://pypi.org/project/Flask-AppBuilder/
Vcs: https://github.com/dpgaspar/Flask-AppBuilder
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-apispec
BuildRequires: python3-module-flask-jwt-extended
BuildRequires: python3-module-marshmallow-sqlalchemy
BuildRequires: python3-module-prison
BuildRequires: python3-module-flask-sqlalchemy
BuildRequires: python3-module-wtforms
BuildRequires: python3-module-flask-babel
BuildRequires: python3-module-dateutil
BuildRequires: python3-module-SQLAlchemy-Utils
Buildrequires: python3-module-flask-wtf
Buildrequires: python3-module-flask-limiter
Buildrequires: python3-module-flask-login
Buildrequires: python3-module-jsonschema
Buildrequires: python3-module-hiro
Buildrequires: python3-module-ldap
Buildrequires: python3-module-authlib
Buildrequires: python3-module-authlib-flask
Buildrequires: python3-module-parameterized
Buildrequires: python3-module-requests
%endif

%description
Flask-AppBuilder is a simple and rapid application development framework,
built on top of Flask. It includes integrated security, SQLAlchemy ORM,
and many built-in functionalities for building web applications.

%prep
%setup 
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.rst LICENSE
%python3_sitelibdir/%mod_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue May 19 2026 Alexey Rodygin <alehandro@altlinux.org> 5.2.1-alt1
- Updated to new version 5.2.1.

* Tue Mar 24 2026 Alexey Rodygin <alehandro@altlinux.org> 5.2.0-alt1
- Updated to new version v5.2.0.

* Tue Jan 13 2026 alehandro <alehandro@altlinux.org> 5.0.1-alt1
- Initial build for ALT Linux.
