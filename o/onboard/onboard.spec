%define _unpackaged_files_terminate_build 1

Name: onboard
Version: 1.4.1
Release: alt7.git8de1177

Summary: Simple on-screen Keyboard
License: GPL-3.0+ and BSD
Group: Graphical desktop/GNOME
URL: https://launchpad.net/onboard/

Source0: http://launchpad.net/%name/0.96/%version/+download/%name-%version.tar.gz
Source1: ru.po
Patch: build-against-Ayatana-AppIndicator.patch
Patch1: 1004-fix-ftbfs-python3-12.patch

BuildRequires(pre): rpm-build-gnome rpm-macros-python3
BuildRequires: gcc-c++
BuildRequires: desktop-file-utils
BuildRequires: intltool
BuildRequires: libXi-devel
BuildRequires: libXtst-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libcanberra-devel
BuildRequires: libdconf-devel
BuildRequires: libgtk+3-devel
BuildRequires: libhunspell-devel
BuildRequires: libxkbfile-devel
BuildRequires: python3-module-distutils-extra >= 2.12
BuildRequires: libudev-devel

Requires: python3-module-dbus
# see ALT bug #35174
Requires: iso-codes

%add_python3_self_prov_path %buildroot%python3_sitelibdir/Onboard/pypredict

%description
An on-screen keyboard useful on tablet PCs or for mobility impaired
users.

%package gnome
Group:    Graphical desktop/GNOME
Summary:  GNOME Shell support for onboard
Requires: onboard = %version-%release
Requires: gnome-shell

%description gnome
GNOME Shell support for onboard.

%prep
%setup -q
%autopatch -p1
install -Dpm0644 %SOURCE1 po/ru.po

%build
%python3_build

%install
%python3_install

desktop-file-install --dir %buildroot%_desktopdir       \
    --remove-category="Accessibility"        \
    build/share/applications/%name.desktop
desktop-file-install --dir %buildroot%_desktopdir       \
    --remove-category="Accessibility"        \
    build/share/applications/%name-settings.desktop

mkdir -p %buildroot%_datadir/locale
cp -a build/mo/* %buildroot%_datadir/locale

# remove themed icons
rm -rf %buildroot%_iconsdir/ubuntu-mono-*

rm -rf %buildroot%_defaultdocdir/%name

%find_lang %name

%files -f %name.lang
%doc AUTHORS README.md HACKING *.example
%_bindir/%name
%_bindir/%name-settings
%_datadir/%name/
%_datadir/glib-2.0/schemas/*.gschema.xml
%_sysconfdir/xdg/autostart/%name-autostart.desktop
%_desktopdir/%name.desktop
%_desktopdir/%name-settings.desktop
%_man1dir/%{name}*.1*
%_iconsdir/HighContrast/symbolic/apps/onboard.svg
%_iconsdir/hicolor/scalable/apps/onboard-symbolic.svg
%_iconsdir/hicolor/scalable/apps/onboard.svg
%_iconsdir/hicolor/*x*/apps/onboard.png
%_datadir/sounds/freedesktop/stereo/onboard-key-feedback.oga
%_datadir/dbus-1/services/*
%python3_sitelibdir/Onboard/
%python3_sitelibdir/%{name}*.egg-info
%_datadir/help/C/%name

%files gnome
%_datadir/gnome-shell/extensions/Onboard_Indicator@onboard.org

%changelog
* Fri Aug 02 2024 Andrey Cherepanov <cas@altlinux.org> 1.4.1-alt7.git8de1177
- New snapshot from https://github.com/dr-ni/onboard (ALT #49818).

* Fri Mar 15 2024 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt6
- NMU: fix BuildRequires(pre)

* Wed Jan 03 2024 Grigory Ustinov <grenka@altlinux.org> 1.4.1-alt5
- Fixed build with python3.12.

* Mon Mar 06 2023 Anton Midyukov <antohami@altlinux.org> 1.4.1-alt4
- NMU: drop 'BuildRequires: libappindicator-gtk3-gir-devel'
- NMU: add patch for Ayatana-AppIndicator support

* Sat Nov 12 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 1.4.1-alt3.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Mon Apr 26 2021 Andrey Cherepanov <cas@altlinux.org> 1.4.1-alt3
- Complete Russian translation (thanks Olesya Gerasimenko).
- Remove Accessability category from desktop files.
- Fix License tag according to SPDX.

* Fri Aug 03 2018 Anton Midyukov <antohami@altlinux.org> 1.4.1-alt2
- Added requires to iso-codes (ALT#35174)

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.1-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 23 2017 Andrey Cherepanov <cas@altlinux.org> 1.4.1-alt1
- New version

* Sun Sep 18 2016 Andrey Cherepanov <cas@altlinux.org> 1.3.0-alt1
- New version

* Thu Jul 07 2016 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1
- New version (use Python3)

* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.96.2-alt2.1
- Rebuild to remove redundant libpython2.7 dependency

* Wed Jan 18 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.96.2-alt2
- hack around startup crash

* Wed Jan 18 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.96.2-alt1
- updated to 0.96.2
- now it is arch-dependent

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.95.1-alt1.1
- Rebuild with Python-2.7

* Sat Oct 01 2011 Andrey Cherepanov <cas@altlinux.org> 0.95.1-alt1
- Initial build in Sisyphus (closes: #26220)
