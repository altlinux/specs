%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define bash_completionsdir %_datadir/bash-completion/completions
%define fish_completionsdir %_datadir/fish/vendor_completions.d
%define zsh_completionsdir %_datadir/zsh/site-functions

Name: codewhale
Version: 0.8.64
Release: alt1

Summary: Agentic coding terminal
License: MIT
Group: Development/Tools
Url: https://codewhale.net/en
Vcs: https://github.com/Hmbown/CodeWhale

# Old architectures run out of memory during building (link-time).
# NOTE: there are few ways to fix that, but it is better to drop
#       support of 32-bit architectures at all.
ExcludeArch: %ix86

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: config.toml
Patch0: %name-%version-alt.patch

# Was 'deepseek-tui' in the past and rebranded without incompatibility
Provides: deepseek-tui
Obsoletes: deepseek-tui

BuildRequires: rust-cargo
BuildRequires: libdbus-devel

%description
DeepSeek-first agentic terminal for open source and open-weight coding
models. It runs from the codewhale command, streams reasoning blocks,
edits local workspaces with approval gates, and can auto-route each
turn to the right DeepSeek model and thinking level.

%prep
%setup -a1
%autopatch -p1
install -vpD %SOURCE2 .cargo/config.toml

%build
cargo build %_smp_mflags --release --offline

%install
install -vpD -m0755 target/release/codew -t %buildroot%_bindir
install -vpD -m0755 target/release/codewhale -t %buildroot%_bindir
install -vpD -m0755 target/release/codewhale-tui -t %buildroot%_bindir

mkdir -p %buildroot%bash_completionsdir
mkdir -p %buildroot%fish_completionsdir
mkdir -p %buildroot%zsh_completionsdir

%buildroot%_bindir/codewhale completions bash \
    > %buildroot%bash_completionsdir/codewhale
%buildroot%_bindir/codewhale completions fish \
    > %buildroot%fish_completionsdir/codewhale.fish
%buildroot%_bindir/codewhale completions zsh \
    > %buildroot%zsh_completionsdir/_codewhale

%files
%doc CHANGELOG.md LICENSE README.md
%_bindir/codew
%_bindir/codewhale
%_bindir/codewhale-tui
%bash_completionsdir/codewhale
%fish_completionsdir/codewhale.fish
%zsh_completionsdir/_codewhale

%changelog
* Wed Jun 24 2026 Anton Zhukharev <ancieg@altlinux.org> 0.8.64-alt1
- Updated to 0.8.64.
- Dropped /usr/bin/codewhale-app-server.

* Mon Jun 15 2026 Anton Zhukharev <ancieg@altlinux.org> 0.8.60-alt1
- Updated to 0.8.60.

* Wed Jun 03 2026 Anton Zhukharev <ancieg@altlinux.org> 0.8.52-alt1
- Updated to 0.8.52.
- Stopped building for i586 machines.

* Tue Jun 02 2026 Anton Zhukharev <ancieg@altlinux.org> 0.8.50-alt1
- Updated to 0.8.50.

* Mon Jun 01 2026 Anton Zhukharev <ancieg@altlinux.org> 0.8.48-alt1
- Updated to 0.8.48.

* Wed May 27 2026 Anton Zhukharev <ancieg@altlinux.org> 0.8.47-alt1
- Updated to 0.8.47.
- Packaged shell completions for bash, fish and zsh.

* Tue May 26 2026 Anton Zhukharev <ancieg@altlinux.org> 0.8.45-alt1
- Updated to 0.8.45.

* Mon May 25 2026 Anton Zhukharev <ancieg@altlinux.org> 0.8.44-alt1
- Updated to 0.8.44.
- Rebranded from DeepSeek-TUI to CodeWhale.

* Fri May 22 2026 Anton Zhukharev <ancieg@altlinux.org> 0.8.40-alt1
- Updated to 0.8.40.

* Sat May 16 2026 Anton Zhukharev <ancieg@altlinux.org> 0.8.37-alt1
- Updated to 0.8.37.

* Thu May 14 2026 Anton Zhukharev <ancieg@altlinux.org> 0.8.34-alt1
- Updated to 0.8.34.

* Wed May 13 2026 Anton Zhukharev <ancieg@altlinux.org> 0.8.32-alt1
- Updated to 0.8.32.

* Mon May 11 2026 Anton Zhukharev <ancieg@altlinux.org> 0.8.29-alt1
- Updated to 0.8.29.

* Fri May 08 2026 Anton Zhukharev <ancieg@altlinux.org> 0.8.20-alt1
- Updated to 0.8.20.

* Thu May 07 2026 Anton Zhukharev <ancieg@altlinux.org> 0.8.17-alt1
- Updated to 0.8.17.

* Thu May 07 2026 Anton Zhukharev <ancieg@altlinux.org> 0.8.16-alt1
- Packaged for ALT Sisyphus.
