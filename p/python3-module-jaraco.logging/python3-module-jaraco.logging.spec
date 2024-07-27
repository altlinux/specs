%define _unpackaged_files_terminate_build 1

%define pypi_name jaraco.logging
%define ns_name jaraco
%define mod_name logging

%def_with check

Name: python3-module-%pypi_name
Version: 3.3.0
Release: alt1

Summary: Support for Python logging facility
License: MIT
Group: Development/Python3
URL: https://github.com/jaraco/jaraco.logging
BuildArch: noarch
Source: %pypi_name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
%py3_provides %pypi_name
# mapping from PyPI name
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra testing
%endif

%description
%summary.

%prep
%setup -n %pypi_name-%version
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -Wignore

%files
%doc README.*
%dir %python3_sitelibdir/%ns_name/
%python3_sitelibdir/%ns_name/%mod_name.py
%dir %python3_sitelibdir/%ns_name/__pycache__/
%python3_sitelibdir/%ns_name/__pycache__/%mod_name.*
%python3_sitelibdir/%pypi_name-%version.dist-info/

%changelog
* Wed Jul 24 2024 Anton Vyatkin <toni@altlinux.org> 3.3.0-alt1
- Initial build for Sisyphus.
