%define _unpackaged_files_terminate_build 1
%define pypi_name python-multipart
%define mod_name multipart

%def_with check

Name: python3-module-%pypi_name
Version: 0.0.10
Release: alt1

Summary: A streaming multipart parser for Python
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/python-multipart/
Vcs: https://github.com/andrew-d/python-multipart

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

# see https://bugzilla.altlinux.org/43483 for more information
%filter_from_provides /python.*/d
Conflicts: python3-module-multipart
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

%check
%pyproject_run_pytest -vra

%files
%doc README.md LICENSE.txt
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
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

