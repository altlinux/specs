%global import_path altlinux.space/alt-orchestra/rootfs-put
%define _unpackaged_files_terminate_build 1

Name: rootfs-put
Version: 0.1.0
Release: alt1

Summary: Tool for copying files with ELF dependencies to a root filesystem and storing package metadata
License: GPL-3.0-or-later
Group: Other
Url: https://altlinux.space/alt-orchestra/rootfs-put
Vcs: https://altlinux.space/alt-orchestra/rootfs-put.git

ExclusiveArch: %go_arches

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
%summary.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export CGO_ENABLED=1

%golang_prepare

%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc *.md
%_bindir/*
%changelog
* Wed Feb 04 2026 Maxim Slipenko <maks1ms@altlinux.org> 0.1.0-alt1
- Initial build.

