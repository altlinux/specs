%define _unpackaged_files_terminate_build 1
%define pypi_name pycron
%define mod_name pycron

%def_with check

Name: python3-module-%pypi_name
Version: 3.3.0
Release: alt1

Summary: Simple cron-like parser for Python, which determines if current datetime matches conditions
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pycron/
Vcs: https://github.com/kipe/pycron

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
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
%pyproject_deps_resync_check_depgroup dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest -v

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Sep 22 2026 Anton Zhukharev <ancieg@altlinux.org> 3.3.0-alt1
- Updated to 3.3.0.

* Fri Jun 06 2025 Anton Vyatkin <toni@altlinux.org> 3.2.0-alt1
- New version 3.2.0.

* Tue Jan 14 2025 Anton Vyatkin <toni@altlinux.org> 3.1.2-alt1
- New version 3.1.2.

* Mon Sep 30 2024 Anton Vyatkin <toni@altlinux.org> 3.1.1-alt1
- New version 3.1.1.

* Tue May 02 2023 Anton Vyatkin <toni@altlinux.org> 3.0.0-alt2
- Fix BuildRequires

* Sat Dec 10 2022 Anton Zhukharev <ancieg@altlinux.org> 3.0.0-alt1
- initial build for Sisyphus
