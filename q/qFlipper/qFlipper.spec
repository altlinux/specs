# I've built it with bundled nanopb to minimize surprises
%def_with bundled_nanopb

Name:    qFlipper
Version: 1.3.3
Release: alt1

Summary: qFlipper - desktop application for updating Flipper Zero firmware via PC

License: GPL-3.0
Group:   Sciences/Computer science
URL:     https://update.flipperzero.one
VCS:     https://github.com/flipperdevices/qFlipper

Source: %name-%version.tar
Source42: %name-%version-driver-tool-libwdi.tar
Source43: %name-%version-3rdparty-nanopb.tar

Patch: 0001-Disable-vendoring-of-nanopb.patch

BuildRequires:  qt5-base-devel
BuildRequires:  qt5-serialport-devel
BuildRequires:  qt5-quickcontrols2-devel
BuildRequires:  qt5-svg-devel
BuildRequires:  qt5-tools
BuildRequires:  libusb-devel
BuildRequires:  zlib-devel
%if_without bundled_nanopb
BuildRequires:  libnanopb-devel
%endif

%description
Graphical desktop application for updating Flipper Zero firmware via PC.

Features:
* Update Flipper's firmware and supplemental data with a press of one button
* Repair a broken fimware installation
* Stream Flipper's display and control it remotely
* Install firmware from a .dfu file
* Backup and restore settings, progress and pairing data
* Automatic self-update feature
* Command line interface

%prep
%setup -a42 -a43

%if_without bundled_nanopb
%patch -p1
%endif

gitver=$(echo %{version} | cut -d+ -f1)
gitdate=$(echo %{version} | tr '.' ' ' | rev | cut -d' ' -f2 | rev)
githash=$(echo %{version} | tr '.' ' ' | rev | cut -d' ' -f1 | rev)
sed -i -e "s|^[ \t]*GIT_VERSION = .*|GIT_VERSION = $gitver|" qflipper_common.pri
sed -i -e "s|^[ \t]*GIT_COMMIT = .*|GIT_COMMIT = $githash|" qflipper_common.pri
sed -i -e "s|^[ \t]*GIT_TIMESTAMP = .*|GIT_TIMESTAMP = $gitdate|" qflipper_common.pri
# Fix the plugins library path
sed -e 's:/lib/:/%_lib/:' \
    -i backend/applicationbackend.cpp plugins/flipperproto0/flipperproto0.pro
sed -i '/addLibraryPath/ s|../lib/|../%_lib/|' backend/applicationbackend.cpp

%build
%qmake_qt5 \
  -spec linux-g++ \
  PREFIX=%buildroot%_prefix \
  CONFIG+=qtquickcompiler \
  DEFINES+=DISABLE_APPLICATION_UPDATES
%make_build

%install
%makeinstall_std

%files
%doc LICENSE *.md
%_bindir/%name
%_bindir/%name-cli
%_udevrulesdir/42-flipperzero.rules
%_libdir/%name/plugins/libflipperproto0.so
%_datadir/applications/%name.desktop
%_datadir/icons/hicolor/512x512/apps/%name.png

%changelog
* Mon Nov 17 2025 Grigory Ustinov <grenka@altlinux.org> 1.3.3-alt1
- Initial build for Sisyphus.
