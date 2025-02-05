%define _unpackaged_files_terminate_build 1

%define pname byzanz

Name: byzanz-mate
Version: 0.3.0
Release: alt1_0.git202502041

Summary: Byzanz small screencast creator with applet for MATE Panel
License: GPLv3+
Group:   Other
Url:     https://github.com/N0rbert/byzanz-mate

Conflicts: byzanz < %version-%release

Source: %name-%version.tar

BuildRequires: mate-common
BuildRequires: glib2-devel
BuildRequires: intltool
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(xdamage)
BuildRequires: pkgconfig(gstreamer-app-1.0)
BuildRequires: pkgconfig(libmatepanelapplet-4.0)

%description
Byzanz is a desktop recorder and command line tool allowing you to record your
current desktop or parts of it to an animated GIF, Ogg Theora, Flash or WebM.
This is especially useful for publishing on the web.

Byzanz also allows recording of audio, when the output format supports it.

%prep
%setup
patch -p1 < debian/patches/Fix-FTBFS-because-of-Wcast-align-error-flag.patch
patch -p1 < debian/patches/audio.patch
patch -p1 < debian/patches/no-Werror.patch
patch -p1 < debian/patches/remove-deprecated-gnome-common-macros.patch
NOCONFIGURE=1 ./autogen.sh

%build
CFLAGS="%{optflags} -Wno-deprecated-declarations"
%configure
%make

%install
%makeinstall_std

%check
%make_build check

%find_lang %{pname}

%files -f %{pname}.lang
%doc AUTHORS ChangeLog COPYING NEWS README
%_bindir/*
%_datadir/icons/hicolor/*/apps/%{pname}-record-area.*
%_datadir/icons/hicolor/*/apps/%{pname}-record-desktop.*
%_datadir/icons/hicolor/*/apps/%{pname}-record-window.*
%_man1dir/*
%_libexecdir/%{pname}-applet
%dir %_datadir/%pname
%_datadir/%pname/%{pname}applet.xml
%_datadir/mate-panel/applets/org.mate.ByzanzApplet.mate-panel-applet
%_datadir/dbus-1/services/org.mate.panel.applet.ByzanzAppletFactory.service
%_datadir/glib-2.0/schemas/org.mate.byzanz.applet.gschema.xml

%changelog
* Wed Feb 05 2025 Nikolay Strelkov <snk@altlinux.org> 0.3.0-alt1_0.git202502041
- Initial build for Sisyphus
