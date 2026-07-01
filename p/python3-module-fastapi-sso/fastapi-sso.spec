%global _unpackaged_files_terminate_build 1
%define pypi_name fastapi-sso

%def_with check

Name: python3-module-fastapi-sso
Version: 0.21.1
Release: alt1

Summary: FastAPI plugin to enable SSO to most common providers
Group: Development/Python3
License: MIT
BuildArch: noarch
Url: https://pypi.org/project/fastapi-sso/
VCS: https://github.com/tomasvotava/fastapi-sso
AutoReq: yes, nopython3

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_runtimedeps_metadata

# Require email-validator for pydantic[email]
Requires: python3-module-email-validator

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
BuildRequires: python3-module-email-validator
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-asyncio
%endif

%description
FastAPI plugin to enable SSO to most common providers (such as Facebook
login, Google login and login via Microsoft Office 365 Account)

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_poetry dev
%endif

# Use default tox.ini instead of upstream one
rm -f ./tox.ini

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%python3_sitelibdir/fastapi_sso/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Jun 23 2026 Egor Ignatov <egori@altlinux.org> 0.21.1-alt1
- New version 0.21.1.

* Thu Apr 30 2026 Egor Ignatov <egori@altlinux.org> 0.21.0-alt1
- Initial build for ALT Linux.
