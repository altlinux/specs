%define _unpackaged_files_terminate_build 1
%define _libexecdir %_prefix/libexec

Name: paperde
Version: 0.3.0
Release: alt1

Summary: Awesome Desktop Environment built on top of Qt/Wayland and Wayfire
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Vcs: https://gitlab.com/cubocore/paper/paperde
URL: https://cubocore.gitlab.io/paperde.html

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson

BuildRequires: meson
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6UiTools)
BuildRequires: pkgconfig(dbusmenu-lxqt)
BuildRequires: pkgconfig(cprime-core)
BuildRequires: pkgconfig(csys)
BuildRequires: pkgconfig(wayqt-qt6)
BuildRequires: pkgconfig(df6sni)
BuildRequires: pkgconfig(df6ipc)
BuildRequires: pkgconfig(df6coreapplication)
BuildRequires: pkgconfig(df6login1)

# components from wayfire.ini
Requires: wayfire
Requires: wayfire-plugins-extra
Requires: xdg-desktop-portal
Requires: xdg-desktop-portal-wlr
Requires: clipman
Requires: wl-clipboard
Requires: gnome-keyring
Requires: swayidle
Requires: swaylock
Requires: libinput-gestures
Requires: mako
Requires: kanshi
Requires: lxqt-policykit
Requires: redshift
Requires: mpv

Requires: wofi
Requires: brightnessctl
Requires: playerctl
Requires: pulseaudio-ctl

%ifnarch i586
Requires: grim
Requires: slurp
%endif

Requires: coreterminal
Requires: corehunt
Requires: coreaction
Requires: coretoppings

Requires: corepad
Requires: coregarage

%description
%summary.

%package -n lib%{name}
Summary: Library files for %name
Group: System/Libraries

%description -n lib%{name}
Library files for %name.

%summary.

%package -n lib%{name}-devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: lib%{name} = %version-%release

%description -n lib%{name}-devel
Development files for %{name}.

%summary.

%prep
%setup
%patch -p1
sed -i "s|join_paths( get_option( 'libdir' ), get_option( 'libexecdir' )|join_paths( get_option( 'libexecdir' )|g" \
       meson.build \
       papershell/bg/meson.build \
       papershell/meson.build \
       papershell/logout/meson.build \
       papershell/menu/meson.build \
       papershell/dock/meson.build \
       papershell/widgets/meson.build
sed -i "s|'UTILS_PATH', join_paths( get_option( 'prefix' ), get_option( 'libdir' ), get_option( 'libexecdir' )|'UTILS_PATH', join_paths( get_option( 'prefix' ), get_option( 'libexecdir' )|g" \
       meson.build

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc LICENSE README.md ReleaseNotes
%doc paperdesktop1.png paperdesktop2.png paperdesktop3.png paperdesktop4.png
%_bindir/papersessionmanager
%_bindir/papersettings
%_bindir/papershell
%dir %_libexecdir/paperde
%_libexecdir/paperde/paperbg
%_libexecdir/paperde/paperdock
%_libexecdir/paperde/paperlogout
%_libexecdir/paperde/papermenu
%_libexecdir/paperde/papersnwatcher
%_libexecdir/paperde/paperwidgets
%_desktopdir/org.cubocore.PaperSettings.desktop
%dir %_datadir/paperde
%dir %_datadir/paperde/background
%_datadir/paperde/background/default.svg
%dir %_datadir/paperde/configs
%_datadir/paperde/configs/fonts.conf
%_datadir/paperde/configs/papershell.conf
%dir %_datadir/paperde/configs/qt5ct
%dir %_datadir/paperde/configs/qt5ct/colors
%_datadir/paperde/configs/qt5ct/colors/Dark.conf
%_datadir/paperde/configs/qt5ct/colors/Light.conf
%_datadir/paperde/configs/qt5ct/qt5ct.conf
%_datadir/paperde/wayfire.ini
%_datadir/wayland-sessions/paperdesktop.desktop

%files -n lib%{name}
%_libdir/libpaperdecore.so.0
%_libdir/libpaperdecore.so.0.2.2
%_libdir/libpaperdegui.so.0
%_libdir/libpaperdegui.so.0.2.2

%files -n lib%{name}-devel
%dir %_includedir/paperde
%_includedir/paperde/dynamiclayout.h
%_includedir/paperde/paper-config.h
%_includedir/paperde/paperglobals.h
%_includedir/paperde/paperlog.h
%_includedir/paperde/papersettings.h
%_libdir/libpaperdecore.so
%_libdir/libpaperdegui.so
%_libdir/pkgconfig/paperdecore.pc
%_libdir/pkgconfig/paperdegui.pc

%changelog
* Mon Dec 29 2025 Nikolay Strelkov <snk@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus
