%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-vcr
%define mod_name pytest_vcr

%def_with check

Name: python3-module-%pypi_name
Version: 1.0.2
Release: alt1

Summary: Plugin for managing VCR.py cassettes
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest-vcr/
Vcs: https://github.com/ktosiek/pytest-vcr
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-macros-pyproject
BuildRequires: rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%endif

%description
A pytest plugin for managing VCR.py cassettes: it provides the vcr
fixture and the vcr marker, and keeps a cassette per test.

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
%pyproject_run_pytest tests

%files
%doc README.rst LICENSE
%python3_sitelibdir/%mod_name.py
%python3_sitelibdir/__pycache__/%mod_name.*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Oct 27 2026 Alexandr Shashkin <dutyrok@altlinux.org> 1.0.2-alt1
- Initial build for ALT Sisyphus.
