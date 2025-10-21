%define _unpackaged_files_terminate_build 1

Name: theclicker
Version: 0.2.3
Release: alt1

Summary: A simple linux (xorg/wayland) autoclicker!
License: MIT
Group: Games/Other
Url: https://github.com/konkitoman/autoclicker
Vcs: https://github.com/konkitoman/autoclicker.git

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: rust-cargo
BuildRequires: /proc

%description
Working on xorg and wayland.
Is using uinput and evdev!

%prep
%setup -a1
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

%check
%rust_test

%files
%doc LICENSE README.md
%_bindir/theclicker

%changelog
* Sun Oct 19 2025 Ajrat Makhmutov <rauty@altlinux.org> 0.2.3-alt1
- First build for ALT.
