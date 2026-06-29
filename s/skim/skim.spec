Name:    skim
Version: 4.10.0
Release: alt1

Summary: Fuzzy Finder in rust
License: MIT
Group:   Development/Tools
Url:     https://github.com/skim-rs/skim

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-rust
BuildRequires(pre): rpm-build-vim
BuildRequires: /proc

# Due to frizbee
ExclusiveArch: x86_64 aarch64

%description
Half of our life is spent on navigation: files, lines, commands...
You need skim!  It's a general fuzzy finder that saves you time.

%package tmux
Summary: Script for launching %name skim in a tmux pane
Group: Development/Tools
Requires: %name = %EVR

%description tmux
Script for launching %name in a tmux pane.

%package -n vim-plugin-%name
Summary: Vim plugin for %name
Group: Editors
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
# frizbee requires nightly toolchain
%rust_build \
    --no-default-features --features cli

%install
%rust_install sk
install -Dm 0755 bin/sk-tmux %buildroot%_bindir/sk-tmux

install -Dm 644 man/man1/*.1 -t %buildroot%_man1dir

install -Dm 644 shell/completion.zsh %buildroot%_datadir/zsh/site-functions/_sk
install -Dm 644 shell/completion.bash %buildroot%_datadir/bash-completion/completions/sk

install -Dm 644 plugin/skim.vim -t %buildroot%vim_runtime_dir/plugin/

%check
SK=%buildroot%_bindir/sk
[ "$(echo -e "apple\nbanana\ncherry" | "$SK" --filter "ban")" == banana ]

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
* Mon Jun 29 2026 Mikhail Gordeev <obirvalger@altlinux.org> 4.10.0-alt1
- new version 4.10.0

* Fri Jun 26 2026 Mikhail Gordeev <obirvalger@altlinux.org> 4.9.0-alt1
- new version 4.9.0

* Wed Jun 17 2026 Mikhail Gordeev <obirvalger@altlinux.org> 4.8.0-alt1
- new version 4.8.0

* Fri May 22 2026 Mikhail Gordeev <obirvalger@altlinux.org> 4.7.0-alt1
- new version 4.7.0

* Mon May 04 2026 Mikhail Gordeev <obirvalger@altlinux.org> 4.6.2-alt1
- new version 4.6.2

* Mon Apr 27 2026 Mikhail Gordeev <obirvalger@altlinux.org> 4.6.1-alt1
- new version 4.6.1

* Fri Apr 24 2026 Mikhail Gordeev <obirvalger@altlinux.org> 4.6.0-alt1
- new version 4.6.0

* Fri Mar 13 2026 Mikhail Gordeev <obirvalger@altlinux.org> 4.0.0-alt1
- new version 4.0.0

* Fri Jan 30 2026 Mikhail Gordeev <obirvalger@altlinux.org> 1.11.2-alt1
- new version 1.11.2

* Sun Jan 12 2025 Mikhail Gordeev <obirvalger@altlinux.org> 0.15.7-alt2
- Fix completions path

* Thu Jan 09 2025 Mikhail Gordeev <obirvalger@altlinux.org> 0.15.7-alt1
- Initial build for Sisyphus
