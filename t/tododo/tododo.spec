%define _unpackaged_files_terminate_build 1
%global import_path github.com/bmarse/tododo

Name: tododo
Version: 0.7.0
Release: alt1
Summary: TUI-based todo manager written in Go
License: MIT
Group: Office
Url: https://github.com/bmarse/tododo
Vcs: https://github.com/bmarse/tododo.git
ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang

%description
Tododo is a terminal-based user interface (TUI) todo manager written in Go.
It provides a simple, keyboard-driven interface for managing tasks stored in
a markdown file (default: .tododo.md). Features include creating, editing,
toggling, and deleting tasks.

%prep
%setup -a 1

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-X main.appVersion=%version"
%golang_prepare
%golang_build .

%install
export BUILDDIR="$PWD/.gopath"
export IGNORE_SOURCES=1
%golang_install

%files
%doc README.md LICENSE
%_bindir/tododo

%changelog
* Mon Aug 25 2025 Aleksandr A. Voyt <sobue@altlinux.org> 0.7.0-alt1
- Initial build.
