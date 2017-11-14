%define rname minuet

Name: kde5-%rname
Version: 16.04.1
Release: alt3
%K5init

Group: Education
Summary: Music Education Software
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Thu May 26 2016 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ gtk-update-icon-cache kf5-kdoctools kf5-kdoctools-devel libEGL-devel libGL-devel libalsa-devel libdrumstick-alsa1 libdrumstick-file1 libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-svg libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms perl pkg-config python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3 xml-common xml-utils
#BuildRequires: drumstick-devel extra-cmake-modules kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdelibs4support kf5-kdoctools-devel-static kf5-ki18n-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel python-module-google python3-dev qt5-declarative-devel ruby ruby-stdlibs
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-declarative-devel
BuildRequires: drumstick-devel libalsa-devel
BuildRequires: kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdelibs4support kf5-kdoctools-devel-static kf5-ki18n-devel kf5-kio-devel
BuildRequires: kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel
BuildRequires: kf5-kxmlgui-devel kf5-solid-devel

%description
Minuet is an application for music education. It features a set of ear training exercises regarding intervals, chords, scales and more.

%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%K5install_move data minuet
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_K5bin/minuet
%_K5data/minuet/
%_K5xmlgui/minuet/
%_K5icon/hicolor/*/apps/minuet.*
%_K5xdgapp/org.kde.minuet.desktop

%changelog
* Tue Nov 14 2017 Oleg Solovyov <mcpain@altlinux.org> 16.04.1-alt3
- fix requires

* Tue Sep 12 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 16.04.1-alt2
- Fixed build with new toolchain.

* Thu May 26 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- initial build
