Name: wallust
Version: 3.3.0
Release: alt1

Summary: Generate colorschemes from images
License: MIT
Group: Graphics
Url: https://github.com/explosion-mental/wallust

# Source-url: https://github.com/explosion-mental/wallust/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust /proc

%description
Wallust is a fast color palette generator from images written in Rust.
It generates colorschemes and applies them to terminals, similar to pywal
but with better performance and more features.

%prep
%setup -a1

mkdir -p .cargo
cat > .cargo/config <<'EOF'
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build

%install
%rust_install

# Install man pages
install -Dpm 0644 man/wallust.1 %buildroot%_man1dir/wallust.1
install -Dpm 0644 man/wallust-cs.1 %buildroot%_man1dir/wallust-cs.1
install -Dpm 0644 man/wallust-run.1 %buildroot%_man1dir/wallust-run.1
install -Dpm 0644 man/wallust-theme.1 %buildroot%_man1dir/wallust-theme.1
install -Dpm 0644 man/wallust.5 %buildroot%_man5dir/wallust.5

# Install shell completions
install -Dpm 0644 completions/wallust.bash %buildroot%_datadir/bash-completion/completions/wallust
install -Dpm 0644 completions/_wallust %buildroot%_datadir/zsh/site-functions/_wallust
install -Dpm 0644 completions/wallust.fish %buildroot%_datadir/fish/vendor_completions.d/wallust.fish

%files
%_bindir/%name
%_man1dir/wallust*.1*
%_man5dir/wallust.5*
%_datadir/bash-completion/completions/wallust
%_datadir/zsh/site-functions/_wallust
%_datadir/fish/vendor_completions.d/wallust.fish
%doc README.md
%doc LICENSE

%changelog
* Sun Jan 19 2026 Vitaly Lipatov <lav@altlinux.ru> 3.3.0-alt1
- initial build for ALT Sisyphus
- add man pages and shell completions
