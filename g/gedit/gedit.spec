%set_verify_elf_method unresolved=relaxed

%define ver_major 3.4
%define api_ver 3.0
%def_enable introspection
%def_enable python
%def_enable zeitgeist

Name: gedit
Version: %ver_major.2
Release: alt1

Summary: gEdit is a small but powerful text editor for GNOME
License: GPLv2
Group: Editors
Url: ftp://ftp.gnome.org/
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

%{?_enable_python:%py_provides gedit}

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz
Patch: %name-2.91.4-alt-settings.patch
Patch1: %name-2.91.6-alt-link.patch
Patch2: %name-2.91.8-alt-gir.patch

# From configure.ac
%define glib_ver 2.28.0
%define gtk_ver 3.3.15
%define gtksourceview_ver 3.4.1
%define peas_ver 1.1.3
%define enchant_ver 1.2.0

Requires: %name-data = %version-%release

BuildPreReq: rpm-build-gnome >= 0.6

# From configure.ac
BuildPreReq: intltool >= 0.40.0
BuildRequires: yelp-tools xmllint itstool
BuildPreReq: gtk-doc >= 1.0
BuildPreReq: libenchant-devel >= %enchant_ver
BuildPreReq: iso-codes-devel >= 0.35
BuildPreReq: libattr-devel
BuildPreReq: glib2-devel >= %glib_ver libgio-devel
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libpeas-devel >= %peas_ver
BuildPreReq: libgtksourceview3-devel >= %gtksourceview_ver
BuildRequires: desktop-file-utils
BuildRequires: gnome-common libxml2-devel libsoup-devel libSM-devel libICE-devel gsettings-desktop-schemas-devel
%{?_enable_zeitgeist:BuildRequires: libzeitgeist-devel}
%{?_enable_python:BuildRequires: python-module-pygobject3-devel}
%{?_enable_introspection:BuildPreReq: gobject-introspection-devel >= 0.10.2 libgtk+3-gir-devel libgtksourceview3-gir-devel}

%description
gEdit is the official text editor of the GNOME desktop environment.

While aiming at simplicity and ease of use, gedit is a powerful general
purpose text editor which features full support for UTF-8, configurable
highlighting for various languages and many other features making it a
great editor for advanced tasks.

%package data
Summary: Arch independent files for gEdit
Group: Editors
BuildArch: noarch

%description data
This package provides noarch data needed for gEdit to work.

%package devel
Group: Development/C
Summary: Libraries needed to develop plugins for gedit
Requires: %name = %version-%release
Requires: libgtksourceview-devel

%description devel
Libraries needed to develop plugins for gedit.

%package gir
Summary: GObject introspection data for the Gedit
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the Gedit

%package gir-devel
Summary: GObject introspection devel data for the Gedit
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the Gedit

%package devel-doc
Group: Development/C
Summary: Development documentation for gedit
Conflicts: %name < %version
BuildArch: noarch

%description devel-doc
This package contains documentation needed to develop plugins for gedit.

%define _libexecdir %_prefix/libexec
%define  gedit_pluginsdir %_libdir/gedit/plugins

%prep
%setup -q
%patch -p1 -b .settings
%patch1 -b .link
%patch2 -b .gir

rm -f data/gedit.desktop.in

%build
%autoreconf
%configure \
    %{subst_enable python} \
    --disable-schemas-compile \
    --disable-static \
    %{?_disable_introspection:--enable-introspection=no}

%make_build

%install
%make_install install DESTDIR=%buildroot

# additional mime types
desktop-file-install --dir %buildroot%_desktopdir \
	--add-mime-type=text/css \
	--add-mime-type=text/csv \
	--add-mime-type=text/english \
	--add-mime-type=text/plain \
	--add-mime-type=text/tab-separated-values \
	--add-mime-type=text/x-adasrc \
	--add-mime-type=text/x-bibtex \
	--add-mime-type=text/x-c++ \
	--add-mime-type=text/x-chdr \
	--add-mime-type=text/x-c++hdr \
	--add-mime-type=text/x-csharp \
	--add-mime-type=text/x-csrc \
	--add-mime-type=text/x-c++src \
	--add-mime-type=text/x-dsrc \
	--add-mime-type=text/x-fortran \
	--add-mime-type=text/x-gle \
	--add-mime-type=text/x-java \
	--add-mime-type=text/x-javascript \
	--add-mime-type=text/x-log \
	--add-mime-type=text/x-makefile \
	--add-mime-type=text/x-objcsrc \
	--add-mime-type=text/x-pascal \
	--add-mime-type=text/x-patch \
	--add-mime-type=text/x-perl \
	--add-mime-type=text/x-php \
	--add-mime-type=text/x-python \
	--add-mime-type=text/x-sql \
	--add-mime-type=text/x-sh \
	--add-mime-type=text/x-tcl \
	--add-mime-type=text/x-tex \
	%buildroot%_desktopdir/gedit.desktop

%find_lang --with-gnome %name

%files
%_bindir/*
%_libdir/%name/lib%name-private.so
%dir %_libdir/%name
%exclude %_libexecdir/%name/gedit-bugreport.sh
%dir %gedit_pluginsdir
%gedit_pluginsdir/*
%{?_enable_python:%python_sitelibdir/gi/overrides/Gedit.py*}

%exclude %gedit_pluginsdir/*.la
%exclude %_libdir/%name/lib%name-private.la

%files data -f %name.lang
%_datadir/%name/
%_desktopdir/*
%_datadir/dbus-1/services/org.gnome.gedit.service
%_mandir/man?/*
%config %_datadir/glib-2.0/schemas/*
%_datadir/GConf/gsettings/gedit.convert
%doc BUGS README AUTHORS NEWS

%files devel
%_includedir/*
%_pkgconfigdir/*

%files devel-doc
%_datadir/gtk-doc/html/%name

%if_enabled introspection
%files gir
%_libdir/girepository-1.0/Gedit-%api_ver.typelib
%files gir-devel
%_datadir/gir-1.0/Gedit-%api_ver.gir
%endif

%changelog
* Thu May 24 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Tue Apr 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Wed Jan 04 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.6-alt1
- 3.2.6
- zeitgeist support
- updated description
- split up noarch data in separate -data subpackage

* Fri Dec 09 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.5-alt1
- 3.2.5

* Thu Dec 08 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.4-alt1
- 3.2.4

* Tue Nov 15 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.3-alt1
- 3.2.3

* Mon Oct 31 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.2.1-alt1.1
- Rebuild with Python-2.7

* Sun Oct 16 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Sat Sep 10 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.5-alt1
- 3.1.5

* Fri Jul 01 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.6-alt1
- 3.0.6

* Thu Jun 16 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.5-alt1
- 3.0.5

* Wed Jun 01 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.4-alt1
- 3.0.4

* Wed May 25 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.3-alt1
- 3.0.3

* Tue May 03 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt2
- 3.0.2

* Tue May 03 2011 Yuri N. Sedunov <aris@altlinux.org> 2.30.4-alt2
- added a lot of additional mime-types to gedit.desktop (viy@)

* Tue Oct 19 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.4-alt1
- 2.30.4

* Mon Jun 21 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.3-alt1
- 2.30.3

* Mon Apr 19 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2

* Sun Apr 18 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Tue Mar 30 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Mon Mar 15 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.9-alt1
- 2.29.9

* Tue Mar 02 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.8-alt1
- 2.29.8

* Sat Dec 19 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.3-alt1
- 2.28.3

* Wed Nov 11 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt1
- 2.28.2

* Tue Nov 10 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Wed Sep 23 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Thu Sep 10 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.6-alt1
- 2.27.6

* Thu Jul 02 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.3-alt1
- 2.26.3

* Sun May 17 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2

* Mon Apr 13 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Mon Mar 16 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0
- updated buildreqs

* Sun Jan 11 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.3-alt1
- 2.24.3

* Sun Nov 23 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt1
- 2.24.2
- remove obsolete %%post{,un} scripts

* Tue Nov 04 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1
- devel-doc subpackage (noarch)

* Tue Sep 30 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt1
- 2.24.0

* Tue Jul 22 2008 Igor Zubkov <icesik@altlinux.org> 2.22.3-alt2
- apply fix from repocop for menus

* Mon Jun 02 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.3-alt1
- new version (2.22.3)

* Wed Apr 09 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt2
- moved settings from post-script to patch1 (#2279)
- fixed build with librarian

* Sun Mar 16 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- new version (2.22.0)

* Fri Feb 08 2008 Grigory Batalov <bga@altlinux.ru> 2.20.4-alt1.1
- Rebuilt with python-2.5.

* Mon Dec 03 2007 Alexey Shabalin <shaba@altlinux.ru> 2.20.4-alt1
- new version (2.20.4)
- add Packager
- add %%gconf2_install gedit-file-browser in %%post
- add %%preun section
- change %%find_lang

* Mon Jul 23 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.2-alt1
- new version (2.18.2)
- use macros from rpm-build-gnome
- the patch for aspell detection is obsolete

* Tue Jan 02 2007 Alexey Rusakov <ktirf@altlinux.org> 2.16.2-alt1
- new version 2.16.2 (with rpmrb script)

* Wed Sep 06 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.1-alt1
- new version
- updated dependencies

* Sun Sep 03 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.9-alt1
- new version (2.15.9)
- updated dependencies and files list
- turned on 'python' switch by default

* Wed May 31 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.3-alt1
- new version 2.14.3 (with rpmrb script)

* Sat Apr 15 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.2-alt1
- new version 2.14.2 (with rpmrb script)

* Sat Mar 25 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.1-alt1
- new version 2.14.1 (with rpmrb script)

* Sat Feb 25 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.91-alt1
- new version (2.13.91)
- revised buildreqs, cleaned up the spec, updated the aspell configure patch.
- removed Debian menu support.
- added python switch (non-functional yet due to lack of deps in Sisyphus).

* Tue Oct 25 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.1-alt2
- Fixed dependencies of the -devel subpackage.

* Tue Oct 04 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.1-alt1
- new version
- Urlified Source tag.

* Tue Sep 06 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.0-alt1
- 2.12.0
- Removed more excess buildreqs.

* Mon Sep 05 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.11.93-alt1
- 2.11.93
- Removed excess buildreqs.

* Mon Jun 13 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.3-alt1
- 2.10.3

* Mon Apr 04 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.2-alt1
- 2.10.2

* Tue Mar 08 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Wed Mar 02 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.7-alt1
- 2.9.7.

* Thu Oct 28 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.1-alt1
- 2.8.1

* Mon Sep 13 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.0-alt1
- 2.8.0

* Tue Jun 29 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Mon May 03 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Fri Mar 26 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Tue Mar 09 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.91-alt1
- 2.5.91

* Tue Feb 24 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.90-alt1
- 2.5.90

* Fri Jan 16 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.3-alt1
- 2.5.3

* Mon Oct 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Fri Sep 19 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt1
- 2.4.0
- patch from vk@ to enable belorussian spell support.

* Wed Aug 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.5-alt1
- 2.3.5

* Tue Jul 01 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.3-alt1
- 2.3.3

* Sat May 24 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.2-alt1
- 2.3.2

* Wed May 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.1-alt1
- 2.3.1
- syntax highlighting via GtkSourceView library.

* Thu Apr 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Thu Mar 13 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Tue Feb 04 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0.1-alt1
- 2.2.0.1

* Mon Jan 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Tue Jan 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.91-alt1
- 2.1.91

* Tue Jan 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.6-alt1
- 2.1.6

* Tue Dec 17 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.5-alt1
- 2.1.5

* Tue Dec 10 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.4-alt1
- 2.1.4

* Wed Nov 27 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.3-alt1
- 2.1.3

* Sat Nov 02 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.2.1-alt1
- 2.1.2.1

* Sat Oct 26 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.1-alt2
- Added some default settings in %%post via %%gconf2_set.

* Tue Oct 22 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Mon Oct 07 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.0.1-alt1
- 2.1.0.1

* Fri Sep 27 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0.5-alt1
- go to gnome2

* Thu Dec 27 2001 Stanislav Ievlev <inger@altlinux.ru> 0.9.6-alt3
- fixed default font
- spec cleanup
- added Belarusian translation

* Tue Apr 17 2001 AEN <aen@logic.ru> 0.9.6-alt2
- i18n printing support added (patch by Vlad Harchev from gnumeric)
* Mon Apr 9 2001 AEN <aen@logic.ru> 0.9.6-alt1
- new version in new environment

* Thu Nov 30 2000 AEN <aen@logic.ru>
- utf8 print patch

* Mon Nov 28 2000 AEN <aen@logic.ru>
- build for RE

* Tue Oct 24 2000 Renaud Chaillat <rchaillat@mandrakesoft.com> 0.9.3-1mdk
- new version 0.9.3
- moved plugins .so in normal package

* Wed Sep 20 2000 Renaud Chaillat <rchaillat@mandrakesoft.com> 0.9.1-1mdk
- new version

* Wed Sep  6 2000 Renaud Chaillat <rchaillat@mandrakesoft.com> 0.9.0-3mdk
- fixed langs
- further macroszification
- fixed icons
- fixed buildroot
- commented out .desktop
- fixed help

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.9.0-2mdk
- automatically added BuildRequires

* Mon Jul 24 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 0.9.0-1mdk
- release 0.9.0 (from helix)
- BM + macroszification

* Wed Jun 28 2000 Alexandre Dussart <adussart@mandrakesoft.com> 0.7.9-1mdk
- 0.7.9

* Tue Jun 20 2000 dam's <damien@mandrakesoft.com> 0.7.0-4mdk
- Corrected po file source name gz -> bz2.

* Sun Jun 18 2000 dam's <damien@mandrakesoft.com> 0.7.0-3mdk
- Re-include po files.

* Thu Jun 15 2000 Reinhard Katzmann <reinhard@suamor.de> 0.7.0-2mdk
- Several important files were not included in the package :-(

* Mon Jun 12 2000 dam's <damien@mandrakesoft.com> 0.7.0-1mdk
- updated from helix.
- clean up spec.

* Fri Apr 28 2000 Vincent Saugey <vince@mandrakesoft.com> 0.6.1-3mdk
- Add icons

* Thu Apr 20 2000 Vincent Saugey <vince@mandrakesoft.com> 0.6.1-2mdk
- Add menu entry

* Tue Mar 28 2000 Daouda Lo <daouda@mandrakesoft.com> 0.6.1-1mdk
- build release
- cleanup spec file .
- add post and postun sections (sometimes handy)
- upgrade from helix

* Sat Mar 25 2000 Daouda Lo <daouda@mandrakesoft.com> 0.5.5-2mdk
- fix group
- package should not be relocatable

* Wed Nov 17 1999 Lenny Cartier <lenny@mandrakesoft.com>
- v0.5.5

* Fri Aug 27 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- get latest translation files from CVS

* Mon Jul 12 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- bzip manpage

* Mon Jul 05 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 0.5.4 from CVS :

	* README: Upped version number to 0.5.4. Also updated various parts
	  of the file to reflect current features and other related items.

	* README.plugins, INSTALL, makeconfig.pl: Upped version number to 0.5.4,
	  in preperation of release.

	* NEWS: Added Announce message for 0.5.4.

	* Erk! i havent been keeping this up to date.. ahwell.. here goes..

	* gE_document.[ch]: (gE_window_new) Make it a GnomeApp arg, instead
	  of a GtkWidget.. much nicer.. And commented out the call to
	  gE_set_menu_toggle_states, gnome-libs 1.0.11 doenst seem to like it..

	* gE_mdi.c: various improvements.. (iirc ;)

	* gE_prefs.[ch]: Added a "close doc" flag..

	* gE_prefs_box.c: Moved the print tab to a Document tab, and added a
	  option for what to do when the last documnet of the window is closed..
	  right now only the first option works.. this corresponds with the
	  flag, above.

	* commands.c: Made the close callback check the "close doc" flag, and
	  it will either open a new doc if there arent any more, or print hola! to
	  stdout.. as i said, its not fully implemented yet.

* Tue May 11 1999 Bernhard Rosenkränzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sat Feb 06 1999 Michael Johnson <johnsonm@redhat.com>
- Cleaned up a bit for Red Hat use

* Thu Oct 22 1998 Alex Roberts <bse@dial.pipex.com>
- First try at an RPM
