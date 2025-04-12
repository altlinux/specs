# tests require running PGSQL
%def_without check

Name: atuin
Version: 18.4.0
Release: alt1

Summary: Magical shell history

License: MIT
Group: Shells
Url: https://github.com/atuinsh/atuin

# Source-url: https://github.com/atuinsh/atuin/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
Atuin replaces your existing shell history with a SQLite database, and records
additional context for your commands. Additionally, it provides optional and
fully encrypted synchronization of your history between machines, via an Atuin
server.

%prep
%setup -a1

cat >.cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"
[source.vendored-sources]
directory = "vendor"
EOF
mkdir completions

%build
%rust_build
for sh in 'bash' 'fish' 'zsh'; do
    "target/release/atuin" gen-completions -s "$sh" -o completions/
done

%install
install -Dm 755 target/release/atuin -t %buildroot%_bindir
install -Dm 644 completions/atuin.bash %buildroot%_datadir/bash-completion/completions/atuin
install -Dm 644 completions/_atuin %buildroot%_datadir/zsh/site-functions/_atuin
install -Dm 644 completions/atuin.fish %buildroot%_datadir/fish/vendor_completions.d/atuin.fish

%files
%_bindir/atuin
%_datadir/bash-completion/completions/atuin
%_datadir/fish/vendor_completions.d/atuin.fish
%_datadir/zsh/site-functions/_atuin
%doc LICENSE

%changelog
* Sat Apr 12 2025 Boris Yumankulov <boria138@altlinux.org> 18.4.0-alt1
- initial build for ALT Sisyphus

