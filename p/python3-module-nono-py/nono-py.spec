%define _unpackaged_files_terminate_build 1

# With -flto=auto the C code of ring and aws-lc-sys is missing from the .so,
# and importing the module fails with undefined symbols
%remove_optflags -flto=auto

Name: python3-module-nono-py

Version: 0.16.0
Release: alt1

Summary: Python Library for nono - kernel enforced agent sandboxing
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/nono-py/
Vcs: https://github.com/nolabs-ai/nono-py

ExcludeArch: %ix86

Source0: %name-%version.tar
Source1: vendor.tar
Source2: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
BuildRequires(pre): rpm-build-rust
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra dev

%description
Python bindings for nono, a capability-based sandboxing library.
nono provides OS-enforced sandboxing using Landlock (Linux) and
Seatbelt (macOS). Once a sandbox is applied, unauthorized operations
are structurally impossible.

%prep
%setup -a1
%rust_prep
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
export TOKIO_WORKER_THREADS=4
%pyproject_run_pytest \
	--basetemp=/tmp/nono-py-tests \
	--deselect tests/test_sandboxed_exec.py::TestSandboxedExecPortFiltering::test_udp_egress_is_not_blocked \
	tests

%files
%doc *.md LICENSE
%python3_sitelibdir/nono_py
%python3_sitelibdir/%{pyproject_distinfo nono_py}

%changelog
* Tue Oct 13 2026 Bogdan Boguslavskij <bogdanb@altlinux.org> 0.16.0-alt1
- Initial build for Sisyphus.

