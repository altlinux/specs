%define _unpackaged_files_terminate_build 1

Name: ingame
Version: 0.4.4
Release: alt1

Summary: A modern GUI for PortProton project.

License: MIT
Group: Games/Other
Url: https://github.com/Castro-Fidel/ingame

Source: %name-%version.tar
Source1: %name.desktop

BuildRequires(pre): rpm-build-python3

Requires: python3-module-%name = %EVR
Requires: python3-module-desktop-parser
Requires: python3-module-steam-api
Requires: python3-module-steamgriddb
Requires: python3-module-pyside6
Requires: python3-module-shiboken6
Requires: python3-module-pyqtgraph
Requires: python3-module-requests
Requires: python3-module-pygame
Requires: python3-module-platformdirs
Requires: qt6-declarative qt6-5compat qt6-svg

BuildArch: noarch

%description
A modern GUI for PortProton project.
For convenient launching of games with gamepads and touch screens.

%package -n python3-module-%name
Summary: Ingame python3 module files
Group: Games/Other
%description -n python3-module-%name
%summary

%prep
%setup

%build
%install
# base files
install -Dm755 ingame.sh %buildroot%_bindir/ingame
install -Dm644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
install -Dm644 qml/icons/%name.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg
mkdir -p %buildroot%_datadir/%name
cp -rv qml %buildroot%_datadir/%name/
sed -i "s|../qml/qml.qml|%_datadir/%name/qml/qml.qml|" ingame/main.py
mv -v ingame/main.py %buildroot%_datadir/%name/

# python3 module files
mkdir -p %buildroot%python3_sitelibdir/%name
cp -rv %name %buildroot%python3_sitelibdir/

%files
%_bindir/ingame
%_datadir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg

%files -n python3-module-%name
%doc *.md LICENSE
%python3_sitelibdir/%name

%changelog
* Thu Aug 15 2024 Mikhail Tergoev <fidel@altlinux.org> 0.4.4-alt1
- updated version to 0.4.4

* Mon Aug 12 2024 Mikhail Tergoev <fidel@altlinux.org> 0.4.3-alt1
- initial build for ALT Sisyphus

