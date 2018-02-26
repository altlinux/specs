Name: ario
Version: 1.5.1
Release: alt2
Summary: Ario is a GTK2 client for MPD

Group: Sound
License: GPLv2
Url: http://ario-player.sourceforge.net/
Source0: %name-%version.tar
Patch1: ario-alt-glib2-2.32.0.patch

BuildRequires: intltool libavahi-glib-devel libcurl-devel libglade-devel libnotify-devel libsoup-devel libtag-devel libgcrypt-devel libgnutls-devel libxml2-devel libdbus-glib-devel libunique-devel libmpdclient-devel
BuildRequires: desktop-file-utils

%description
Ario is a GTK2 client for MPD (Music player daemon).
The interface used to browse the library is inspired 
by Rhythmbox but Ario aims to be much lighter and faster.

%prep
%setup -q
%patch1 -p2

%build
autoreconf -fisv
%configure
%make_build

%install
%makeinstall_std
%find_lang %name
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Player \
	%buildroot%_desktopdir/ario.desktop

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%_datadir/%name
%_desktopdir/%name.desktop
%_libdir/%name
%_bindir/%name
%_liconsdir/%name.png
%_miconsdir/%name.png
%_niconsdir/%name.png
%_iconsdir/hicolor/*/apps/*.png
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog
* Thu Apr 19 2012 Aeliya Grevnyov <gray_graff@altlinux.org> 1.5.1-alt2
- fixed build with new glib2

* Thu Jul 07 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 1.5.1-alt1
- new version 1.5.1

* Thu Jul 07 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 1.5-alt1
- new version 1.5

* Wed May 18 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.3-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for ario
  * postclean-03-private-rpm-macros for ([not specified])
  * postclean-05-filetriggers for ([not specified])

* Tue Apr 19 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3-alt2
- fix build

* Mon May 25 2009 Lebedev Sergey <barabashka@altlinux.org> 1.3-alt1
- new version 1.3 from upstream
- fixed build with new automake-1.11

* Wed May 13 2009 Lebedev Sergey <barabashka@altlinux.org> 1.2.2-alt1
- initial build
