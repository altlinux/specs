%define _unpackaged_files_terminate_build 1

Name: cameractrls
Version: 0.5.11
Release: alt1

Summary: Camera controls

License: MIT
Group: Video
Url: https://github.com/soyersoyer/cameractrls

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

Requires: python3-module-%name = %EVR
Requires: python3-module-pygobject3 libgtk4-gir

BuildArch: noarch

%description
It's a standalone Python CLI and GUI (GTK3, GTK4, TK) and camera Viewer (SDL)
to set the camera controls in Linux. It can set the V4L2 controls and it is
extendable with the non standard controls. Currently it has a Logitech extension
(LED mode, LED frequency, BRIO FoV, relative Pan/Tilt), Kiyo Pro extension
(HDR, HDR mode, FoV, AF mode, Save), Systemd extension (Save and restore
controls with Systemd path+service).

%package -n python3-module-%name
Summary: Camera controls python3 module files
Group: Video
Requires: python3 libjpeg libSDL2
%py3_provides %name

%description -n python3-module-%name
%summary

%prep
%setup

%build
%install
pushd pkg
install -Dm644 hu.irl.%name.desktop %buildroot%_desktopdir/hu.irl.%name.desktop
install -Dm644 hu.irl.%name.svg %buildroot%_iconsdir/hicolor/scalable/apps/hu.irl.%name.svg
install -Dm644 hu.irl.%name.svg %buildroot%python3_sitelibdir/CameraCtrls/images/hu.irl.%name.svg
install -Dm644 hu.irl.%name.metainfo.xml %buildroot%_datadir/appdata/hu.irl.%name.metainfo.xml
popd

install -Dm755 *.py %buildroot%python3_sitelibdir/CameraCtrls

mkdir -p %buildroot%_bindir
ln -s %python3_sitelibdir/CameraCtrls/%{name}gtk4.py %buildroot%_bindir/%{name}gtk4
ln -s %python3_sitelibdir/CameraCtrls/%name.py %buildroot%_bindir/%name

pushd %buildroot%_desktopdir
%__subst "s/Exec=.*/Exec=%{name}gtk4/" hu.irl.%name.desktop
%__subst "s/Name=.*/Name=Cameractrls/" hu.irl.%{name}.desktop
%__subst "/Comment=/aComment[ru]=Управление камерой" hu.irl.%name.desktop
popd

%files
%_bindir/%name
%_bindir/%{name}gtk4
%_desktopdir/hu.irl.%name.desktop
%_datadir/appdata/hu.irl.%name.metainfo.xml
%_iconsdir/hicolor/scalable/apps/hu.irl.%name.svg

%files -n python3-module-%name
%doc LICENSE CHANGELOG.md README.md
%python3_sitelibdir/CameraCtrls

%changelog
* Wed Nov 08 2023 Mikhail Tergoev <fidel@altlinux.org> 0.5.11-alt1
- initial build for ALT Sisyphus
