%define _unpackaged_files_terminate_build 1

%global import_path github.com/Vanilla-OS/apx
Name: apx
Version: 2.5.0
Release: alt1

Summary: Package manager with support for multiple sources
License: GPL-3.0-only
Group: System/Configuration/Packaging
Url: https://github.com/Vanilla-OS/apx

Source: %name-%version.tar

Source1: %name-development-%version.tar

# default configs from stale repository
# https://github.com/Vanilla-OS/vanilla-apx-configs
# at commit hash 37a7ce46c5387f70e99cb618532da90de31653f4
# replaced OpenSuSe 15.6 with 16.0
# and added supported versions of ALT and Debian, Ubuntu devel
Patch: vanilla-apx-configs.patch

BuildRequires(pre): rpm-build-golang

BuildRequires: golang
BuildRequires: distrobox

Requires: distrobox

%description
Apx is the default package manager in Vanilla OS.
It is a wrapper around multiple package managers to install
packages and run commands inside a managed container.

%prep
%setup -a1
%patch -p1
%patch -p2
sed -i "s|/usr/share/apx/distrobox|/usr/bin|" config/apx.json

%build
export GOROOT="%_libexecdir/golang"
%gobuild -mod=vendor -ldflags "-X main.Version=v%version"

%install

install -Dpm755 %name %buildroot%_bindir/%name
install -Dpm644 "config/apx.json" %buildroot%_datadir/apx/apx.json
install -Dpm755 man/man1/apx.1 %buildroot%_man1dir/apx.1

# create and install completions
mkdir -p %buildroot%_datadir/bash-completion/completions/
./%name completion bash > %buildroot%_datadir/bash-completion/completions/%name

mkdir -p %buildroot%_datadir/fish/vendor_completions.d/
./%name completion fish > %buildroot%_datadir/fish/vendor_completions.d/%{name}.fish

mkdir -p %buildroot%_datadir/zsh/site-functions/
./%name completion zsh > %buildroot%_datadir/zsh/site-functions/_%{name}

# install vanilla-apx-configs
cp -rpv config/stacks %buildroot%_datadir/apx/
cp -rpv config/package-managers %buildroot%_datadir/apx/

%check
[[ "$(./%name --version)" == "%name version v%version" ]]

%post
echo "NOTE: This package requires Podman, see"
echo "      https://www.altlinux.org/Podman for details."

%files
%doc README.md docs apx-logo.svg
%_bindir/apx
%_man1dir/apx.1*
%dir %_datadir/apx
%_datadir/apx/apx.json
%dir %_datadir/apx/package-managers
%dir %_datadir/apx/package-managers/*.yaml
%dir %_datadir/apx/stacks
%dir %_datadir/apx/stacks/*.yaml
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%{name}.fish
%_datadir/zsh/site-functions/_%{name}

%changelog
* Tue Jan 20 2026 Nikolay Strelkov <snk@altlinux.org> 2.5.0-alt1
- Initial build for Sisyphus
