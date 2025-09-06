%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

Name: lomiri-system-settings
Version: 1.3.1
Release: alt2

Summary: System Settings application for Lomiri
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/core/lomiri-system-settings

Source: %name-%version.tar

# sync with version 1.3.1-6 from Debian unstable + local fixes
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires(pre): rpm-macros-qt5
BuildRequires(pre): rpm-build-qml

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt5Concurrent)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(polkit-agent-1)
BuildRequires: pkgconfig(upower-glib)
BuildRequires: pkgconfig(accountsservice)
BuildRequires: pkgconfig(geonames)
BuildRequires: pkgconfig(click-0.4)
BuildRequires: pkgconfig(gsettings-qt)
BuildRequires: pkgconfig(gnome-desktop-3.0)
BuildRequires: pkgconfig(deviceinfo)

%if_with check
BuildRequires: ctest
BuildRequires: dbus
BuildRequires: /proc
BuildRequires: /usr/bin/dbus-test-runner
BuildRequires: /usr/bin/xvfb-run
BuildRequires: pkgconfig(libqtdbusmock-1)
BuildRequires: ayatana-cmake-modules
BuildRequires: lomiri-ui-toolkit
BuildRequires: lomiri-settings-components
BuildRequires: python3(dbusmock)
BuildRequires: qt5-graphicaleffects
%endif

Requires: accountsservice
Requires: bluez
Requires: glib2
Requires: gsettings-desktop-schemas
Requires: fonts-ttf-google-noto-sans
# qt5/qml/Lomiri/Connectivity/qmldir
Requires: lomiri-indicator-network
Requires: lomiri-schemas
Requires: lomiri-sounds
Requires: lomiri-wallpapers
Requires: libgsettings-qt1
# qt5/qml/Lomiri/Components/ListItems/qmldir, qt5/qml/Lomiri/Components/Pickers/qmldir, qt5/qml/Lomiri/Components/Popups/qmldir, qt5/qml/Lomiri/Components/Styles/qmldir, qt5/qml/Lomiri/Components/qmldir
Requires: lomiri-ui-toolkit
# qt5/qml/Lomiri/Components/Extras/PamAuthentication/qmldir, qt5/qml/Lomiri/Components/Extras/Printers/qmldir, qt5/qml/Lomiri/Components/Extras/qmldir
Requires: lomiri-ui-extras
# qt5/qml/Lomiri/Content/qmldir
Requires: lomiri-content-hub
# qt5/qml/Lomiri/Settings/Components/qmldir, qt5/qml/Lomiri/Settings/Fingerprint/qmldir, qt5/qml/Lomiri/Settings/Menus/Style/qmldir, qt5/qml/Lomiri/Settings/Menus/qmldir, qt5/qml/Lomiri/Settings/Vpn/qmldir
Requires: lomiri-settings-components
# qt5/qml/QOfono/qmldir
Requires: libqofono
# qt5/qml/Qt/labs/folderlistmodel/qmldir
Requires: libqt5-qml
# qt5/qml/QtSystemInfo/qmldir
Requires: libqt5-qtsystems

%ifnarch i586 riscv64
Requires: signon-ui
%endif

Requires: upower

Requires: qt5-quickcontrols2
Requires: maliit-keyboard
Requires: lomiri-keyboard-data
Requires: tecla

%description
The system settings application (and library) for the Lomiri desktop
enviroment.

%package -n lib%{name}
Summary: %name shared library
Group: System/Libraries

%description -n lib%{name}
%{name} shared library.

%package -n lib%{name}-private
Summary: %{name} private shared library
Group: System/Libraries

%description -n lib%{name}-private
%{name} private shared library.

%package -n lib%{name}-devel
Summary: Development files for %{name}
Group: Development/Other
Requires: lib%{name} = %{version}-%{release}
Requires: lib%{name}-private = %{version}-%{release}

%description -n lib%{name}-devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup
%patch -p1

%build
%cmake \
       -DENABLE_LIBDEVICEINFO=ON \
%if_with check
       -DENABLE_TESTS=ON \
       -Dqmlplugindump_exe=%_qt5_bindir/qmlplugindump \
       -Dqmltestrunner_exe=%_qt5_bindir/qmltestrunner
%else
       -DENABLE_TESTS=OFF
%endif
%cmake_build

%install
%cmake_install

%find_lang %name --all-name

%check
%ctest -j1 -VV

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING README.md
%_bindir/%name
%_desktopdir/%{name}.desktop
%_datadir/glib-2.0/schemas/com.lomiri.%{name}.gschema.xml
%dir %_datadir/lomiri-url-dispatcher
%_datadir/lomiri-url-dispatcher/*
%dir %_datadir/%name
%_datadir/%name/*
%dir %_libdir/%name
%_libdir/%name/*
%exclude %_datadir/locale/it_CARES/LC_MESSAGES/lomiri-system-settings.mo
%exclude %_datadir/locale/zh_LATN@pinyin/LC_MESSAGES/lomiri-system-settings.mo

%files -n lib%{name}
%_libdir/libLomiriSystemSettings.so.1*

%files -n lib%{name}-private
%_libdir/libLomiriSystemSettingsPrivate.so.0.0

%files -n lib%{name}-devel
%dir %_includedir/LomiriSystemSettings
%_includedir/LomiriSystemSettings/*
%_libdir/libLomiriSystemSettings.so
%_libdir/libLomiriSystemSettingsPrivate.so
%_pkgconfigdir/LomiriSystemSettings.pc

%changelog
* Sat Sep 06 2025 Nikolay Strelkov <snk@altlinux.org> 1.3.1-alt2
- Enabled install on riscv64 architecture

* Mon Jul 14 2025 Nikolay Strelkov <snk@altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus
