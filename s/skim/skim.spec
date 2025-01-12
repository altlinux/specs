Name:    skim
Version: 0.15.7
Release: alt2

Summary: Fuzzy Finder in rust
License: MIT
Group:   Development/Tools
Url:     https://github.com/skim-rs/skim

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-rust
BuildRequires(pre): rpm-build-vim
BuildRequires: /proc

%description
Half of our life is spent on navigation: files, lines, commands...
You need skim!  It's a general fuzzy finder that saves you time.

%package tmux
Summary: Script for launching %name skim in a tmux pane
Group: Development/Tools
BuildArch: noarch
Requires: %name = %EVR

%description tmux
Script for launching %name in a tmux pane.

%package -n vim-plugin-%name
Summary: Vim plugin for %name
Group: Editors
BuildArch: noarch
Requires: %_bindir/vim
Requires: %name = %EVR

%description -n vim-plugin-%name
Vim plugin for %name

%prep
%setup
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build

%install
%rust_install sk
install -Dm 0755 bin/sk-tmux %buildroot%_bindir/sk-tmux

install -Dm 644 man/man1/*.1 -t %buildroot%_man1dir

install -Dm 644 shell/completion.zsh %buildroot%_datadir/zsh/site-functions/_sk
install -Dm 644 shell/completion.bash %buildroot%_datadir/bash-completion/completions/sk

install -Dm 644 plugin/skim.vim -t %buildroot%vim_runtime_dir/plugin/

%check
%rust_test

%files
%doc *.md
%_bindir/sk
%_datadir/zsh/site-functions/_sk
%_datadir/bash-completion/completions/sk
%_man1dir/sk.1*

%files tmux
%_bindir/sk-tmux
%_man1dir/sk-tmux.1*

%files -n vim-plugin-%name
%vim_runtime_dir/plugin/*

%changelog
* Sun Jan 12 2025 Mikhail Gordeev <obirvalger@altlinux.org> 0.15.7-alt2
- Fix completions path

* Thu Jan 09 2025 Mikhail Gordeev <obirvalger@altlinux.org> 0.15.7-alt1
- Initial build for Sisyphus
