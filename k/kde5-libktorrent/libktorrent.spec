
%define sover 6
%define libktorrent libktorrent%sover

Name: kde5-libktorrent
Version: 2.0.1
Release: alt1

Group: System/Libraries
Summary: BitTorrent library for KDE
Url: http://ktorrent.org/
License: GPLv2

Source: libktorrent-%version.tar

# Automatically added by buildreq on Mon Apr 18 2016 (-bi)
# optimized out: cmake cmake-modules elfutils gcc-c++ libEGL-devel libGL-devel libgpg-error libgpg-error-devel libqca-qt5 libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-svg libqt5-test libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcbutil-keysyms perl python-base python-modules python3 python3-base qt5-base-devel rpm-build-python3 ruby ruby-stdlibs
#BuildRequires: boost-devel-headers doxygen extra-cmake-modules graphviz kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-ki18n-devel kf5-kio-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel libgcrypt-devel libgmp-devel libqca-qt5-devel python-module-google python3-dev rpm-build-ruby
BuildRequires: rpm-build-kf5
BuildRequires: boost-devel doxygen extra-cmake-modules graphviz
BuildRequires: libgcrypt-devel libgmp-devel libqca-qt5-devel
BuildRequires: kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-ki18n-devel kf5-kio-devel kf5-kitemviews-devel
BuildRequires: kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kxmlgui-devel kf5-solid-devel

%description
Library that allow using BitTorrent with KDE programs

%package common
BuildArch: noarch
Summary: Common %name files
Group: System/Libraries
%description common
Common %name files

%package -n %libktorrent
Summary: KTorrent library
Group: System/Libraries
Requires: %name-common
%description -n %libktorrent
KTorrent library

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: libgcrypt-devel libqca-qt5-devel
%description devel
This package contains the development files for %name.


%prep
%setup -qn libktorrent-%version

%build
%K5build \
    -DKDE_INSTALL_INCLUDEDIR=%_K5inc \
    -DKDE_INSTALL_LOCALEDIR=%_K5i18n \
  #

%install
%K5install
%find_lang --with-kde --all-name %name

%files common -f %name.lang

%files -n %libktorrent
%_libdir/libktorrent.so.%sover
%_libdir/libktorrent.so.%sover.*

%files devel
%_K5lib/cmake/LibKTorrent/
%_K5inc/libktorrent/
%_K5link/lib*.so

%changelog
* Mon Apr 18 2016 Sergey V Turchin <zerg@altlinux.org> 2.0.1-alt1
- initial build
