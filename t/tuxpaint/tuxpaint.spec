Name: tuxpaint
Version: 0.9.21
Release: alt3

Summary: A drawing program for young children
Summary(ru_RU.UTF8): Простая детская программа для рисования
License: GPL
Group: Graphics
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

Url: http://www.tuxpaint.org/
Source: %name-%version.tar.gz
Source1: %name.desktop
Patch1: %name-0.9.19-default-size.patch

BuildRequires: libSDL-devel >= 1.2.4 libSDL_image-devel libSDL_mixer-devel libSDL_pango-devel libSDL_ttf-devel
BuildRequires: libpng-devel zlib-devel gettext librsvg-devel libpaper-devel libfribidi-devel

%description
"Tux Paint" is a drawing program for young children.
It provides a simple interface and fixed canvas size,
and provides access to previous images using a thumbnail
browser (e.g., no access to the underlying file-system).

Unlike popular drawing programs like "The GIMP," it has a
very limited tool-set. However, it provides a much simpler
interface, and has entertaining, child-oriented additions
such as sound effects.

%description -l ru_RU.UTF8
"Tux Paint" является детской программой для рисования.
Она предоставляет простой интерфейс и фиксированый размер холста,
и позволяет просматривать изображениям, используя "thumbnail" браузер
(т.е., нет необходимости иметь доступ к основной файловой системе).

В отличие от популярных программ для рисования таких как "The GIMP",
она имеет очень ограниченный набор инструментов. Однако, это обеспечивает
намного более простой интерфейс, и имеет интересные, ориентированные на 
ребенка дополнения, типа звуковых эффектов.

Входит в состав GCompris. Также может использываться отдельно

%package devel
Summary: Development shared library for %name
Group: Development/C
Requires: %name = %version-%release
%description devel
Development shared library for %name

%prep
%setup -n %name-%version
%patch1 -p1

subst "s|/share/doc/tuxpaint|/share/doc/tuxpaint-%version|g" Makefile
subst "s|\$(PREFIX)/lib|%_libdir|g" Makefile
subst "s|< \$(PLUGIN_LIBS)|< \$(PLUGIN_LIBS) \$(SDL_LIBS) \$(PNG)|g" Makefile
sed -i '/^linux_ARCH_LINKS/s/\$(FRIBIDI_LIB)/\$(FRIBIDI_LIB) \$(PNG)/g' Makefile
sed -i 's|^\(CFLAGS\).*=\(.*\))|\1 = -g \2|' Makefile

%build
%make PREFIX=/usr MAGIC_PREFIX=%_libdir/%name/plugins

%install
%make install PREFIX=/usr \
		PKG_ROOT=%buildroot \
		MAGIC_PREFIX=%buildroot%_libdir/%name/plugins \
    X11_ICON_PREFIX=%buildroot%_datadir/pixmaps/ \
    GNOME_PREFIX=/usr \
    KDE_PREFIX="" \
    KDE_ICON_PREFIX=/usr/share/icons \
    DEVDOC_PREFIX=%buildroot%_defaultdocdir/%name-devel-%version

%find_lang %name

# Add tuxpaint.desktop
install -d %buildroot%_datadir/applications
cp -aRf %SOURCE1 %buildroot%_datadir/applications/

%files -f %name.lang
# bin files
%_bindir/tuxpaint*
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/%name.conf
%_libdir/%name


# docs files
%_docdir/%name-%version
%_man1dir/tuxpaint*
%exclude %_docdir/%name-%version/Makefile

# data files
%_datadir/%name
%_datadir/applications/*
%_iconsdir/hicolor/*/*/*

# menu
%_datadir/pixmaps/*

%files devel
%_bindir/tp-magic-config
%_includedir/%name
%_docdir/%name-devel-%version
%exclude %_docdir/%name-devel-%version/Makefile
%_man1dir/tp-magic-config*

%changelog
* Mon May 21 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.21-alt3
- Fix DSO linking

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.21-alt1.2.1
- Rebuild with Python-2.7

* Wed Mar 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.21-alt1.2
- Rebuilt for debuginfo

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.21-alt1.1
- Rebuilt with python 2.6

* Tue Jun 30 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.21-alt1
- Update to 0.9.21

* Sat Nov 29 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.20-alt3
- Remmove depricated update-menus

* Tue Aug 26 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.20-alt2
- Fix #16854

* Wed Jul 16 2008 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.9.20-alt1
- Update to 0.9.19

* Thu Apr 24 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.19-alt2
- Add tuxpaint-0.9.19-default-size.patch from mex3@

* Thu Mar 13 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.19-alt1
- Update to 0.9.19
- Remove exclude %_libdir/%name/plugins/kalidescope*
- Add exclude %_docdir/%name-%version/Makefile

* Fri Nov 30 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.18-alt2
- Fix Categories in tuxpaint.desktop (#13550)

* Thu Nov 29 2007 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.9.18-alt1
- Update to 0.9.18
- Add subpackage devel
- Fixed #13319
- Add BuildRequires: libSDL_pango-devel

* Wed Oct 31 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.17-alt2
- Fix build on x86_64
- Remove BuildRequires: esound kdelibs
- Add options for make and make install

* Tue Oct 30 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.17-alt1
- Update to 0.9.17
- Add BuildRequires: librsvg-devel libpaper-devel

* Mon Oct 23 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.9.16-alt0
- Update to 0.9.16

* Fri Dec 30 2005 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.9.15-alt3.b
- Add tuxpaint.desktop

* Mon Nov 28 2005 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.9.15-alt2.b
- Update to 0.9.15b

* Fri Sep 09 2005 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.9.15-alt1.cvs20050909
- built for ALT Linux
