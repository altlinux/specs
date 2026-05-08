%global _unpackaged_files_terminate_build 1
%global import_path code.gitea.io/tea

Name: gitea-tea
Version: 0.14.0
Release: alt1
Summary: command line tool to interact with Gitea

License: MIT
Group: Development/Other
Url: https://gitea.com/gitea/tea
Vcs: https://gitea.com/gitea/tea.git
Source: %name-%version.tar
Patch: %name-%version.patch

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.25

%description
tea is a productivity helper for Gitea.
It can be used to manage most entities on one or multiple Gitea instances
and provides local helpers like 'tea pull checkout'.
tea makes use of context provided by the repository in $PWD if available,
but is still usable independently of $PWD.
Configuration is persisted in $XDG_CONFIG_HOME/tea.

%prep
%setup
%patch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare
export VERSION=%version
export COMMIT=%release
export BRANCH=altlinux
export LDFLAGS="-X main.Version=$VERSION"
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"
export IGNORE_SOURCES=1

%golang_install
# install completions
mkdir -p %buildroot%_datadir/{bash-completion/completions,fish/vendor_completions.d,zsh/site-functions}
%buildroot%_bindir/tea completion bash > %buildroot%_datadir/bash-completion/completions/tea
%buildroot%_bindir/tea completion fish > %buildroot%_datadir/fish/vendor_completions.d/tea.fish
%buildroot%_bindir/tea completion zsh  > %buildroot%_datadir/zsh/site-functions/_tea

%files
%doc *.md
%_bindir/*
%_datadir/bash-completion/completions/tea
%_datadir/fish/vendor_completions.d/tea.fish
%_datadir/zsh/site-functions/_tea

%changelog
* Fri May 08 2026 Alexey Shabalin <shaba@altlinux.org> 0.14.0-alt1
- updated from 0.12.0 to 0.14.0

* Fri Feb 20 2026 Alexey Shabalin <shaba@altlinux.org> 0.12.0-alt1
- updated from 0.11.1 to 0.12.0

* Thu Jan 08 2026 Alexey Shabalin <shaba@altlinux.org> 0.11.1-alt1
- New version 0.11.1.

* Thu Aug 21 2025 Andrey Limachko <liannnix@altlinux.org> 0.10.1-alt2
- Fix bash autocomplete script to use --generate-shell-completion
  flag

* Tue Jun 17 2025 Alexey Shabalin <shaba@altlinux.org> 0.10.1-alt1
- New version 0.10.1.

* Tue Jul 25 2023 Alexander Burmatov <thatman@altlinux.org> 0.9.2-alt2
- Remove autocomplete command.

* Mon Jul 10 2023 Alexey Shabalin <shaba@altlinux.org> 0.9.2-alt1
- New version 0.9.2.

* Mon Sep 26 2022 Alexey Shabalin <shaba@altlinux.org> 0.9.0-alt1
- 0.9.0

* Mon Nov 15 2021 Alexey Shabalin <shaba@altlinux.org> 0.8.0-alt1
- Initial build for ALT
