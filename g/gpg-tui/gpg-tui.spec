%define _unpackaged_files_terminate_build 1

Name: gpg-tui
Version: 0.11.0
Release: alt3

Summary: Terminal User Interface for GnuPG
License: MIT
Group: File tools
Url: https://github.com/orhun/gpg-tui
Vcs: https://github.com/orhun/gpg-tui

Source0: %name-%version.tar
Source1: vendor.tar

Patch0: gpg-tui-0.11.0-crate-nix-loongarch64-support.patch

BuildRequires: /proc
BuildRequires: rust-cargo
BuildRequires: libgpgme-devel
BuildRequires: libxcb-devel
BuildRequires: libxkbcommon-devel

%description
It aims to ease the key management operations such as listing/exporting/signing
by providing an interface along with the command-line fallback for more complex
operations. It is not trying to be a full-fledged interface for all the features
that gpg provides but it tries to bring a more interactive
approach to key management.

%prep
%setup -a1
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true
quiet = false

[install]
root = "%buildroot%prefix"

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1"]

[profile.release]
strip = false
EOF

%patch0 -p1
sed -i -e 's/"files":{[^}]*}/"files":{}/' \
    ./vendor/nix/.cargo-checksum.json

%build
cargo build %_smp_mflags --offline --release
mkdir completions/
OUT_DIR=completions/ target/release/gpg-tui-completions

%install
cargo install %_smp_mflags --offline --no-track --path .
install -Dm 644 man/%name.1 %buildroot/%_man1dir/%name.1
install -Dm 644 man/%name.toml.5 %buildroot/%_man5dir/%name.toml.5
install -Dm 644 completions/%name.bash \
    %buildroot/%_datadir/bash-completion/completions/%name
install -Dm 644 completions/%name.fish \
    %buildroot/%_datadir/fish/vendor_completions.d/%name.fish
install -Dm 644 completions/_%name \
    %buildroot/%_datadir/zsh/site-functions/_%name

%files
%doc README* demo LICENSE
%_bindir/%name
%_man1dir/%name.1*
%_man5dir/%name.toml.5*
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%_datadir/zsh/site-functions/_%name
%exclude %_bindir/%name-completions

%changelog
* Mon Jan 27 2025 Ilya Sorochan <k0tran@altlinux.org> 0.11.0-alt3
- Add patch for nix crate for loongarch64 support.

* Thu Nov 28 2024 Denis Rastyogin <gerben@altlinux.org> 0.11.0-alt2
- Removed unnecessary vendor files.

* Fri May 31 2024 Denis Rastyogin <gerben@altlinux.org> 0.11.0-alt1
- Initial build for ALT Sisyphus.
