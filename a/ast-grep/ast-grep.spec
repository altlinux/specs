%define _unpackaged_files_terminate_build 1

Name: ast-grep
Version: 0.44.0
Release: alt1

Summary: A CLI tool for code structural search, lint and rewriting
License: MIT
Group: Development/Tools
Url: https://ast-grep.github.io
VCS: https://github.com/ast-grep/ast-grep

# Source-url: https://github.com/ast-grep/%name/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar
Source1: vendor-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: cargo-vendor-checksum
BuildRequires: rust-cargo

%description
ast-grep(sg) is a CLI tool for code structural search, lint, and
rewriting.

%prep
%setup -a1
rm -rf .cargo
%rust_prep
cargo-vendor-checksum --vendor vendor --all

%build
%rust_build

%install
%rust_install

%files
%doc README.md
%_bindir/%name

%changelog
* Mon Jun 22 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.44.0-alt1
- new version

* Wed May 27 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.43.0-alt1
- new version

* Wed May 20 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.42.3-alt1
- new version

* Tue May 12 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.42.2-alt1
- new version

* Tue Apr 06 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.42.1-alt1
- new version

* Tue Mar 17 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.42.0-alt1
- new version

* Wed Mar 11 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.41.1-alt1
- new version

* Thu Feb 26 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.41.0-alt1
- new version

* Mon Feb 16 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.40.5-alt1
- initial build for ALT Linux