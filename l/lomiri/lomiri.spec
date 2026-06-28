%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

%define _libexecdir %_prefix/libexec

%set_verify_elf_skiplist %_libexecdir/lomiri/tests/*

Name: lomiri
Version: 0.5.0
Release: alt2

Summary: Shell of the Lomiri Operating Environment
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/core/lomiri

Source: %name-%version.tar

# sync with package version 0.5.0-14 from Debian unstable
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
BuildRequires: pkgconfig(gnome-desktop-3.0)
BuildRequires: pkgconfig(lomiri-app-launch-0)
BuildRequires: pkgconfig(LomiriGestures)
BuildRequires: pkgconfig(deviceinfo)
BuildRequires: pkgconfig(lomiri-schemas)
BuildRequires: pkgconfig(liblightdm-qt5-3)
BuildRequires: pkgconfig(mirserver)
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
BuildRequires: pkgconfig(qtmirserver)
BuildRequires: doxygen
BuildRequires: /usr/bin/dot

%if_with check
BuildRequires: ctest
BuildRequires: pkgconfig(libqtdbustest-1)
BuildRequires: pkgconfig(libqtdbusmock-1)
BuildRequires: dbus-test-runner
BuildRequires: qtdbustest-runner
BuildRequires: python3(dbusmock)
%endif

Requires: ayatana-indicator-bluetooth
Requires: ayatana-indicator-display
Requires: ayatana-indicator-keyboard
Requires: ayatana-indicator-messages
Requires: ayatana-indicator-power
Requires: ayatana-indicator-session
Requires: ayatana-indicator-sound
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

# qt5/qml/Lomiri/Settings/Components/qmldir qt5/qml/Lomiri/Settings/Menus/Style/qmldir qt5/qml/Lomiri/Settings/Menus/qmldir
Requires: lomiri-settings-components
# qt5/qml/Lomiri/Thumbnailer.0.1/qmldir
Requires: lomiri-thumbnailer

Requires: lomiri-schemas
Requires: lomiri-notifications

Requires: qt5-graphicaleffects
# qt5/qml/QtMultimedia/qmldir
Requires: libqt5-multimedia

%description
Shell of the Lomiri Operating environment optimized for touch based
human-machine interaction, but also supporting convergence (i.e.
switching between tablet/phone and desktop mode). Lomiri is the user
shell driving Ubuntu Touch based mobile devices.

This package provides the Lomiri shell. 

%package -n lib%{name}
Summary: %{name} shared library
Group: System/Libraries

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
%systemd_user_post lomiri-full-greeter.service
%systemd_user_post lomiri-full-shell.service
%systemd_user_post lomiri-greeter.service
%systemd_user_post lomiri-indicators.target
%systemd_user_post lomiri-shell.service

echo "NOTE: upstream project does not provide systemd preset for user units,"
echo "      so you need to run the below commands to enable all essential"
echo "      systemd user units of the Lomiri environment as normal user:"
echo " "
echo "systemctl --user enable --now ayatana-indicator-bluetooth.service"
echo "systemctl --user enable --now ayatana-indicator-display.service"
echo "systemctl --user enable --now ayatana-indicator-keyboard.service"
echo "systemctl --user enable --now ayatana-indicator-messages.service"
echo "systemctl --user enable --now ayatana-indicator-power.service"
echo "systemctl --user enable --now ayatana-indicator-session.service"
echo "systemctl --user enable --now ayatana-indicator-sound.service"
echo "systemctl --user enable --now lomiri-indicator-datetime.service"
echo "systemctl --user enable --now lomiri-indicator-network.service"
echo "systemctl --user enable --now lomiri-url-dispatcher-update-system-dir.{service,path}"
echo "systemctl --user enable --now lomiri-url-dispatcher-update-user-dir.{service,path}"
echo " "
echo "And then you can login to the Lomiri session using preffered login manager."

%preun
%systemd_user_preun lomiri-full-greeter.service
%systemd_user_preun lomiri-full-shell.service
%systemd_user_preun lomiri-greeter.service
%systemd_user_preun lomiri-indicators.target
%systemd_user_preun lomiri-shell.service

%postun
%systemd_user_postun lomiri-full-greeter.service
%systemd_user_postun lomiri-full-shell.service
%systemd_user_postun lomiri-greeter.service
%systemd_user_postun lomiri-indicators.target
%systemd_user_postun lomiri-shell.service

%check
%ctest -j1 -VV

# do not package lomiri-tests
rm -vrf %buildroot%_libdir/lomiri/qml/mocks
rm -vf  %buildroot%_bindir/lomiri-mock-indicator-service
rm -vf  %buildroot%_libexecdir/lomiri/uqmlscene
rm -vrf %buildroot%_libexecdir/lomiri/tests/

%files -f %{name}.lang
%doc AUTHORS ChangeLog CODING COPYING COPYING.LGPL LGPL_EXCEPTION.txt README.md
%_bindir/indicators-client
%_bindir/lomiri
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
%_desktopdir/indicators-client.desktop
%_desktopdir/lomiri.desktop
%_userunitdir/lomiri-full-greeter.service
%_userunitdir/lomiri-full-shell.service
%_userunitdir/lomiri-greeter.service
%_userunitdir/lomiri-indicators.target
%_userunitdir/lomiri-shell.service

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
* Sun Jun 28 2026 Nikolay Strelkov <snk@altlinux.org> 0.5.0-alt2
- Updated to allow build with mir 2.28.0.
- Enabled tests.

* Sat Jul 12 2025 Nikolay Strelkov <snk@altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus
