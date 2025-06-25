%define _unpackaged_files_terminate_build 1

Name: edit
Version: 1.2.0
Release: alt1

Summary: A simple editor for simple needs

License: MIT
Group: Editors
Url: https://github.com/microsoft/edit

# Source-url: https://github.com/microsoft/edit/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

Patch: edit-1.2.0-alt-enable-debug-info-for-rpm.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
An editor that pays homage to the classic MS-DOS Editor, but with a modern interface and input controls similar to VS Code.

%prep
%setup -a1
%patch -p1

cat >.cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"
[source.vendored-sources]
directory = "vendor"
EOF

%build
# allow nightly features
export RUSTC_BOOTSTRAP=1
%rust_build

%install
install -Dm 755 target/release/edit -t %buildroot%_bindir

%check
export RUSTC_BOOTSTRAP=1
%rust_test

%files
%_bindir/edit
%doc LICENSE

%changelog
* Sun Jun 22 2025 Boris Yumankulov <boria138@altlinux.org> 1.2.0-alt1
- initial build for ALT Sisyphus


