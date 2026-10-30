%define _unpackaged_files_terminate_build 1
%define pypi_name pyupgrade
%define mod_name pyupgrade

%def_with check

Name: python3-module-%pypi_name
Version: 3.22.0
Release: alt1

Summary: A tool to automatically upgrade syntax for newer versions of the language
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pyupgrade/
Vcs: https://github.com/asottile/pyupgrade

BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

%pyproject_configure_without_autodiscovery
%pyproject_configure_with_check_deps pip_reqfile requirements-dev.txt
%pyproject_configure_pypi_package
BuildRequires(pre): rpm-build-pyproject >= 0.3.0

%description
%summary.

%prep
%setup
%autopatch -p1
%pyproject_setup_deps

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%_bindir/pyupgrade
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Oct 30 2026 Anton Zhukharev <ancieg@altlinux.org> 3.22.0-alt1
- Updated to 3.22.0.

* Mon Dec 22 2025 Anton Zhukharev <ancieg@altlinux.org> 3.21.2-alt1
- Updated to 3.21.2.

* Wed Nov 12 2025 Anton Zhukharev <ancieg@altlinux.org> 3.21.1-alt1
- Updated to 3.21.1.

* Tue Oct 28 2025 Anton Zhukharev <ancieg@altlinux.org> 3.21.0-alt1
- Updated to 3.21.0.

* Thu May 29 2025 Anton Zhukharev <ancieg@altlinux.org> 3.20.0-alt1
- Updated to 3.20.0.

* Mon Feb 10 2025 Anton Zhukharev <ancieg@altlinux.org> 3.19.1-alt1
- Updated to 3.19.1.

* Tue Oct 22 2024 Anton Zhukharev <ancieg@altlinux.org> 3.19.0-alt1
- Updated to 3.19.0.

* Sat Oct 12 2024 Anton Zhukharev <ancieg@altlinux.org> 3.18.0-alt1
- Updated to 3.18.0.

* Mon Jul 29 2024 Anton Zhukharev <ancieg@altlinux.org> 3.17.0-alt1
- Updated to 3.17.0.

* Wed Jul 03 2024 Anton Zhukharev <ancieg@altlinux.org> 3.16.0-alt1
- Updated to 3.16.0.

* Sat Mar 30 2024 Anton Zhukharev <ancieg@altlinux.org> 3.15.2-alt1
- Updated to 3.15.2.

* Sun Feb 18 2024 Anton Zhukharev <ancieg@altlinux.org> 3.15.1-alt1
- Updated to 3.15.1.

* Sun Oct 08 2023 Anton Zhukharev <ancieg@altlinux.org> 3.15.0-alt1
- Updated to 3.15.0.

* Tue Oct 03 2023 Anton Zhukharev <ancieg@altlinux.org> 3.14.0-alt1
- Updated to 3.14.0.

* Mon Sep 25 2023 Anton Zhukharev <ancieg@altlinux.org> 3.13.0-alt1
- Updated to 3.13.0.

* Fri Sep 22 2023 Anton Zhukharev <ancieg@altlinux.org> 3.12.0-alt1
- Updated to 3.12.0.

* Sat Sep 16 2023 Anton Zhukharev <ancieg@altlinux.org> 3.11.0-alt1
- Updated to 3.11.0.

* Tue Aug 01 2023 Anton Zhukharev <ancieg@altlinux.org> 3.10.1-alt1
- Updated to 3.10.1.

* Wed Jul 26 2023 Anton Zhukharev <ancieg@altlinux.org> 3.9.0-alt1
- Updated to 3.9.0.

* Wed May 10 2023 Anton Zhukharev <ancieg@altlinux.org> 3.4.0-alt1
- New version.

* Mon Feb 13 2023 Anton Zhukharev <ancieg@altlinux.org> 3.3.1-alt1
- 3.2.2 -> 3.3.1

* Tue Nov 15 2022 Anton Zhukharev <ancieg@altlinux.org> 3.2.2-alt1
- 2.38.2 -> 3.2.2

* Sat Oct 01 2022 Anton Zhukharev <ancieg@altlinux.org> 2.38.2-alt1
- initial build for Sisyphus
