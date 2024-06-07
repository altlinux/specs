%define _unpackaged_files_terminate_build 1
%define pypi_name pipx
%define mod_name %pypi_name

# tests require running pypi-server
%def_without check

Name: python3-module-%pypi_name
Version: 1.6.0
Release: alt1

Summary: Install and Run Python Applications in Isolated Environments
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pipx/
Vcs: https://github.com/pypa/pipx

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
# pyproject-installer can't work with `nox'.
BuildRequires: python3-module-pytest
%endif

%description
%summary.

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE README.md CHANGELOG.md
%_bindir/%pypi_name
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Jun 07 2024 Ajrat Makhmutov <rauty@altlinux.org> 1.6.0-alt1
- Updated to 1.6.0.

* Mon Apr 01 2024 Anton Zhukharev <ancieg@altlinux.org> 1.5.0-alt1
- Updated to 1.5.0.

* Wed Feb 07 2024 Anton Zhukharev <ancieg@altlinux.org> 1.4.3-alt1
- Updated to 1.4.3.

* Tue Jan 09 2024 Anton Zhukharev <ancieg@altlinux.org> 1.4.1-alt1
- Updated to 1.4.1.

* Fri Dec 29 2023 Anton Zhukharev <ancieg@altlinux.org> 1.4.0-alt1
- Updated to 1.4.0.

* Thu Dec 07 2023 Anton Zhukharev <ancieg@altlinux.org> 1.3.3-alt1
- Updated to 1.3.3.

* Thu Nov 23 2023 Anton Zhukharev <ancieg@altlinux.org> 1.2.1-alt1
- Built for ALT Sisyphus.

