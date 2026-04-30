%define _unpackaged_files_terminate_build 1
%define icu_ver %(echo %{feature_icu} | tr -d .)

Name: edit
Version: 2.0.0
Release: alt1

Summary: A simple editor for simple needs

License: MIT
Group: Editors
Url: https://github.com/microsoft/edit

# Source-url: https://github.com/microsoft/edit/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

Patch: edit-1.2.0-alt-enable-debug-info-for-rpm.patch

# Fix icu tests called Result::unwrap() on an Err value: Error(0)
Patch1: edit-2.0.0-alt-revert-Fix-zero-width-regex-replace.patch

BuildRequires(pre): rpm-macros-rust rpm-macros-features
BuildRequires: rpm-build-rust
BuildRequires: libicu%icu_ver

%description
An editor that pays homage to the classic MS-DOS Editor, but with a modern interface and input controls similar to VS Code.

%prep
%setup -a1
%patch -p1
%patch1 -p1

cat >.cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"
[source.vendored-sources]
directory = "vendor"
EOF

%build
export EDIT_CFG_ICUUC_SONAME=libicuuc.so.%icu_ver
export EDIT_CFG_ICUI18N_SONAME=libicui18n.so.%icu_ver
export EDIT_CFG_ICU_RENAMING_VERSION=%icu_ver

%rust_build

%install
install -Dm 755 target/release/edit -t %buildroot%_bindir

%check
%rust_test

%files
%_bindir/edit
%doc LICENSE

%changelog
* Wed Apr 29 2026 Boris Yumankulov <boria138@altlinux.org> 2.0.0-alt1
- new version 2.0.0

* Tue Sep 09 2025 Boris Yumankulov <boria138@altlinux.org> 1.2.0-alt2
- add icu dependency (ALT bug: 55886)

* Sun Jun 22 2025 Boris Yumankulov <boria138@altlinux.org> 1.2.0-alt1
- initial build for ALT Sisyphus


