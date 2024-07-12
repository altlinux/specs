%define _unpackaged_files_terminate_build 1

Name: tealdeer
Version: 1.6.1
Release: alt2

Summary: A very fast implementation of tldr in Rust.
License: MIT and Apache-2.0
Group: Documentation
Vcs: https://github.com/dbrgn/tealdeer
Packager: Michael Chernigin <chernigin@altlinux.ru>

Source0: %name-%version.tar
ExcludeArch: ppc64le
BuildRequires: rust-cargo
BuildRequires: /proc
Conflicts: python3-module-tldr tlrc

%global bin_name tldr

%description
A very fast implementation of tldr in Rust: Simplified, example based and
community-driven man pages.

%prep
%setup -q
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
cargo build --offline --release

%install
mkdir -p %buildroot%_bindir
install -Dm0755 target/release/%bin_name %buildroot%_bindir/
install -Dm 0644 completion/bash_%name %buildroot%_datadir/bash-completion/completions/%name
install -Dm 0644 completion/fish_%name %buildroot%_datadir/fish/vendor_completions.d/%name.fish
install -Dm 0644 completion/zsh_%name  %buildroot%_datadir/zsh/site-functions/_%name

%check
cargo test -- --skip test_autoupdate_cache \
              --skip test_create_cache_directory_path \
              --skip test_pager_flag_enable \
              --skip test_quiet_cache \
              --skip test_quiet_failures \
              --skip test_quiet_old_cache \
              --skip test_spaces_find_command \
              --skip test_update_cache

%files
%doc LICENSE-APACHE
%doc LICENSE-MIT
%doc README.md
%_bindir/%bin_name
%_datadir/zsh/site-functions/_%name
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish

%changelog
* Fri Jul 12 2024 Alexander Stepchenko <geochip@altlinux.org> 1.6.1-alt2
- NMU: Add tlrc to the Conflicts.

* Tue Jul 17 2023 Michael Chernigin <chernigin@altlinux.org> 1.6.1-alt1
- Update to 7c371a68 from upstream, branch main
- Initial build for ALT Linux

