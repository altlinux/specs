Name: mate-control-center
Version: 1.28.1
Release: alt1
Epoch: 2
Summary: MATE Desktop control-center
License: LGPLv2+ and GPLv2+
Group: Graphical desktop/MATE
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Provides: %name-filesystem = %version-%release
Requires: gsettings-desktop-schemas mate-settings-daemon gnome-keyring

BuildRequires: mate-common libSM-devel libXScrnSaver-devel libXcursor-devel libXi-devel libXxf86misc-devel libcanberra-gtk3-devel
BuildRequires: libdconf-devel mate-desktop-devel libmatekbd-devel librsvg-devel libxml2-devel mate-menus-devel mate-settings-daemon-devel
BuildRequires: mate-window-manager-devel yelp-tools desktop-file-utils libpolkit-devel libaccountsservice-devel
BuildRequires: libayatana-appindicator3-devel libgtop-devel libudisks2-devel libsystemd-devel

%description
MATE Control Center configures system settings such as themes,
keyboards shortcuts, etc.

%package devel
Group: Development/C
Summary: Development files for mate-settings-daemon

%description devel
Development files for mate-control-center

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--disable-update-mimedb \
	--disable-schemas-compile \
	--disable-static

%make_build

%install
%make DESTDIR=%buildroot install

find %buildroot%_libdir -name \*.la -delete

%find_lang %name --with-gnome --all-name

%files -f %name.lang
%doc AUTHORS COPYING README
%config %_sysconfdir/xdg/menus/matecc.menu
%_bindir/mate-*
%_sbindir/mate-display-properties-install-systemwide
%exclude %_desktopdir/mate-system-info.desktop
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/*/*
%_datadir/mate-control-center
%_datadir/desktop-directories/matecc.directory
%_datadir/glib-2.0/schemas/org.mate.*.xml
%_datadir/mime/packages/mate-theme-package.xml
%_datadir/thumbnailers/mate-font-viewer.thumbnailer
%_datadir/polkit-1/actions/org.mate.randr.policy
%_man1dir/mate-*.1.*

%files devel
%_pkgconfigdir/*.pc

%changelog
* Mon Oct 21 2024 Valery Inozemtsev <shrek@altlinux.ru> 2:1.28.1-alt1
- 1.28.1

* Tue Feb 27 2024 Valery Inozemtsev <shrek@altlinux.ru> 2:1.28.0-alt1
- 1.28.0

* Thu Jan 25 2024 Anton Midyukov <antohami@altlinux.org> 2:1.26.1-alt3
- NMU: use upstream russian translation, because recommended by translator
  Maria Shikunova (Closes: 49174)

* Wed Jun 14 2023 Anton Midyukov <antohami@altlinux.org> 2:1.26.1-alt2
- NMU: rebuild with libayatana-appindicator3

* Thu May 11 2023 Valery Inozemtsev <shrek@altlinux.ru> 2:1.26.1-alt1
- 1.26.1

* Tue Dec 13 2022 Valery Inozemtsev <shrek@altlinux.ru> 2:1.26.0-alt4
- updated translation

* Mon Dec 12 2022 Valery Inozemtsev <shrek@altlinux.ru> 2:1.26.0-alt3
- rebuild

* Mon Nov 21 2022 Valery Inozemtsev <shrek@altlinux.ru> 2:1.26.0-alt2
- updated ru translation

* Sun Aug 08 2021 Valery Inozemtsev <shrek@altlinux.ru> 2:1.26.0-alt1
- 1.26.0

* Thu Aug 20 2020 Valery Inozemtsev <shrek@altlinux.ru> 2:1.24.1-alt1
- 1.24.1

* Tue Feb 25 2020 Valery Inozemtsev <shrek@altlinux.ru> 2:1.24.0-alt1
- 1.24.0

* Tue Oct 15 2019 Valery Inozemtsev <shrek@altlinux.ru> 2:1.22.2-alt1
- 1.22.2

* Tue Apr 23 2019 Valery Inozemtsev <shrek@altlinux.ru> 2:1.22.1-alt1
- 1.22.1

* Mon Mar 04 2019 Valery Inozemtsev <shrek@altlinux.ru> 2:1.22.0-alt1
- 1.22.0

* Mon Dec 24 2018 Valery Inozemtsev <shrek@altlinux.ru> 2:1.20.4-alt1
- 1.20.4

* Fri Jun 15 2018 Valery Inozemtsev <shrek@altlinux.ru> 2:1.20.3-alt1
- 1.20.3

* Wed Mar 28 2018 Valery Inozemtsev <shrek@altlinux.ru> 2:1.20.2-alt1
- 1.20.2

* Tue Mar 27 2018 Valery Inozemtsev <shrek@altlinux.ru> 2:1.20.1-alt1
- 1.20.1

* Thu Mar 01 2018 Valery Inozemtsev <shrek@altlinux.ru> 2:1.20.0-alt1
- initial build from git.mate-desktop.org

* Tue Feb 20 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1:1.20.0-alt1_1
- new fc release
