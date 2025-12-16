%define _unpackaged_files_terminate_build 1
%define import_path github.com/autovia/git-lfs-transfer

Name: git-lfs-transfer
Version: 0.9.0
Release: alt1

Summary: Server-side implementation of Git LFS over SSH
License: MIT
Group: Networking/File transfer
Url: https://github.com/autovia/git-lfs-transfer
Vcs: https://github.com/autovia/git-lfs-transfer

ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-golang

%description
git-lfs-transfer is the server-side implementation of Git LFS using the SSH
protocol.

%prep
%setup -a1
%autopatch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare
pushd $BUILDDIR/src/$IMPORT_PATH
%golang_build .
popd

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%files
%doc README.md LICENSE
%_bindir/%name

%changelog
* Tue Dec 16 2025 Artem Krasovskiy <aibure@altlinux.org> 0.9.0-alt1
- Initial build for Sisyphus.
