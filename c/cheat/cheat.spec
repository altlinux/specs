%define _unpackaged_files_terminate_build 1
%global import_path github.com/cheat/cheat

Name: cheat
Version: 5.1.0
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
# install man file
mkdir -p %buildroot%_man1dir/
install -Dm644 doc/%name.1 %buildroot%_man1dir/

%files
%doc README.md HACKING.md INSTALLING.md
%_bindir/%name
%_man1dir/*.1*

%changelog
* Thu Feb 26 2026 Pavel Shilov <zerospirit@altlinux.org> 5.1.0-alt1
- 4.4.2 -> 5.1.0

* Tue May 06 2025 Pavel Shilov <zerospirit@altlinux.org> 4.4.2-alt1
- Initial build for Sisyphus.
