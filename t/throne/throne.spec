%define _unpackaged_files_terminate_build 1
%define _cmake__builddir build

Name: throne
Version: 1.1.4
Release: alt1
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

ExclusiveArch: x86_64 aarch64 loongarch64 riscv64

Requires: throne-sing-geosite throne-sing-geoip

%description
Qt based cross-platform GUI proxy configuration manager

%package sing-geosite
Summary: Geosite Database for sing-box
Group: System/Servers
Provides: sing-geosite

%description sing-geosite
Geosite Database for sing-box

%package sing-geoip
Summary: Geoip Database for sing-box
Group: System/Servers
Provides: sing-geoip

%description sing-geoip
Geoip Database for sing-box

%prep
%setup -a1
%patch -p1

%build
%cmake
%cmake_build

pushd core/server
export GOFLAGS="-buildmode=pie -trimpath -modcacherw -mod=vendor"
export VERSION_SINGBOX=$(go list -m -f '{{.Version}}' github.com/sagernet/sing-box)
export TAGS="with_clash_api,with_gvisor,with_quic,with_wireguard,with_utls,with_dhcp,with_tailscale"
go build -o "../../%_cmake__builddir" \
    -ldflags="-linkmode=external -w -s -X 'github.com/sagernet/sing-box/constant.Version=${VERSION_SINGBOX}'" \
    -tags="${TAGS}"
popd

%install
install -dm 755 %buildroot%_bindir
install -dm 755 %buildroot%_libexecdir/throne
install -dm 755 %buildroot%_datadir/applications
install -dm 755 %buildroot%_datadir/sing-box/rule-set

pushd %_cmake__builddir
install -pm 755 ./Throne %buildroot%_libexecdir/throne/Throne
install -pm 755 ./ThroneCore %buildroot%_libexecdir/throne/ThroneCore
install -pm 755 %SOURCE2 %buildroot/%_bindir/throne
install -pm 644 %SOURCE3 %buildroot%_datadir/applications/Throne.desktop
popd

install -Dm644 ./res/public/Throne.png -t %buildroot%_datadir/pixmaps/

install -Dm755 ./sing-box/*.db %buildroot%_datadir/sing-box
install -Dm755 ./sing-box/rule-set/*.srs %buildroot%_datadir/sing-box/rule-set

%files
%_libexecdir/throne/ThroneCore
%_libexecdir/throne/Throne
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
* Mon May 26 2026 Andrey Kovalev <ded@altlinux.org> 1.1.4-alt1
- Updated to upstream version 1.1.4.

* Tue May 19 2026 Andrey Kovalev <ded@altlinux.org> 1.1.3-alt1
- Updated to upstream version 1.1.3.

* Tue May 05 2026 Andrey Kovalev <ded@altlinux.org> 1.1.2-alt1
- Updated to upstream version 1.1.2.

* Tue Apr 07 2026 Andrey Kovalev <ded@altlinux.org> 1.1.1-alt1
- Updated to upstream version 1.1.1 (closes: #57585, #56993).

* Tue Sep 30 2025 Ivan A. Melnikov <iv@altlinux.org> 1.0.6-alt2
- NMU: Build on riscv64 and loongarch64.

* Tue Sep 30 2025 Andrey Kovalev <ded@altlinux.org> 1.0.6-alt1
- Updated to upstream version 1.0.6 (closes: #56192).

* Tue Sep 02 2025 Andrey Kovalev <ded@altlinux.org> 1.0.2-alt3
- Fixed runtime failure by reverting a faulty commit and pre-building protorpc 
stubs (closes: #55737).

* Wed Aug 27 2025 Andrey Kovalev <ded@altlinux.org> 1.0.2-alt2
- Fixed VCS and URL.

* Tue Aug 19 2025 Andrey Kovalev <ded@altlinux.org> 1.0.2-alt1
- Intial build for Sisyphus (closes: #55551).
