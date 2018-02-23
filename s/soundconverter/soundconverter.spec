Name: soundconverter
Version: 3.0.0
Release: alt1

Summary: A simple sound converter application for GNOME
License: GPLv3
Group: Sound

Url: https://github.com/kassoulet/soundconverter
Source: %name-%version.tar
Patch: drop-unity.patch
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildRequires: intltool
BuildRequires: python3-devel
BuildRequires: typelib(Gtk) = 3.0
BuildRequires: python3(gi)
BuildRequires: gir(Gst) = 1.0
BuildRequires: desktop-file-utils
Requires: typelib(Gtk) = 3.0
Requires: gst-plugins-ugly1.0
Requires: gst-plugins-good1.0
Requires: GConf

%description
A simple sound converter application for the GNOME environment.
It reads and writes anything the GStreamer library can.

%prep
%setup
%patch -p2

%build
mkdir -p m4
%autoreconf
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
%_datadir/appdata/*
%_desktopdir/*%name.desktop
%_iconsdir/hicolor/48x48/apps/*.png
%_iconsdir/hicolor/scalable/apps/*.svg

%changelog
* Fri Feb 23 2018 Anton Midyukov <antohami@altlinux.org> 3.0.0-alt1
- 3.0.0 beta 1

* Sat Sep 24 2016 Anton Midyukov <antohami@altlinux.org> 2.1.6-alt1
- 2.1.6

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
