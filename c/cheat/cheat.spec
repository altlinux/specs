%define _unpackaged_files_terminate_build 1
%global import_path github.com/cheat/cheat

Name: cheat
Version: 4.4.2
Release: alt1
Summary: Cheat allows you to create and view interactive cheatsheets on the command-line.
License: MIT
Group: Terminals
Url: https://github.com/cheat/cheat

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Cheat allows you to create and view interactive cheatsheets on the command-line.
It was designed to help remind *nix system administrators of options for
commands that they use frequently, but not frequently enough to remember.

%prep
%setup -a 1
%patch -p1

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"

%golang_prepare

%golang_build cmd/%name

%install
export BUILDDIR="$PWD/.gopath"
export GOPATH="$BUILDDIR:%go_path"
export IGNORE_SOURCES=1
mkdir -p %buildroot%_datadir/%name
%golang_install
install -Dm 0644 -p scripts/cheat.bash %buildroot%_datadir/bash-completion/completions/%name
install -Dm 0644 -p scripts/cheat.fish %buildroot%_datadir/zsh/site-functions/%name.fish
install -Dm 0644 -p scripts/cheat.zsh  %buildroot%_datadir/zsh/site-functions/_cheat
# install man file
mkdir -p %buildroot%_man1dir/
install -Dm644 doc/%name.1 %buildroot%_man1dir/
#install config file
mkdir -m 0755 -p %buildroot%_sysconfdir/%name
install -m 0644 -p configs/conf.yml %buildroot%_sysconfdir/%name/conf.yml

%files
%doc README.md HACKING.md INSTALLING.md
%_bindir/%name
%dir %_datadir/%name
%config(noreplace) %_sysconfdir/%name/conf.yml
%_datadir/bash-completion/completions/*
%_datadir/zsh/site-functions/*
%_man1dir/*.1*

%changelog
* Tue May 06 2025 Pavel Shilov <zerospirit@altlinux.org> 4.4.2-alt1
- Initial build for Sisyphus.
