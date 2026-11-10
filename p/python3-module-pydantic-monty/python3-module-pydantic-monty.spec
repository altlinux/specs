%define _unpackaged_files_terminate_build 1
%define pypi_name pydantic-monty
%define client_pypi_name pydantic-monty-client
%define mod_name pydantic_monty
%define client_dir crates/monty-python
%define runtime_pypi_name pydantic-monty-runtime
%define runtime_dir crates/monty-runtime
%define meta_dir packages/pydantic-monty
# upstream tests assume a 64-bit ssize_t and fail on i586
%ifnarch %ix86
%def_with check
%else
%def_without check
%endif

# C objects built by cargo crates must not be LTO bytecode: rustc links
# them as a static archive
%add_optflags -fno-lto

Name: python3-module-%pypi_name
Version: 1.5.0
Release: alt1

Summary: Monty, the Python sandbox: bindings plus the worker binary
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pydantic-monty
Vcs: https://github.com/pydantic/monty

Source0: %name-%version.tar
Source1: vendor.tar
Source2: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-pyproject
BuildRequires: rpm-build-pyproject
BuildRequires: rust-cargo
BuildRequires: /proc

%pyproject_builddeps -- client_pep518
%pyproject_builddeps -- runtime_pep518
%pyproject_builddeps -- meta_pep518
%pyproject_builddeps -- client_metadata %{?pyproject_deps_check_filter:--exclude %pyproject_deps_check_filter}
%pyproject_builddeps_check
%pyproject_runtimedeps -- meta_metadata

%description
Monty is a secure, snapshotable Python sandbox written in Rust. This
metapackage installs the pydantic_monty client and the monty worker
binary at matching versions. The source package also builds the
pydantic-monty-client and pydantic-monty-runtime PyPI projects.

%package -n python3-module-%pypi_name+opentelemetry
Summary: Extra "opentelemetry" for %pypi_name
Group: Development/Python3
BuildArch: noarch
Requires: python3-module-%pypi_name = %version-%release
Requires: python3-module-%client_pypi_name+opentelemetry = %version-%release

%description -n python3-module-%pypi_name+opentelemetry
Extra "opentelemetry" for %pypi_name.

%package -n python3-module-%client_pypi_name
Summary: Python client for the Monty sandbox
Group: Development/Python3
%pyproject_runtimedeps -- client_metadata

%description -n python3-module-%client_pypi_name
Python client for Monty, a secure, snapshotable Python sandbox written
in Rust. This package ships the pydantic_monty module with its native
extension. To run a local worker, install the python3-module-pydantic-monty
package, which also pulls in the runtime binary.

%package -n python3-module-%client_pypi_name+opentelemetry
Summary: Extra "opentelemetry" for %client_pypi_name
Group: Development/Python3
Requires: python3-module-%client_pypi_name = %version-%release
%pyproject_runtimedeps -- client_metadata --extra opentelemetry

%description -n python3-module-%client_pypi_name+opentelemetry
Extra "opentelemetry" for %client_pypi_name.

%package -n python3-module-%runtime_pypi_name
Summary: The monty CLI binary, a worker for pydantic-monty
Group: Development/Python3

%description -n python3-module-%runtime_pypi_name
The monty command line binary, a secure and snapshotable Python sandbox
written in Rust. The pydantic-monty client spawns it as worker
subprocesses.

%prep
%setup -a1
%autopatch -p1
mkdir .cargo
cat > .cargo/config.toml <<'EOF'
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF
export CARGO_HOME=${PWD}/cargo
export CARGO_NET_OFFLINE=true

cd %meta_dir
%pyproject_deps_resync meta_pep518 pep518
%pyproject_deps_resync meta_metadata metadata
cd -

cd %client_dir
%pyproject_deps_resync client_pep518 pep518
%pyproject_deps_resync client_metadata metadata
%pyproject_deps_resync_check_depgroup dev
cd -

cd %runtime_dir
%pyproject_deps_resync runtime_pep518 pep518
cd -

%build
export CARGO_HOME=${PWD}/cargo
export CARGO_NET_OFFLINE=true
cd %runtime_dir
%pyproject_build
cd -

cd %client_dir
%pyproject_build
cd -

cd %meta_dir
%pyproject_build
cd -

%install
cd %runtime_dir
%pyproject_install
cd -

cd %client_dir
%pyproject_install
cd -

cd %meta_dir
%pyproject_install
cd -
# the main package is arch (it shares the source with the arch subpackages),
# so its dist-info must not live in the noarch directory; on i586 both
# directories are the same and there is nothing to move
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
distinfo=%{pyproject_distinfo %pypi_name}
install -Dpm644 %buildroot%python3_sitelibdir_noarch/$distinfo/METADATA \
	%buildroot%python3_sitelibdir/$distinfo/METADATA
install -Dpm644 %buildroot%python3_sitelibdir_noarch/$distinfo/entry_points.txt \
	%buildroot%python3_sitelibdir/$distinfo/entry_points.txt
rm -r %buildroot%python3_sitelibdir_noarch/$distinfo
%endif

%check
# the tests spawn the monty worker binary built above
export MONTY_BIN=%buildroot%_bindir/monty
cd %client_dir
# readme examples need the repository root as cwd, remote tests need grpc,
# the test_parallel_exec* tests assert wall-clock speedup and are flaky
# on loaded builders
%pyproject_run_pytest -m 'not remote' \
	--ignore=tests/test_readme_examples.py \
	--ignore=tests/test_remote.py \
	--deselect=tests/test_callback_context.py::test_callback_contexts[remote] \
	--deselect=tests/test_threading.py::test_parallel_exec \
	--deselect=tests/test_threading.py::test_parallel_exec_ext_functions
cd -

%files
%doc %meta_dir/README.md LICENSE
%_bindir/pydantic-monty
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%files -n python3-module-%pypi_name+opentelemetry

%files -n python3-module-%client_pypi_name
%doc %client_dir/README.md LICENSE
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %client_pypi_name}/

%files -n python3-module-%client_pypi_name+opentelemetry

%files -n python3-module-%runtime_pypi_name
%doc %runtime_dir/README.md LICENSE
%_bindir/monty
%python3_sitelibdir/%{pyproject_distinfo %runtime_pypi_name}/

%changelog
* Tue Nov 10 2026 Andrey Kovalev <ded@altlinux.org> 1.5.0-alt1
- Initial build for ALT Sisyphus.
