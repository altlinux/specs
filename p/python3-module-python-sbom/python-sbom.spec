%define _unpackaged_files_terminate_build 1
%define pypi_name python-sbom
%define mod_name python_sbom

%def_with check

Name: python3-module-%pypi_name
Version: 0.3.1
Release: alt1
Summary: SBOMs for Python distributions: write PEP 770 CycloneDX SBOMs into wheels
License: MIT and Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/python-sbom
Vcs: https://github.com/tox-dev/python-sbom
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch
%pyproject_configure_pypi_package
BuildRequires(pre): rpm-build-pyproject >= 0.3.0
%pyproject_configure_pypi_subpackage validate
%pyproject_configure_pypi_subpackage hatch
%pyproject_configure_pypi_subpackage pdm
%pyproject_configure_pypi_subpackage setuptools

%description
%summary.

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_setup_deps

%build
%pyproject_build

%install
%pyproject_install

%check
# see tox.toml
%pyproject_run_pytest -vra tests --ignore tests/examples

%files
%_bindir/python-sbom
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Nov 18 2026 Stanislav Levin <slev@altlinux.org> 0.3.1-alt1
- Initial build for sisyphus.
