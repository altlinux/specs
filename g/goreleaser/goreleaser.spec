%global import_path github.com/goreleaser/goreleaser
Name:    goreleaser
Version: 1.18.2
Release: alt1

Summary: Deliver Go binaries as fast and easily as possible
License: MIT
Group:   Other
Url:     https://github.com/goreleaser/goreleaser

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
GoReleaser builds Go binaries for several platforms, creates a GitHub release
and then pushes a Homebrew formula to a tap repository. All that wrapped in
your favorite CI.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-s -w -X main.version=%version -X main.builtBy=alt $LDFLAGS"

%golang_prepare

cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

mkdir -p %buildroot%_datadir/zsh/site-functions
%buildroot%_bindir/%name completion zsh > %buildroot%_datadir/zsh/site-functions/_%name
mkdir -p %buildroot%_datadir/bash-completion/completions
%buildroot%_bindir/%name completion bash > %buildroot%_datadir/bash-completion/completions/%name
mkdir -p %buildroot%_datadir/fish/vendor_completions.d
%buildroot%_bindir/%name completion fish > %buildroot%_datadir/fish/vendor_completions.d/%name.fish

%files
%doc *.md
%_bindir/*
%_datadir/zsh/site-functions/_%name
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish

%changelog
* Mon May 15 2023 Mikhail Gordeev <obirvalger@altlinux.org> 1.18.2-alt1
- Initial build for Sisyphus
