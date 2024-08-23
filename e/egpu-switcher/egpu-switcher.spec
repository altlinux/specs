%global _unpackaged_files_terminate_build 1
%global import_path github.com/hertg/egpu-switcher

Name: egpu-switcher
Version: 0.19.0
Release: alt1

Summary: Setup script for eGPUs in Linux
License: GPL-3.0
Group: System/Configuration/Hardware
Url: https://github.com/hertg/egpu-switcher

Source0: %name-%version.tar
Source1: %name-vendor.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-golang
BuildRequires: /proc

%description
Distribution agnostic eGPU script that works with NVIDIA and AMD cards.

%prep
%setup -a1

%build
export CGO_CFLAGS=$CFLAGS
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"
export GOROOT="%_libexecdir/golang"

%golang_prepare
pushd .gopath/src/%import_path
%golang_build .
popd

%install
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path:$PWD"
export RELEASE_VERSION=v%version
export RELEASE_NUMBER=%version

pushd $BUILDDIR
mkdir -p %buildroot%_sbindir
install -pm755 bin/%name %buildroot%_sbindir/
popd

%files
%doc LICENSE *.md
%_sbindir/%name

%changelog
* Fri Aug 23 2024 L.A. Kostis <lakostis@altlinux.ru> 0.19.0-alt1
- Initial build for ALTLinux.


