Name:     qslave
Version:  1.0.2
Release:  alt1%ubt

Summary:  Modbus network emulator
License:  GPL-2.0
Group:    Engineering
Url:      https://github.com/maisvendoo/qslave

Packager: Anton Midyukov <antohami@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires: gcc-c++ qt5-base-devel pkgconfig(Qt5SerialPort)

%description
%summary

%prep
%setup

%build
%qmake_qt5
%make_build

%install
cat >%name.desktop<<END
[Desktop Entry]
Name=%name
Exec=%_bindir/%name
Icon=%name
Terminal=false
Type=Application
Categories=Network;Engineering
END

install -Dm644 %name.desktop %buildroot%_desktopdir/%name.desktop
install -Dm644 %name-gui/resources/img/logo.png %buildroot%_pixmapsdir/%name.png
install -Dm644 cfg/example/example.net %buildroot%_sysconfdir/%name/example/example.net
install -Dm644 cfg/example/traffic-light.xml %buildroot%_sysconfdir/%name/example/traffic-light.xml

cd ../bin
install -Dm755 %name-gui %buildroot%_bindir/%name

%files
%doc LICENSE
%_bindir/%name
%_sysconfdir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png

%changelog
* Fri Dec 29 2017 Anton Midyukov <antohami@altlinux.org> 1.0.2-alt1%ubt
- Initial build for Sisyphus
