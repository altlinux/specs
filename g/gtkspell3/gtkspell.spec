Name: gtkspell3
Version: 3.0.0
Release: alt0.pre1

Summary: On-the-fly spell checking for GtkTextView widgets, GTK+3 version
License: GPLv2+
Group: Graphical desktop/GNOME
Url: http://gtkspell.sourceforge.net/
# http://download.sourceforge.net/%name/%name-%version.tar.gz
Source: %name-%version.tar

%def_disable static

# Automatically added by buildreq on Tue Aug 23 2011
# optimized out: docbook-dtds docbook-style-xsl fontconfig fontconfig-devel glib2-devel libatk-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libpango-devel perl-XML-Parser pkg-config xml-common xsltproc
BuildRequires: gtk-doc intltool libenchant-devel libgtk+3-devel

%description
This is the GTK+3 version og the library.

GtkSpell provides word-processor-style highlighting and replacement of
misspelled words in a GtkTextView widget as you type.  Right-clicking a
misspelled word pops up a menu of suggested replacements.

%package -n lib%name
Summary: On-the-fly spell checking for GtkTextView widgets, GTK+3 version
Group: System/Libraries

%description -n lib%name
This is the GTK+3 version og the library.

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

%prep
%setup

%build
%configure %{subst_enable static}
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
%doc %_datadir/gtk-doc/html/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%changelog
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
