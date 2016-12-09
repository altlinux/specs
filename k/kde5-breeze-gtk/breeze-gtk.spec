%define rname breeze-gtk

Name: kde5-%rname
Version: 5.8.4
Release: alt1%ubt
%K5init no_altplace

Group: Graphical desktop/KDE
Summary: Breeze GTK2/3 theme
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Provides: kde5-breeze-dark-gtk = %EVR

Source: %rname-%version.tar
Patch1: alt-conf-update.patch

# Automatically added by buildreq on Wed Oct 05 2016 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ libqt5-core libstdc++-devel perl python-base python-modules python3 python3-base rpm-build-python3
#BuildRequires: extra-cmake-modules python-module-google python3-dev qt5-base-devel ruby ruby-stdlibs
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules qt5-base-devel
BuildRequires: gtk-engines-pixmap libgtk+3-devel pkg-config

%description
This is GTK2/3 port of default KDE Breeze style.

%package -n gtk-theme-breeze
Group: Graphical desktop/KDE
Summary: %summary
#Requires: gtk-engines-pixmap
Provides: gtk2-theme-breeze = %version-%release
Provides: gtk3-theme-breeze = %version-%release
%description -n gtk-theme-breeze
%{description}

%prep
%setup -n %rname-%version
%patch1 -p1

%build
%K5build \
    -DWITH_GTK3_VERSION=`pkg-config --modversion gtk+-3.0` \
    #

%install
%K5install
%K5install_move data kconf_update

%files -n gtk-theme-breeze
%_K5conf_bin/gtkbreeze*
%_K5conf_up/gtkbreeze*
%_datadir/themes/Breeze*

%changelog
* Fri Dec 09 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.4-alt1%ubt
- new version

* Wed Nov 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.3-alt0.M80P.1
- build for M80P

* Tue Nov 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.3-alt1
- new version

* Tue Oct 25 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.2-alt1
- new version

* Tue Oct 18 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.1-alt0.M80P.1
- build for M80P

* Fri Oct 14 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.1-alt1
- new version

* Thu Oct 06 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt3
- fix update GTK settings

* Wed Oct 05 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt2
- fix gtk3 theme

* Wed Oct 05 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt1
- initial build
