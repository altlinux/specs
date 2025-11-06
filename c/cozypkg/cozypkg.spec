%global import_path github.com/cozystack/cozypkg
Name:    cozypkg
Version: 1.2.0
Release: alt1

Summary: Cozy wrapper around Helm and Flux CD for local development
License: Apache-2.0
Group:   Other
Url:     https://github.com/cozystack/cozypkg

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
%summary

%prep
%setup
%patch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-X main.Version=%version"

%golang_prepare

%golang_build .

$BUILDDIR/bin/%name completion bash > %name.bash
$BUILDDIR/bin/%name completion zsh > %name.zsh
$BUILDDIR/bin/%name completion fish > %name.fish

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

install -Dm 644 %name.bash %buildroot%_datadir/bash-completion/completions/%name
install -Dm 644 %name.zsh %buildroot%_datadir/zsh/site-functions/_%name
install -Dm 644 %name.fish %buildroot%_datadir/fish/vendor_completions.d/%name.fish

%files
%doc *.md
%_bindir/%name
%_datadir/bash-completion/completions/%name
%_datadir/zsh/site-functions/_%name
%_datadir/fish/vendor_completions.d/%name.fish

%changelog
* Thu Nov 06 2025 Nadezhda Fedorova <fedor@altlinux.org> 1.2.0-alt1
- Initial build for ALTLinux.
