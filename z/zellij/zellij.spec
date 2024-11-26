Name:    zellij
Version: 0.41.2
Release: alt1

Summary: A terminal workspace with batteries included
License: MIT
Group:   Terminals
URL:     https://github.com/zellij-org/zellij
VCS:     https://github.com/zellij-org/zellij

ExclusiveArch: x86_64 aarch64

Source0: %name-%version.tar
Source1: vendor.tar
Source2: config.toml

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc
BuildRequires: perl-IPC-Cmd
BuildRequires: mandown

%description
Zellij is a workspace aimed at developers, ops-oriented people and
anyone who loves the terminal. Similar programs are sometimes called
"Terminal Multiplexers". Zellij is designed around the philosophy that
one must not sacrifice simplicity for power, taking pride in its great
experience out of the box as well as the advanced features it places at
its users' fingertips.

%prep
%setup -a1
install -vpD %SOURCE2 .cargo/config.toml

%build
%rust_build
for shell in "zsh" "bash" "fish"
do
  ./target/release/zellij setup --generate-completion "$shell" > ./target/zellij."$shell"
done
mandown docs/MANPAGE.md > ./target/zellij.1

%install
%rust_install
install -Dm644 -T ./target/zellij.bash %buildroot%_datadir/bash-completion/completions/zellij
install -Dm644 -T ./target/zellij.fish %buildroot%_datadir/fish/vendor_completions.d/zellij.fish
install -Dm644 -T ./target/zellij.zsh %buildroot%_datadir/zsh/site-functions/_zellij
install -Dm644 -T ./target/zellij.1 %buildroot%_man1dir/zellij.1
install -Dm644 -T %_builddir/%name-%version/assets/logo.png %buildroot%_datadir/pixmaps/%name.png
install -Dm644 -T %_builddir/%name-%version/assets/%name.desktop %buildroot%_datadir/applications/%name.desktop
cp -r ./example %buildroot%_datadir/example

# No tests because building plugins for tests requires wasm32-wasi std crate

%files
%doc *.md docs/*.md
%_bindir/zellij
%_man1dir/zellij.1*
%_datadir/pixmaps/*
%_datadir/applications/*
%_datadir/bash-completion/*
%_datadir/fish/*
%_datadir/zsh/*
%_datadir/example

%changelog
* Mon Nov 25 2024 Ilya Sorochan <k0tran@altlinux.org> 0.41.2-alt1
- Update version.

* Thu Nov 07 2024 Ilya Sorochan <k0tran@altlinux.org> 0.41.1-alt1
- Initial build for Sisyphus.
