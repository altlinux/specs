%global glib_version 2.69.0
%global gtk3_version 3.19.8
%global gsettings_desktop_schemas_version 40~alpha
%global json_glib_version 0.12.0
%global libinput_version 1.19.0
%global pipewire_version 0.3.33
%global lcms2_version 2.6
%global colord_version 1.4.5
%global magpie_abi_version magpie-0

Name: magpie
Version: 0.9.3
Release: alt1

Summary: Window manager for Budgie Desktop

License: GPL-2.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/BuddiesOfBudgie/magpie

# Source0-url: %url/releases/download/v%version/%name-%version.tar.xz
Source0: %name-%version.tar

Patch0: Add-API-replacing-gsd-powers-use-of-libgnome-rr.patch
Patch1: Create-the-new-X11-scaling-dbus-interface-that-GSD-4.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-meson
BuildRequires: pkgconfig(gobject-introspection-1.0) >= 1.41.0
BuildRequires: pkgconfig(sm)
BuildRequires: pkgconfig(libwacom)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xdamage)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(x11-xcb)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xkbcommon-x11)
BuildRequires: pkgconfig(xkbfile)
BuildRequires: pkgconfig(xtst)
BuildRequires: pkgconfig(xinerama)
BuildRequires: gir(Pango)
BuildRequires: gir(Atk)
BuildRequires: gir(Json)
BuildRequires: gir(Gdk) = 3.0
BuildRequires: pkgconfig(wayland-server)

BuildRequires: libEGL-devel
BuildRequires: libGLES-devel
BuildRequires: libGL-devel
BuildRequires: libgbm-devel

BuildRequires: %_bindir/g-ir-scanner
BuildRequires: pkgconfig(glesv2)
BuildRequires: pkgconfig(graphene-gobject-1.0)
BuildRequires: gir(Graphene)
BuildRequires: libpam0-devel
BuildRequires: pkgconfig(libpipewire-0.3) >= %pipewire_version
BuildRequires: pkgconfig(sysprof-capture-4)
BuildRequires: sysprof-devel
BuildRequires: pkgconfig(libsystemd)
#BuildRequires: xorg-x11-server-Xorg
#BuildRequires: xorg-x11-server-Xvfb
BuildRequires: pkgconfig(xkeyboard-config)
BuildRequires: zenity
BuildRequires: desktop-file-utils
# Bootstrap requirements
#BuildRequires: gtk-doc gettext-devel git-core
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(gsettings-desktop-schemas) >= %gsettings_desktop_schemas_version
BuildRequires: gir(GDesktopEnums)
BuildRequires: pkgconfig(gnome-settings-daemon)
BuildRequires: cvt
BuildRequires: rpm-build-cmake
BuildRequires: meson
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(gnome-desktop-3.0)
BuildRequires: pkgconfig(gudev-1.0)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libstartup-notification-1.0)
BuildRequires: pkgconfig(lcms2) >= %lcms2_version
BuildRequires: pkgconfig(colord) >= %colord_version

BuildRequires: pkgconfig(json-glib-1.0) >= %json_glib_version
BuildRequires: pkgconfig(libinput) >= %libinput_version
BuildRequires: pkgconfig(fribidi)
BuildRequires: pkgconfig(dbus-1)

#Requires: control-center-filesystem
#Requires: mutter-common

Requires: gsettings-desktop-schemas >= %gsettings_desktop_schemas_version
Requires: gnome-settings-daemon
#Requires: gtk3 >= %gtk3_version
#Requires: json-glib >= %json_glib_version
#Requires: libinput >= %libinput_version
#Requires: pipewire >= %pipewire_version
#Requires: startup-notification
Requires: dbus
Requires: zenity

#Provides: firstboot(windowmanager) = magpie

# Cogl and Clutter were forked at these versions, but have diverged
# significantly since then.
#Provides: bundled(cogl) = 1.22.0
#Provides: bundled(clutter) = 1.26.0

%description
Magpie is the window manager used by Budgie Desktop.

%package -n lib%name-devel
Summary: Development package for %name
Group: Development/C
Requires: %name = %EVR
# for EGL/eglmesaext.h that's included from public cogl-egl-defines.h header
Requires: libEGL-devel

%description -n lib%name-devel
Header files and libraries for developing against Magpie.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%meson -Degl_device=true
%meson_build

%install
%meson_install

%find_lang %name

%files -f %name.lang
%doc COPYING
%_libdir/lib%magpie_abi_version.so.0
%_libdir/lib%magpie_abi_version.so.0.0.0
%dir %_libdir/%magpie_abi_version/
%_libdir/%magpie_abi_version/Cally-0.*
%_libdir/%magpie_abi_version/Clutter-0.*
%_libdir/%magpie_abi_version/Cogl-0.*
%_libdir/%magpie_abi_version/CoglPango-0.*
%_libdir/%magpie_abi_version/Meta-0.*
%_libdir/%magpie_abi_version/lib%name-clutter-0.*
%_libdir/%magpie_abi_version/lib%name-cogl-0.*
%_libdir/%magpie_abi_version/lib%name-cogl-pango-0.*

%files -n lib%name-devel
%_includedir/%magpie_abi_version
%_libdir/lib%magpie_abi_version.so
%_pkgconfigdir/lib%magpie_abi_version.pc
%_pkgconfigdir/%name-clutter-0.pc
%_pkgconfigdir/%name-cogl-0.pc
%_pkgconfigdir/%name-cogl-pango-0.pc

%changelog
* Sun Mar 09 2025 Vitaly Lipatov <lav@altlinux.ru> 0.9.3-alt1
- initial build for ALT Sisyphus

* Fri Jan 24 2025 Joshua Strobl <me@joshuastrobl.com> - 0.9.3-4
- Fix FTBFS due to missing build deps (cvt) #2340810

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Sep 26 2024 Joshua Strobl <me@joshuastrobl.com> - 0.9.3-2
- Added patch to support X11 scaling changes in newest GNOME Settings Daemon

* Tue Sep 17 2024 Joshua Strobl <me@joshuastrobl.com> - 0.9.3-1
- Update to 0.9.3 and add patch for gnome-settings-daemon breakage

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Aug 20 2023 Joshua Strobl <me@joshuastrobl.com> - 0.9.2-1
- Initial inclusion of magpie
