%define _unpackaged_files_terminate_build 1
%define pypi_name agent-detector
%define module_name agent_detector

%def_with check

Name: python3-module-%pypi_name
Version: 2.0.0
Release: alt1

Summary: Detect AI coding agents from their execution environment or User-Agent
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/agent-detector/
Vcs: https://github.com/patrick91/agent-detector
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-macros-pyproject
BuildRequires: rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
BuildRequires: python3-module-pytest-cov
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Agent Detector is a small, dependency-free package for detecting which
AI coding agent is driving the current process, and for parsing that
identity back out of a User-Agent header.

It returns evidence rather than only a boolean, so callers can
distinguish an explicit identity from a broad environmental hint.

%prep
%setup
%autopatch -p1

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
%pyproject_run_pytest --no-cov

%files
%doc LICENSE README.md
%_bindir/%pypi_name
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Sep 03 2026 Alexandr Shashkin <dutyrok@altlinux.org> 2.0.0-alt1
- Initial build for ALT Sisyphus.
