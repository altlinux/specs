%define _unpackaged_files_terminate_build 1

Name: dusage
Version: 0.3.6
Release: alt1
Summary: A command line disk usage information tool
License: MIT
Group: System/Base
Url: https://github.com/mihaigalos/dusage

ExcludeArch: i586

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: rust-cargo

%description
%summary.

%prep
%setup
%patch -p1
tar -xf %SOURCE1
mkdir -p .cargo
cat > .cargo/config.toml <<EOF
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
%doc README.md
%_bindir/%name

%changelog
* Wed Nov 20 2024 Pavel Shilov <zerospirit@altlinux.org> 0.3.6-alt1
- initial build for Sisyphus
