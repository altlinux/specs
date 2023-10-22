%def_with check

Name: bottom
Version: 0.9.6
Release: alt1
Summary: Yet another cross-platform graphical process/system monitor
License: MIT
Group: Monitoring
Url: https://clementtsang.github.io/bottom
Vcs: https://github.com/ClementTsang/bottom
Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: rust-cargo

%description
A customizable cross-platform graphical process/system monitor for the terminal.

%prep
%setup -a 1
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
%rust_install btm

%check
%rust_test

%files
%_bindir/btm

%changelog
* Sun Oct 22 2023 Alexander Makeenkov <amakeenk@altlinux.org> 0.9.6-alt1
- Updated to version 0.9.6.

* Thu Jan 26 2023 Alexander Makeenkov <amakeenk@altlinux.org> 0.8.0-alt1
- Initial build for ALT

