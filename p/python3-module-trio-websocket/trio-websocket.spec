%define _unpackaged_files_terminate_build 1
%define pypi_name trio-websocket
%define mod_name trio_websocket

%def_with check

Name: python3-module-%pypi_name
Version: 0.11.1
Release: alt2
Summary: WebSocket library for Trio
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/trio-websocket
Vcs: https://github.com/python-trio/trio-websocket
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter pip-tools
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
This library implements both server and client aspects of the the WebSocket
protocol, striving for safety, correctness, and ergonomics. It is based on the
wsproto project, which is a Sans-IO state machine that implements the majority
of the WebSocket protocol, including framing, codecs, and events. This library
handles I/O using the Trio framework.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements-dev.in
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon May 27 2024 Stanislav Levin <slev@altlinux.org> 0.11.1-alt2
- Fixed FTBFS (trio 0.25.0).

* Thu Mar 28 2024 Stanislav Levin <slev@altlinux.org> 0.11.1-alt1
- Initial build for Sisyphus.
