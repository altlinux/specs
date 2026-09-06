%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define _libexecdir %_prefix/libexec

%filter_from_requires /^.usr.libexec.gdm-wayland-session/d
%filter_from_requires /^.etc.vconsole.conf/d

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

Name: singularity-desktop
Version: 0.1.0
Release: alt1.git20260904.d642160

Summary: The Singularity Desktop Environment
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/singularityos-lab/singularity-desktop

Source: %name-%version.tar
Source1: submodules-%name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): meson
BuildRequires(pre): rpm-build-vala
BuildRequires(pre): rpm-build-systemd

BuildRequires: vala-tools
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libpeas-2)
BuildRequires: pkgconfig(gtksourceview-5)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gtk4-layer-shell-0)
BuildRequires: /usr/bin/g-ir-compiler
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(gudev-1.0)
BuildRequires: pkgconfig(upower-glib)
BuildRequires: pkgconfig(libnm)
BuildRequires: /usr/bin/sassc
BuildRequires: vapi(gtk4-layer-shell-0)

# singularity-gestures
#BuildRequires: /usr/bin/sdl2-config
#BuildRequires: pkgconfig(sdl2)
#BuildRequires: pkgconfig(glu)
#BuildRequires: pkgconfig(gstreamer-1.0)
#BuildRequires: pkgconfig(gstreamer-app-1.0)
#BuildRequires: pkgconfig(xkbcommon)

# xdg-desktop-portal-singularity
BuildRequires: pkgconfig(libpipewire-0.3)

# singularity-shell
BuildRequires: pkgconfig(vte-2.91-gtk4)
BuildRequires: pkgconfig(poppler-glib)
BuildRequires: pkgconfig(goa-1.0)
BuildRequires: pkgconfig(dbusmenu-glib-0.4)
BuildRequires: pkgconfig(atspi-2)
BuildRequires: pkgconfig(tracker-sparql-3.0)
BuildRequires: pkgconfig(pam)

# singularity-files
BuildRequires: /usr/bin/vetro
BuildRequires: pkgconfig(xkbcommon)

# singularity-edit
BuildRequires: pkgconfig(webkitgtk-6.0)

# singularity-demo
BuildRequires: pkgconfig(libsecret-1)

# singularity-videos
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-video-1.0)

# singularity-keyring
BuildRequires: pkgconfig(libgcrypt)
BuildRequires: pkgconfig(libsodium)

# libsingularity
BuildRequires: libsingularity-devel

# requires
## common
Requires: libsingularity
Requires: /usr/bin/labwc
## singularity-git
Requires: git
## singularity-store
Requires: flatpak
## singularity-videos
Requires: gst-plugin-gtk4
## singularity-write
Requires: /usr/bin/bwrap
Requires: /usr/bin/xdg-dbus-proxy

%description
A Wayland desktop environment built on GTK4 and the labwc compositor.
It provides the shell (panel, dock, overview, workspaces, notifications,
settings, spotlight, lock screen and greeter) and a first-party set of
applications, all sharing the libsingularity toolkit.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %{version}-%{release}
Requires: libsingularity-devel

Conflicts: gnome-keyring
Conflicts: oo7

%description devel
Development files for %name.

%prep
%setup -a1
%patch -p1
sed -i "s|, 'strip=true'||" meson.build subprojects/singularity-shell/meson.build

# already packaged externally
sed -i "s|^subproject('libsingularity')|#subproject('libsingularity')|" meson.build

# TODO - see https://github.com/singularityos-lab/singularity-desktop/issues/246
sed -i "s|^subproject('singularity-gestures')|#subproject('singularity-gestures')|" meson.build

%build
%meson
%meson_build

%install
%meson_install

install -Dm644 /dev/stdin \
"%buildroot%_datadir/wayland-sessions/singularity.desktop" << 'EOF'
[Desktop Entry]
Name=Singularity
Comment=The Singularity Desktop Environment
Exec=/usr/bin/singularity-labwc-session
TryExec=/usr/bin/singularity-labwc-session
Type=Application
DesktopNames=Singularity
EOF

%files
%doc CONTRIBUTING.md LICENSE README.md
%_sysconfdir/pam.d/singularity-lockscreen

%_bindir/singularity-calculator
%_bindir/singularity-calendar
%_bindir/singularity-demo
%_bindir/singularity-desktop
%_bindir/singularity-desktop-session
%_bindir/singularity-edit
%_bindir/singularity-files
%_bindir/singularity-git
%_bindir/singularity-greeter
%_bindir/singularity-keyboard-reset
%_bindir/singularity-keyring
%_bindir/singularity-labwc-session
%_bindir/singularity-leafs
%_bindir/singularity-lockscreen
%_bindir/singularity-monitor
%_bindir/singularity-music
%_bindir/singularity-photos
%_bindir/singularity-region-picker
%_bindir/singularity-screencast-chooser
%_bindir/singularity-screenshot
%_bindir/singularity-splash
%_bindir/singularity-store
%_bindir/singularity-videos
%_bindir/singularity-write

%_desktopdir/dev.sinty.calculator.desktop
%_desktopdir/dev.sinty.calendar.desktop
%_desktopdir/dev.sinty.demo.desktop
%_desktopdir/dev.sinty.edit.desktop
%_desktopdir/dev.sinty.files.desktop
%_desktopdir/dev.sinty.git.desktop
%_desktopdir/dev.sinty.leafs.desktop
%_desktopdir/dev.sinty.monitor.desktop
%_desktopdir/dev.sinty.music.desktop
%_desktopdir/dev.sinty.photos.desktop
%_desktopdir/dev.sinty.store.desktop
%_desktopdir/dev.sinty.videos.desktop
%_desktopdir/dev.sinty.write.desktop

%_datadir/wayland-sessions/singularity.desktop

%_userunitdir/singularity-polkit-agent.service
%_userunitdir/xdg-desktop-portal-singularity.service

%_datadir/xdg-desktop-portal/portals/singularity.portal
%_datadir/xdg-desktop-portal/singularity-portals.conf
%dir %_datadir/themes/Kids
%_datadir/themes/Kids/*
%dir %_datadir/themes/SingularityShell
%_datadir/themes/SingularityShell/*
%dir %_datadir/singularity
%dir %_datadir/singularity/app-settings
%_datadir/singularity/app-settings/*.json
%dir %_datadir/singularity/apps
%_datadir/singularity/apps/*.json
%dir %_datadir/singularity/labwc
%_datadir/singularity/labwc/*
%dir %_datadir/singularity/widgets
%_datadir/singularity/widgets/*.widget
%dir %_datadir/singularity-edit
%dir %_datadir/singularity-edit/queries
%_datadir/singularity-edit/queries/README.md
%dir %_datadir/singularity-edit/queries/go
%_datadir/singularity-edit/queries/go/*.scm
%dir %_datadir/singularity-edit/queries/python
%_datadir/singularity-edit/queries/python/*.scm
%dir %_datadir/singularity-edit/queries/rust
%_datadir/singularity-edit/queries/rust/*.scm
%dir %_datadir/singularity-edit/queries/tsx
%_datadir/singularity-edit/queries/tsx/*.scm
%dir %_datadir/singularity-edit/queries/typescript
%_datadir/singularity-edit/queries/typescript/*.scm

%dir %_libdir/singularity
%dir %_libdir/singularity/plugins
%_libdir/singularity/plugins/*
%dir %_libdir/singularity/widgets
%_libdir/singularity/widgets/*

%_libexecdir/singularity-polkit-agent
%_libexecdir/singularity-polkit-auth-helper
%_libexecdir/xdg-desktop-portal-singularity

%_datadir/accountsservice/interfaces/com.singularity.Desktop.xml

%_datadir/dbus-1/services/org.freedesktop.secrets.service

%_datadir/glib-2.0/schemas/dev.sinty.*.gschema.xml

%dir %_iconsdir/Singularity
%_iconsdir/Singularity/index.theme
%_iconsdir/hicolor/scalable/apps/*.svg

%dir %_datadir/backgrounds/singularity
%_datadir/backgrounds/singularity/*.png
%_datadir/backgrounds/singularity/*.svg

# already packaged in libsingularity
%exclude %_datadir/singularity/avatars
%exclude %_datadir/themes/Singularity
%exclude %_libdir/girepository-1.0/Singularity-1.0.typelib
%exclude %_libdir/libsingularity.so.0*
%exclude %_libdir/libsingularity-system.so.0*

%files devel
# already packaged in libsingularity-devel
%exclude %_includedir/singularity.h
%exclude %_includedir/singularity-system.h
%exclude %_libdir/libsingularity.so
%exclude %_libdir/libsingularity-system.so
%exclude %_libdir/pkgconfig/singularity-1.0.pc
%exclude %_libdir/pkgconfig/singularity-system-1.0.pc
%exclude %_datadir/gir-1.0/Singularity-1.0.gir
%exclude %_vapidir/singularity-1.0.deps
%exclude %_vapidir/singularity-1.0.vapi
%exclude %_vapidir/singularity-system-1.0.deps
%exclude %_vapidir/singularity-system-1.0.vapi

%_includedir/loginui.h
%_includedir/widget.h
%_libdir/libloginui.a
%_libdir/pkgconfig/singularity-loginui.pc

%changelog
* Sat Sep 05 2026 Nikolay Strelkov <snk@altlinux.org> 0.1.0-alt1.git20260904.d642160
- Initial build for Sisyphus
