%global _unpackaged_files_terminate_build 1

Name: xfr
Version: 0.9.18
Release: alt1
Summary: A modern iperf3 alternative with a live TUI
License: MIT or Apache-2.0
Group: Monitoring
Url: https://crates.io/crates/xfr
VCS: https://github.com/lance0/xfr

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
A modern iperf3 alternative with a live TUI,
multi-client server, MPTCP, and QUIC support.
Built in Rust.

%prep
%setup -a 1
%rust_prep

%build
%rust_build
target/release/%name --completions bash > %name.bash
target/release/%name --completions zsh > %name.zsh
target/release/%name --completions fish > %name.fish

%install
%rust_install

install -Dm 0644 %name.bash %buildroot%_datadir/bash-completion/completions/%name
install -Dm 0644 %name.zsh %buildroot%_datadir/zsh/site-functions/_%name
install -Dm 0644 %name.fish %buildroot%_datadir/fish/vendor_completions.d/%name.fish

%check
%rust_test

%files
%_bindir/%name
%_datadir/zsh/site-functions/_%name
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish

%changelog
* Fri Jun 12 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.9.18-alt1
- Updated to version 0.9.18.

* Sat May 09 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.9.14-alt1
- Updated to version 0.9.14.

* Sat May 02 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.9.11-alt1
- Initial build for ALT.
