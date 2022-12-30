%define gstapi	1.0

Name:		audio-recorder
Version:	2.2.3
Release:	alt2

Summary:	Audio recorder application for the GNOME 3

License:	GPLv3+
Group:		Sound
Url:		https://launchpad.net/audio-recorder

# Source0-url:	https://launchpad.net/%{name}/trunk/stable/+download/%{name}_%{version}.tar.xz
Source0:        %name-%version.tar

Patch0:		audio-recorder-correct-desktop-menu.patch
Patch1:		0001-Port-to-Ayatana-AppIndicator.patch
Patch2:         audio-recorder-1.9.7-no-autostart.patch
Patch3:         0002-audio-recorder-2.2.3-update-russian-translation.patch

BuildRequires:	intltool
BuildRequires:	pkgconfig(ayatana-appindicator3-0.1)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(dconf)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gstreamer-%{gstapi})
BuildRequires:	pkgconfig(gstreamer-pbutils-%{gstapi})
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libpulse)

Requires:	gst-plugins-bad1.0
Requires:	gst-plugins-base1.0
Requires:	gst-plugins-good1.0
Requires:	gst-plugins-ugly1.0

%description
Audio-recorder allows you to record your favourite music or audio to
a file. It can record audio from your system's soundcard,
microphones, browsers, webcams & more. Put simply: if it plays out of
your loudspeakers you can record it.

%prep
%setup -q -n %name-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
autoreconf -vfi
%configure
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog README
%_bindir/%name
%_datadir/%name/
%_datadir/pixmaps/%name/
%_datadir/applications/%name.desktop
%_iconsdir/hicolor/scalable/*/%{name}*.svg
%_datadir/glib-2.0/schemas/org.gnome.%name.gschema.xml
%_mandir/man1/%name.1*

%changelog
* Thu Dec 29 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 2.2.3-alt2
- Initial build
