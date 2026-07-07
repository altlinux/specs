%define _unpackaged_files_terminate_build 1
%define pypi_name pdoc-pyo3-sample-library
%define module_name pdoc_pyo3_sample_library

Name: python3-module-%pypi_name
Version: 1.0.11
Release: alt1

Summary: This is a sample PyO3 library used for testing pdoc
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pdoc-pyo3-sample-library/
Vcs: https://github.com/mitmproxy/pdoc-pyo3-sample-library

Source0: %name-%version.tar
Source1: vendor.tar
Source2: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-macros-pyproject
%pyproject_builddeps_build
BuildRequires: rpm-build-pyproject
BuildRequires: python3-dev
BuildRequires: /proc

%description
%summary.

%prep
%setup -a1
mkdir -p ".cargo"
cat << EOF > .cargo/config.toml
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
sed -i '/^version/s/= ".*"/= "%version"/' Cargo.toml

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md LICENSE
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Jul 07 2026 Andrey Kuzma <kuzmaav@altlinux.org> 1.0.11-alt1
- Initial build for Sisyphus.
