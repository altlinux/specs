%define _unpackaged_files_terminate_build 1
%define pypi_name pydantic-core
%define mod_name pydantic_core

%def_with check

Name: python3-module-%pypi_name
Version: 2.14.5
Release: alt1

Summary: Core validation logic for pydantic written in rust
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pydantic-core
Vcs: https://github.com/pydantic/pydantic-core

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Source2: crates.tar

%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
BuildRequires: rust-cargo
BuildRequires: /proc
BuildRequires: libmimalloc-devel
BuildRequires: python3-dev

%if_with check
BuildRequires: python3-module-pytest-benchmark
%add_pyproject_deps_check_filter pydantic
%add_pyproject_deps_check_filter pytest-example
%add_pyproject_deps_check_filter pytest-speed
%add_pyproject_deps_check_filter pytest-codspeed
%pyproject_builddeps_check
%endif

%description
This package provides the core functionality for pydantic validation
and serialization.
Pydantic-core is currently around 17x faster than pydantic V1. See
tests/benchmarks/ for details.

%prep
%setup -a2
mkdir -p .cargo
cat << EOF > .cargo/config.toml
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[build]
rustflags = [
    "-C", "link-args=-lmimalloc",
]
EOF

%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile tests/requirements.txt
%endif

%build
export CARGO_HOME=${PWD}/cargo
%ifarch aarch64
# To avoid undefined symbols (start with '__aarch64_') which are specific for
# only aarch64 and which break tests
export CFLAGS="$CFLAGS -mno-outline-atomics"
%endif
%pyproject_build

%install
%pyproject_install

%check
# tests/benchmarks: do not execute benchmark tests
%pyproject_run_pytest --ignore='tests/benchmarks'

%files
%doc README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %mod_name}

%changelog
* Thu Nov 23 2023 Alexandr Shashkin <dutyrok@altlinux.org> 2.14.5-alt1
- 2.10.1 -> 2.14.5

* Fri Sep 29 2023 Alexandr Shashkin <dutyrok@altlinux.org> 2.10.1-alt1
- 2.6.3 -> 2.10.1

* Thu Aug 24 2023 Alexandr Shashkin <dutyrok@altlinux.org> 2.6.3-alt1
- 2.4.0 -> 2.6.3

* Tue Aug 15 2023 Alexandr Shashkin <dutyrok@altlinux.org> 2.4.0-alt1
- Initial build for Sisyphus

