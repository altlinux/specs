%define _unpackaged_files_terminate_build 1

Name: pyLinuxWheel
Version: 0.6.1
Release: alt2

Summary: A simple utility to configure logitech steering wheels for Linux

License: GPLv3
Group: Development/Python3
Url: https://gitlab.com/OdinTdh/pyLinuxWheel

# Source-url: https://gitlab.com/OdinTdh/pyLinuxWheel/-/archive/%version/pyLinuxWheel-%version.tar.gz
Source: %name-%version.tar

Patch1: pyLinuxWheel-0.6.1-alt-added_ru_locale.patch

BuildRequires(pre): rpm-build-python3
# For desktop file & AppData
BuildRequires: libappstream-glib desktop-file-utils

Requires: python3-module-pycairo python3-module-evdev python3-module-pygobject python3-module-pyudev
Requires: udev

AutoReq: no

BuildArch: noarch

%description
%summary

%prep
%setup
%patch1 -p1
pushd locale/ru/LC_MESSAGES/
msgfmt -o %name.mo %name.po
popd
rm -v locale/%name.pot
rm -v locale/*/LC_MESSAGES/*.po

%__subst 's/Utility/Game/' data/desktop/io.itch.pyLinuxWheel.desktop
%__subst 's/Exec=pyLinuxWheel/Exec=pylinuxwheel/' data/desktop/io.itch.pyLinuxWheel.desktop

%build
%install
mkdir -p %buildroot%_bindir/
install -m 755 pyLinuxWheel.py %buildroot%_bindir/pylinuxwheel
mkdir -p %buildroot%_desktopdir/
install -m 644 data/desktop/io.itch.pyLinuxWheel.desktop %buildroot%_desktopdir/pyLinuxWheel.desktop
mkdir -p %buildroot%_pixmapsdir/
install -m 644 data/img/icon-64-pyLinuxWheel.png %buildroot%_pixmapsdir/pyLinuxWheel.png
mkdir -p %buildroot%_datadir/pyLinuxWheel/
cp -rv data %buildroot%_datadir/pyLinuxWheel/
cp -rv locale %buildroot%_datadir/
mkdir -p %buildroot%_datadir/metainfo
cp -rv metainfo/io.itch.pyLinuxWheel.appdata.xml %buildroot%_datadir/metainfo/io.itch.pyLinuxWheel.appdata.xml
mkdir -p  %buildroot/lib/udev/rules.d/
cp -rv data/rules/99-logitech-wheel-perms.rules %buildroot/lib/udev/rules.d/
%find_lang %name

%files -f %name.lang
%doc *.md LICENSE
%_bindir/pylinuxwheel
%_desktopdir/pyLinuxWheel.desktop
%_pixmapsdir/pyLinuxWheel.png
%_datadir/pyLinuxWheel/
%_udevrulesdir/99-logitech-wheel-perms.rules
%_datadir/metainfo/io.itch.pyLinuxWheel.appdata.xml

%check
%_bindir/desktop-file-validate %buildroot%_desktopdir/pyLinuxWheel.desktop
%_bindir/appstream-util validate-relax --nonet %buildroot%_datadir/metainfo/io.itch.pyLinuxWheel.appdata.xml

%changelog
* Mon Aug 28 2023 Mikhail Tergoev <fidel@altlinux.org> 0.6.1-alt2
- find_lang is used for translation
- added Russian translation

* Wed Aug 02 2023 Mikhail Tergoev <fidel@altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus
