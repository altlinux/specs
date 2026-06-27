%define commit 01f3d4f2b
%define date 20260605
%define _unpackaged_files_terminate_build 1

%define import_path github.com/arduino/arduino-cli
%define version_package %import_path/internal/version
%define globals_package %import_path/internal/arduino/globals

%define package_index_url https://altlinux.space/arduino/library-registry/releases/download/latest/package_index.tar.bz2
%define library_index_url https://altlinux.space/arduino/library-registry/releases/download/latest/library_index.tar.bz2

Name: arduino-cli
Version: 1.5.1
Release: alt1

Summary: Arduino command line tool
License: GPL-3.0
Group: Other
Url: https://github.com/arduino/arduino-cli
Vcs: https://github.com/arduino/arduino-cli.git
ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Patch0: %name-%version-%release.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Arduino CLI is an all-in-one solution that provides Boards and Library
Managers, a sketch builder, board detection, an uploader, and other tools
needed to use Arduino-compatible boards and platforms from the command line
or through machine interfaces.

%prep
%setup -a1
%autopatch -p1

%build
export GOROOT=%_libexecdir/golang
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-buildvcs=false"
export LDFLAGS="-X %version_package.defaultVersionString=%version \
	-X %version_package.commit=%commit \
	-X %version_package.date=%date \
	-X %globals_package.DefaultIndexURL=%package_index_url \
	-X %globals_package.LibrariesIndexURLString=%library_index_url"

%golang_prepare

pushd "$BUILDDIR/src/$IMPORT_PATH"
%golang_build .
popd

%install
export GOROOT=%_libexecdir/golang
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc LICENSE.txt README.md
%_bindir/arduino-cli

%changelog
* Tue Jun 23 2026 Grant Makyan <karonus@altlinux.org> 1.5.1-alt1
- Use ALT package index for Arduino Libraries.
- New version.

* Mon Jun 22 2026 Grant Makyan <karonus@altlinux.org> 1.3.1-alt2
- Keep upstream sources, packaging metadata, and vendored modules in one branch.
- Build upstream sources from the recorded v1.3.1 tag.

* Mon Sep 08 2025 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt1
- New version.

* Tue Nov 19 2024 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt2
- Set application version.

* Mon Nov 18 2024 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus.
