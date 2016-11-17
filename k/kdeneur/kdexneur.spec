Name: kdeneur
Version: 0.19.0
Release: alt1

Summary: KDE frontend for X Neural Switcher

License: GPL
Group: Office
Url: http://xneur.ru/

Source: %{name}_%version.orig.tar.gz

Requires: xneur >= %version

# Automatically added by buildreq on Mon Oct 28 2013
# optimized out: fontconfig gnu-config kde4libs libX11-devel libdbusmenu-qt2 libgdk-pixbuf libgst-plugins libpcre-devel libqt4-core libqt4-dbus libqt4-declarative libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-script libqt4-sql libqt4-svg libqt4-uitools libqt4-webkit libqt4-xml libqt4-xmlpatterns libstdc++-devel pkg-config xorg-kbproto-devel xorg-xproto-devel
BuildRequires: gcc-c++ kde4libs-devel libxneur-devel

%description
Xneur is program like Punto Switcher, but has other
functionality and features for configuring.

%prep
%setup

%build
%configure
%make_build CXXFLAGS="-I%_includedir/kde4" LDFLAGS="-L%_libdir/kde4/devel"

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog NEWS README TODO
%_bindir/*
%_datadir/%name/
%_man1dir/*
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*
%_iconsdir/hicolor/scalable/apps/%name.*

%changelog
* Thu Nov 17 2016 Fr. Br. George <george@altlinux.ru> 0.19.0-alt1
- Autobuild version bump to 0.19.0

* Mon Oct 28 2013 Fr. Br. George <george@altlinux.ru> 0.17.0-alt1
- Initial build

