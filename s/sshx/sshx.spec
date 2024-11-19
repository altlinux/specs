%define _unpackaged_files_terminate_build 1

Name: sshx
Version: 0.2.5
Release: alt1
Summary: Fast, collaborative live terminal sharing over the web.
License: MIT 
Group: Networking/Remote access
Url: https://sshx.io/
Vcs: https://github.com/ekzhang/sshx

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch
ExcludeArch: ppc64le

BuildRequires(pre): rpm-build-rust 
BuildRequires: rust-cargo
BuildRequires: protobuf-compiler
BuildRequires: rust

%description
%summary

%prep
%setup
%patch -p1
tar -xf %SOURCE1
mkdir -p .cargo
cat > .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"
 
[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build

%install
%rust_install

%files
%doc README.md
%_bindir/*

%changelog
* Sat Nov 02 2024 Pavel Shilov <zerospirit@altlinux.org> 0.2.5-alt1
- initial build for Sisyphus
