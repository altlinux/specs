%define _unpackaged_files_terminate_build 1
%define pypi_name marshmallow-sqlalchemy
%define mod_name marshmallow_sqlalchemy

%def_with check

Name: python3-module-%pypi_name
Version: 1.5.0
Release: alt1
Summary: SQLAlchemy integration with the marshmallow (de)serialization library
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/marshmallow-sqlalchemy/
Vcs: https://github.com/marshmallow-code/marshmallow-sqlalchemy
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit-core

%if_with check
BuildRequires: python3-module-pytest-lazy-fixtures
BuildRequires: python3-module-marshmallow
BuildRequires: python3-module-sqlalchemy
%endif

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.rst LICENSE docs/
%python3_sitelibdir/%mod_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue May 26 2026 Alexey Rodygin <alehandro@altlinux.org> 1.5.0-alt1
- Updated to new version 1.5.0.

* Tue Jan 13 2026 Alexey Rodygin <alehandro@altlinux.org> 1.4.2-alt1
- Initial build for ALT Linux
