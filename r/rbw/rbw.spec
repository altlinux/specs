Name: rbw
Version: 1.11.1
Release: alt1

Summary: Unofficial bitwarden cli

License: MIT
Group: Other
Url: https://git.tozt.net/rbw

# Source-url: https://git.tozt.net/rbw/snapshot/rbw-%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
This is an unofficial command line client for Bitwarden. Although it does come with its own command line client,
this client is limited by being stateless - to use it, you're required to manually lock and unlock the client,
and pass the temporary keys around in environment variables, which makes it very difficult to use.
This client avoids this problem by maintaining a background process which is able to hold the keys in memory,
similar to the way that ssh-agent or gpg-agent work. This allows the client to be used in a much simpler way,
with the background agent taking care of maintaining the necessary state.

%prep
%setup -a 1

mkdir .cargo
cat >.cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"
[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build

cargo run --release --locked --bin rbw -- gen-completions bash >bash-completions
cargo run --release --locked --bin rbw -- gen-completions zsh >zsh-completions
cargo run --release --locked --bin rbw -- gen-completions fish >fish-completions

%install
install -Dm 755 target/release/rbw -t %buildroot%_bindir
install -Dm 755 target/release/rbw-agent -t %buildroot%_bindir
install -Dm 644 bash-completions %buildroot%_datadir/bash-completion/completions/rbw
install -Dm 644 zsh-completions %buildroot%_datadir/zsh/site-functions/_rbw
install -Dm 644 fish-completions %buildroot%_datadir/fish/vendor_completions.d/rbw.fish

%files
%_bindir/rbw
%_bindir/rbw-agent
%_datadir/bash-completion/completions/rbw
%_datadir/fish/vendor_completions.d/rbw.fish
%_datadir/zsh/site-functions/_rbw

%changelog
* Tue Jul 23 2024 Ivan Mazhukin <vanomj@altlinux.org> 1.11.1-alt1
- new version 1.11.1 (with rpmrb script)

* Sat May 25 2024 Ivan Mazhukin <vanomj@altlinux.org> 1.10.2-alt1
- new version 1.10.2 (with rpmrb script)

* Wed May 08 2024 Ivan Mazhukin <vanomj@altlinux.org> 1.10.0-alt1
- initial build for ALT Sisyphus

