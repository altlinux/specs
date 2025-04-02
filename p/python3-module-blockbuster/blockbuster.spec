%define _unpackaged_files_terminate_build 1
%def_with check
%define pypi_name blockbuster
%define module_name %pypi_name

Name: python3-module-%pypi_name
Version: 1.5.23
Release: alt1

Summary: Utility to detect blocking calls in the async event loop
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/blockbuster/
Vcs: https://github.com/cbornet/blockbuster

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

Requires: python3-modules-sqlite3

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
BuildRequires: python3-modules-sqlite3
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Blockbuster is a Python package designed to detect and prevent blocking
calls within an asynchronous event loop. It is particularly useful when
executing tests to ensure that your asynchronous code does not inadvertently
call blocking operations, which can lead to performance bottlenecks and
unpredictable behavior.
In Python, the asynchronous event loop allows for concurrent execution of
tasks without the need for multiple threads or processes. This is achieved
by running tasks cooperatively, where tasks yield control back to the event
loop when they are waiting for I/O operations or other long-running tasks
to complete.
However, blocking calls, such as file I/O operations or certain networking
operations, can halt the entire event loop, preventing other tasks from
running. This can lead to increased latency and reduced performance,
defeating the purpose of using asynchronous programming.
The difficulty with blocking calls is that they are not always obvious,
especially when working with third-party libraries or legacy code. This
is where Blockbuster comes in: it helps you identify and eliminate blocking
calls in your codebase during testing, ensuring that your asynchronous code
runs smoothly and efficiently. It does this by wrapping common blocking
functions and raising an exception when they are called within an asynchronous
context.

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
# tests/test_blockbuster.py::test_ssl_socket:
# It's deselected since internet and DNS resolving are required.
%pyproject_run_pytest --deselect tests/test_blockbuster.py::test_ssl_socket tests/

%files
%doc README.md
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Apr 02 2025 Alexandr Shashkin <dutyrok@altlinux.org> 1.5.23-alt1
- Initial build for ALT Sisyphus.

