%define _unpackaged_files_terminate_build 1

Name: oha
Version: 1.9.0
Release: alt1
Summary: Ohayou, HTTP load generator with tui animation
License: MIT
Group: Networking/Remote access
Url: https://github.com/hatoo/oha

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: rust-cargo
BuildRequires: pkgconfig(openssl)

%description
Oha is a tiny program that sends some load to a web application and show
realtime tui inspired by rakyll/hey.

%prep
%setup -a 1
%patch -p1
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF

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
%doc README.md CHANGELOG.md
%_bindir/%name

%changelog
* Fri Jul 11 2025 Pavel Shilov <zerospirit@altlinux.org>  1.9.0-alt1
- Initial build for Sisyphus.
