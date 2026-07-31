%define _unpackaged_files_terminate_build 1

Name: pik
Version: 1.0.0
Release: alt1
Summary: Process Interactive Kill.
License: MIT
Group: System/Base
Url: https://github.com/jacek-kurlit/pik

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: rust-cargo

%description
Process Interactive Kill is a command line tool that helps to find and kill process.
It works like pkill command but search is interactive.

%prep
%setup -a 1
%autopatch -p1

%build
mkdir -p .cargo
cat > .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%rust_build

%install
%rust_install

%files
%doc *.md
%_bindir/%name

%changelog
* Fri Jul 31 2026 Pavel Shilov <zerospirit@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus.