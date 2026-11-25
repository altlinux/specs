%define _unpackaged_files_terminate_build 1
%def_with check

# A 32-bit compiler runs out of address space with full debug info and fat LTO.
%ifarch i586
%define monty_release_profile --config 'profile.release.debug=false' --config 'profile.release.lto="off"' --config 'profile.release.codegen-units=16'
%else
%define monty_release_profile %{nil}
%endif

Name: monty
Version: 1.6.0
Release: alt1

Summary: Secure, snapshotable Python sandbox written in Rust
License: MIT
Group: Development/Other
Url: https://github.com/pydantic/monty
Vcs: https://github.com/pydantic/monty

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: rust-cargo >= 1.98
BuildRequires: gcc
BuildRequires: /proc

%description
Monty is a sandboxed Python interpreter written in Rust. It executes
untrusted Python code in a restricted runtime and provides a
command-line interface and a subprocess worker for isolated execution.

%prep
%setup -a1
%autopatch -p1
%rust_prep

%build
%ifarch i586
export RUSTFLAGS="${RUSTFLAGS} -C debuginfo=0"
cargo build --release %{?_smp_mflags} --offline -p monty-runtime --locked %monty_release_profile
%else
%rust_build -p monty-runtime --locked %monty_release_profile
%endif

%install
%rust_install

%check
%rust_test -p monty-runtime --locked %monty_release_profile

%files
%doc README.md LICENSE
%_bindir/%name

%changelog
* Tue Nov 24 2026 Andrey Kuzma <kuzmaav@altlinux.org> 1.6.0-alt1
- Initial build for ALT Sisyphus.
