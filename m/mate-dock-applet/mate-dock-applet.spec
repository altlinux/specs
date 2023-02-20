%define _localedir %_datadir/locale
%ifnarch x86_64
%define _libdir /usr/lib
%endif

Name: mate-dock-applet
Version: 21.10.0
Release: alt1.1

Summary: application dock for the MATE panel
License: GPL-3.0
Group: Development/Python3
Url: https://github.com/ubuntu-mate/mate-dock-applet

Packager: Artyom Bystrov <arbars@altlinux.org>

BuildRequires: libgio-devel python-devel rpm-build-python3
BuildRequires: python3 python3-tools
BuildRequires: pkgconfig(glib-2.0)

Requires: python3 python3-tools
Requires: mate-panel >= 1.20.0
Requires: python3-module-pyxdg
Requires: python3-module-pycairo
Requires: python3-module-pygobject3 python3-module-pygobject3-pygtkcompat
Requires: python3-module-Pillow
Requires: python3-module-xlib

BuildArch: noarch

Source: %name-%version.tar

%description
MATE Dock Applet is a MATE Panel applet that displays
running application windows as icons. The applet features
options to pin applications to the dock, supports multiple
workspaces, and can be added to any MATE Panel, regardless
of size and orientation

%prep
%setup -n %name-%version


%build
autoreconf -fi
./configure --prefix=/usr --with-gtk3
make

%install
%makeinstall_std

%find_lang %name --all-name

%files
%doc COPYING
%doc AUTHORS ChangeLog README
%_localedir/*/LC_MESSAGES/mate-dock-applet.mo
%_datadir/dbus-1/services/org.mate.panel.applet.DockAppletFactory.service
%_datadir/glib-2.0/schemas/org.mate.panel.applet.dock.gschema.xml
%_datadir/mate-panel/applets/org.mate.panel.DockApplet.mate-panel-applet
%_libdir/mate-applets/mate-dock-applet/

%changelog
* Mon Feb 20 2023 Artyom Bystrov <arbars@altlinux.org> 21.10.0-alt1.1
- new version 21.10.0, fix bug ALT#45088

* Mon Feb 20 2023 Artyom Bystrov <arbars@altlinux.org> V0.89-alt1
- Initial build for Sisyphus
