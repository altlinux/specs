%define _unpackaged_files_terminate_build 1

%def_with check
%def_with docs

Name: zoxide
Version: 0.9.0
Release: alt1

Summary:  A smarter cd command. Supports all major shells.
License: MIT
Group: System/Libraries

Url: https://github.com/ajeetdsouza/zoxide
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires: /proc
BuildRequires: rust
BuildRequires: rust-cargo

%description
zoxide is a smarter cd command, inspired by z and autojump.

It remembers which directories you use most frequently, so you can
"jump" to them in just a few keystrokes.  zoxide works on all major
shells.


%prep
%setup
%patch0 -p1

mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

sed -i -e '/^strip/ s/true/false/' Cargo.toml
sed -i -e '/^debug/ s/0/true/' Cargo.toml

%build
export CARGO_HOME=${PWD}/cargo
cargo build --release

%install
export CARGO_HOME=${PWD}/cargo
cargo install --force --root %buildroot/%_prefix --path ./ --no-track

install -Dm 0644 man/man1/* -t %buildroot%_man1dir
install -Dm 0644 contrib/completions/zoxide.bash \
	-t %buildroot%_datadir/bash-completion/completions/
install -Dm 0644 contrib/completions/_zoxide \
	-t %buildroot%_datadir/zsh/site-functions/
install -Dm 0644 contrib/completions/zoxide.fish \
	-t %buildroot%_datadir/fish/vendor_completions.d/

%check
export CARGO_HOME=${PWD}/cargo
cargo test --release

%files
%doc LICENSE README.md
%_bindir/*
%_man1dir/*
%_datadir/bash-completion/completions/zoxide.bash
%_datadir/zsh/site-functions/_zoxide
%_datadir/fish/vendor_completions.d/zoxide.fish

%changelog
* Tue Jan 10 2023 Egor Ignatov <egori@altlinux.org> 0.9.0-alt1
- 0.9.0

* Sat Sep 03 2022 Egor Ignatov <egori@altlinux.org> 0.8.3-alt1
- new version 0.8.3

* Mon Jun 27 2022 Egor Ignatov <egori@altlinux.org> 0.8.2-alt1
- new version 0.8.2

* Mon Apr 25 2022 Egor Ignatov <egori@altlinux.org> 0.8.1-alt1
- new version 0.8.1

* Tue Jan 18 2022 Egor Ignatov <egori@altlinux.org> 0.8.0-alt2
- spec: fix url

* Tue Jan 11 2022 Egor Ignatov <egori@altlinux.org> 0.8.0-alt1
- Firt build for ALT
