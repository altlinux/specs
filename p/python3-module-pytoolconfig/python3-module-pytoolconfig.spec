%define _unpackaged_files_terminate_build 1
%define pypi_name pytoolconfig

%def_with check

Name: python3-module-%pypi_name
Version: 1.3.1
Release: alt1.1

Summary: Python tool configuration
License: LGPL-3.0
Group: Development/Python3
Vcs: https://github.com/bagel897/pytoolconfig
Url: https://pypi.org/project/pytoolconfig/

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
Requires: python3-module-platformdirs
Requires: python3-module-tabulate
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter tox-pdm
%add_pyproject_deps_check_filter sphinx-rtd-theme
%add_pyproject_deps_check_filter pytest-emoji
%add_pyproject_deps_check_filter pytest-md
%add_pyproject_deps_check_filter tox-gh
%pyproject_builddeps_metadata_extra gendocs
%pyproject_builddeps_check
BuildRequires: python3-module-tabulate
BuildRequires: python3-module-sphinx
%endif

%description
The goal of this project is to manage configuration for python tools,
such as black and rope and add support for a pyproject.toml
configuration file.

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pdm dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE README.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Apr 24 2024 Stanislav Levin <slev@altlinux.org> 1.3.1-alt1.1
- NMU: fixed FTBFS (rpm-build-pyproject 0.0.5).

* Fri Feb 09 2024 Anton Zhukharev <ancieg@altlinux.org> 1.3.1-alt1
- Updated to 1.3.1.

* Mon Oct 16 2023 Anton Zhukharev <ancieg@altlinux.org> 1.2.6-alt1
- Updated to 1.2.6.

* Thu Sep 28 2023 Anton Zhukharev <ancieg@altlinux.org> 1.2.5-alt1
- Updated to 1.2.5.

* Tue Oct 25 2022 Stanislav Levin <slev@altlinux.org> 1.2.2-alt2
- Fixed FTBFS (pdm-pep517 1.0.5).

* Thu Oct 06 2022 Anton Zhukharev <ancieg@altlinux.org> 1.2.2-alt1
- initial build for Sisyphus

