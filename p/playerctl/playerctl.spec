Name: playerctl
Version: 2.4.1
Release: alt1

Summary: CLI for MPRIS-compatible players
License: LGPLv3
Group: Sound
Url: https://github.com/altdesktop/playerctl

Source: %name-%version-%release.tar

BuildRequires: meson gtk-doc
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(glib-2.0)

%package -n libplayerctl
Summary: MPRIS-compatible players library
Group: System/Libraries

%package devel
Summary: CLI for MPRIS-compatible players
Group: Development/C

%define desc \
Playerctl is a command-line utility and library for controlling media players \
that implement the MPRIS D-Bus Interface Specification. \
Playerctl makes it easy to bind player actions, such as play and pause, to media keys. \
You can also get metadata about the playing track such as the artist and title \
for integration into statusline generators or other command-line tools. \
Playerctl also comes with a daemon that allows it to act on the currently active \
media player called `playerctld`.

%description %desc

%description -n libplayerctl %desc
This package contains shared playerctl library.

%description devel %desc
This package contains header files needed to develop
applications using playerctl.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc COPYING README*
%_bindir/playerctl
%_bindir/playerctld
%_datadir/dbus-1/services/*.service
%_man1dir/*

%files -n libplayerctl
%_libdir/libplayerctl.so.*
%_typelibdir/*.typelib

%files devel
%_includedir/playerctl
%_girdir/*.gir
%_datadir/gtk-doc/*/playerctl
%_libdir/libplayerctl.so
%_pkgconfigdir/playerctl.pc

%changelog
* Tue Sep 13 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4.1-alt1
- 2.4.1 released
