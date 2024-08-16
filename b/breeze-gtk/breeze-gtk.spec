%define rname breeze-gtk

Name: %rname
Version: 6.1.4
Release: alt1
%K6init no_altplace

Group: Graphical desktop/KDE
Summary: Breeze GTK2/3 theme
Url: http://www.kde.org
License: GPL-2.0-or-later

Provides: breeze-dark-gtk = %EVR
Provides: plasma5-breeze-gtk = %EVR
Obsoletes: plasma5-breeze-gtk < %EVR

Source: %rname-%version.tar
Patch1: alt-conf-update.patch
Patch2: alt-gtk2-progressbar.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-base-devel
BuildRequires: gtk-engines-pixmap libgtk+3-devel pkg-config
BuildRequires: /usr/bin/sassc python3-module-pycairo
BuildRequires: libvulkan-devel
BuildRequires: plasma6-breeze plasma6-breeze-devel

%description
This is GTK2/3 port of default KDE Breeze style.

%package -n gtk-theme-breeze
Group: Graphical desktop/KDE
Summary: %summary
#Requires: gtk-engines-pixmap for gtk2-theme-breeze
Provides: gtk2-theme-breeze = %version-%release
Provides: gtk3-theme-breeze = %version-%release
Provides: gtk4-theme-breeze = %version-%release
%description -n gtk-theme-breeze
%{description}

%prep
%setup -n %rname-%version
#%patch1 -p1
#%patch2 -p1

%build
%K6build \
    -DWITH_GTK3_VERSION=`pkg-config --modversion gtk+-3.0` \
    #

%install
%K6install
%K6install_move data kconf_update

%files -n gtk-theme-breeze
%doc LICENSES/*
#%_K6conf_bin/gtkbreeze*
#%_K6conf_up/gtkbreeze*
%_datadir/themes/Breeze*



%changelog
* Thu Aug 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt1
- new version

* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build

