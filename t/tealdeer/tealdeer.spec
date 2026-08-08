%global _unpackaged_files_terminate_build 1
%global bin_name tldr
%def_with check

Name: tealdeer
Version: 1.8.1
Release: alt1
Summary: A very fast implementation of tldr in Rust
License: MIT and Apache-2.0
Group: Documentation
URL: https://tealdeer-rs.github.io/tealdeer
VCS: https://github.com/tealdeer-rs/tealdeer

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

Conflicts: tlrc
Conflicts: python3-module-tldr

%description
A very fast implementation of tldr in Rust: Simplified,
example based and community-driven man pages.

%prep
%setup -a1
%rust_prep

%build
%rust_build

%install
%rust_install %bin_name
install -Dm 0644 completion/bash_%name %buildroot%_datadir/bash-completion/completions/%bin_name
install -Dm 0644 completion/fish_%name %buildroot%_datadir/fish/vendor_completions.d/%bin_name.fish
install -Dm 0644 completion/zsh_%name  %buildroot%_datadir/zsh/site-functions/_%bin_name

%check
# Integration tests build the binary with Cargo themselves. Running them under
# `cargo test` deadlocks because Cargo keeps the target-directory lock while
# the test binary is running. Build the test binary first, then run it after
# Cargo has released the lock. Network-dependent tests are not suitable for
# the build environment.
tealdeer_target=$(rustc -vV | sed -n 's/^host: //p')
cargo build --release %{?_smp_mflags} --target "$tealdeer_target"
cargo test --release %{?_smp_mflags} --features ignore-online-tests --no-run --test lib
find target/release/deps -maxdepth 1 -type f -name 'lib-*' -executable -exec {} --test-threads=1 \;

%files
%_bindir/%bin_name
%_datadir/zsh/site-functions/_%bin_name
%_datadir/bash-completion/completions/%bin_name
%_datadir/fish/vendor_completions.d/%bin_name.fish

%changelog
* Sat Aug 08 2026 Alexander Makeenkov <amakeenk@altlinux.org> 1.8.1-alt1
- Updated to version 1.8.1.
- Fixed shell completions packaging.

* Fri Jul 12 2024 Alexander Stepchenko <geochip@altlinux.org> 1.6.1-alt2
- NMU: Add tlrc to the Conflicts.

* Mon Jul 17 2023 Michael Chernigin <chernigin@altlinux.org> 1.6.1-alt1
- Update to 7c371a68 from upstream, branch main
- Initial build for ALT Linux
