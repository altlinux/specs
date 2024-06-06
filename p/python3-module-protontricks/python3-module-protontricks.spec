%define _unpackaged_files_terminate_build 1
%define pypi_name protontricks

%def_with check

Name: python3-module-%pypi_name
Version: 1.11.1
Release: alt2

Summary: A wrapper that does winetricks things for Proton enabled games, requires Winetricks
License: GPL-3.0
Group: File tools
Url: https://pypi.org/project/protontricks/
Vcs: https://github.com/Matoking/protontricks

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
Requires: winetricks
Provides: %pypi_name = %EVR
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%summary.

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements_dev.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc README.md CHANGELOG.md TROUBLESHOOTING.md
%_bindir/%{pypi_name}*
%_desktopdir/%{pypi_name}*
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Jun 06 2024 Anton Zhukharev <ancieg@altlinux.org> 1.11.1-alt2
- Added winetricks requirement (closes 50554).

* Wed Feb 21 2024 Anton Zhukharev <ancieg@altlinux.org> 1.11.1-alt1
- Updated to 1.11.1.

* Sun Feb 11 2024 Anton Zhukharev <ancieg@altlinux.org> 1.11.0-alt1.gitbb1da5a
- Updated to bb1da5a (fixed FTBFS).

* Sat Dec 30 2023 Anton Zhukharev <ancieg@altlinux.org> 1.11.0-alt1
- Updated to 1.11.0.

* Fri Dec 08 2023 Anton Zhukharev <ancieg@altlinux.org> 1.10.5-alt1
- Built for ALT Sisyphus.

