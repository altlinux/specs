%define _unpackaged_files_terminate_build 1
%define pypi_name Flask-Pydantic
%define pypi_nname flask-pydantic
%define mod_name flask_pydantic

%def_with check

Name: python3-module-%pypi_nname
Version: 0.13.2
Release: alt1

Summary: Flask extension for integration with the awesome pydantic package
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/Flask-Pydantic/
Vcs: https://github.com/pallets-eco/flask-pydantic

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
# well-known PyPI name
Provides: python3-module-%pypi_name = %EVR
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
BuildRequires: python3-module-flask+async
%endif

%description
Flask extension for integration of the awesome pydantic package
with Flask.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements/test.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc CHANGES.md LICENSE.txt README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Sep 25 2025 Anton Zhukharev <ancieg@altlinux.org> 0.13.2-alt1
- Packaged for ALT Sisyphus.
