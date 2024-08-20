%define _unpackaged_files_terminate_build 1

Name: oversteer
Version: 0.8.3
Release: alt1

Summary: Steering wheel manager

License: GPLv3
Group: System/Configuration/Hardware
Url: https://github.com/berarma/oversteer

Source: %name-%version.tar
Patch2: %name-0.8.0-alt-fix-ru-locale.patch

BuildRequires(pre): rpm-build-python3 rpm-macros-meson
BuildRequires: meson pkgconfig(udev) /usr/bin/appstream-util
BuildRequires: python3-module-evdev python3-module-pyudev python3-module-pygobject3
BuildRequires: python3-module-pyxdg python3-module-matplotlib-gtk3 python3-module-scipy

Requires: python3-module-matplotlib-gtk3 python3-module-pyudev python3-module-scipy
Requires: python3-module-%name = %EVR

Conflicts: pyLinuxWheel

BuildArch: noarch

%description
Oversteer manages steering wheels on Linux using the features provided
by the loaded modules. It doesn't provide hardware support, you'll still
need a driver module that enables the hardware on Linux.

%package -n python3-module-%name
Summary: Oversteer python3 module files
Group: System/Configuration/Hardware
%description -n python3-module-%name
%summary

%prep
%setup
%patch2 -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_datadir/metainfo/io.github.berarma.Oversteer.appdata.xml
%_desktopdir/io.github.berarma.Oversteer.desktop
%_iconsdir/hicolor/scalable/apps/io.github.berarma.Oversteer.svg
%_udevrulesdir/*

%files -n python3-module-%name
%doc LICENSE README.md
%python3_sitelibdir/%name

%changelog
* Tue Aug 20 2024 Mikhail Tergoev <fidel@altlinux.org> 0.8.3-alt1
- 0.8.3

* Tue Dec 12 2023 Mikhail Tergoev <fidel@altlinux.org> 0.8.0-alt1
- Initial build for ALT Sisyphus.
