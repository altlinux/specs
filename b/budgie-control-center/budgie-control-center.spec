%global cheese_version 3.28.0
%global glib2_version 2.64
%global gnome_online_accounts_version 3.44.0
%global gnome_stack 42.0
%global gtk3_version 3.24
%global polkit_version 0.105
%global upower_version 0.99.8
%global vala_version 0.52.5

Name: budgie-control-center
Version: 1.4.0
Release: alt1

Summary: A fork of GNOME Control Center for the Budgie 10 Series

License: GPL-2.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/BuddiesOfBudgie/budgie-control-center

# Source0-url: %url/releases/download/v%version/budgie-control-center-%version.tar.xz
Source0: %name-%version.tar

Patch0: 0001-fix-FTBFS-with-incompatible-pointer-types.patch
Patch1: 0002-disable-gnome-bluetooth.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: chrpath
BuildRequires: libcups-devel
BuildRequires: desktop-file-utils
BuildRequires: docbook-style-xsl xsltproc
BuildRequires: gcc
BuildRequires: gettext-tools
BuildRequires: libappstream-glib
BuildRequires: meson
BuildRequires: pkgconfig(accountsservice)
BuildRequires: pkgconfig(cheese) >= %cheese_version
BuildRequires: pkgconfig(colord-gtk)
BuildRequires: pkgconfig(gcr-3)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(gnome-desktop-3.0) >= %gnome_stack
BuildRequires: pkgconfig(gnome-settings-daemon) >= %gnome_stack
BuildRequires: pkgconfig(gio-2.0) >= %glib2_version
BuildRequires: pkgconfig(grilo-0.3)
BuildRequires: pkgconfig(gsettings-desktop-schemas) >= %gnome_stack
BuildRequires: pkgconfig(gsound)
BuildRequires: pkgconfig(gtk+-3.0) >= %gtk3_version
BuildRequires: pkgconfig(gudev-1.0)
BuildRequires: pkgconfig(ibus-1.0)
BuildRequires: pkgconfig(libcanberra-gtk3)
BuildRequires: pkgconfig(libgtop-2.0)
BuildRequires: pkgconfig(libhandy-1)
BuildRequires: pkgconfig(libnm) >= 1.24
BuildRequires: pkgconfig(libnma)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libpulse-mainloop-glib)
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(malcontent-0)
BuildRequires: pkgconfig(mm-glib)
BuildRequires: pkgconfig(polkit-gobject-1)
BuildRequires: pkgconfig(pwquality)
BuildRequires: pkgconfig(smbclient)
BuildRequires: pkgconfig(udisks2)
BuildRequires: pkgconfig(upower-glib) >= 0.99.13
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xi)

BuildRequires: pkgconfig(epoxy)
BuildRequires: pkgconfig(gnutls)
BuildRequires: pkgconfig(krb5)

#BuildRequires: rpm-build-cmake

#BuildRequires: pkgconfig(gnome-bluetooth-3.0) >= 3.34.0
#BuildRequires: pkgconfig(gnome-bluetooth-ui-3.0)
BuildRequires: pkgconfig(libwacom)

#Requires: cheese-libs%{?_isa} >= %cheese_version
#Requires: glib2%{?_isa} >= %glib2_version
#Requires: gnome-desktop3%{?_isa} >= %gnome_stack
#Requires: gnome-settings-daemon%{?_isa} >= %gnome_stack
#Requires: gsettings-desktop-schemas%{?_isa} >= %gnome_stack
#Requires: gtk3%{?_isa} >= %gtk3_version
#Requires: upower%{?_isa} >= %upower_version

#Requires: gnome-bluetooth%{?_isa}

# Need common
Requires: %name-common = %EVR

# For user accounts
Requires: accountsservice
Requires: libalsa

# For the thunderbolt panel
#Recommends: bolt

# For the color panel
Requires: colord

# For the printers panel
Requires: cups-pk-helper
Requires: dbus

# For the info/details panel
Requires: %_bindir/glxinfo
#Recommends: switcheroo-control

# For the user languages
Requires: iso-codes

# For the network panel
#Recommends: NetworkManager-wifi
#Recommends: nm-connection-editor

# For parental controls support
Requires: malcontent
Requires: malcontent-control

# Fingerprint support
Requires: fprintd

# For Show Details in the color panel
#Recommends: gnome-color-manager

# For the power panel
#Recommends: ppd-service
#%if 0%{?fedora} && 0%{?fedora} < 41
#Suggests: power-profiles-daemon
#%else
#Suggests: tuned-ppd
#%endif

%description
A fork of GNOME Control Center for the Budgie 10 Series.

%package common
License: GPL-2.0-or-later
Summary: Common assets for %name
BuildArch: noarch
Group: Graphical desktop/Other

Requires: hicolor-icon-theme
# owners of dirs
Requires: dbus libgio polkit


%description common
This package contains architecture-agnostic common assets for ${name}

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%meson \
    -Ddark_mode_distributor_logo=%_pixmapsdir/system-logo-white.png \
    -Ddocumentation=true \
    -Dmalcontent=true
%meson_build

%install
%meson_install
mkdir -p %buildroot%_datadir/budgie/wm-properties
rm -rf %buildroot%_datadir/budgie/autostart
rm -rf %buildroot%_datadir/budgie/cursor-fonts
chrpath --delete %buildroot%_bindir/%name
%find_lang %name --all-name --with-gnome

%check
desktop-file-validate %buildroot%_desktopdir/*.desktop
appstream-util validate-relax --nonet %buildroot%_datadir/metainfo/%name.appdata.xml

%files
%doc LICENSE
%doc README.md
%_bindir/%name
%_libexecdir/budgie-cc-remote-login-helper
%_libexecdir/%name-print-renderer
%_desktopdir/*.desktop
%_iconsdir/hicolor/scalable/apps/org.buddiesofbudgie.Settings-*.svg
%_man1dir/%name.1*
%_datadir/metainfo/%name.appdata.xml

%files common -f %name.lang
%dir %_datadir/budgie/
%dir %_datadir/%name/
%dir %_datadir/%name/keybindings/
%dir %_datadir/%name/pixmaps/
%dir %_pixmapsdir/budgie-faces
%dir %_pixmapsdir/budgie-faces/legacy
%dir %_datadir/sounds/budgie
%dir %_datadir/sounds/budgie/default
%dir %_datadir/sounds/budgie/default/alerts
%_datadir/bash-completion/completions/%name
%_datadir/dbus-1/services/org.buddiesofbudgie.ControlCenter.service
%_datadir/glib-2.0/schemas/org.buddiesofbudgie.ControlCenter.gschema.xml
%_datadir/budgie/wm-properties
%_pixmapsdir/budgie-faces/*.jpg
%_pixmapsdir/budgie-faces/*.png
%_pixmapsdir/budgie-faces/legacy/*.jpg
%_pixmapsdir/budgie-faces/legacy/*.png
%_pixmapsdir/budgie-logo.png
%_datadir/%name/keybindings/*.xml
%_datadir/%name/pixmaps/noise-texture-light.png
%_iconsdir/hicolor/scalable/*/budgie-*.svg
%_iconsdir/hicolor/scalable/apps/org.buddiesofbudgie.Settings.Devel.svg
%_iconsdir/hicolor/scalable/apps/org.buddiesofbudgie.Settings.svg
%_iconsdir/hicolor/symbolic/apps/org.buddiesofbudgie.Settings-symbolic.svg
%_datadir/polkit-1/actions/org.buddiesofbudgie.controlcenter.*.policy
%_datadir/polkit-1/rules.d/%name.rules
%_datadir/sounds/budgie/default/alerts/*.ogg

%changelog
* Sun Mar 09 2025 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt1
- initial build for ALT Sisyphus

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 11 2024 Joshua Strobl <me@joshuastrobl.com> - 1.4.0-5
- Add ppd-service as recommends, tuned-ppd as suggests

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.4.0-4
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 15 2024 Kate Hsuan <hpa@redhat.com> - 1.4.0-2
- tuned is the default power profile management daemon in Fedora
- https://pagure.io/fesco/issue/3222

* Sun Mar 17 2024 Joshua Strobl <me@joshuastrobl.com> - 1.4.0-1
- Update to 1.4.0

* Wed Mar 06 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.3.0-4
- goa-backend rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Aug 4 2023 Joshua Strobl <me@joshuastrobl.com> - 1.3.0-1
- Update to 1.3.0

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jan 29 2023 Joshua Strobl <me@joshuastrobl.com> - 1.2.0-1
- Update to 1.2.0

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 13 2022 Joshua Strobl <me@joshuastrobl.com> - 1.1.1-6
- Updated to 1.1.1 release

* Sat Aug 06 2022 Joshua Strobl <me@joshuastrobl.com> - 1.1.0-5
- Updated to 1.1.0 release
- Fixes #2113132

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Joshua Strobl <me@joshuastrobl.com> - 1.0.2-3
- Added missing sources file

* Wed Jul 13 2022 Joshua Strobl <me@joshuastrobl.com> - 1.0.2-2
- Updated sources for koji build
- Build fixes for s390 and s390x architectures

* Tue Jul 12 2022 Joshua Strobl <me@joshuastrobl.com> - 1.0.2-1
- Initial packaging of Budgie Control Center
