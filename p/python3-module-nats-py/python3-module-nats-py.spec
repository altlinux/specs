%define _unpackaged_files_terminate_build 1
%define pypi_name nats-py
%define mod_name nats

# tests require running NATS server
%def_without check

Name: python3-module-%pypi_name
Version: 2.8.0
Release: alt1

Summary: Python3 client for NATS
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/nats-py/
Vcs: https://github.com/nats-io/nats.py

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
%endif

%description
An asyncio Python client for the NATS messaging system.

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
%doc LICENSE README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Jul 08 2024 Anton Zhukharev <ancieg@altlinux.org> 2.8.0-alt1
- Updated to 2.8.0.

* Tue Apr 02 2024 Anton Zhukharev <ancieg@altlinux.org> 2.7.2-alt1
- Updated to 2.7.2.

* Tue Feb 13 2024 Anton Zhukharev <ancieg@altlinux.org> 2.7.0-alt1
- Updated to 2.7.0.

* Tue Nov 07 2023 Anton Zhukharev <ancieg@altlinux.org> 2.6.0-alt1
- Updated to 2.6.0.

* Tue Sep 26 2023 Anton Zhukharev <ancieg@altlinux.org> 2.4.0-alt1
- Updated to 2.4.0.

* Thu Sep 07 2023 Anton Zhukharev <ancieg@altlinux.org> 2.3.1-alt1
- Updated to 2.3.1.

* Sat May 13 2023 Anton Zhukharev <ancieg@altlinux.org> 2.2.0-alt1
- Initial build for ALT Sisyphus.

