%define _unpackaged_files_terminate_build 1
%define pypi_name yubikey-manager

%def_with check

Name: python3-module-%pypi_name
Version: 5.2.1
Release: alt1

Summary: Tool for managing your YubiKey configuration
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/yubikey-manager/
Vcs: https://github.com/Yubico/yubikey-manager
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

Requires: ykpers
Requires: libykpers-1
Requires: pcsc-lite-ccid

Provides: ykman

%py3_provides %pypi_name

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%add_pyproject_deps_check_filter pyinstaller
%add_pyproject_deps_check_filter sphinx-rtd-theme
%pyproject_builddeps_metadata_extra main
%pyproject_builddeps_check
%endif

%description
Python 3.6 (or later) library for configuring a YubiKey.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%if_with check
%pyproject_deps_resync_check_poetry dev
%endif

%build
%pyproject_build

%install
%pyproject_install

install -pD -m0644 man/ykman.1 %buildroot%_man1dir/ykman.1

%check
%pyproject_run_pytest

%files
%doc COPYING NEWS
%_bindir/*
%_man1dir/*
%python3_sitelibdir/*

%changelog
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

