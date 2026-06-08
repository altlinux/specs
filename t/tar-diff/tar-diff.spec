%global import_path github.com/containers/tar-diff

%define _unpackaged_files_terminate_build 1

Name: tar-diff
Version: 0.4.0
Release: alt1

Summary: Set of commandline tools to diff and patch tar files
License: Apache-2.0
Group: Other
URL: https://github.com/containers/tar-diff
VCS: https://github.com/containers/tar-diff.git

ExclusiveArch: %go_arches

Source: %name-%version.tar
Source10: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
tar-diff is a golang library and set of commandline tools to diff and patch
tar files.

pkg/tar-diff and the tar-diff tool take one or more old tar files (optionally
compressed) and a new tar file to generate a single file representing the
delta between them (a tardiff file).

pkg/tar-patch takes a tardiff file and the uncompressed contents (such as an
extracted directory) of the old tar file(s) and reconstructs (binary
identically) the new tar file (uncompressed).

%prep
%setup -a10
%autopatch -p1

%build
export GOROOT="%_libexecdir/golang"
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

%golang_build cmd/*

%install
export IGNORE_SOURCES=1
export GOROOT="%_libexecdir/golang"
export BUILDDIR="$PWD/.build"

%golang_install

%check
export GOROOT="%_libexecdir/golang"

%make test

%files
%_bindir/%name
%_bindir/tar-patch

%changelog
* Mon Jun 08 2026 Vladimir Romanov <rirusha@altlinux.org> 0.4.0-alt1
- Initial build.
