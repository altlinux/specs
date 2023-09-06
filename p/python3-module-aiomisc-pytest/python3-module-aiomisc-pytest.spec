%define _unpackaged_files_terminate_build 1
%define pypi_name aiomisc-pytest
%define mod_name aiomisc_pytest

# tests are broken
%def_without check

Name: python3-module-%pypi_name
Version: 1.1.1
Release: alt1

Summary: Pytest plugin for aiomisc
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/aiomisc-pytest/
Vcs: https://github.com/aiokitchen/aiomisc-pytest

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%py3_provides %pypi_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
This package contains a plugin for pytest.

%prep
%setup

# fix version in pyproject.toml
sed -i '/version/s/= .*$/= "%version"/' pyproject.toml

%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%if_with check
%pyproject_deps_resync_check_poetry dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc COPYING README.md
%python3_sitelibdir/%mod_name.py
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%python3_sitelibdir/__pycache__/%mod_name.*.pyc

%changelog
* Wed Sep 06 2023 Anton Zhukharev <ancieg@altlinux.org> 1.1.1-alt1
- Updated to 1.1.1.

* Thu May 11 2023 Anton Zhukharev <ancieg@altlinux.org> 1.1-alt1
- Initial build for ALT Sisyphus.

