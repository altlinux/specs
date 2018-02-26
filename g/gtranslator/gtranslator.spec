%define ver_major 2.91
%define api_ver 3.0
%def_enable introspection

Name: gtranslator
Version: %ver_major.5
Release: alt1.1

Summary: A GNOME po file editor with many bells and whistles.
License: GPL
Group: Development/Tools
URL: http://gtranslator.sourceforge.net
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
Patch: %name-2.91.5-alt-pkgconfig.patch

Requires: libgda4-sqlite

%define gtk_ver 3.4.0
%define gtkspell_ver 3.0

BuildRequires: gnome-common gnome-doc-utils gtk-doc intltool libgtk+3-devel >= %gtk_ver
BuildRequires: libgda4-devel libgdl3-devel libgtksourceview3-devel
BuildRequires: librarian libsoup-devel libpeas-devel
BuildRequires: gsettings-desktop-schemas-devel iso-codes-devel
BuildRequires: libgdict-devel libgtkspell3-devel >= %gtkspell_ver libjson-glib-devel
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgtk+3-gir-devel libgtksourceview3-gir-devel}

%description
gtranslator is a quite comfortable gettext po/po.gz/(g)mo files editor
for the GNOME 3.x platform with many features. It's evolving quite fast
and many useful functions are already implemented; gtranslator aims to
be a very complete editing environment for translation issues within the
GNU gettext/GNOME desktop world.

%package devel
Summary: %name header files
Group: Development/C
Requires: %name = %version-%release

%description devel
This package provides header files needed for build %name plugins.

%package devel-doc
Summary: %name development documentation
Group: Development/C
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
This package contains documentation needed to develop %name plugins.

%set_typelibdir %_libdir/%name/girepository-1.0

%prep
%setup -q
%patch

%build
gnome-doc-prepare -f
%autoreconf
%configure \
	--disable-schemas-compile \
	--disable-static \
	--with-gda=4.0
%make_build

%install
%make DESTDIR=%buildroot install

find %buildroot%_libdir/%name -name \*.la -delete

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_libdir/%name/
%_datadir/%name/
%_datadir/glib-2.0/schemas/*.xml
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.*
%_man1dir/%name.1*
%doc AUTHORS NEWS README THANKS

%files devel
%_includedir/%name-%api_ver/%name/
%_pkgconfigdir/%name.pc
%_datadir/gtk-doc/html/%name/

%changelog
* Tue Jun 12 2012 Yuri N. Sedunov <aris@altlinux.org> 2.91.5-alt1.1
- used %%set_typelibdir macros

* Thu Jun 07 2012 Yuri N. Sedunov <aris@altlinux.org> 2.91.5-alt1
- 2.91.5

* Sat Oct 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.9.12-alt1
- 1.9.12

* Fri May 14 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.9.11-alt1
- 1.9.11

* Wed Apr 21 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.9.10-alt1
- 1.9.10

* Sun Feb 21 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.9.9-alt1
- 1.9.9

* Thu Feb 11 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.9.8-alt1
- 1.9.8

* Mon Feb 01 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.9.7-alt1
- 1.9.7

* Wed Dec 23 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.9.6-alt2
- rebuild with libgdl 2.28.2

* Tue Aug 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.9.6-alt1
- 1.9.6

* Fri Jul 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.9.5-alt3
- updated translation

* Tue Jun 09 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.9.5-alt2
- updated build dependencies

* Wed Jun 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.9.5-alt1
- initial relese

