%define import_path github.com/regclient/regclient
%global _unpackaged_files_terminate_build 1

Name:           regclient
Version:        0.6.0
Release:        alt1

Summary:        Client interface for the registry API
License:        Apache-2.0
Group:          Development/Other
URL:            https://github.com/regclient/regclient
Source:         %name-%version.tar

Patch: %name-%version-%release.patch

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: golang >= 1.19
BuildRequires: /proc

%description
Client interface for the registry API.
This includes regctl for a command line interface to manage registries.

%prep
%setup
%patch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export TAGS="nolegacy"

%golang_prepare
pushd $BUILDDIR/src/%import_path
%golang_build cmd/*
popd

$BUILDDIR/bin/regbot completion bash > regbot.bash
$BUILDDIR/bin/regbot completion zsh > regbot.zsh
$BUILDDIR/bin/regbot completion fish > regbot.fish

$BUILDDIR/bin/regctl completion bash > regctl.bash
$BUILDDIR/bin/regctl completion zsh > regctl.zsh
$BUILDDIR/bin/regctl completion fish > regctl.fish

$BUILDDIR/bin/regsync completion bash > regsync.bash
$BUILDDIR/bin/regsync completion zsh > regsync.zsh
$BUILDDIR/bin/regsync completion fish > regsync.fish

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install


install -Dm 644 regbot.bash %buildroot%_datadir/bash-completion/completions/regbot
install -Dm 644 regbot.zsh %buildroot%_datadir/zsh/site-functions/_regbot
install -Dm 644 regbot.fish %buildroot%_datadir/fish/vendor_completions.d/regbot.fish

install -Dm 644 regctl.bash %buildroot%_datadir/bash-completion/completions/regctl
install -Dm 644 regctl.zsh %buildroot%_datadir/zsh/site-functions/_regctl
install -Dm 644 regctl.fish %buildroot%_datadir/fish/vendor_completions.d/regctl.fish

install -Dm 644 regsync.bash %buildroot%_datadir/bash-completion/completions/regsync
install -Dm 644 regsync.zsh %buildroot%_datadir/zsh/site-functions/_regsync
install -Dm 644 regsync.fish %buildroot%_datadir/fish/vendor_completions.d/regsync.fish


%files
%doc *.md
%_bindir/*
%_datadir/bash-completion/completions/*
%_datadir/zsh/site-functions/_*
%_datadir/fish/vendor_completions.d/*.fish

%changelog
* Thu Mar 28 2024 Nadezhda Fedorova <fedor@altlinux.org> 0.6.0-alt1
- 0.6.0
- initial build for ALT Linux
