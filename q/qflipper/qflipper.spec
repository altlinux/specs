%global commit 3ec0fd9debd531faaabb391d900dcfc6ee3c0aca
# git log -1 --pretty=format:%%ct
%global timestamp 1664810141
%global nanopb_commit 13666952914f3cf43a70c6b9738a7dc0dd06a6dc

%global srcname qFlipper
%global forgeurl https://github.com/flipperdevices/%srcname
%global shortcommit %(c=%commit; echo ${c:0:7})

Name: qflipper
Version: 1.2.1
Release: alt1

Summary: Desktop application for updating Flipper Zero firmware via PC
# qFlipper proper is GPLv3, the bundled nanopb library is zlib
License: GPLv3 and Zlib
Group: System/Configuration/Hardware

Url: https://update.flipperzero.one
Source0: %forgeurl/archive/%version/%srcname-%version.tar.gz
Source1: https://github.com/nanopb/nanopb/archive/%nanopb_commit/nanopb-%nanopb_commit.tar.gz
Source2: 42-flipperzero.rules
Source3: one.flipperzero.qflipper.metainfo.xml

# qFlipper fails to build on i686
ExcludeArch: %ix86

BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: libappstream-glib
BuildRequires: make
BuildRequires: sed
#BuildRequires:  systemd-rpm-macros

BuildRequires: libusb-devel
BuildRequires: qt5-linguist
BuildRequires: qt5-base-devel
BuildRequires: qt5-quickcontrols2-devel
BuildRequires: qt5-serialport-devel
BuildRequires: qt5-svg-devel
BuildRequires: zlib-devel

BuildRequires: rpm-macros-fedora-compat

# nanopb needs to be compiled in, and needs to match the one used in the
# firmware on the device side
Provides: bundled(nanopb) = 0.4.5

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
%setup -n %srcname-%version -b 1

# Use the correct nanopb snapshot
rmdir 3rdparty/nanopb
ln -s ../../nanopb-%nanopb_commit 3rdparty/nanopb

# Set the version
sed -i qflipper_common.pri \
    -e 's/$$GIT_VERSION/%version/' \
    -e 's/$$GIT_COMMIT/%shortcommit/' \
    -e 's/$$GIT_TIMESTAMP/%timestamp/'

# Fix the plugins library path
sed -e 's:/lib/:/%_lib/:' \
    -i backend/applicationbackend.cpp plugins/flipperproto0/flipperproto0.pro

%build
%qmake_qt5 \
  PREFIX=%buildroot%prefix \
  CONFIG+=qtquickcompiler \
  DEFINES+=DISABLE_APPLICATION_UPDATES

%make_build

%install
%makeinstall_std

# application.pro has it inconvenient for patching
mkdir -p %buildroot%_udevrulesdir
mv %buildroot{/usr/lib/udev/rules.d,%_udevrulesdir}/42-flipperzero.rules

# Install the appdata file
install -Dpm0644 -t %buildroot%_metainfodir %SOURCE3

%check
# Validate desktop files
appstream-util validate-relax --nonet %buildroot%_metainfodir/*.metainfo.xml
desktop-file-validate %buildroot/%_datadir/applications/%srcname.desktop

%files
%doc LICENSE 3rdparty/nanopb/LICENSE.txt
%doc README.md screenshot.png
%_bindir/*
%_libdir/%srcname
%_datadir/applications/%srcname.desktop
%_datadir/icons/hicolor/512x512/apps/%srcname.png
%_metainfodir/one.flipperzero.qflipper.metainfo.xml
%_udevrulesdir/42-flipperzero.rules

%changelog
* Sun Nov 13 2022 Michael Shigorin <mike@altlinux.org> 1.2.1-alt1
- built for ALT Linux for ge0gr4f
  + based on Fedora package 1.2.1-1
  + see also http://t.me/e2k_chat/170965
  + do not install custom udev rules, just fix upstream installation path

* Sat Oct 15 2022 Davide Cavalca <dcavalca@fedoraproject.org> 1.2.1-1
- Update to 1.2.1; Fixes: RHBZ#2110813

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 24 2022 Davide Cavalca <dcavalca@fedoraproject.org> 1.1.0-1
- Update to 1.1.0; Fixes: RHBZ#2072789

* Sat Mar 26 2022 Davide Cavalca <davide@cavalca.name> 1.0.0-1
- Update to 1.0.0; Fixes: RHBZ#2068765

* Mon Mar 14 2022 Davide Cavalca <dcavalca@fedoraproject.org> 0.9.2-1
- Initial import; Fixes: RHBZ#2063445
