%define _unpackaged_files_terminate_build 1

Name: boulette
Version: 0.2.3
Release: alt1
Summary: A terminal confirmation prompt that prevents you from accidentally damaging remote hosts.
License: GPL-2.0
Group: Networking/Remote access
Url: https://github.com/pipelight/boulette

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-rust
BuildRequires: rust-cargo
BuildRequires: rust
BuildRequires: zstd

%description
Boulette prevents you from accidentally damaging remote hosts by raising a
warning prompt on dangerous commands. The prompt simply asks for user
confirmation, and can also enforce a challenge resolution to decide whether to
resume(or abort) the command.

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

%check
%rust_test

%files
%doc CHANGELOG.md README.md
%_bindir/*

%changelog
* Wed May 07 2024 Pavel Shilov <zerospirit@altlinux.org> 0.2.3-alt1
- initial build for Sisyphus.
