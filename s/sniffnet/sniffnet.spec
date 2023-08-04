%define _unpackaged_files_terminate_build 1

Name: sniffnet
Version: 1.1.3
Release: alt1

Summary: Application to comfortably monitor your network traffic
License: Apache-2.0 or MIT
Group: Networking/Other
Url: https://github.com/GyulyVGC/sniffnet

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rust-cargo
BuildRequires: /proc
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libssl-devel
BuildRequires: libalsa-devel
BuildRequires: fontconfig-devel
BuildRequires: libpcap-devel

%description
%summary

%prep
%setup -a1
mkdir .cargo
cat << EOF >> .cargo/config.toml
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%ifarch i586 armh
# Do not append '-g' to RUSTFLAGS. It's needed because passing '-g' option
# leads to "out of memory" error on 32-bit machines.
cargo build --release %{?_smp_mflags} --offline
%else
%rust_build
%endif

%install
%rust_install

%files
%_bindir/*
%doc README.md LICENSE*

%changelog
* Mon Jul 24 2023 Alexandr Shashkin <dutyrok@altlinux.org> 1.1.3-alt1
- Initial build for Sisyphus

