Name: kde-gtk-config
Version: 2.2.1
Release: alt2

Summary: GTK2 and GTK3 configurator for KDE
License: GPLv3
Group: Graphical desktop/KDE

Url: https://projects.kde.org/projects/playground/base/kde-gtk-config
Source: ftp://ftp.kde.org/pub/kde/stable/%name/%version/src/%name-%version.tar.xz
Patch1: kde-gtk-config-2.2-gtkrc-2.0-kde-config-file.patch
Patch2: kde-gtk-config-2.2.1-fix-ftbfs.patch

BuildPreReq: rpm-macros-kde-common-devel
BuildRequires: kde4libs-devel
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: gcc-c++ 

%description
Configuration dialog to adapt GTK applications appearance to your taste
under KDE. Among its many features, it lets you:
- Choose which theme is used for GTK2 and GTK3 applications.
- Tweak some GTK applications behaviour.
- Select what icon theme to use in GTK applications.
- Select GTK applications default fonts.
- Easily browse and install new GTK2 and GTK3 themes.

%prep
%setup
%patch1 -p1
%patch2 -p2

%build
%K4build

%install
%K4install
%find_lang %name

%files -f %name.lang
%doc README COPYING ChangeLog
%_K4libdir/kde4/libexec/gtk_preview
%_K4libdir/kde4/libexec/gtk3_preview
%_K4libdir/kde4/libexec/reload_gtk_apps
%_K4libdir/kde4/kcm_cgc.so
%_K4apps/kcm-gtk-module/preview.ui
%_K4conf/cgcgtk3.knsrc
%_K4conf/cgcicon.knsrc
%_K4conf/cgctheme.knsrc
%_K4iconsdir/hicolor/48x48/apps/kde-gtk-config.png
%_K4srv/kde-gtk-config.desktop

%changelog
* Fri Nov 17 2017 Oleg Solovyov <mcpain@altlinux.org> 2.2.1-alt2
- fix build

* Mon Mar 09 2015 Michael Shigorin <mike@altlinux.org> 2.2.1-alt1
- built for ALT Linux (based on Rosa's 2.2.1-2 package)

