Name: soundconverter
Version: 2.0.2
Release: alt1

Summary: A simple sound converter application for GNOME
License: GPLv3
Group: Sound

Url: http://soundconverter.org
Source: https://launchpad.net/%name/trunk/%version/+download/%name-%version.tar.xz
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Sat Oct 17 2009
BuildRequires: intltool python-devel python-module-pygnome
BuildRequires: desktop-file-utils

Requires: python-module-pygnome-gnome-vfs
Requires: python-module-pygtk-libglade
Requires: python-module-pygnome-gconf
Requires: python-module-pygobject
Requires: python-module-pygnome
Requires: python-module-notify
Requires: python-module-pygtk
Requires: python-module-gst
Requires: gst-plugins-base
Requires: gst-plugins-good

%description
A simple sound converter application for the GNOME environment.
It reads and writes anything the GStreamer library can.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std
%find_lang %name
desktop-file-install \
	--dir %buildroot%_desktopdir \
	%buildroot%_desktopdir/%name.desktop
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Audio \
	--add-category=AudioVideoEditing \
	%buildroot%_desktopdir/soundconverter.desktop

%files -f %name.lang
%doc ChangeLog COPYING README TODO
%doc %_man1dir/*
%_bindir/%name
%_libdir/%name
%_datadir/%name
%_desktopdir/*%name.desktop
%_iconsdir/hicolor/48x48/apps/*.png
%_iconsdir/hicolor/scalable/apps/*.svg

%changelog
* Sat Apr 21 2012 Michael Shigorin <mike@altlinux.org> 2.0.2-alt1
- 2.0.2

* Fri Oct 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.4-alt1.qa1.1
- Rebuild with Python-2.7

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.5.4-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for soundconverter

* Fri Jan 21 2011 Michael Shigorin <mike@altlinux.org> 1.5.4-alt1
- 1.5.4 (thanks force@)
- dropped patch

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.4-alt1.1
- Rebuilt with python 2.6

* Sat Oct 17 2009 Michael Shigorin <mike@altlinux.org> 1.4.4-alt1
- adapted for Sisyphus (heavily cleaned up fedora package)
