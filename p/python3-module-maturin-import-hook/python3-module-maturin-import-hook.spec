%define _unpackaged_files_terminate_build 1
# Disable tests, most of them require an internet connection, multiple versions
# of pyo3 libraries that aren't allowed in cargo (offline) and also require a
# .git directory.  @sbolshakov (python3-module-maturin maintainer) About
# 'maturin new\init functions': I don't see any need to support additional
# functionality, at least for now.
%def_without check
%define pypi_name maturin-import-hook

Name: python3-module-%pypi_name
Version: 0.3.0
Release: alt1

Summary: A python import hook to automatically rebuild maturin projects
License: MIT
Group: Development/Python3
Url: https://www.maturin.rs/import_hook
Vcs: https://github.com/PyO3/maturin-import-hook.git
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Source2: %name-%version-tests-maturin.tar
Source3: %name-%version-vendor.tar
Source4: replace_pyo3_versions.sh
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
%pyproject_builddeps_build

BuildRequires(pre): rpm-build-pyproject
BuildRequires: /proc

%if_with check
%pyproject_builddeps_metadata
BuildRequires: python3-module-maturin
BuildRequires: python3-module-uv
BuildRequires: python3-module-boltons
%endif

%description
A python import hook to automatically rebuild maturin projects and import
stand-alone rust files.  Using this import hook reduces friction when
developing mixed python/rust codebases because changes made to rust components
take effect automatically like changes to python components do.

%prep
%setup
%if_with check
%autopatch -p1
tar -xf %SOURCE2
tar -xf %SOURCE3
cp %SOURCE4 .
chmod +x replace_pyo3_versions.sh
./replace_pyo3_versions.sh

mkdir -pv .cargo
cat >> .cargo/config.toml <<EOF

[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF
%endif

%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
export CARGO_HOME="$PWD/.cargo/"
%__python3 tests/runner.py \
  --workspace ./test_workspace \
  "tests/test_import_hook" \
  #

%files
%python3_sitelibdir_noarch/maturin_import_hook/
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}

%changelog
* Sun Jun 29 2025 Ivan Khanas <xeno@altlinux.org> 0.3.0-alt1
- First build for ALT.
