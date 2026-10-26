# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

%define import_path github.com/Gaurav-Gosain/tuios
%define go_builddir .build

Name: tuios
Version: 0.11.1
Release: alt1
Summary: Terminal UI Operating System, a terminal-based window manager
License: MIT
Group: Terminals
Url: https://tuios.dev
Vcs: https://github.com/Gaurav-Gosain/tuios

ExcludeArch: %ix86

Source: %name-%version.tar
BuildRequires(pre): rpm-build-golang
BuildRequires: golang >= 1.26.6
# internal/worktree exercises real git plumbing in %check.
BuildRequires: git
# The pane-spawning tests in %check open /dev/ptmx; the file dependency makes
# hasher mount devpts, which also provides the ptmx node.
%{?!_without_check:BuildRequires: /dev/pts /proc}

%description
TUIOS is a terminal-based window manager built on the Charm stack
(Bubble Tea, Lip Gloss). It provides a vim-like modal interface,
workspaces, window tiling, mouse interaction, an SSH server mode, a web
terminal server (tuios-web), and a terminal UI that watches what AI
coding agents are doing.

%prep
%setup
# The release build works from the go.mod pins, not from the workspace.
rm -f go.work go.work.sum
# hasher mounts /proc with hidepid=2, so the daemon cannot see whether pid 1
# is inside a pane and answers conservatively; the assertion needs a plain
# /proc, which the build chroot never has.
%__sed -i '/func TestPaneGrantsAnswersForAPeerPID/a t.Skip("hidepid on /proc in the build chroot")' internal/session/pane_grants_hold_test.go
# In a hasher chroot the top directories belong to the invoking user, not to
# root, so the OpenSSH-style safe-path walk behind ownedSocket can never
# pass there.
%__sed -i '/func TestOwnedSocket/a t.Skip("chroot top dirs are not root-owned")' internal/session/ssh_follow_unix_test.go

%build
export BUILDDIR="$PWD/%go_builddir"
export IMPORT_PATH="%import_path"
export GOTOOLCHAIN=local
export CGO_ENABLED=0
export GOFLAGS="-buildmode=pie"
export LDFLAGS="-X main.version=%version -X main.builtBy=altlinux"
%golang_prepare
%golang_build %go_builddir/src/%import_path/cmd/%name
%golang_build %go_builddir/src/%import_path/cmd/%{name}-web
set -C
./%go_builddir/bin/%name completion bash > _bash
./%go_builddir/bin/%name completion zsh  > _zsh
./%go_builddir/bin/%name completion fish > _fish

%install
export BUILDDIR="$PWD/%go_builddir"
export IGNORE_SOURCES=1

%golang_install
%__install -Dpm644 _bash %buildroot%_datadir/bash-completion/completions/%name
%__install -Dpm644 _fish %buildroot%_datadir/fish/vendor_completions.d/%name.fish
%__install -Dpm644 _zsh  %buildroot%_datadir/zsh/site-functions/_%name

%check
export GOTOOLCHAIN=local
# The build chroot runs with TMPDIR=/usr/src/tmp, and the tests place the
# sandbox home under it; the kitty file-medium rules then refuse that TMPDIR
# (a directory holding the home is not temporary). /tmp is what the suite
# expects, as on a developer machine.
export TMPDIR=/tmp
%buildroot%_bindir/%name --version | grep -F '%version ['
cd %go_builddir/src/%import_path/
%gotest ./...

%files
%doc README.md
%_bindir/%name
%_bindir/%{name}-web
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%_datadir/zsh/site-functions/_%name

%changelog
* Mon Oct 26 2026 Andrey Limachko <liannnix@altlinux.org> 0.11.1-alt1
- updated from 0.9.3 to 0.11.1

* Fri Oct 23 2026 Andrey Limachko <liannnix@altlinux.org> 0.9.3-alt1
- Initial package for ALT Linux.

