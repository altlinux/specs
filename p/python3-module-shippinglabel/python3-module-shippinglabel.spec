%define _unpackaged_files_terminate_build 1
%define pypi_name shippinglabel

# tests require the Internet connection
%def_without check

Name: python3-module-%pypi_name
Version: 1.7.2
Release: alt1

Summary: Utilities for handling packages
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/shippinglabel/
Vcs: https://github.com/domdfcoding/shippinglabel

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

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
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile tests/requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE README.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon May 27 2024 Anton Zhukharev <ancieg@altlinux.org> 1.7.2-alt1
- Updated to 1.7.2.

* Mon Feb 12 2024 Anton Zhukharev <ancieg@altlinux.org> 1.7.1-alt1
- Updated to 1.7.1.

* Wed Dec 27 2023 Anton Zhukharev <ancieg@altlinux.org> 1.6.0-alt1
- Updated to 1.6.0.

* Fri Jul 21 2023 Anton Zhukharev <ancieg@altlinux.org> 1.5.0-alt1
- Updated to 1.5.0.

* Thu Sep 29 2022 Anton Zhukharev <ancieg@altlinux.org> 1.4.1-alt1
- initial build for Sisyphus

