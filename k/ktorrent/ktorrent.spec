%ifarch %not_qt6_qtwebengine_arches
%def_disable qtwebengine
%else
%def_enable qtwebengine
%endif

%define rname ktorrent
%define sover 16
%define libktcore libktcore%sover

%add_findreq_skiplist %_K6data/%rname/scripts/*.py

Name: %rname
Version: 24.08.1
Release: alt1
%K6init

Group:     Networking/File transfer
Summary:   KDE client for BitTorrent network 
License:   GPL-2.0-or-later
URL:       http://ktorrent.org

Provides: kde5-ktorrent = %EVR
Obsoletes: kde5-ktorrent < %EVR

Source: %rname-%version.tar

# ALT
Patch10: alt-defaults.patch
Patch11: alt-short-date.patch
Patch12: alt-find-taglib.patch

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine

BuildRequires: boost-devel extra-cmake-modules
BuildRequires: qt6-phonon-devel qt6-declarative-devel qt6-5compat-devel
%if_enabled qtwebengine
BuildRequires: qt6-webengine-devel
%endif
BuildRequires: libmaxminddb-devel libgmp-devel libtag-devel
BuildRequires: kde6-libktorrent-devel kf6-syndication-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcmutils-devel kf6-kcodecs-devel kf6-kcompletion-devel
BuildRequires: kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdbusaddons-devel
BuildRequires: kf6-kdnssd-devel kf6-kstatusnotifieritem-devel
BuildRequires: kf6-kdoctools-devel  kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel
BuildRequires: kf6-kio-devel kf6-kitemmodels-devel kf6-kitemviews-devel kf6-kjobwidgets-devel
BuildRequires: kf6-knotifications-devel kf6-knotifyconfig-devel kf6-kparts-devel kf6-kplotting-devel
BuildRequires: kf6-kservice-devel kf6-ktextwidgets-devel kf6-kunitconversion-devel kf6-kwidgetsaddons-devel
BuildRequires: kf6-kwindowsystem-devel kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel
# tmp BuildRequires: workspace-devel

%description
ktorrent - KDE BitTorrent client. It comes with many useful plugins.

%package -n %libktcore
Summary: KTorrent library
Group: System/Libraries
Requires: kde-common
%description -n %libktcore
KTorrent library

%prep
%setup -q -n %rname-%version
%patch10 -p1 -b .defaults
%patch11 -p1
%patch12 -p1

#sed -i 's|^add_subdirectory(plasma)||' CMakeLists.txt

%build
%K6build \
 -DWITH_SYSTEM_GEOIP:BOOL=ON \
 -DKDE_INSTALL_KXMLGUIDIR=%_K6xmlgui \
 #


%install
%K6install
%K6install_move data ktorrent
for f in %buildroot/%_K6xmlgui/%rname/*.rc ; do
    ln -sr $f %buildroot/%_K6data/
done

%find_lang --with-kde %rname


%files -f %rname.lang
%doc LICENSES/*
%_K6bin/*
%_K6icon/hicolor/*/*/kt*.*
%_K6xdgapp/org.kde.%rname.desktop
%_K6plug/ktorrent_plugins/
%_K6notif/%rname.notifyrc
%_K6xmlgui/ktorrent/
%_K6data/*torrent*.rc
%if_enabled qtwebengine
%_K6data/%rname/
%endif
%_datadir/metainfo/*.xml

%files -n %libktcore
%_libdir/libktcore.so.%sover
%_libdir/libktcore.so.*

%changelog
* Wed Sep 25 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.1-alt1
- initial build

