%define rname kamerka
Name: kde5-kamerka
Version: 0.20
Release: alt2
%K5init

Group: Video
Summary: Take photos using your webcam and shiny interface
Url: http://dos1.github.com/kamerka/
License: GPLv2+

Source: %rname-%version.tar
Patch1: alt-desktop.patch
Source10: ru.po

# Automatically added by buildreq on Wed Apr 17 2019 (-bi)
# optimized out: cmake cmake-modules elfutils fontconfig gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 kf5-karchive-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kcrash-devel kf5-kdbusaddons-devel kf5-kdesignerplugin-devel kf5-kdoctools kf5-kdoctools-devel kf5-kemoticons-devel kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kinit-devel kf5-kitemmodels-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-knotifications-devel kf5-kparts-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kunitconversion-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel kf5-sonnet-devel libGL-devel libdbusmenu-qt52 libgpg-error libqt4-core libqt4-devel libqt4-gui libqt5-concurrent libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-script libqt5-svg libqt5-texttospeech libqt5-widgets libqt5-x11extras libqt5-xml libsasl2-3 libssl-devel libstdc++-devel libxcbutil-keysyms pkg-config python-base python-modules python3 python3-base qt5-base-devel qt5-declarative-devel rpm-build-python3 sh4
#BuildRequires: appstream extra-cmake-modules kf5-kdeclarative-devel kf5-kdelibs4support-devel kf5-kio-devel kf5-kpackage-devel libqimageblitz-devel libv4l-devel python3-dev qt5-phonon-devel qt5-script-devel qt5-wayland-devel
BuildRequires(pre): rpm-build-kf5
BuildRequires: rpm-build-kf5
BuildRequires: qt5-phonon-devel qt5-script-devel qimageblitz5-devel
BuildRequires: extra-cmake-modules
BuildRequires: kf5-kdeclarative-devel kf5-kdelibs4support-devel kf5-kio-devel kf5-kpackage-devel libv4l-devel

%description
Kamerka is a KDE application which uses Video4Linux to get image from
webcam, with ability to save photos. It features easy to use, animated
and well-integrated user interface.

%prep
%setup -qn %rname-%version
%patch1 -p1

cat %SOURCE10 > po/ru.po

%build
%K5build \
    -DDATA_INSTALL_DIR=%_K5data \
    #


%install
%K5install

%find_lang --with-kde %rname

%files -f %rname.lang
%doc AUTHORS README
%_K5bin/%rname
%_K5cfg/%rname.*
%_K5xdgapp/%rname.*
%_K5data/%rname/
%_K5notif/%rname.*
%_pixmapsdir/%rname.*
#%_man1dir/%rname.*

%changelog
* Fri Oct 15 2021 Sergey V Turchin <zerg@altlinux.org> 0.20-alt2
- update russian translation

* Wed Apr 17 2019 Sergey V Turchin <zerg@altlinux.org> 0.20-alt1
- new version

* Thu Mar 17 2016 Sergey V Turchin <zerg@altlinux.org> 0.12-alt1
- new version

* Fri May 30 2014 Sergey V Turchin <zerg@altlinux.org> 0.8.5-alt0.M70P.1
- built for M70P

* Fri May 30 2014 Sergey V Turchin <zerg@altlinux.org> 0.8.5-alt1
- initial build

