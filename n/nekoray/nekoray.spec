%define _unpackaged_files_terminate_build 1

Name: nekoray
Version: 4.0.1
Release: alt1
Summary: Qt based cross-platform GUI proxy configuration manager
License: GPLv3
Group: System/Servers
URL: https://github.com/MatsuriDayo/nekoray

Source: %name-%version.tar
Source1: %name-vendors-%version.tar
Source2: nekobox.sh
Source3: nekobox.desktop

Patch1: nekoray-4.0.1-alt-build.patch

BuildRequires: cmake
BuildRequires: golang
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: qt5-svg-devel
BuildRequires: qt5-tools-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: protobuf-compiler
BuildRequires: protobuf-c-compiler
BuildRequires: libprotobuf-devel
BuildRequires: libprotobuf-c-devel
BuildRequires: libyaml-cpp-devel
BuildRequires: libzxing-cpp-devel

ExclusiveArch: x86_64 aarch64

%description
Qt based cross-platform GUI proxy configuration manager

%prep
%setup -a 1
%patch1 -p1

rm -rf 3rdparty/QHotkey

mv %name-vendors-%version/3rdparty/* 3rdparty/
mv %name-vendors-%version/nekobox_core-vendor go/cmd/nekobox_core/vendor
mv %name-vendors-%version/updater-vendor go/cmd/updater/vendor

rm -rf %name-vendors-%version

%build
mkdir build

pushd build
cmake .. -DCMAKE_INSTALL_PREFIX=%_prefix
%make_build
popd

export GOFLAGS=-mod=vendor
export GOOS=linux
%ifarch x86_64
export GOARCH=amd64
%else
export GOARCH=arm64
%endif

./libs/build_go.sh

%install
pushd build
install -dm 755 %buildroot%_bindir
install -dm 755 %buildroot%_libexecdir/nekobox
install -dm 755 %buildroot%_datadir/applications

install -pm 755 ./nekobox %buildroot%_libexecdir/nekobox/nekobox
install -pm 755 %SOURCE2 %buildroot/%_bindir/nekobox
install -pm 644 %SOURCE3 %buildroot%_datadir/applications/nekobox.desktop

install -Dm644 ../res/public/nekobox.png -t %buildroot%_datadir/pixmaps/

%ifarch x86_64
install -Dm755 ../deployment/linux64/* -t %buildroot%_libexecdir/nekobox/
%else
install -Dm755 ../deployment/linux-arm64/* -t %buildroot%_libexecdir/nekobox/
%endif
popd

%files
%_libexecdir/nekobox/nekobox
%_libexecdir/nekobox/nekobox_core
%_libexecdir/nekobox/launcher
%_bindir/nekobox
%_datadir/applications/nekobox.desktop
%_datadir/pixmaps/nekobox.png

%changelog
* Tue Feb 11 2025 Andrey Kovalev <ded@altlinux.org> 4.0.1-alt1
- Updated to upstream version 4.0.1.

* Mon Sep 16 2024 Andrey Kovalev <ded@altlinux.org> 3.26-alt1
- Initial build for Sisyphus.

