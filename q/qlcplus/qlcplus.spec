%def_with qmlui

Name:     qlcplus
Version:  5.0.1
Release:  alt2

Summary:  Q Light Controller Plus

License:  Apache-2.0
Group:    Other
Url:      https://github.com/mcallegari/qlcplus

Source:   %name-%version.tar
Patch1:   qlcplus-qmlui.patch

BuildRequires: gcc-c++
BuildRequires: libalsa-devel libftdi1-devel libudev-devel libusb-compat-devel
BuildRequires: qt6-base-devel
BuildRequires: qt6-multimedia-devel
BuildRequires: qt6-serialport-devel
BuildRequires: qt6-tools
BuildRequires: qt6-websockets-devel
%if_with qmlui
BuildRequires: qt6-3d-devel
BuildRequires: qt6-svg-devel
%endif

%description
QLC+ is a fork of the great QLC project written by Heikki Junnila. This project
aims to continue the development of QLC and to introduce new features.
The primary goal is to bring QLC+ at the level of other lighting control
commercial softwares.

%prep
%setup
sed -ie '/UDEVRULESDIR/s|/etc/udev/rules.d|/usr/lib/udev/rules.d|' variables.pri
%ifarch %ix86
sed -ie "s/QMAKE_CXXFLAGS += -Werror/#&/g" variables.pri
%endif
export LANG="C.UTF-8"
%if_with qmlui
%autopatch -p1
%endif

%build
export LANG="C.UTF-8"
%if_with qmlui
./translate.sh release qmlui
qmake-qt6 CONFIG+=qmlui
%else
./translate.sh release ui
qmake-qt6
%endif
%make_build

%install
export LANG="C.UTF-8"
INSTALL_ROOT=%buildroot make install
%if_with qmlui
mv %buildroot/%_bindir/qlcplus-qml %buildroot/%_bindir/qlcplus
sed -i -e 's/Exec=qlcplus --open %f/Exec=qlcplus/g' %buildroot/%_datadir/applications/qlcplus.desktop
%endif

%files
%_bindir/qlcplus
%_libdir/libqlcplusengine*
%_datadir/qlcplus/
%_libdir/qt6/plugins/qlcplus/
%_datadir/applications/qlcplus.desktop
%_datadir/mime/packages/%name.xml
%_datadir/pixmaps/qlcplus.png
%_datadir/mime/packages/qlcplus.xml
%_datadir/metainfo/org.qlcplus.*
%_udevrulesdir/*
%if_without qmlui
%_bindir/qlcplus-fixtureeditor
%_libdir/libqlcplusui*
%_libdir/libqlcpluswebaccess*
%_man1dir/*
%_datadir/applications/qlcplus-fixtureeditor.desktop
%_datadir/pixmaps/qlcplus-fixtureeditor.png
%endif

%changelog
* Wed Dec 24 2025 Andrew A. Vasilyev <andy@altlinux.org> 5.0.1-alt2
- Add translations and new UI.

* Tue Dec 23 2025 Andrew A. Vasilyev <andy@altlinux.org> 5.0.1-alt1
- Update to 5.0.1.
- Build with qt6.

* Wed Sep 09 2020 Grigory Ustinov <grenka@altlinux.org> 5.0.0-alt1.alpha3
- Build again without Werror flag (Closes: #36799).
- Fix license.

* Mon May 27 2019 Grigory Ustinov <grenka@altlinux.org> 5.0.0-alt0.alpha3
- Initial build for Sisyphus (Closes: #36799).
