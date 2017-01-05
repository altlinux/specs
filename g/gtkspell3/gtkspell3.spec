%def_disable static
%def_enable gtk_doc
%def_enable introspection

Name: gtkspell3
Version: 3.0.9
Release: alt1

Summary: On-the-fly spell checking for GtkTextView widgets, GTK+3 version
License: GPLv2+
Group: Graphical desktop/GNOME
Url: http://gtkspell.sourceforge.net/
# http://download.sourceforge.net/%name/%name-%version.tar.gz
# Source-git: git://git.code.sf.net/p/gtkspell/gtkspell
Source: %name-%version.tar


BuildRequires: gtk-doc intltool
BuildRequires: vala vala-tools libvala-devel
BuildRequires: gobject-introspection-devel
BuildRequires: gir(GObject) = 2.0 gir(GLib) = 2.0 gir(Gtk) = 3.0
BuildRequires: pkgconfig(glib-2.0) pkgconfig(gtk+-3.0) pkgconfig(enchant) pkgconfig(iso-codes)

%description
This is the GTK+3 version of the library.

GtkSpell provides word-processor-style highlighting and replacement of
misspelled words in a GtkTextView widget as you type.  Right-clicking a
misspelled word pops up a menu of suggested replacements.

%package -n lib%name
Summary: On-the-fly spell checking for GtkTextView widgets, GTK+3 version
Group: System/Libraries

%description -n lib%name
This is the GTK+3 version of the library.

GtkSpell provides word-processor-style highlighting and replacement of
misspelled words in a GtkTextView widget as you type.  Right-clicking a
misspelled word pops up a menu of suggested replacements.

%package -n lib%name-devel
Summary: Development files needed to build applications with %name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package provides files for developing applications
which use GtkSpell.

%package -n lib%name-devel-static
Summary: Static library needed to build static applications with %name
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
This package provides files for developing statically linked
applications which use GtkSpell.

%package -n lib%name-devel-doc
Summary: Development package for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: lib%name < %version

%description -n lib%name-devel-doc
Contains developer documentation for %name.

%package -n lib%name-gir
Summary: GObject introspection data for the %name library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the %name library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the %name library
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the %name library


%prep
%setup
sed -i 's,GTK_SPELL_CFLAGS,GTK_SPELL3_CFLAGS,' \
  gtkspell/Makefile.am

%build
%autoreconf
%configure \
	%{subst_enable static} \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	%{subst_enable introspection}

%make_build

%install
%makeinstall_std
%find_lang %name

%files -n lib%name -f %name.lang
%_libdir/*.so.*
%doc AUTHORS ChangeLog README

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*
%_datadir/vala/vapi/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/*

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/*.typelib

%files -n lib%name-gir-devel
%_girdir/*.gir
%endif

%changelog
* Thu Jan 05 2017 Vitaly Lipatov <lav@altlinux.ru> 3.0.9-alt1
- 3.0.9 (ALT bug #32524)
- fix doc subpackage name

* Tue Jun 14 2016 Alexey Shabalin <shaba@altlinux.ru> 3.0.8-alt1
- 3.0.8

* Tue Jul 01 2014 Alexey Shabalin <shaba@altlinux.ru> 3.0.6-alt1
- 3.0.6

* Wed Mar 27 2013 Alexey Shabalin <shaba@altlinux.ru> 3.0.2-alt1
- 3.0.2

* Tue Dec 11 2012 Alexey Shabalin <shaba@altlinux.ru> 3.0.0-alt1
- release 3.0.0
- move gtk-doc documentation to lib%name-devel-doc

* Tue Aug 23 2011 Ildar Mulyukov <ildar@altlinux.ru> 3.0.0-alt0.pre1
- 1st version of gtkspell3: GTK3 version of gtkspell

* Tue May 24 2011 Alexey Shabalin <shaba@altlinux.ru> 2.0.16-alt2
- rebuild for debuginfo

* Thu Dec 09 2010 Dmitry V. Levin <ldv@altlinux.org> 2.0.16-alt1
- Updated to 2.0.16.
- Fixed packaging.

* Wed Oct 14 2009 Vitaly Lipatov <lav@altlinux.ru> 2.0.15-alt1
- new version 2.0.15 (with rpmrb script)
- enchant support integrated since 2.0.13

* Mon Jan 07 2008 Vitaly Lipatov <lav@altlinux.ru> 2.0.11-alt1
- new version 2.0.11 (fix bug #13840), change Packager
- rename spec, cleanup spec, update buildreqs
- really disabled static library
- apply new enchant support patch

* Thu May 11 2006 Vital Khilko <vk@altlinux.ru> 2.0.4-alt6
- #9229

* Thu May 11 2006 Vital Khilko <vk@altlinux.ru> 2.0.4-alt5
- #9497
- removed ru and be package description

* Mon May 16 2005 Vital Khilko <vk@altlinux.ru> 2.0.4-alt4
- remove gcc3.2-c++ dependencies

* Wed Aug 04 2004 Vital Khilko <vk@altlinux.ru> 2.0.4-alt3
- replaced add_word_to_session() to add_word_to_personal() in enchant patch
- added ru and be package description

* Fri Jul 09 2004 Dmitry Vukolov <dav@altlinux.ru> 2.0.4-alt2
- NMU to fix incorrect i18n patch behaviour that interfered with applications'
  own internationalization (#4745)

* Thu Dec 11 2003 Vital Khilko <vk@altlinux.ru> 2.0.4-alt1
- added enchant support instead aspell
- added i18n support by VK@
- added russian and belarusian translation
