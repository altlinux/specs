
Name:           bangarang
Version:        2.1
Release:        alt2

Group: Video
Summary:        Media Player for KDE4
Url:            http://www.kde-apps.org/content/show.php/Bangarang?content=113305
License:        GPLv3

Source:        %name-%version.tar
Patch1: alt-nepomuk-warning.patch

# Automatically added by buildreq on Wed Feb 22 2012 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde-common-devel kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-script libqt4-svg libqt4-xml libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base shared-desktop-ontologies-devel soprano-backend-redland soprano-backend-virtuoso xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4libs-devel libicu libqt3-devel libtag-devel soprano zlib-devel-static
BuildRequires: gcc-c++ kde4libs-devel libtag-devel kde-common-devel
BuildRequires: soprano-backend-redland soprano-backend-virtuoso soprano

%description
Bangarang is a KDE media player. The name comes from the Jamaican word
for noisy, chaos or disorder.

As much as possible, the pillars of KDE and existing KDE infrastructures
are/will be used.

%prep
%setup -q
%patch1 -p1

%build
%K4build

%install
%K4install

%K4find_lang --with-kde %name

%files -f %name.lang
%doc README
%_K4bindir/%{name}*
%_K4xdg_apps/%{name}.desktop
%_K4apps/solid/actions/%{name}*.desktop
%_K4iconsdir/hicolor/*/apps/%{name}*.*
%_K4iconsdir/hicolor/*/status/%{name}*.*
%_K4iconsdir/hicolor/*/actions/%{name}*.*

%changelog
* Mon Feb 27 2012 Sergey V Turchin <zerg@altlinux.org> 2.1-alt2
- don't warn about nepomuk

* Wed Feb 22 2012 Sergey V Turchin <zerg@altlinux.org> 2.1-alt0.M60P.1
- built for M60P

* Wed Feb 22 2012 Sergey V Turchin <zerg@altlinux.org> 2.1-alt1
- initial build

