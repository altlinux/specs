%define _unpackaged_files_terminate_build 1

Name: nekoray
Version: 4.3.2
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
BuildRequires: qt6-base-devel
BuildRequires: qt6-svg-devel
BuildRequires: qt6-tools-devel
BuildRequires: qt6-charts-devel
BuildRequires: protobuf-compiler
BuildRequires: protobuf-c-compiler
BuildRequires: libprotobuf-devel
BuildRequires: libprotobuf-c-devel
BuildRequires: libyaml-cpp-devel
BuildRequires: libzxing-cpp-devel
BuildRequires: libcpr-devel

ExclusiveArch: x86_64 aarch64

Requires: sing-geosite sing-geoip

%description
Qt based cross-platform GUI proxy configuration manager

%package -n sing-geosite
Summary: Geosite Database for sing-box
Group: System/Servers

%description -n sing-geosite
Geosite Database for sing-box

%package -n sing-geoip
Summary: Geoip Database for sing-box
Group: System/Servers

%description -n sing-geoip
Geoip Database for sing-box

%prep
%setup -a 1
%patch1 -p1

mv %name-vendors-%version/server-vendor core/server/vendor
mv %name-vendors-%version/updater-vendor core/updater/vendor

install -dm 755 sing-box/rule-set

mv %name-vendors-%version/sing-geosite/*.db sing-box/
mv %name-vendors-%version/sing-geosite/rule-set/*.srs sing-box/rule-set

mv %name-vendors-%version/sing-geoip/*.db sing-box/ 
mv %name-vendors-%version/sing-geoip/rule-set/*.srs sing-box/rule-set 

rm -rf %name-vendors-%version

%build
mkdir build

pushd build
cmake .. -DCMAKE_INSTALL_PREFIX=%_prefix -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%make_build
popd

export GOFLAGS=-mod=vendor
export GOOS=linux
%ifarch x86_64
export GOARCH=amd64
%else
export GOARCH=arm64
%endif

./script/build_go.sh

%install
install -dm 755 %buildroot%_bindir
install -dm 755 %buildroot%_libexecdir/nekobox
install -dm 755 %buildroot%_datadir/applications
install -dm 755 %buildroot%_datadir/sing-box/rule-set

pushd build
install -pm 755 ./nekoray %buildroot%_libexecdir/nekobox/nekobox
install -pm 755 %SOURCE2 %buildroot/%_bindir/nekobox
install -pm 644 %SOURCE3 %buildroot%_datadir/applications/nekobox.desktop
popd

install -Dm644 ./res/public/nekobox.png -t %buildroot%_datadir/pixmaps/

%ifarch x86_64
install -Dm755 ./deployment/linux64/* -t %buildroot%_libexecdir/nekobox/
%else
install -Dm755 ./deployment/linux-arm64/* -t %buildroot%_libexecdir/nekobox/
%endif

install -Dm755 ./sing-box/*.db %buildroot%_datadir/sing-box
install -Dm755 ./sing-box/rule-set/*.srs %buildroot%_datadir/sing-box/rule-set

%files
%_libexecdir/nekobox/nekobox
%_libexecdir/nekobox/nekobox_core
%_libexecdir/nekobox/updater
%_bindir/nekobox
%_datadir/applications/nekobox.desktop
%_datadir/pixmaps/nekobox.png

%files -n sing-geosite
%_datadir/sing-box/geosite*.db
%_datadir/sing-box/rule-set/geosite-*.srs

%files -n sing-geoip
%_datadir/sing-box/geoip*.db
%_datadir/sing-box/rule-set/geoip-*.srs

%changelog
* Thu Apr 10 2025 Andrey Kovalev <ded@altlinux.org> 4.3.2-alt1
- Updated to upstream version 4.3.2.
- Fixed FTBFS with cmake4.

* Fri Feb 14 2025 Andrey Kovalev <ded@altlinux.org> 4.0.1-alt2
- Added sing-geoip and sing-geosite for VLess and VMess (closes: #53059).

* Tue Feb 11 2025 Andrey Kovalev <ded@altlinux.org> 4.0.1-alt1
- Updated to upstream version 4.0.1.

* Mon Sep 16 2024 Andrey Kovalev <ded@altlinux.org> 3.26-alt1
- Initial build for Sisyphus.

