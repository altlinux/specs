%global import_path altlinux.space/alt-atomic/layersize
%define _unpackaged_files_terminate_build 1

Name: layersize
Version: 0.2.0
Release: alt1

Summary: Annotate every layer of an OCI image with its uncompressed size
License: GPL-3.0-or-later
Group: Other
Url: https://altlinux.space/alt-atomic/layersize
Vcs: https://altlinux.space/alt-atomic/layersize.git

ExclusiveArch: %go_arches

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
%summary.

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export CGO_ENABLED=1

%golang_prepare

%golang_build cmd/layersize

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc *.md
%_bindir/%name

%changelog
* Wed Oct 07 2026 Maxim Slipenko <maks1ms@altlinux.org> 0.2.0-alt1
- Initial build.
