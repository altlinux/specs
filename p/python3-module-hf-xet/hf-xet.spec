%define _unpackaged_files_terminate_build 1
%define mod_name hf_xet
%define pypi_name hf-xet

%def_with check

Name: python3-module-%pypi_name
Version: 1.4.2
Release: alt1
Summary: hf-xet xet client tech, used in huggingface_hub
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/hf-xet/
Vcs: https://github.com/huggingface/xet-core
ExcludeArch: i586

Source: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-pyproject rpm-macros-rust rpm-build-rust
BuildRequires: python3-module-maturin
BuildRequires: python3(wheel)
BuildRequires: python
BuildRequires: gdb
BuildRequires: build-essential
BuildRequires: rust-cargo
BuildRequires: rust-src
BuildRequires: pkgconfig(libssh2)
BuildRequires: liblmdb-devel

Requires: python3-module-huggingface-hub

%if_with check
BuildRequires: python3(pytest)
%endif

%py3_provides %pypi_name

%description
%summary

%prep
%setup -a1
%autopatch -p1
#mkdir -p .cargo
#cat > .cargo/config.toml <<EOF
#[source.crates-io]
#replace-with = "vendored-sources"
#
#[source.vendored-sources]
#directory = "vendor"
#EOF
cd %mod_name
mkdir -p .cargo
cat > .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF


%build
export MAPFILE="%{_builddir}/%{name}-%{version}/exports.map"
cat > "$MAPFILE" <<'EOF'
EXPORTS {
    global: PyInit_hf_xet;
    local: *;
};
EOF
export CARGO_NET_OFFLINE=true
export CFLAGS="${CFLAGS:-} -fvisibility=hidden"
export CXXFLAGS="${CXXFLAGS:-} -fvisibility=hidden"
# export RUSTFLAGS="-C link-arg=-Wl,--gc-sections -C link-arg=-Wl,--exclude-libs,ALL -C link-arg=-Wl,--version-script=$MAPFILE"
export CARGO_PROFILE_RELEASE_LTO=fat
export CARGO_PROFILE_RELEASE_CODEGEN_UNITS=1
export CARGO_PROFILE_RELEASE_OPT_LEVEL=s
export MATURIN_BUILD_ARGS=--release
export ZSTD_SYS_USE_PKG_CONFIG=1
cd %mod_name
%pyproject_build

%install
cd %mod_name
%pyproject_install

%check
#pyproject_run_pytest 

%files
%doc *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Mar 27 2026 Pavel Shilov <zerospirit@altlinux.org> 1.4.2-alt1
- Update to new version 1.4.2.

* Fri Nov 28 2025 Pavel Shilov <zerospirit@altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus.
