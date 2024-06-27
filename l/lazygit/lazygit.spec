%global import_path github.com/jesseduffield/lazygit
%global _unpackaged_files_terminate_build 1

Name: lazygit
Version: 0.42.0
Release: alt1

Summary: Simple terminal UI for git commands
License: MIT
Group: Development/Other
URL: https://github.com/jesseduffield/lazygit

ExclusiveArch: %go_arches

#Source-url: %url/archive/v%version/%name-%version.tar.gz
Source: %name-%version.tar
Patch3500: pty-loongarch64.patch

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

Requires: git-core

%description
A simple terminal UI for git commands, written in Go with the gocui
library.

Rant time: You've heard it before, git is powerful, but what good is
that power when everything is so damn hard to do? Interactive rebasing
requires you to edit a goddamn TODO file in your editor? Are you
kidding me? To stage part of a file you need to use a command line
program to step through each hunk and if a hunk can't be split down any
further but contains code you don't want to stage, you have to edit an
arcane patch file by hand? Are you KIDDING me?! Sometimes you get asked
to stash your changes when switching branches only to realise that
after you switch and unstash that there weren't even any conflicts and
it would have been fine to just checkout the branch directly? YOU HAVE
GOT TO BE KIDDING ME!

If you're a mere mortal like me and you're tired of hearing how
powerful git is when in your daily life it's a powerful pain in your
ass, lazygit might be for you.

%prep
%setup
%patch3500 -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="${LDFLAGS:-} main.version=%version"

%golang_prepare

cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc README.md LICENSE docs/
%_bindir/%name

%changelog
* Thu Jun 27 2024 Ilya Demyanov <turbid@altlinux.org> 0.42.0-alt1
- new version

* Wed Apr 03 2024 Ilya Demyanov <turbid@altlinux.org> 0.41.0-alt2
- define %%import_path macros

* Tue Apr 02 2024 Ilya Demyanov <turbid@altlinux.org> 0.41.0-alt1
- new version

* Thu Mar 07 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.40.2-alt2
- NMU: fixed FTBFS on LoongArch (trivial patch for creack/pty module)

* Thu Aug 17 2023 Ilya Demyanov <turbid@altlinux.org> 0.40.2-alt1
- new version
- moving sources to a subdirectory
- fix spec according to comments from #44756

* Fri May 26 2023 Ilya Demyanov <turbid@altlinux.org> 0.38.2-alt1
- new version

* Wed May 03 2023 Ilya Demyanov <turbid@altlinux.org> 0.38.1-alt1
- new version

* Fri Feb 17 2023 Ilya Demyanov <turbid@altlinux.org> 0.37.0-alt1
- new version

* Tue Jan 10 2023 Ilya Demyanov <turbid@altlinux.ru> 0.36.0-alt2
- add _unpackaged_files_terminate_build macros
- add ExclusiveArch field

* Mon Jan 09 2023 Ilya Demyanov <turbid@altlinux.ru> 0.36.0-alt1
- initial build for ALT
