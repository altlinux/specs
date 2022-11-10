%define ver_major 43
%define xdg_name org.gnome.Packages

Name: gnome-packagekit
Version: %ver_major.0
Release: alt1

Summary: A PackageKit client for the GNOME desktop
Group: Graphical desktop/GNOME
License: GPLv2+
Url: http://www.packagekit.org

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

BuildRequires(pre): rpm-macros-meson rpm-build-systemd
BuildRequires: meson desktop-file-utils docbook-utils
BuildRequires: xsltproc yelp-tools libappstream-devel
BuildRequires: glib2-devel >= 2.56
BuildRequires: libgtk+3-devel >= 3.24
BuildRequires: libpackagekit-glib-devel >= 0.9.1
BuildRequires: libnotify-devel >= 0.7.0
#BuildRequires: libstartup-notification-devel libcanberra-gtk3-devel
BuildRequires: libgudev-devel libpolkit-devel

# the top level package depends on all the apps to make upgrades work
Requires: %name-installer
Requires: %name-updater

%description
GNOME PackageKit is the name of the collection of graphical tools for
PackageKit to be used in the GNOME desktop.

%package common
Summary: Common files required for %name
Group: Graphical desktop/GNOME
Requires: adwaita-icon-theme
Requires: packagekit
Requires: iso-codes

# required because KPackageKit provides exactly the same interface
Provides: PackageKit-session-service

%description common
Files shared by all subpackages of %name

%package installer
Summary: PackageKit package installer
Group: Graphical desktop/GNOME
Requires: %name-common = %version-%release

%description installer
A graphical package installer for PackageKit which is used to manage software
not shown in GNOME Software.

%package updater
Summary: PackageKit package updater
Group: Graphical desktop/GNOME
Requires: %name-common = %version-%release

%description updater
A graphical package updater for PackageKit which is used to update packages
without rebooting.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

# use gnome-software for installing local files
rm -f $RPM_BUILD_ROOT%_datadir/applications/gpk-install-local-file.desktop

%find_lang %name --with-gnome

%files
# nada

%files common -f %name.lang
%_bindir/gpk-log
%_bindir/gpk-prefs
%_datadir/%name/
%_desktopdir/gpk-log.desktop
%_desktopdir/gpk-prefs.desktop
%_iconsdir/hicolor/scalable/*/*.svg*
%_datadir/glib-2.0/schemas/org.gnome.packagekit.gschema.xml
%_datadir/GConf/gsettings/org.gnome.packagekit.gschema.migrate
%_man1dir/gpk-log.1*
%_man1dir/gpk-prefs.1*
%doc AUTHORS README*

%files installer
%_bindir/gpk-application
%_desktopdir/%xdg_name.desktop
%_datadir/metainfo/%xdg_name.metainfo.xml
%_man1dir/gpk-application.1*

%files updater
%_bindir/gpk-update-viewer
%_desktopdir/org.gnome.PackageUpdater.desktop
%_datadir/metainfo/org.gnome.PackageUpdater.metainfo.xml
%_man1dir/gpk-update-viewer.1*

%changelog
* Thu Nov 10 2022 Yuri N. Sedunov <aris@altlinux.org> 43.0-alt1
- 43.0

