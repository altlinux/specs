%define _unpackaged_files_terminate_build 1
%define import_path github.com/wzv5/pping

Name: pping
Version: 0.8.6
Release: alt1

Summary: tcp ping, tls ping, http ping, icmp ping, dns ping, quic ping.
License: MIT
Group: Networking/Other
Url: https://github.com/wzv5/pping

BuildRequires(pre): rpm-build-golang

Source: %name-%version.tar

%description
tcp ping, tls ping, http ping, icmp ping, dns ping, quic ping.

%global import_path github.com/wzv5/%name

%prep
%setup -q

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"

%golang_prepare

pushd $BUILDDIR/src/%import_path
%golang_build cmd/%name
popd

# Completions
$BUILDDIR/bin/%name completion bash > %name.bash
$BUILDDIR/bin/%name completion fish > %name.fish
$BUILDDIR/bin/%name completion zsh > %name.zsh

%install
export BUILDDIR="$PWD/.gopath"
export IGNORE_SOURCES=1

install -Dm644 %name.bash %buildroot%_datadir/bash-completion/completions/%name
install -Dm644 %name.fish %buildroot%_datadir/fish/vendor_completions.d/%name.fish
install -Dm644 %name.zsh %buildroot%_datadir/zsh/site-functions/_%name

%golang_install

%files
%_bindir/%name
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%_datadir/zsh/site-functions/_%name

%changelog
* Fri Aug 15 2025 Korney Gedert <kiper@altlinux.org> 0.8.6-alt1
- Initial release.
