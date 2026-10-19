%define _unpackaged_files_terminate_build 1
%define _bash_completions_dir %_datadir/bash-completion/completions
%define _fish_complete_dir %_datadir/fish/vendor_completions.d
%define _zsh_complete_dir %_datadir/zsh/site-functions

Name: vtcode
Version: 0.179.6
Release: alt1
Summary: Terminal coding agent with modular architecture and multiple LLM providers
License: Apache-2.0
Group: Development/Tools
Url: https://github.com/vinhnx/vtcode
Vcs: https://github.com/vinhnx/vtcode.git
ExcludeArch: %ix86 %arm

Source: %name-%version.tar
Source1: %name-predownloaded-%version.tar
Patch1: %name-noupdate.patch
Patch2: %name-xtask-completions.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust gcc-c++
BuildRequires: pkgconfig(dbus-1)
# Several unit tests spawn real `git` / `ripgrep` (worktree, code_search).
BuildRequires: git-core ripgrep

Requires: ca-certificates
BuildRequires: git-core ripgrep

%description
VT Code is a terminal coding agent built in Rust. It supports multiple LLM
providers (OpenAI, Anthropic, Ollama and others) with a modular architecture.

%prep
%setup -a1
%patch1 -p1
%patch2 -p1
%rust_prep

%build
%rust_build --bin vtcode
%rust_build -p xtask

%install
%ifarch %ix86
# Fat LTO with one codegen unit exhausts the 32-bit rustc address space.
export CARGO_PROFILE_RELEASE_LTO=off
export CARGO_PROFILE_RELEASE_CODEGEN_UNITS=16
%endif

%rust_install vtcode
mkdir -p %buildroot{%_man1dir,%_bash_completions_dir,%_fish_complete_dir,%_zsh_complete_dir}
./target/release/xtask gen-man --out-dir %buildroot%_man1dir

./target/release/xtask gen-completions
install -Dm644 dist/completions/bash/vtcode      %buildroot%_bash_completions_dir/vtcode
install -Dm644 dist/completions/fish/vtcode.fish %buildroot%_fish_complete_dir/vtcode.fish
install -Dm644 dist/completions/zsh/_vtcode      %buildroot%_zsh_complete_dir/_vtcode

%files
%doc README.md LICENSE THIRD-PARTY-NOTICES
%_bindir/vtcode
%_man1dir/*
%_bash_completions_dir/vtcode
%_fish_complete_dir/vtcode.fish
%_zsh_complete_dir/_vtcode

%changelog
* Mon Oct 19 2026 Alexey Shabalin <shaba@altlinux.org> 0.179.6-alt1
- updated from 0.179.0 to 0.179.6

* Fri Oct 16 2026 Alexey Shabalin <shaba@altlinux.org> 0.179.0-alt1
- updated from 0.176.0 to 0.179.0

* Tue Oct 13 2026 Alexey Shabalin <shaba@altlinux.org> 0.176.0-alt1
- Initial build for Sisyphus.

