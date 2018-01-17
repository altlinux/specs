Name: yad
Version: 0.40.0
Release: alt1
Summary: Display graphical dialogs from shell scripts or command line

Group: Graphical desktop/GNOME
License: GPLv3+
Url: http://sourceforge.net/projects/yad-dialog/
Source0: http://downloads.sourceforge.net/%name-dialog/%name-%version.tar.xz
Patch0: fix-missing-buttons.patch

BuildRequires: desktop-file-utils
# Automatically added by buildreq on Fri Oct 10 2014
# optimized out: at-spi2-atk fontconfig glib2-devel libX11-devel libat-spi2-core libatk-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libcloog-isl4 libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libpango-devel libwayland-client libwayland-cursor libwayland-server perl-Encode perl-XML-Parser pkg-config xorg-xproto-devel xz
BuildRequires: intltool libgtk+3-devel

%description
Yad (yet another dialog) is a fork of zenity with many improvements, such as
custom buttons, additional dialogs, pop-up menu in notification icon and more.

%prep
%setup
%patch0 -p0

%build
%configure \
    --with-gtk=gtk3 \
    --with-rgb=/usr/share/X11/rgb.txt \
    --enable-icon-browser \
    #

%make_build

%install
%makeinstall_std

%find_lang %name

desktop-file-install --remove-key Encoding     \
    --remove-category Development              \
    --add-category    Utility                  \
    --dir=%buildroot%_desktopdir \
    %buildroot%_desktopdir/%name-icon-browser.desktop

%files -f %name.lang
%doc AUTHORS COPYING NEWS THANKS TODO
%_bindir/*
%_iconsdir/hicolor/*/apps/*
%exclude %_datadir/aclocal/%name.m4
%_man1dir/*
%_desktopdir/*

%changelog
* Wed Jan 17 2018 Fr. Br. George <george@altlinux.ru> 0.40.0-alt1
- Autobuild version bump to 0.40.0

* Fri May 19 2017 Fr. Br. George <george@altlinux.ru> 0.39.0-alt1
- Autobuild version bump to 0.39.0

* Mon Mar 13 2017 Fr. Br. George <george@altlinux.ru> 0.38.2-alt1
- Autobuild version bump to 0.38.2

* Mon Oct 31 2016 Fr. Br. George <george@altlinux.ru> 0.37.0-alt1
- Autobuild version bump to 0.37.0

* Tue Jul 26 2016 Fr. Br. George <george@altlinux.ru> 0.36.3-alt1
- Autobuild version bump to 0.36.3

* Thu Dec 24 2015 Fr. Br. George <george@altlinux.ru> 0.32.0-alt1
- Autobuild version bump to 0.32.0

* Wed Nov 18 2015 Fr. Br. George <george@altlinux.ru> 0.31.3-alt1
- Autobuild version bump to 0.31.3

* Wed Oct 21 2015 Fr. Br. George <george@altlinux.ru> 0.31.2-alt1
- Autobuild version bump to 0.31.2

* Fri Oct 10 2014 Fr. Br. George <george@altlinux.ru> 0.27.0-alt1
- Fresh build from FC

* Thu Oct 31 2013 Afanasov Dmitry <ender@altlinux.org> 0.23.1-alt1
- initial build

