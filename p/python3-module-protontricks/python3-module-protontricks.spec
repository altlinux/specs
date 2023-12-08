%define _unpackaged_files_terminate_build 1
%define pypi_name protontricks

%def_with check

Name: python3-module-%pypi_name
Version: 1.10.5
Release: alt1

Summary: A wrapper that does winetricks things for Proton enabled games, requires Winetricks
License: GPL-3.0
Group: File tools
Url: https://pypi.org/project/protontricks/
Vcs: https://github.com/Matoking/protontricks

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
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
* Fri Dec 08 2023 Anton Zhukharev <ancieg@altlinux.org> 1.10.5-alt1
- Built for ALT Sisyphus.

