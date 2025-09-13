%define _unpackaged_files_terminate_build 1

%global import_path github.com/Adembc/lazyssh
Name: lazyssh
Version: 0.2.1
Release: alt1

Summary: A terminal-based SSH manager inspired by lazydocker and k9s
License: Apache-2.0
Group: Terminals
Url: https://github.com/Adembc/lazyssh

Source: %name-%version.tar
Source1: %name-development-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Lazyssh is a terminal-based, interactive SSH manager inspired by tools
like lazydocker and k9s - but built for managing your fleet of servers
directly from your terminal.

With lazyssh, you can quickly navigate, connect, manage, and transfer
files between your local machine and any server defined in your 
~/.ssh/config. No more remembering IP addresses or running long scp
commands - just a clean, keyboard-driven UI.

%prep
%setup -a1
%patch -p1

%build
export GOROOT="%_libexecdir/golang"
%gobuild -mod=vendor -ldflags "-X main.version=%version" ./cmd/main.go

%install
install -Dpm755 main %buildroot%_bindir/%name

%files
%doc LICENSE README.md docs
%_bindir/*

%changelog
* Sat Sep 13 2025 Nikolay Strelkov <snk@altlinux.org> 0.2.1-alt1
- Initial build for Sisyphus
