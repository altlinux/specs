%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%global qt_dir coolercontrol
%global ap_id org.coolercontrol.CoolerControl
%global group System/Configuration/Hardware
# https://github.com/mozilla/sccache/issues/862
%global optflags_lto %optflags_lto -ffat-lto-objects

Name: coolercontrol
Version: 2.2.1
Release: alt1
Summary: Monitor and control your cooling devices
Group: %group

License: GPL-3.0-or-later
Url: https://gitlab.com/coolercontrol/coolercontrol

# desktop app
BuildRequires(pre): cmake
BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: qt6-base-devel
BuildRequires: qt6-webengine-devel
BuildRequires: qt6-webchannel-devel
Requires: icon-theme-hicolor > 0
Requires: coolercontrold = %EVR

# rust daemon
BuildRequires: /proc rust rust-cargo rpm-macros-rust
BuildRequires: pkgconfig(libdrm_amdgpu) pkgconfig(libdrm)

# ui part
BuildRequires: npm

# python3 library for liquidctl
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-liquidctl

VCS: https://gitlab.com/coolercontrol/coolercontrol.git
Source: %name-%version.tar
Source1: %{name}d-vendor.tar
Source2: %name-ui-node-modules.tar

# due missing qtwebengine on ix86
# and npm modules unresolved deps
ExclusiveArch: x86_64

%description
CoolerControl is a program to monitor and control your cooling devices.

It offers an easy-to-use user interface with various control features and also
provides live thermal performance details.

%package -n %{name}d
Summary: Monitor and control your cooling devices daemon
Group: %group

%description -n %{name}d
%{name}d is the main daemon containing the core logic for interfacing with
devices, and is installed as "coolercontrold". It is meant to run in the
background as a system daemon. It handles all device communication and data
management and processing, additionally connecting to the coolercontrol-liqctld
daemon for liquidctl supported devices.

It has a REST API that services client programs, such as the Desktop
Application and Web UI.  Additionally, the Web UI is embedded in the daemon for
access over a local browser without the need for any additional package.

%package -n %name-liqctld
Summary: %name service daemon written in Python for interacting with liquidctl
Group: %group
BuildArch: noarch
Requires: python3-module-%{name}_liqctld = %EVR

%description -n %name-liqctld
%name service daemon written in Python for interacting with liquidctl

%package -n python3-module-%{name}_liqctld
Summary: %name service daemon written in Python for interacting with liquidctl
Group: Development/Python3
BuildArch: noarch

%description -n python3-module-%{name}_liqctld
Python3 module for interacting with liquidctl

%prep
%setup
pushd %{name}d
tar -xf %SOURCE1
mkdir -p .cargo
cat > .cargo/config.toml << EOF
[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://github.com/codifryed/nvml-wrapper?branch=coolercontrol-2-0"]
git = "https://github.com/codifryed/nvml-wrapper"
branch = "coolercontrol-2-0"
replace-with = "vendored-sources"

[source."git+https://github.com/codifryed/tower-governor"]
git = "https://github.com/codifryed/tower-governor"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
[profile.release]
strip = "none"
lto= "thin"
debug = "full"
EOF
popd
pushd %name-ui
tar -xf %SOURCE2
popd

%build
# python
pushd %name-liqctld
%pyproject_build
popd
# desktop app
pushd %qt_dir
%cmake
%cmake_build
popd

# daemon and web-ui
make build-daemon-offline

%install
(cd %name-liqctld; %pyproject_install)
install -Dpm 755 %{name}d/target/release/%{name}d -t %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
cp -p packaging/systemd/{%{name}d,%name-liqctld}.service %{buildroot}%{_unitdir}
(cd %qt_dir; %cmake_install)
desktop-file-install --dir=%buildroot%_desktopdir packaging/metadata/%ap_id.desktop
mkdir -p %buildroot%_iconsdir/hicolor/scalable/apps
cp -p packaging/metadata/%ap_id.svg %buildroot%_iconsdir/hicolor/scalable/apps/
mkdir -p %buildroot%_iconsdir/hicolor/symbolic/apps
cp -p packaging/metadata/%ap_id-symbolic.svg %buildroot%_iconsdir/hicolor/symbolic/apps/
mkdir -p %buildroot%_iconsdir/hicolor/256x256/apps
cp -p packaging/metadata/%ap_id.png %buildroot%_iconsdir/hicolor/256x256/apps/
mkdir -p %buildroot%_datadir/metainfo
cp -p packaging/metadata/%ap_id.metainfo.xml %buildroot%_datadir/metainfo/

%check
(cd %{name}d; /usr/bin/cargo test --locked --profile release --no-fail-fast)
appstream-util validate-relax --nonet %buildroot%_datadir/metainfo/*.metainfo.xml

%files -n %{name}d
%{_bindir}/%{name}d
%{_unitdir}/%{name}d.service
%doc LICENSE README.md CHANGELOG.md

%files -n %name-liqctld
%_bindir/%name-liqctld
%{_unitdir}/%name-liqctld.service

%files -n python3-module-%{name}_liqctld
%python3_sitelibdir_noarch/%{name}_liqctld
%python3_sitelibdir_noarch/%{name}_liqctld-%{version}.dist-info/

%files
%_bindir/%name
%_desktopdir/%ap_id.desktop
%_iconsdir/hicolor/scalable/apps/%ap_id.svg
%_iconsdir/hicolor/symbolic/apps/%ap_id-symbolic.svg
%_iconsdir/hicolor/256x256/apps/%ap_id.png
%_datadir/metainfo/%ap_id.metainfo.xml
%doc LICENSE README.md CHANGELOG.md

%changelog
* Fri Jun 20 2025 L.A. Kostis <lakostis@altlinux.ru> 2.2.1-alt1
- 2.2.1.

* Fri Jun 06 2025 L.A. Kostis <lakostis@altlinux.ru> 2.2.0-alt1
- Initial build for ALTLinux.

