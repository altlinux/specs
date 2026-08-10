%define _unpackaged_files_terminate_build 1
%global import_path github.com/legostin/cull

Name: cull
Version: 0.8.1
Release: alt1
Summary: Interactive TUI disk space analyzer.
License: MIT
Group: System/Base
Url: https://github.com/legostin/cull

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-golang

%description
Interactive TUI disk space analyzer. Scan directories,
find what's eating your disk, and delete it all from the terminal.

%prep
%setup -a 1
%patch -p1

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"

%golang_prepare

%golang_build .

%install
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export IGNORE_SOURCES=1
%golang_install

%files
%doc *.md 
%_bindir/%name

%changelog
* Fri Aug 07 2026 Pavel Shilov <zerospirit@altlinux.org> 0.8.1-alt1
- updated from 0.7.0 to 0.8.1

* Fri Jul 31 2026 Pavel Shilov <zerospirit@altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus.
