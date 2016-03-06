Name: djview4
Version: 4.10.6
Release: alt1

Summary: DjVu viewers, encoders and utilities (QT4 based version)
License: GPLv2+
Group: Publishing
Url: http://djvu.sourceforge.net/djview4.html

# http://download.sourceforge.net/djvu/djview-%version.tar.gz
Source: djview-%version.tar

Patch1: djview-4.8-rh-include.patch

%def_disable static
%define qtdir %_libdir/qt4

Provides: djvu-viewer = %EVR
Obsoletes: djvu-viewer < %EVR

BuildRequires: libdjvu-devel >= 3.5.25
BuildRequires: browser-plugins-npapi-devel

# Automatically added by buildreq on Sat Apr 13 2013
# optimized out: fontconfig gnu-config libICE-devel libSM-devel libX11-devel libXext-devel libqt4-core libqt4-gui libqt4-network libstdc++-devel pkg-config phonon-devel xorg-xproto-devel
BuildRequires: gcc-c++ glib2-devel libXt-devel libdjvu-devel libqt4-devel libtiff-devel xdg-utils

%description
This package contains the djview4 viewer and browser plugin.
This new viewer relies on the DjVulibre library and the Qt4 toolkit.

Highlights:
- entirely based on the public djvulibre api.
- entirely written in portable Qt4.
- has been reported to work with Qt/Mac.
- should work with Qt/Windows as well.
- continuous scrolling of pages
- side-by-side display of pages
- ability to specify a url to the djview command
- all plugin and cgi options available from the command line
- all silly annotations implemented
- display thumbnails as a grid
- display outlines
- page names supported (see djvused command set-page-title)
- metadata dialog (see djvused command set-meta)
- implemented as reusable Qt widgets

%package -n mozilla-plugin-djvu4
Summary: DjVu NPAPI plugin (QT4 based version)
Group: Networking/WWW
Requires: %name = %EVR
Requires: browser-plugins-npapi 
Conflicts: mozilla-plugin-djvu < 4.1
Obsoletes: mozilla-plugin-djvu < 4.1

%description -n mozilla-plugin-djvu4
Under Unix/X11, djview4 can be used as a browser plugin
by means of the small shared library named nsdejavu.so.
The djview3 distributed with djvulibre uses the same approach.

%prep
%setup -n djview-%version
%patch1 -p1

sed -i '/^#/d' desktopfiles/djvulibre-djview4.desktop
sed -i 's,^\(plugindir[[:space:]]*=[[:space:]]*\).*,\1%browser_plugins_path,' nsdejavu/Makefile.in

%build
export QTDIR=%qtdir
export PATH=$QTDIR/bin:$PATH
%configure %{subst_enable static}
%make_build NSDEJAVU_LIBS='-lXt -lX11'

%install
%makeinstall_std

# Перемещаем плагин для браузеров в предназначенное для этого место.
mkdir -p %buildroot%browser_plugins_path
mv %buildroot%_libdir/mozilla/plugins/nsdejavu.so %buildroot%browser_plugins_path/nsdejavu.so
# Стираем файл .la, который нужен лишь libtool'у для генерации имён библиотек.
rm -f %buildroot%_libdir/mozilla/plugins/nsdejavu.la

install -Dpm644 desktopfiles/prebuilt-hi32-djview4.png \
	%buildroot%_niconsdir/djvulibre-djview4.png
install -Dpm644 desktopfiles/djvulibre-djview4.desktop \
	%buildroot%_desktopdir/djvulibre-djview4.desktop

mv %buildroot%_bindir/djview %buildroot%_bindir/djview4
ln -s %buildroot%_bindir/djview4 djview

%find_lang %name
%set_verify_elf_method strict

%files
%_bindir/djview*
%_mandir/man?/djview*
%_desktopdir/*.desktop
%_datadir/djvu/%name/
%_niconsdir/*
%_iconsdir/hicolor/32x32/mimetypes/*
%_iconsdir/hicolor/64x64/mimetypes/*
%_iconsdir/hicolor/scalable/mimetypes/*

%files -n mozilla-plugin-djvu4
%browser_plugins_path/*.so*
%_mandir/man?/nsdejavu*

%changelog
* Sun Mar 06 2016 Andrey Bergman <vkni@altlinux.org> 4.10.6-alt1
- Updated to 4.10.6.

* Mon Jan 11 2016 Andrey Bergman <vkni@altlinux.org> 4.10.5-alt1
- Updated to 4.10.5.

* Fri Jul 03 2015 Andrey Bergman <vkni@altlinux.org> 4.10.3-alt1
- Updated to 4.10.3. Removed unnecessary patch, added mime icons.

* Sat Apr 13 2013 Dmitry V. Levin <ldv@altlinux.org> 4.8-alt1
- Updated to 4.8.

* Wed Sep 30 2009 Alexey Gladkov <legion@altlinux.ru> 4.5-alt1.1
- NMU: Rebuilt with browser-plugins-npapi.

* Sun Jun 28 2009 Evgeny Sinelnikov <sin@altlinux.ru> 4.5-alt1
- Update to new release

* Mon Nov 24 2008 Evgeny Sinelnikov <sin@altlinux.ru> 4.4-alt1
- Update to new release

* Sun Jan 27 2008 Evgeny Sinelnikov <sin@altlinux.ru> 4.3-alt1
- Update to new release

* Wed Oct 10 2007 Evgeny Sinelnikov <sin@altlinux.ru> 4.1.2-alt1
- Initial release
