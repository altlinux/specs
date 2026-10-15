%define _unpackaged_files_terminate_build 1
%define import_path github.com/git-bug/git-bug

Name: git-bug
Version: 0.11.0
Release: alt2

Summary: Distributed, offline-first bug tracker embedded in git
License: GPL-3.0-or-later
Group: Development/Tools
URL: https://github.com/git-bug/git-bug
VCS: https://github.com/git-bug/git-bug

# webui does not support building on the %ix86 architecture
ExcludeArch: %ix86

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: node_modules.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: rpm-build-nodejs

%description
git-bug is a standalone, distributed, offline-first issue management tool that
embeds issues, comments, and more as objects in a git repository (not files!),
enabling you to push and pull them to one or more remotes.

%prep
%setup -a1 -a2
%autopatch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare
pushd $BUILDDIR/src/$IMPORT_PATH/webui
npm run build
popd
pushd $BUILDDIR/src/$IMPORT_PATH
export LDFLAGS="-X main.version=%version"
export TAGS="webui"
go generate
%golang_build .
popd

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

# Install shell completions
install -Dpm 0644 misc/completion/bash/%name %buildroot%_datadir/bash-completion/completions/%name
install -Dpm 0644 misc/completion/fish/%name %buildroot%_datadir/fish/vendor_completions.d/%name.fish
install -Dpm 0644 misc/completion/zsh/%name %buildroot%_datadir/zsh/site-functions/_%name

# Install man pages
install -Dpm 0644 -t %buildroot%_man1dir doc/man/*.1

%files
%doc README.md LICENSE
%_bindir/%name
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%_datadir/zsh/site-functions/_%name
%_man1dir/*

%changelog
* Thu Oct 15 2026 Ulysses Apokin <ulysses@altlinux.org> 0.11.0-alt2
- Build binary with embedded web UI.

* Wed Sep 23 2026 Ulysses Apokin <ulysses@altlinux.org> 0.11.0-alt1
- New version.

* Fri Jun 26 2026 Ulysses Apokin <ulysses@altlinux.org> 0.10.1-alt2
- Packaged man pages and shell completions.
- Clarified license and group identifiers.

* Thu Sep 18 2025 Artem Krasovskiy <aibure@altlinux.org> 0.10.1-alt1
- Initial build for Sisyphus.
