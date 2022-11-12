Name: gcolor3
Version: 2.4.0
Release: alt1
Summary: A simple color chooser written in GTK3 (like gcolor2)

License: GPLv2+
Group: Graphics
Url: https://www.hjdskes.nl/projects/gcolor3/

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar
Patch1: gcolor3-2.4.0-libportal-0.5.patch

BuildRequires: gcc
BuildRequires: meson
BuildRequires: gnome-common
BuildRequires: libgtk+3-devel >= 3.12.0
BuildRequires: intltool
BuildRequires: desktop-file-utils
BuildRequires: gettext-tools
BuildRequires: libappstream-glib
BuildRequires: make
BuildRequires: pkgconfig(libportal-gtk3)
Requires: hicolor-icon-theme

%description
Gcolor3 is a color selection dialog written in GTK+ 3. It is much alike Gcolor2,
but uses the newer GTK+ version to better integrate into your modern desktop.
It has the same feature set as Gcolor2, except that recent versions of Gcolor3
use an .ini style file to save colors (older versions use the same file as
Gcolor2).

%prep
%setup -n %name-%version
%patch1 -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang gcolor3
desktop-file-validate %buildroot%_desktopdir/nl.hjdskes.gcolor3.desktop
appstream-util validate-relax --nonet %buildroot%_datadir/metainfo/nl.hjdskes.gcolor3.appdata.xml

%files -f gcolor3.lang
%doc README.md
%doc LICENSE
%_bindir/gcolor3
%_desktopdir/nl.hjdskes.gcolor3.desktop
%_iconsdir/hicolor/scalable/apps/nl.hjdskes.gcolor3.svg
%_iconsdir/hicolor/symbolic/apps/nl.hjdskes.gcolor3-symbolic.svg
%_datadir/metainfo/nl.hjdskes.gcolor3.appdata.xml
%_man1dir/gcolor3.1*

%changelog
* Sat Nov 12 2022 Artyom Bystrov <arbars@altlinux.org> 2.4.0-alt1
- initial build for ALT Sisyphus
