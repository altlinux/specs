%define _unpackaged_files_terminate_build 1
%define pypi_name granian
%define mod_name %pypi_name

# Link Time Optimization causes undefined symbols and makes granian unusable
# so it should be turned off.
%global optflags %(echo '%optflags' | sed 's/-flto=auto/-fno-lto/')

%def_with check

Name: python3-module-%pypi_name
Version: 2.8.2
Release: alt1

Summary: Rust HTTP server for Python applications built on top of Hyper and Tokio
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/granian/
Vcs: https://github.com/emmett-framework/granian

Source0: %name-%version.tar
Source1: vendor.tar
Source2: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-macros-pyproject
%pyproject_builddeps_build
BuildRequires: rpm-build-pyproject
BuildRequires: python3-dev
BuildRequires: /proc
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
BuildRequires: python3-module-pytest-timeout
%endif

%description
Granian is a Rust HTTP server for Python applications built on top of
Hyper and Tokio.

The main reasons behind Granian design are:
* Have a single, correct HTTP implementation, supporting versions 1, 2
  (and eventually 3).
* Provide a single package for several platforms.
* Avoid the usual Gunicorn + uvicorn + http-tools dependency
  composition on unix systems.
* Provide stable performance when compared to existing alternatives.

%prep
%setup -a1
mkdir -p .cargo
cat << EOF > .cargo/config.toml
[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://github.com/gi0baro/pyo3-log.git?branch=pyo3-027"]
git = "https://github.com/gi0baro/pyo3-log.git"
branch = "pyo3-027"
replace-with = "vendored-sources"

[source."git+https://github.com/gi0baro/tls-listener.git?branch=0.11.x"]
git = "https://github.com/gi0baro/tls-listener.git"
branch = "0.11.x"
replace-with = "vendored-sources"

[source."git+https://github.com/kotauskas/interprocess.git?\
rev=44351c4fe88c72ead4f3b0b762c4cf45beb90841"]
git = "https://github.com/kotauskas/interprocess.git"
rev = "44351c4fe88c72ead4f3b0b762c4cf45beb90841"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[install]
root = "%buildroot%prefix"

[profile.release]
strip = "none"
EOF
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup test
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- python3 -P -m pytest --session-timeout=300 --full-trace tests/

%files
%doc README.md LICENSE
%_bindir/%mod_name
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Sep 01 2026 Andrey Kuzma <kuzmaav@altlinux.org> 2.8.2-alt1
- Initial build for Sisyphus.
