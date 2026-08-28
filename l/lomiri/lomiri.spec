%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

%define _libexecdir %_prefix/libexec
%define _udevrulesdir /lib/udev/rules.d

%set_verify_elf_skiplist %_libexecdir/lomiri/tests/*

Name: lomiri
Version: 0.6.1
Release: alt2

Summary: Shell of the Lomiri Operating Environment
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/core/lomiri

Source: %name-%version.tar

# sync with package version 0.6.1-1 from Debian unstable
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires(pre): rpm-macros-systemd
BuildRequires(pre): rpm-macros-qt5
BuildRequires(pre): rpm-build-qml

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(lomiri-shell-application)
BuildRequires: pkgconfig(geonames)
BuildRequires: pkgconfig(qmenumodel)
BuildRequires: pkgconfig(gnome-desktop-4)
BuildRequires: pkgconfig(lomiri-app-launch-0)
BuildRequires: pkgconfig(LomiriGestures)
BuildRequires: pkgconfig(deviceinfo)
BuildRequires: pkgconfig(lomiri-schemas)
BuildRequires: pkgconfig(liblightdm-qt5-3)
BuildRequires: pkgconfig(qtmirserver)
BuildRequires: pkgconfig(LomiriSystemSettings)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(lomiri-connectivity-qt1)
BuildRequires: pkgconfig(gsettings-qt)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: ayatana-cmake-modules
BuildRequires: pkgconfig(libusermetricsoutput-1)
BuildRequires: pkgconfig(ldm-common)
BuildRequires: pkgconfig(libevdev)
BuildRequires: /usr/bin/Xwayland
BuildRequires: libpam0-devel
BuildRequires: doxygen
BuildRequires: /usr/bin/dot

%if_with check
BuildRequires: ctest
BuildRequires: pkgconfig(libqtdbustest-1)
BuildRequires: pkgconfig(libqtdbusmock-1)
BuildRequires: dbus-test-runner
BuildRequires: qtdbustest-runner
BuildRequires: python3(dbusmock)
BuildRequires: /usr/bin/xvfb-run
%endif

Requires: ayatana-indicator-bluetooth
Requires: ayatana-indicator-display
Requires: ayatana-indicator-keyboard
Requires: ayatana-indicator-messages
Requires: ayatana-indicator-power
Requires: ayatana-indicator-session
Requires: ayatana-indicator-sound
Requires: deviceinfo-tools
Requires: lomiri-app-launch
Requires: x-cursor-themes-dmz
Requires: gsettings-desktop-schemas-data
Requires: libcap-utils
# qt5/qml/Biometryd/qmldir
Requires: biometryd
# qt5/qml/Lomiri/Components/ListItems/qmldir qt5/qml/Lomiri/Components/Pickers/qmldir qt5/qml/Lomiri/Components/Popups/qmldir qt5/qml/Lomiri/Components/Styles/qmldir qt5/qml/Lomiri/Components/qmldir qt5/qml/Lomiri/Layouts/qmldir
Requires: lomiri-ui-toolkit
# qt5/qml/Lomiri/Telephony/qmldir
Requires: lomiri-telephony-service
# qt5/qml/QMenuModel.1/qmldir
Requires: qml-module-qmenumodel1
# qt5/qml/Qt/labs/folderlistmodel/qmldir, qt5/qml/Qt/labs/settings/qmldir, qt5/qml/QtQml/StateMachine/qmldir, qt5/qml/QtQuick/Layouts/qmldir
Requires: libqt5-qml
# qt5/qml/QtMir/Application/qmldir
Requires: qtmir
# qt5/qml/QtQuick/XmlListModel/qmldir
Requires: libqt5-xmlpatterns
# qt5/qml/QtSystemInfo/qmldir
Requires: libqt5-qtsystems
# qt5/qml/Hfd/qmldir
Requires: hfd-service

Requires: lomiri-indicator-datetime
Requires: lomiri-indicator-network
Requires: lomiri-system-settings
Requires: lomiri-url-dispatcher
Requires: lomiri-content-hub
Requires: lomiri-ui-extras

# qt5/qml/Lomiri/Settings/Components/qmldir qt5/qml/Lomiri/Settings/Menus/Style/qmldir qt5/qml/Lomiri/Settings/Menus/qmldir
Requires: lomiri-settings-components
# qt5/qml/Lomiri/Thumbnailer.0.1/qmldir
Requires: lomiri-thumbnailer

Requires: lomiri-schemas
Requires: lomiri-notifications

Requires: qt5-graphicaleffects
# qt5/qml/QtMultimedia/qmldir
Requires: libqt5-multimedia

Requires: qt5-wayland

%description
Shell of the Lomiri Operating environment optimized for touch based
human-machine interaction, but also supporting convergence (i.e.
switching between tablet/phone and desktop mode). Lomiri is the user
shell driving Ubuntu Touch based mobile devices.

This package provides the Lomiri shell.

%package -n lib%{name}
Summary: %{name} shared library
Group: System/Libraries
Requires: lomiri-schemas
Requires: libgsettings-qt1
Requires: libqt5-multimedia

%description -n lib%{name}
%{name} shared library.

%package -n lib%{name}-devel
Summary: Development files for %{name}
Group: Development/Other
Requires: lib%{name} = %{version}-%{release}

%description -n lib%{name}-devel
The %{name}-devel package contains private library for %{name}.

%package -n %{name}-lightdm-greeter
Summary: LightDM Greeter for the Lomiri Operating Environment
Group: Graphical desktop/Other
Requires: %{name} = %{version}-%{release}
Requires: lightdm

%description -n %{name}-lightdm-greeter
LightDM Greeter for the Lomiri Operating Environment

%prep
%setup
%patch -p1
sed -i "s|QDBUSXML2CPP_EXECUTABLE qdbusxml2cpp|QDBUSXML2CPP_EXECUTABLE qdbusxml2cpp-qt5|" tests/CMakeLists.txt

%build
%cmake \
       -Wno-dev \
       -Dqmlplugindump_exe=%_qt5_bindir/qmlplugindump \
       -DCMAKE_INSTALL_LOCALSTATEDIR="/var" \
       -DDISPLAYED_DISTRO_NAME="ALT Linux" \
       -DWITH_MIR2=ON \
%if_with check
       -DNO_TESTS=OFF \
       -Dqmltestrunner_exe=%_qt5_bindir/qmltestrunner
%else
       -DNO_TESTS=ON
%endif
%cmake_build

%install
%cmake_install

install -m 0755 data/lomiri-greeter-wrapper %buildroot%_bindir
install -pDm 0644 data/lomiri-greeter.rules %buildroot%_datadir/polkit-1/rules.d/lomiri-greeter.rules
install -pDm 0644 debian/lomiri-common.udev %buildroot%_udevrulesdir/60-lomiri-common.rules
install -pDm 0644 data/devices.conf %buildroot%_sysconfdir/lomiri/devices.conf

# follow debian/rules
rm -vf %buildroot%_bindir/indicators-client
rm -vf %buildroot%_desktopdir/indicators-client.desktop
rm -vf %buildroot%_datadir/lomiri/unlock-device
rm -vf %buildroot%_datadir/lomiri/Wizard/Pages/*-update.qml*
rm -vf %buildroot%_userunitdir/*.service

# create configuration files
mkdir -p %buildroot/etc/lightdm/lightdm.conf.d/

cat <<EOF > %buildroot/etc/lightdm/lightdm.conf.d/90-default-session-lomiri.conf
[Seat:*]
user-session=lomiri
EOF

cat <<EOF > %buildroot/etc/lightdm/lightdm.conf.d/91-lomiri-enable-user-list.conf
[Seat:*]

# show local user names at Lomiri Greeter login prompt
greeter-hide-users=false

# don't neither show a username / password login prompt for local login
greeter-show-manual-login=false
EOF

%find_lang %name

%post
%systemd_user_post lomiri-indicators.target

%preun
%systemd_user_preun lomiri-indicators.target

%postun
%systemd_user_postun lomiri-indicators.target

%check
%ctest -j1 -VV -R xvfballtests

# do not package lomiri-tests
rm -vrf %buildroot%_libdir/lomiri/qml/mocks
rm -vf  %buildroot%_bindir/lomiri-mock-indicator-service
rm -vf  %buildroot%_libexecdir/lomiri/uqmlscene
rm -vrf %buildroot%_libexecdir/lomiri/tests/

%files -f %{name}.lang
%doc AUTHORS COPYING COPYING.LGPL LGPL_EXCEPTION.txt README.md
%_bindir/lomiri
%_sysconfdir/lomiri/devices.conf
%exclude %_datadir/locale/it_CARES/LC_MESSAGES/lomiri.mo
%exclude %_datadir/locale/zh_LATN@pinyin/LC_MESSAGES/lomiri.mo
%dir %_libdir/lomiri
%_libdir/lomiri/*
%_libexecdir/Xwayland.lomiri
%_libexecdir/lomiri-systemd-wrapper
%dir %_datadir/lomiri
%_datadir/lomiri/*
%_datadir/polkit-1/rules.d/50-com.lomiri.wizard.rules
%_datadir/accountsservice/interfaces/com.lomiri.shell.AccountsService.xml
%_desktopdir/lomiri.desktop
%_userunitdir/lomiri-indicators.target
%_udevrulesdir/60-lomiri-common.rules

%dir %_localstatedir/lomiri
%_localstatedir/lomiri/version

%files -n %{name}-lightdm-greeter
%_sysconfdir/lightdm/lightdm.conf.d/90-default-session-lomiri.conf
%_sysconfdir/lightdm/lightdm.conf.d/91-lomiri-enable-user-list.conf
%_bindir/lomiri-greeter-wrapper
%_datadir/lightdm/greeters/lomiri-greeter.desktop
%_datadir/lightdm/lightdm.conf.d/51-lomiri-greeter.conf
%_datadir/polkit-1/rules.d/lomiri-greeter.rules

%files -n lib%{name}
%_libdir/liblomiri-private.so.0*

%files -n lib%{name}-devel
%_libdir/liblomiri-private.so
%_datadir/dbus-1/interfaces/com.lomiri.ProcessControl.xml
%_datadir/dbus-1/interfaces/com.lomiri.shell.AccountsService.xml

%changelog
* Fri Aug 28 2026 Nikolay Strelkov <snk@altlinux.org> 0.6.1-alt2
* Updated systemd user target.

* Wed Aug 26 2026 Nikolay Strelkov <snk@altlinux.org> 0.6.1-alt1
- New version 0.6.1.

* Thu Jul 23 2026 Nikolay Strelkov <snk@altlinux.org> 0.6.0-alt1
- New version 0.6.0.

* Sun Jun 28 2026 Nikolay Strelkov <snk@altlinux.org> 0.5.0-alt2
- Updated to allow build with mir 2.28.0.
- Enabled tests.

* Sat Jul 12 2025 Nikolay Strelkov <snk@altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus
