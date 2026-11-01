%define _unpackaged_files_terminate_build 1
%define pypi_name protontricks
%define mod_name protontricks

%def_with check

Name: python3-module-%pypi_name
Version: 1.15.0
Release: alt1

Summary: Python package for protontricks
License: GPL-3.0
Group: Development/Python3
Url: https://pypi.org/project/protontricks/
Vcs: https://github.com/Matoking/protontricks

BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

%pyproject_configure_pypi_package
Requires: winetricks
BuildRequires(pre): rpm-build-pyproject >= 0.3.0

%description
%summary.

%package -n %pypi_name
Summary: A wrapper that does winetricks things for Proton enabled games
Group: File tools
Requires: winetricks

%description -n %pypi_name
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

# do not ship desktop file installer
rm %buildroot%_bindir/protontricks-desktop-install

%check
%pyproject_run_pytest -vra \
  --deselect tests/test_steam.py::TestFindSteamCompatToolApp::test_find_compat_tool_not_arm64

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%files -n %pypi_name
%_bindir/protontricks*
%_desktopdir/protontricks*.desktop

%changelog
* Fri Oct 30 2026 Anton Zhukharev <ancieg@altlinux.org> 1.15.0-alt1
- Updated to 1.15.0.

* Tue Mar 31 2026 Anton Zhukharev <ancieg@altlinux.org> 1.14.1-alt1
- Updated to 1.14.1.

* Tue Feb 24 2026 Anton Zhukharev <ancieg@altlinux.org> 1.14.0-alt1
- Updated to 1.14.0.

* Tue Dec 23 2025 Anton Zhukharev <ancieg@altlinux.org> 1.13.1-alt1
- Updated to 1.13.1.

* Tue Aug 12 2025 Anton Zhukharev <ancieg@altlinux.org> 1.13.0-alt1
- Updated to 1.13.0.

* Sun Mar 09 2025 Anton Zhukharev <ancieg@altlinux.org> 1.12.1-alt1
- Updated to 1.12.1.

* Wed Sep 25 2024 Anton Zhukharev <ancieg@altlinux.org> 1.12.0-alt1
- Updated to 1.12.0.

* Mon Jul 08 2024 Anton Zhukharev <ancieg@altlinux.org> 1.11.1-alt3
- Separated protontricks package (closes 50567).
- Stopped shipping desktop files installer.

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
