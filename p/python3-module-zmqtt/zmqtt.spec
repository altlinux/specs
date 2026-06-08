%global _unpackaged_files_terminate_build 1
%define pypi_name zmqtt

%def_with check

Name: python3-module-zmqtt
Version: 0.0.5
Release: alt1

Summary: Pure asyncio MQTT 3.1.1/5.0 client library
Group: Development/Python3
License: MIT
BuildArch: noarch

Url: https://pypi.org/project/zmqtt/
VCS: https://github.com/faststream-community/zMQTT
AutoReq: yes, nopython3

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

BuildRequires(pre): rpm-build-pyproject

BuildRequires: python3-module-typing_extensions

%pyproject_builddeps_build
%pyproject_runtimedeps_metadata

%if_with check
%add_pyproject_deps_check_filter bandit
%add_pyproject_deps_check_filter semgrep
%add_pyproject_deps_check_filter zizmor
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Pure asyncio MQTT 3.1.1 and 5.0 client library.  No paho dependency, no
threading, no god classes.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_depgroup dev

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v -m "not broker"

%files
%python3_sitelibdir/zmqtt
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Jun 08 2026 Egor Ignatov <egori@altlinux.org> 0.0.5-alt1
- New version 0.0.5.

* Tue Jun 02 2026 Egor Ignatov <egori@altlinux.org> 0.0.4-alt1
- Initial build for ALT Linux.
