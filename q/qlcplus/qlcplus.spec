%def_with qmlui
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

Name:     qlcplus
Version:  5.2.2
Release:  alt1

Summary:  Q Light Controller Plus

License:  Apache-2.0
Group:    Other
Url:      https://github.com/mcallegari/qlcplus
Vcs:      https://github.com/mcallegari/qlcplus.git

Source:   %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++
BuildRequires: /proc
BuildRequires: libalsa-devel
BuildRequires: libcups-devel
BuildRequires: libftdi1-devel
BuildRequires: libudev-devel
BuildRequires: libusb-compat-devel
BuildRequires: pkgconfig(fftw3)
BuildRequires: pkgconfig(libftdi1)
BuildRequires: pkgconfig(sndfile)
BuildRequires: qt6-base-devel
BuildRequires: qt6-multimedia-devel
BuildRequires: qt6-serialport-devel
BuildRequires: qt6-tools
BuildRequires: qt6-tools-devel
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
sed -ie '/UDEVRULESDIR/s|/etc/udev/rules.d|/usr/lib/udev/rules.d|' variables.cmake
export LANG="C.UTF-8"

%build
export LANG="C.UTF-8"
%add_optflags -Wno-error=odr
%ifarch %ix86
%add_optflags -Wno-error=sign-compare
%endif
%if_with qmlui
./translate.sh release qmlui
%cmake -Dqmlui=ON
%else
./translate.sh release ui
%cmake
%endif
%cmake_build

%install
export LANG="C.UTF-8"
%cmake_install
%if_with qmlui
mv %buildroot%_bindir/qlcplus-qml %buildroot%_bindir/qlcplus
mv %buildroot%_datadir/applications/qlcplus5.desktop %buildroot%_datadir/applications/qlcplus.desktop
sed -i -e 's/Exec=qlcplus --open %f/Exec=qlcplus/g' %buildroot%_datadir/applications/qlcplus.desktop
%endif
rm %buildroot%_libdir/*.a

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
* Sun Jun 14 2026 Andrew A. Vasilyev <andy@altlinux.org> 5.2.2-alt1
- Update to 5.2.2.

* Sun Mar 15 2026 Andrew A. Vasilyev <andy@altlinux.org> 5.2.1-alt1
- Update to 5.2.1.

* Fri Feb 06 2026 Andrew A. Vasilyev <andy@altlinux.org> 5.2.0-alt1
- Update to 5.2.0.

* Tue Jan 06 2026 Andrew A. Vasilyev <andy@altlinux.org> 5.1.0-alt1
- Update to 5.1.0.
- Build with cmake.

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
