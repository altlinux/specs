%define _unpackaged_files_terminate_build 1
%def_with check

Name: rustup
Version: 1.29.0
Release: alt2

Summary: The Rust toolchain installer
License: Apache-2.0 or MIT
Group: Development/Tools
Url: https://rust-lang.github.io/rustup/
Vcs: https://github.com/rust-lang/rustup

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: libssl-devel

%description
This is the Rust official toolchain manager. It's used for downloading
toolchains from official rust chanels such as "stable", "beta" and
"nightly".

%prep
%setup -a 1
%rust_prep

%build
%rust_build -F "no-self-update"

%install
install -Dm 755 "target/release/rustup-init" "%buildroot%_bindir/rustup"
ln -srv "%buildroot%_bindir/rustup" "%buildroot%_bindir/rustup-init"

# Fallback configuration.
mkdir -pv %buildroot%_sysconfdir/rustup
cat >%buildroot%_sysconfdir/rustup/settings.toml <<EOF
default_toolchain = "stable"
EOF

pushd %buildroot
mkdir -pv .%_datadir/bash-completion/completions/ .%_datadir/zsh/site-functions/ .%_datadir/fish/vendor_completions.d/

.%_bindir/rustup completions bash > .%_datadir/bash-completion/completions/rustup
.%_bindir/rustup completions zsh > .%_datadir/zsh/site-functions/_rustup
.%_bindir/rustup completions fish > .%_datadir/fish/vendor_completions.d/rustup.fish
popd

%check
# Skipped test either requires network or can't be ran in hasher.
%rust_test -F test --                       \
    --skip rustup-init                      \
    --skip check_updates_some               \
    --skip check_updates_none               \
    --skip store_static_roots               \
    --skip check_updates_with_update        \
    --skip rustup_init_ui_doc_text_tests    \
    --skip rustup_init_sh_help_flag stdout

%files
%doc LICENSE-MIT
%_bindir/rustup
%_bindir/rustup-init
%_sysconfdir/rustup
%_datadir/bash-completion/completions/rustup
%_datadir/zsh/site-functions/_rustup
%_datadir/fish/vendor_completions.d/rustup.fish

%changelog
* Fri May 29 2026 Sergey Zhidkih <rx1513@altlinux.org> 1.29.0-alt2
- Add shell completions (Closes: 49831).

* Thu Apr 23 2026 Sergey Zhidkih <rx1513@altlinux.org> 1.29.0-alt1
- Initial build.
