%define _unpackaged_files_terminate_build 1
%define pypi_name Flask-JWT-Extended
%define pypi_nname flask-jwt-extended
%define mod_name flask_jwt_extended

%def_with check

Name: python3-module-%pypi_nname
Version: 4.7.4
Release: alt1
Summary: Support for using JSON Web Tokens (JWT) to Flask for protecting routes
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/Flask-JWT-Extended
Vcs: https://github.com/vimalloc/flask-jwt-extended
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-black
BuildRequires: python3-module-cryptography
BuildRequires: python3-module-flask
BuildRequires: python3-module-pre-commit
BuildRequires: python3-module-jwt
BuildRequires: python3-module-tox
BuildRequires: python3-module-dateutil
%endif

%description
Flask-JWT-Extended not only adds support for using JSON Web Tokens (JWT) to 
Flask for protecting routes, but also many helpful (and optional) features built 
in to make working with JSON Web Tokens easier.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.md LICENSE docs/
%python3_sitelibdir/%mod_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue May 19 2026 Alexey Rodygin <alehandro@altlinux.org> 4.7.4-alt1
- Updated to new version 4.7.4.

* Tue Jan 13 2026 Alexey Rodygin <alehandro@altlinux.org> 4.7.1-alt1
- Initial build for ALT Linux
