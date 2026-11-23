%define _unpackaged_files_terminate_build 1
%def_enable check

%define pypi_name swe-rex

Name: swe-rex
Version: 1.4.0
Release: alt1

Summary: Sandboxed code execution for LM agents, locally or on the cloud

License: MIT
Group: Development/Python
URL: https://swe-rex.com

VCS: https://github.com/SWE-agent/SWE-rex
Source: %name-%version-%release.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
Requires: python3-module-%pypi_name = %EVR
%if_enabled check
BuildRequires: /dev/pts
BuildRequires: python3(pytest)
BuildRequires: python3-module-aiohttp
BuildRequires: python3-module-bashlex
BuildRequires: python3-module-fastapi
BuildRequires: python3-module-pexpect
BuildRequires: python3-module-pydantic
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-python-multipart
BuildRequires: python3-module-requests
BuildRequires: python3-module-rich
BuildRequires: python3-module-typing_extensions
BuildRequires: python3-module-uvicorn
%endif

%description
SWE-ReX is a runtime interface for interacting with sandboxed shell
environments, allowing you to effortlessly let your LM agent run any
command on any environment.
Whether commands are executed locally or remotely in Podman containers,
AWS remote machines, Modal, or something else, your agent code remains
the same.
It enables interacting with running shell sessions, using interactive
command line tools like ipython or gdb, and managing multiple such shell
sessions in parallel.

%package -n python3-module-%pypi_name
Summary: Python module for %name
Group: Development/Python

%description -n python3-module-%pypi_name
SWE-ReX is a runtime interface for interacting with sandboxed shell
environments, allowing you to effortlessly let your LM agent run any
command on any environment.

This package contains the swerex Python module.
Modal, Fargate and Daytona deployments are not included in this build.

%prep
%setup -n %name-%version-%release
rm src/swerex/deployment/{daytona.py,fargate.py,modal.py}

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest \
 --ignore=tests/test_docker_deployment.py \
 --ignore=tests/test_fargate_deployment.py \
 --ignore=tests/test_modal_deployment.py \
 --ignore=tests/test_get_deployment.py \
 --deselect tests/test_execution.py::test_run_in_shell_timeout \
 --deselect tests/test_execution.py::test_run_in_shell_interactive_command_timeout \
 --deselect tests/test_execution.py::test_interrupt_pager \
 --deselect tests/test_server.py::test_unauthenticated_request \
 #

%files
%doc README.md LICENSE.txt
%_bindir/swerex-remote

%files -n python3-module-%pypi_name
%python3_sitelibdir_noarch/swerex
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Nov 20 2026 Arseny Maslennikov <arseny@altlinux.org> 1.4.0-alt1
- Initial build for ALT Sisyphus.
