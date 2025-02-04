%define _unpackaged_files_terminate_build 1

%define bash_completionsdir %_datadir/bash-completion/completions
%define zsh_completionsdir %_datadir/zsh/site-functions
%define fish_completionsdir %_datadir/fish/vendor_completions.d

Name: asciinema
Version: 3.0.0
Release: alt1.rc3

Summary: Terminal session recorder
License: GPLv3
Group: Terminals
Url: https://asciinema.org
Vcs: https://github.com/asciinema/asciinema

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires: /proc
BuildRequires: rust-cargo

%description
asciinema [as-kee-nuh-muh] is a free and open source solution for
recording terminal sessions and sharing them on the web.

%prep
%setup -a1
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true
quiet = false

[install]
root = "%buildroot%_prefix"

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1"]

[profile.release]
strip = false
EOF

%build
export ASCIINEMA_GEN_DIR=doc
cargo build --release %{?_smp_mflags} --all-targets --offline

%install
install -Dp target/release/%name -t %buildroot%_bindir

# add shell completion
install -Dm 644 doc/completion/%name.bash %buildroot%bash_completionsdir/%name
install -Dm 644 doc/completion/_%name %buildroot%zsh_completionsdir/_%name
install -Dm 644 doc/completion/%name.fish %buildroot%fish_completionsdir/%name.fish

# add man pages
install -Dm 644 doc/man/%name.1 %buildroot%_man1dir/%name.1
install -Dm 644 doc/man/%name-auth.1 %buildroot%_man1dir/%name-auth.1
install -Dm 644 doc/man/%name-cat.1 %buildroot%_man1dir/%name-cat.1
install -Dm 644 doc/man/%name-convert.1 %buildroot%_man1dir/%name-convert.1
install -Dm 644 doc/man/%name-play.1 %buildroot%_man1dir/%name-play.1
install -Dm 644 doc/man/%name-rec.1 %buildroot%_man1dir/%name-rec.1
install -Dm 644 doc/man/%name-stream.1 %buildroot%_man1dir/%name-stream.1
install -Dm 644 doc/man/%name-upload.1 %buildroot%_man1dir/%name-upload.1

%files
%_bindir/%name
%doc README.md
%_man1dir/%{name}*
%bash_completionsdir/%name
%zsh_completionsdir/_%name
%fish_completionsdir/%name.fish

%changelog
* Tue Feb 04 2025 Denis Sergeev <zeff@altlinux.org> 3.0.0-alt1.rc3
- 3.0.0-rc3.

* Sat Dec  8 2018 Terechkov Evgenii <evg@altlinux.org> 2.0.1-alt1
- 2.0.1

* Mon Feb 19 2018 Terechkov Evgenii <evg@altlinux.org> 2.0.0-alt1
- 2.0.0

* Sun Sep  3 2017 Terechkov Evgenii <evg@altlinux.org> 1.4.0-alt1
- Initial build for ALT Linux Sisyphus
