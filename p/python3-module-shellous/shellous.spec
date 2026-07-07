%define _unpackaged_files_terminate_build 1
%define pypi_name shellous
%define module_name %pypi_name
%def_with check

Name: python3-module-%pypi_name
Version: 0.40.0
Release: alt1

Summary: A concise API for running subprocesses using asyncio
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/shellous/
Vcs: https://github.com/byllyfish/shellous
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-macros-pyproject
BuildRequires: rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
BuildRequires: /dev
BuildRequires: /dev/pts
BuildRequires: /proc
BuildRequires: lsof
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
shellous provides a concise API for running subprocesses using asyncio.
It is similar to and inspired by sh.

Benefits:
- Run programs asynchronously in a single line.
- Redirect stdin, stdout and stderr to files, memory buffers, async
  streams or loggers.
- Iterate asynchronously over subprocess output.
- Set timeouts and reliably cancel running processes.
- Run a program with a pseudo-terminal (pty).
- Use send() and expect() to manually control a subprocess.
- Construct pipelines and use process substitution directly from Python
  (no shell required).
- Runs on Linux, MacOS, FreeBSD and Windows.
- Monitor processes being started and stopped with audit_callback API.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_poetry dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -s

%files
%doc README.md LICENSE
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Jul 07 2026 Andrey Kuzma <kuzmaav@altlinux.org> 0.40.0-alt1
- Initial build for Sisyphus.
