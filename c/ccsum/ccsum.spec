Name:    ccsum
Version: 0.1.0
Release: alt1

Summary: Convenient Checksum
License: MIT
Group:   Other
Url:     https://github.com/sevenc-nanashi/ccsum
VCS:     https://github.com/sevenc-nanashi/ccsum.git

Source: %name-%version.tar
Source1: %name-vendor-%version.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc
BuildRequires: gcc-c++

%description
%summary

%prep
%setup -a1

mkdir -p .cargo
cat >> .cargo/config <<EOF
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
%doc LICENSE README.*
%_bindir/%name

%changelog
* Sun Jan 26 2025 Sergey Palcheh <minergenon@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus
