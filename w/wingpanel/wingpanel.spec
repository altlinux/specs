Name: wingpanel
Version: 0.2.5
Release: alt1

Summary: A super sexy space-saving top panel
Group: Graphical desktop/Other
License: GPLv3+
Url: https://launchpad.net/wingpanel

Source0: %name-%version.tgz

Packager: Igor Zubkov <icesik@altlinux.org>

BuildRequires: cmake glib2-devel libindicator-gtk3-devel libgranite-devel
BuildRequires: libpixman-devel libexpat-devel libXdmcp-devel libXdamage-devel
BuildRequires: libXxf86vm-devel libharfbuzz-devel libpng-devel
BuildRequires: libXinerama-devel libXi-devel libXrandr-devel libXcursor-devel
BuildRequires: libXcomposite-devel libxkbcommon-devel libwayland-cursor-devel
BuildRequires: at-spi2-atk-devel gcc-c++ libgranite-vala

#Recommends: indicator-application,
#            indicator-datetime,
#            indicator-me,
#            indicator-messages,
#            indicator-session,
#            indicator-sound
#Provides: indicator-renderer

%description
A replacement for the traditional GNOME Panel, designed to be a lightweight
container for system/application indicators and notification icons.
Designed by elementary Project.

%prep
%setup -q

%build
%cmake_insource
%make_build VERBOSE=1

%install
%make_install DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%_bindir/*
%_datadir/applications/wingpanel.desktop
%_datadir/glib-2.0/schemas/org.pantheon.desktop.wingpanel.gschema.xml
%_datadir/icons/hicolor/scalable/apps/wingpanel.svg

%changelog
* Mon Oct 07 2013 Igor Zubkov <icesik@altlinux.org> 0.2.5-alt1
- 0.2.3 -> 0.2.5

* Sun Sep 15 2013 Igor Zubkov <icesik@altlinux.org> 0.2.3-alt1
- build for Sisyphus

