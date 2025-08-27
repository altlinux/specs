%define _unpackaged_files_terminate_build 1
%define _cmake__builddir BUILD

Name: throne
Version: 1.0.2
Release: alt2
Summary: Qt based cross-platform GUI proxy configuration manager
License: GPLv3
Group: System/Servers
URL: https://github.com/throneproj/Throne
VCS: https://github.com/throneproj/Throne.git

Source: %name-%version.tar
Source1: %name-vendors-%version.tar
Source2: throne.sh
Source3: Throne.desktop

Patch: %name-%version-%release.patch

Provides: nekoray

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
BuildRequires: protobuf-go

ExclusiveArch: x86_64 aarch64

Requires: throne-sing-geosite throne-sing-geoip

%description
Qt based cross-platform GUI proxy configuration manager

%package sing-geosite
Summary: Geosite Database for sing-box
Group: System/Servers
Conflicts: sing-geosite

%description sing-geosite
Geosite Database for sing-box

%package sing-geoip
Summary: Geoip Database for sing-box
Group: System/Servers
Conflicts: sing-geoip

%description sing-geoip
Geoip Database for sing-box

%prep
%setup -a 1
%patch -p1

mv %name-vendors-%version/protorpc-vendor core/protorpc/vendor
mv %name-vendors-%version/server-vendor core/server/vendor
mv %name-vendors-%version/updater-vendor core/updater/vendor

install -dm 755 sing-box/rule-set

mv %name-vendors-%version/sing-geosite/*.db sing-box/
mv %name-vendors-%version/sing-geosite/rule-set/*.srs sing-box/rule-set

mv %name-vendors-%version/sing-geoip/*.db sing-box/ 
mv %name-vendors-%version/sing-geoip/rule-set/*.srs sing-box/rule-set 

rm -rf %name-vendors-%version

%build
%cmake
%cmake_build

export GOFLAGS=-mod=vendor
export GOOS=linux
%ifarch x86_64
export GOARCH=amd64
%else
export GOARCH=arm64
%endif

pushd core/protorpc/protoc-gen-protorpc
go build .
go install .
popd

PATH=$PATH:%homedir/go/bin/ ./script/build_go.sh

%install
install -dm 755 %buildroot%_bindir
install -dm 755 %buildroot%_libexecdir/throne
install -dm 755 %buildroot%_datadir/applications
install -dm 755 %buildroot%_datadir/sing-box/rule-set

pushd %_cmake__builddir
install -pm 755 ./Throne %buildroot%_libexecdir/throne/Throne
install -pm 755 %SOURCE2 %buildroot/%_bindir/throne
install -pm 644 %SOURCE3 %buildroot%_datadir/applications/Throne.desktop
popd

install -Dm644 ./res/public/Throne.png -t %buildroot%_datadir/pixmaps/

%ifarch x86_64
install -Dm755 ./deployment/linux-amd64/* -t %buildroot%_libexecdir/throne/
%else
install -Dm755 ./deployment/linux-arm64/* -t %buildroot%_libexecdir/throne/
%endif

install -Dm755 ./sing-box/*.db %buildroot%_datadir/sing-box
install -Dm755 ./sing-box/rule-set/*.srs %buildroot%_datadir/sing-box/rule-set

%files
%_libexecdir/throne/Core
%_libexecdir/throne/Throne
%_libexecdir/throne/updater
%_bindir/throne
%_datadir/applications/Throne.desktop
%_datadir/pixmaps/Throne.png

%files sing-geosite
%_datadir/sing-box/geosite*.db
%_datadir/sing-box/rule-set/geosite-*.srs

%files sing-geoip
%_datadir/sing-box/geoip*.db
%_datadir/sing-box/rule-set/geoip-*.srs

%changelog
* Wed Aug 27 2025 Andrey Kovalev <ded@altlinux.org> 1.0.2-alt2
- Fixed VCS and URL.

* Tue Aug 19 2025 Andrey Kovalev <ded@altlinux.org> 1.0.2-alt1
- Intial build for Sisyphus (closes: #55551).
