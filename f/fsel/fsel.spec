%define _unpackaged_files_terminate_build 1

Name: fsel
Version: 3.5.2
Release: alt1

Summary: Fast TUI app launcher for GNU/Linux and *BSD 
License: BSD-2-Clause
Group: Development/Tools
Url: https://github.com/Mjoyufull/fsel
VCS: https://github.com/Mjoyufull/fsel

Requires: cclip

# Source-url: https://github.com/Mjoyufull/%name/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar
Source1: vendor-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: cargo-vendor-checksum
BuildRequires: rust-cargo

%description
%summary

%prep
%setup -a1
%rust_prep
cargo-vendor-checksum --vendor vendor --all

%build
%rust_build

%install
%rust_install

mkdir -p %buildroot%_datadir/%name
install -pm 644 {config,keybinds,color_examples}.toml \
    %buildroot%_datadir/%name/

%files
%doc README.md USAGE.md
%_bindir/%name
%_datadir/%name

%changelog
* Thu Jun 18 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 3.5.2-alt1
- new version

* Wed May 13 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 3.5.1-alt1
- new version

* Tue May 12 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 3.5.0-alt1
- new version

* Mon Apr 20 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 3.4.1-alt1
- new version

* Wed Apr 15 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 3.4.0-alt1
- new version

* Tue Apr 07 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 3.3.1-alt2
- fixed an error when starting fsel with `--cclip` flag (closes: 58544)

* Mon Mar 30 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 3.3.1-alt1
- initial build for ALT Linux
