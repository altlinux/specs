%define _unpackaged_files_terminate_build 1

%def_with check

Name: bookokrat
Version: 0.3.9
Release: alt2

Summary: A terminal EPUB / PDF Book Reader
License: AGPL-3.0-or-later
Group: Office
Url: https://bugzmanov.github.io/bookokrat/
VCS: https://github.com/bugzmanov/bookokrat.git

# Source-url: https://github.com/bugzmanov/%name/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: vendor-%version.tar
Patch1: alt-fix-active-terminal-detection.patch
Patch2: alt-fix-multibyte-character-search.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: cargo-vendor-checksum
BuildRequires: rust-cargo
BuildRequires: gcc-c++
BuildRequires: clang-devel
BuildRequires: libmupdf-devel
BuildRequires: unzip
%if_with check
BuildRequires: fontconfig-devel
%endif

%description
Terminal EPUB/PDF/DJVU reader focused on speed, smooth navigation, and
Vim-style workflows.

%prep
%setup -a1
%autopatch -p1
%rust_prep
cargo-vendor-checksum --vendor vendor --all

%build
export RUST_FONTCONFIG_DLOPEN=on
%rust_build

%install
%rust_install

%check
export SNAPSHOTS=overwrite
%rust_test

%files
%doc README.md
%_bindir/%name

%changelog
* Mon Apr 20 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.3.9-alt2
- fixes the missing display of opened from kitty when launched from another
  terminal (closes: 58767)
- fix a crash during multi-byte character search (closes: 58769)

* Thu Apr 09 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.3.9-alt1
- initial build for ALT Linux
