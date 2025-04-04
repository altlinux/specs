%define _unpackaged_files_terminate_build 1
%def_with check
%define pypi_name typing-inspection
%define module_name typing_inspection

Name: python3-module-%pypi_name
Version: 0.4.0
Release: alt1

Summary: Runtime typing introspection tools
License: MIT
Group: Development/Python3
Url: https://typing-inspection.pydantic.dev/latest/
Vcs: https://github.com/pydantic/typing-inspection

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
typing-inspection provides tools to inspect type annotations at runtime.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup tests
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE README.md
%python3_sitelibdir/%module_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Apr 04 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.4.0-alt1
- Initial build for ALT Sisyphus.

