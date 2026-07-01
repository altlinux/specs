%define _unpackaged_files_terminate_build 1
%define pypi_name yubikey-manager
%define mod_name ykman

%def_with check

Name: python3-module-%pypi_name
Version: 5.9.2
Release: alt1

Summary: Library and CLI for managing your YubiKey configuration
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/yubikey-manager/
Vcs: https://github.com/Yubico/yubikey-manager

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

Requires: pcsc-lite-ccid
Provides: %mod_name = %EVR
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter pyinstaller
%add_pyproject_deps_check_filter sphinx-rtd-theme
%pyproject_builddeps_metadata_extra main
%pyproject_builddeps_check
%endif

%description
Python library and command line tool for configuring any YubiKey over
all USB interfaces.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup dev
%endif

%build
%pyproject_build

%install
%pyproject_install

install -pD -m0644 man/ykman.1 %buildroot%_man1dir/ykman.1

%check
%pyproject_run_pytest -vra

%files
%doc COPYING NEWS
%_bindir/ykman
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/yubikit/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%_man1dir/%mod_name.1.*

%changelog
* Wed Jul 01 2026 Anton Zhukharev <ancieg@altlinux.org> 5.9.2-alt1
- Updated to 5.9.2.

* Thu Apr 16 2026 Anton Zhukharev <ancieg@altlinux.org> 5.9.1-alt1
- Updated to 5.9.1.

* Fri Apr 03 2026 Anton Zhukharev <ancieg@altlinux.org> 5.9.0-alt2
- Removed dependency on ykpers.

* Fri Jan 23 2026 Anton Zhukharev <ancieg@altlinux.org> 5.9.0-alt1
- Updated to to 5.9.0.

* Fri Sep 26 2025 Anton Zhukharev <ancieg@altlinux.org> 5.8.0-alt1
- Updated to 5.8.0.

* Mon Jun 23 2025 Anton Zhukharev <ancieg@altlinux.org> 5.7.2-alt1
- Updated to 5.7.2.

* Thu May 29 2025 Anton Zhukharev <ancieg@altlinux.org> 5.7.0-alt1
- Updated to 5.7.0.

* Thu Mar 20 2025 Anton Zhukharev <ancieg@altlinux.org> 5.6.1-alt1
- Updated to 5.6.1.

* Fri Mar 14 2025 Anton Zhukharev <ancieg@altlinux.org> 5.6.0-alt1
- Updated to 5.6.0.

* Fri Jul 05 2024 Anton Zhukharev <ancieg@altlinux.org> 5.5.1-alt1
- Updated to 5.5.1.

* Thu Mar 28 2024 Anton Zhukharev <ancieg@altlinux.org> 5.4.0-alt1
- Updated to 5.4.0.

* Fri Feb 09 2024 Anton Zhukharev <ancieg@altlinux.org> 5.3.0-alt1
- Updated to 5.3.0.

* Wed Oct 11 2023 Anton Zhukharev <ancieg@altlinux.org> 5.2.1-alt1
- Updated to 5.2.1.

* Mon Aug 21 2023 Anton Zhukharev <ancieg@altlinux.org> 5.2.0-alt1
- Updated to 5.2.0.

* Mon May 08 2023 Anton Zhukharev <ancieg@altlinux.org> 5.1.1-alt1
- New version.

* Sun Mar 05 2023 Anton Zhukharev <ancieg@altlinux.org> 5.0.1-alt1
- 4.0.9 -> 5.0.1.
- Removed ykman subpackage.

* Wed Sep 14 2022 Stanislav Levin <slev@altlinux.org> 4.0.9-alt4
- NMU: Fixed FTBFS (poetry-core 1.1.0).

* Sat Sep 10 2022 Anton Zhukharev <ancieg@altlinux.org> 4.0.9-alt3
- add ykpers dependency

* Mon Jul 25 2022 Anton Zhukharev <ancieg@altlinux.org> 4.0.9-alt2
- add pcsc-lite-ccid dependency

* Sat Jul 23 2022 Anton Zhukharev <ancieg@altlinux.org> 4.0.9-alt1
- initial build for Sisyphus

