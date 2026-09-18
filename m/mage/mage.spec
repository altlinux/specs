%define _unpackaged_files_terminate_build 1
%define import_path github.com/magefile/mage

%define bash_completionsdir %_datadir/bash-completion/completions
%define fish_completionsdir %_datadir/fish/vendor_completions.d
%define zsh_completionsdir %_datadir/zsh/site-functions

Name: mage
Version: 1.17.2
Release: alt1

Summary: A Make/rake-like dev tool using Go
License: Apache-2.0
Group: Development/Other
Url: https://magefile.org/
Vcs: https://github.com/magefile/mage

ExclusiveArch: %go_arches

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: git-core

%description
Mage is a make-like build tool using Go. You write plain-old go functions,
and Mage automatically uses them as Makefile-like runnable targets.

%prep
%setup
%autopatch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

cd .build/src/%import_path

# for golang's debug.BuildInfo
git init
git config user.email '%packagerAddress'
git config user.name '%packagerName'
git add -A
export GIT_COMMITER_DATE="@$SOURCE_DATE_EPOCH"
export GIT_AUTHOR_DATE="@$SOURCE_DATE_EPOCH"
git commit -q -m 'Release v%version' --allow-empty
git tag -a 'v%version' -m 'Version v%version'

%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%buildroot%_bindir/mage -install bash
%buildroot%_bindir/mage -install fish
%buildroot%_bindir/mage -install zsh

install -Dvpm0644 $HOME/.config/mage/completion.bash \
                  %buildroot%bash_completionsdir/mage
install -Dvpm0644 $HOME/.config/fish/completions/mage.fish \
                  %buildroot%fish_completionsdir/mage.fish
install -Dvpm0644 $HOME/.config/mage/completion.bash \
                  %buildroot%zsh_completionsdir/_mage

%check
%buildroot%_bindir/mage -version

%files
%_bindir/mage
%bash_completionsdir/mage
%fish_completionsdir/mage.fish
%zsh_completionsdir/_mage

%changelog
* Mon Sep 07 2026 Anton Zhukharev <ancieg@altlinux.org> 1.17.2-alt1
- Packaged for ALT Sisyphus.
