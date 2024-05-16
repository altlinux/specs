%define _unpackaged_files_terminate_build 1
%define pypi_name dramatiq

# tests require rabbitmq, redis, prometheus running services
%def_without check

Name: python3-module-%pypi_name
Version: 1.17.0
Release: alt1

Summary: A fast and reliable distributed task processing library for Python 3
License: GPL-3.0 or LGPL-3.0
Group: Development/Python3
Url: https://pypi.org/project/dramatiq/
Vcs: https://github.com/Bogdanp/dramatiq

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra dev
%pyproject_builddeps_check
%endif

%description
%summary.

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
%doc COPYING COPYING.LESSER README.md
%_bindir/%{pypi_name}*
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu May 16 2024 Anton Zhukharev <ancieg@altlinux.org> 1.17.0-alt1
- Updated to 1.17.0.

* Fri Feb 09 2024 Anton Zhukharev <ancieg@altlinux.org> 1.16.0-alt1
- Updated to 1.16.0.

* Thu Nov 02 2023 Anton Zhukharev <ancieg@altlinux.org> 1.15.0-alt1
- Updated to 1.15.0.

* Tue Mar 28 2023 Anton Zhukharev <ancieg@altlinux.org> 1.14.2-alt1
- New version.

* Wed Oct 05 2022 Anton Zhukharev <ancieg@altlinux.org> 1.13.0-alt1
- initial build for Sisyphus

