%define _unpackaged_files_terminate_build 1

Name: snitch
Version: 0.2.2
Release: alt1
Summary: a prettier way to inspect network connections
License: MIT
Group: Networking/Other
Url: https://github.com/karol-broda/snitch

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: help2man

%description
A friendlier ss / netstat for humans.
Inspect network connections with a clean tui or styled tables.

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

help2man -N -n "a prettier way to inspect network connections" $BUILDDIR/bin/%name > %name.1

%install
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export IGNORE_SOURCES=1
%golang_install
mkdir -p %buildroot%_man1dir
install -Dm 0644 %{name}.1 %buildroot%_man1dir/

%files
%doc README.md
%_bindir/%name
%_man1dir/%name.1.*

%changelog
* Wed Sep 16 2026 Pavel Shilov <zerospirit@altlinux.org> 0.2.2-alt1
- Initial buils for Sisyphus.