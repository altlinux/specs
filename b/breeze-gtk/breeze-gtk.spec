%define rname breeze-gtk

Name: %rname
Version: 6.7.2
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
* Wed Jul 01 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt1
- new version

* Mon Jun 29 2026 Sergey V Turchin <zerg@altlinux.org> 6.7.1-alt1
- new version

* Tue May 12 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.5-alt1
- new version

* Thu Apr 09 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.4-alt1
- new version

* Mon Mar 30 2026 Sergey V Turchin <zerg@altlinux.org> 6.6.3-alt1
- new version

* Wed Mar 11 2026 Sergey V Turchin <zerg@altlinux.org> 6.5.6-alt1
- new version

* Thu Jan 15 2026 Sergey V Turchin <zerg@altlinux.org> 6.5.5-alt1
- new version

* Wed Dec 10 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.4-alt1
- new version

* Tue Nov 18 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.3-alt1
- new version

* Thu Nov 13 2025 Sergey V Turchin <zerg@altlinux.org> 6.5.2-alt1
- new version

* Wed Nov 12 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.6-alt1
- new version

* Tue Sep 16 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.5-alt1
- new version

* Fri Aug 22 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.4-alt1
- new version

* Tue Jul 15 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.3-alt1
- new version

* Tue Jul 08 2025 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt1
- new version

* Wed May 07 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.5-alt1
- new version

* Wed Apr 02 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.4-alt1
- new version

* Wed Mar 12 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.3-alt1
- new version

* Wed Feb 26 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.2-alt1
- new version

* Wed Feb 19 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.1-alt1
- new version

* Fri Feb 14 2025 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Thu Jan 09 2025 Sergey V Turchin <zerg@altlinux.org> 6.2.5-alt1
- new version

* Tue Nov 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt1
- new version

* Wed Nov 06 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.3-alt1
- new version

* Mon Oct 28 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.2-alt1
- new version

* Tue Sep 10 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.5-alt1
- new version

* Thu Aug 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.4-alt1
- new version

* Thu Jul 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.2-alt1
- new version

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.1-alt1
- new version

* Tue Jun 25 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- initial build

