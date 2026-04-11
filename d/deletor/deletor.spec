%define _unpackaged_files_terminate_build 1
%global import_path github.com/pashkov256/deletor

Name: deletor
Version: 2.0.0
Release: alt1
Summary: Manage and delete files efficiently with an interactive TUI and scriptable CLI.
License: MIT
Group: File tools
Url: https://github.com/pashkov256/deletor

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
%name is a handy file deletion tool that combines a powerful text interface
(TUI) with visual directory navigation, and classic command line mode (CLI).
With it, you can quickly find and delete files by filters, send them to the
trash or completely erase them, as well as clear the cache, both interactively
and through scripts.

%prep
%setup -a 1
%autopatch -p1

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"

%golang_prepare

%golang_build .

%install
export BUILDDIR="$PWD/.gopath"
%golang_install

rm -rf -- %buildroot%_datadir
rm -rf -- %buildroot%go_root


%files
%doc *.mod
%_bindir/%name

%changelog
* Fri Apr 10 2026 Pavel Shilov <zerospirit@altlinux.org> 2.0.0-alt1
- Update to new version 2.0.0.

* Tue Feb 17 2026 Pavel Shilov <zerospirit@altlinux.org> 1.5.0-alt1
- Initial build for Sisyphus.

