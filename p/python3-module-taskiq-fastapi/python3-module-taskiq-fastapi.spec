%define _unpackaged_files_terminate_build 1
%define pypi_name taskiq-fastapi
%define mod_name taskiq_fastapi

Name: python3-module-%pypi_name
Version: 0.3.1
Release: alt1

Summary: FastAPI integration for taskiq
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/taskiq-fastapi/
Vcs: https://github.com/taskiq-python/taskiq-fastapi

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%py3_provides %pypi_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
%summary.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Oct 13 2023 Anton Zhukharev <ancieg@altlinux.org> 0.3.1-alt1
- Updated to 0.3.1.

* Tue Jul 25 2023 Anton Zhukharev <ancieg@altlinux.org> 0.3.0-alt1
- Updated to 0.3.0.

* Wed Jun 14 2023 Anton Zhukharev <ancieg@altlinux.org> 0.2.0-alt1
- New version.

* Sat May 13 2023 Anton Zhukharev <ancieg@altlinux.org> 0.1.2-alt1
- Initial build for ALT Sisyphus.

