%define import_path github.com/google/gops
%define _unpackaged_files_terminate_build 1

Name:    gops
Version: 0.3.29
Release: alt1

Summary: gops is a command to list and diagnose Go processes currently running on your system
License: BSD-3-Clause
Group:   System/Configuration/Other
Url:     https://github.com/google/gops

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: rpm-build-golang
BuildRequires: golang
BuildRequires: /proc

%description
%summary

%prep
%setup
%patch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

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
* Wed Mar 25 2026 Nadezhda Fedorova <fedor@altlinux.org> 0.3.29-alt1
- New version 0.3.29.

* Tue Nov 11 2025 Nadezhda Fedorova <fedor@altlinux.org> 0.3.28-alt2
- Delete wrong require.

* Wed Oct 22 2025 Nadezhda Fedorova <fedor@altlinux.org> 0.3.28-alt1
- Initial build for ALTLinux.
