%define _unpackaged_files_terminate_build 1
%define pypi_name python-multipart
%define mod_name python_multipart

%def_with check

Name: python3-module-%pypi_name
Version: 0.0.31
Release: alt1

Summary: A streaming multipart parser for Python
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/python-multipart/
Vcs: https://github.com/Kludex/python-multipart

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

# see https://bugzilla.altlinux.org/43483 for more information
AutoProv: nopython3
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
python-multipart is an Apache2 licensed streaming multipart parser for Python.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

# To avoid conflict with python3-module-multipart
rm -r %buildroot%python3_sitelibdir/multipart/

%check
%pyproject_run_pytest -vra

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Jun 04 2026 Anton Zhukharev <ancieg@altlinux.org> 0.0.31-alt1
- Updated to 0.0.30 (fixes GHSA-v9pg-7xvm-68h, GHSA-5rvq-cxj2-64vf,
  GHSA-6jv3-5f52-599m, GHSA-vffw-93wf-4j4q).

* Fri May 29 2026 Anton Zhukharev <ancieg@altlinux.org> 0.0.29-alt1
- Updated to 0.0.29 (fixes GHSA-pp6c-gr5w-3c5g).

* Sat Apr 11 2026 Anton Zhukharev <ancieg@altlinux.org> 0.0.26-alt1
- Updated to 0.0.26.

* Mon Apr 06 2026 Anton Zhukharev <ancieg@altlinux.org> 0.0.24-alt1
- Updated to 0.0.24.

* Mon Jan 26 2026 Anton Zhukharev <ancieg@altlinux.org> 0.0.22-alt1
- Updated to 0.0.22 (fixes GHSA-wp53-j4wj-2cfg).

* Fri Dec 19 2025 Anton Zhukharev <ancieg@altlinux.org> 0.0.21-alt1
- Updated to 0.0.21.

* Fri Jul 18 2025 Anton Zhukharev <ancieg@altlinux.org> 0.0.20-alt2
- Removed 'multipart' import name to avoid conflict with 'multipart' package.
- Actualized upstream VCS location.

* Mon Dec 23 2024 Anton Zhukharev <ancieg@altlinux.org> 0.0.20-alt1
- Updated to 0.0.20.

* Fri Dec 13 2024 Anton Zhukharev <ancieg@altlinux.org> 0.0.19-alt1
- Updated to 0.0.19 (fixes CVE-2024-53981).

* Fri Nov 01 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.17-alt1
- Updated to 0.0.17.

* Tue Oct 29 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.16-alt1
- Updated to 0.0.16.

* Fri Oct 25 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.14-alt1
- Updated to 0.0.14.

* Mon Sep 30 2024 Anton Zhukharev <ancieg@altlinux.org> 0.0.12-alt1
- Updated to 0.0.12.

* Tue Sep 24 2024 Anton Zhukharev <ancieg@altlinux.org> 0.0.10-alt1
- Updated to 0.0.10.

* Sun Feb 11 2024 Anton Zhukharev <ancieg@altlinux.org> 0.0.9-alt1
- Updated to 0.0.9.

* Mon Feb 05 2024 Anton Zhukharev <ancieg@altlinux.org> 0.0.7-alt1
- Updated to 0.0.7.

* Tue Aug 01 2023 Anton Zhukharev <ancieg@altlinux.org> 0.0.6-alt1
- Updated to 0.0.6.

* Sat Sep 17 2022 Anton Zhukharev <ancieg@altlinux.org> 0.0.5-alt2.gitd4831a3f
- bump release
- comment provides (closes: #43483)

* Sat Sep 17 2022 Anton Zhukharev <ancieg@altlinux.org> 0.0.5-alt1.gitd4831a3f
- initial build for Sisyphus
