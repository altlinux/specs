%define rname kde-gtk-config

Name: %rname
Version: 6.1.5
Release: alt1
#Epoch: 1
%K6init

Group: Graphical desktop/KDE
Summary: KDE Frameworks 6 GNOME/GTK Application Style
Url: http://www.kde.org
License: GPL-2.0-or-later

Requires: xsettingsd
Provides: plasma5-kde-gtk-config = 1:%version-%release
Obsoletes: plasma5-kde-gtk-config < 1:%version-%release

Source: %rname-%version.tar
Patch1: alt-defaults.patch
Patch2: alt-def-font.patch

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-svg-devel
BuildRequires: sassc
BuildRequires: libgtk+2-devel libgtk+3-devel libXcursor-devel
BuildRequires: libvulkan-devel
BuildRequires: kf6-karchive-devel kf6-kauth-devel kf6-kbookmarks-devel kf6-kcmutils-devel kf6-kcodecs-devel kf6-kcompletion-devel
BuildRequires: kf6-kconfig-devel kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kdbusaddons-devel kf6-kglobalaccel-devel
BuildRequires: kf6-kguiaddons-devel kf6-ki18n-devel kf6-kiconthemes-devel kf6-kio-devel kf6-kitemviews-devel kf6-kjobwidgets-devel
BuildRequires: kf6-knewstuff-devel kf6-kservice-devel kf6-ktextwidgets-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel
BuildRequires: kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel kf6-kconfig-devel kf6-kcolorscheme-devel
BuildRequires: plasma6-kdecoration-devel
# workaround against pango includes
BuildRequires: libharfbuzz-devel

%description
Widget Style of GNOME/GTK Applications.

%prep
%setup -n %rname-%version
#%patch1 -p1
%patch2 -p1

%build
ADD_OPTFLAGS=`pkg-config --cflags harfbuzz`
%add_optflags $ADD_OPTFLAGS
%K6build \
    -DLIBEXEC_INSTALL_DIR=%_K6exec \
    -DDATA_INSTALL_DIR=%_K6data \
    #

%install
%K6install
%K6install_move data kconf_update
#K6install_move data kcm-gtk-module knsrcfiles
%find_lang %name --all-name

%files -f %name.lang
%doc LICENSES/*
%_K6libexecdir/*gtk*
%_K6conf_bin/*gtk*
%_K6plug/kf6/kded/*gtk*.so
%_libdir/gtk-*/modules/*.so
%_K6conf_up/*gtk*.*
%_K6data/kcm-gtk-module/
%_datadir/themes/Breeze/window_decorations.css



%changelog
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

