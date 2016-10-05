%define rname breeze-gtk

Name: kde5-%rname
Version: 5.8.0
Release: alt1
%K5init no_altplace

Group: Graphical desktop/KDE
Summary: Breeze GTK2/3 theme
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Provides: kde5-breeze-dark-gtk = %EVR

Source: %rname-%version.tar

# Automatically added by buildreq on Wed Oct 05 2016 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ libqt5-core libstdc++-devel perl python-base python-modules python3 python3-base rpm-build-python3
#BuildRequires: extra-cmake-modules python-module-google python3-dev qt5-base-devel ruby ruby-stdlibs
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-base-devel
BuildRequires: gtk-engines-pixmap

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

%build
%K5build

%install
%K5install
%K5install_move data kconf_update

%files -n gtk-theme-breeze
%_K5conf_bin/gtkbreeze*
%_K5conf_up/gtkbreeze*
%_datadir/themes/Breeze*

%changelog
* Wed Oct 05 2016 Sergey V Turchin <zerg@altlinux.org> 5.8.0-alt1
- initial build
