%define _unpackaged_files_terminate_build 1
%define pypi_name spyder-kernels
%define mod_name spyder_kernels

%def_with check

Name: python3-module-%pypi_name
Version: 2.5.1
Release: alt1

Summary: Jupyter Kernels for the Spyder console
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/spyder-kernels/
Vcs: https://github.com/spyder-ide/spyder-kernels

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra test
BuildRequires: xvfb-run
BuildRequires: python3-module-pandas-tests
%endif

%description
Package that provides Jupyter kernels for use with the consoles of Spyder,
the Scientific Python Development Environment.

These kernels can launched either through Spyder itself or in an independent
Python session, and allow for interactive or file-based execution of Python
code inside Spyder.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- xvfb-run -- pytest -vra

%files
%doc AUTHORS.txt CHANGELOG.md LICENSE.txt README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue May 21 2024 Anton Zhukharev <ancieg@altlinux.org> 2.5.1-alt1
- Updated to 2.5.1.
- Built from upstream VCS.

* Sat Jul 29 2023 Vitaly Lipatov <lav@altlinux.ru> 2.4.4-alt1
- new version 2.4.4 (with rpmrb script)

* Sun Apr 23 2023 Vitaly Lipatov <lav@altlinux.ru> 2.4.3-alt1
- new version 2.4.3 (with rpmrb script)

* Mon Mar 13 2023 Vitaly Lipatov <lav@altlinux.ru> 2.4.2-alt1
- new version 2.4.2 (with rpmrb script)

* Sun Sep 11 2022 Vitaly Lipatov <lav@altlinux.ru> 2.3.3-alt1
- new version 2.3.3 (with rpmrb script)

* Mon Jul 18 2022 Vitaly Lipatov <lav@altlinux.ru> 2.3.2-alt1
- new version 2.3.2 (with rpmrb script)

* Tue Apr 05 2022 Vitaly Lipatov <lav@altlinux.ru> 2.3.0-alt1
- new version 2.3.0 (with rpmrb script)

* Sun Sep 12 2021 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt1
- new version 2.1.1 (with rpmrb script)

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt1
- new version 2.1.0 (with rpmrb script)

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 2.0.4-alt1
- new version 2.0.4 (with rpmrb script)

* Tue Jun 08 2021 Vitaly Lipatov <lav@altlinux.ru> 2.0.3-alt1
- new version 2.0.3 (with rpmrb script)

* Mon Apr 19 2021 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt1
- new version 2.0.1 (with rpmrb script)

* Tue Apr 06 2021 Vitaly Lipatov <lav@altlinux.ru> 1.10.2-alt1
- new version 1.10.2 (with rpmrb script)

* Fri Jan 22 2021 Vitaly Lipatov <lav@altlinux.ru> 1.10.1-alt1
- new version 1.10.1 (with rpmrb script)

* Wed Nov 04 2020 Vitaly Lipatov <lav@altlinux.ru> 1.9.4-alt1
- new version 1.9.4 (with rpmrb script)

* Tue Feb 04 2020 Vitaly Lipatov <lav@altlinux.ru> 1.8.1-alt1
- initial build for ALT Sisyphus
