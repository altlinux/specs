%define _unpackaged_files_terminate_build 1
%define pypi_name cron-converter
%define module_name cron_converter
%def_with check

Name: python3-module-%pypi_name
Version: 1.2.2
Release: alt1

Summary: Cron string converter for Python
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/cron-converter/
Vcs: https://github.com/Sonic0/cron-converter
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-macros-pyproject
BuildRequires: rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra test
%endif

%description
Cron-converter provides a Cron string parser (from string/lists to
string/lists) and iteration for the datetime object with a cron like
format.
This project would be a transposition in Python of JS cron-converter
by roccivic.

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
%pyproject_run_unittest discover -v tests/unit
%pyproject_run_unittest discover -v tests/integration

%files
%doc README.md LICENSE
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Oct 16 2025 Alexandr Shashkin <dutyrok@altlinux.org> 1.2.2-alt1
- Initial build for ALT Sisyphus.
