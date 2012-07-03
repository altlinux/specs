%define ver_major 3.4
# need glade3 > 3.11.0 (for gtk+3)
%def_disable glade

Name: anjuta
Version: %ver_major.2
Release: alt1
Summary: GNOME IDE for C and C++
Group: Development/GNOME and GTK+
License: GPLv2+
Url: http://anjuta.org/

Requires: autogen >= 5.0 libgda4-sqlite
Obsoletes: %{name}2 < %version lib%name libgnome-build <= 2.26
Obsoletes: %{name}2-docs < %version %{name}2-core < %version %{name}2-project-templates < %version
Provides: %{name}2 = %version-%release lib%name
Provides: %{name}2-docs = %version-%release %{name}2-core = %version-%release %{name}2-project-templates = %version-%release

Source: %name-%version.tar
#Patch: %name-%version-%release.patch

BuildRequires: dconf flex gcc-c++ autogen gnome-common gtk-doc intltool
BuildRequires: gobject-introspection-devel >= 0.6.7
BuildRequires: libgjs-devel
BuildRequires: glib2-devel >= 2.28.0 libgio-devel
BuildRequires: libgtk+3-devel >= 3.0.0 libgtk+3-gir-devel
BuildRequires: libgdk-pixbuf-devel >= 2.0.0 libgdk-pixbuf-gir-devel
BuildRequires: libxml2-devel >= 2.4.23
BuildRequires: libgdl3-devel >= 2.91.4
BuildRequires: libvte3-devel >= 0.27.6
BuildRequires: libdevhelp-devel >= 3.0.0
%{?_enable_glade:BuildRequires: libgladeui-devel >= 3.9.0}
BuildRequires: libgtksourceview3-devel >= 2.91.8
BuildRequires: libvala-devel vala
BuildRequires: python-devel python-modules-compiler
BuildRequires: libgda4-devel >= 4.2.0 libsqlite3-devel
BuildRequires: libXrender-devel libXext-devel
BuildRequires: libgraphviz-devel
BuildRequires: perl-devel perl-Locale-gettext

%description
Anjuta DevStudio is a versatile Integrated Development Environment (IDE)
for GNOME Desktop Environment. It features a number of advanced
programming facilities. These include project management, application and
class wizards, an on-board interactive debugger, a powerful source editor,
syntax highlighting, Intellisense-like autocompletion, symbol navigation,
integration with version control systems and a GUI designer, and other
tools.

%package devel
Summary: Development files for Anjuta
Group: Development/Other
Requires: %name = %version-%release
Obsoletes: %{name}2-devel-doc < %version
Obsoletes: %{name}2-devel < %version
Provides: %{name}2-devel-doc
Provides: %{name}2-devel

%description devel
Libraries and header files necessary to develop and build Anjuta plugins.

%package cvs
Summary: CVS support in Anjuta
Group: Development/GNOME and GTK+
Requires: %name = %version-%release
Requires: cvs
Obsoletes: %{name}2-cvs < %version
Provides: %{name}2-cvs

%description cvs
CVS support plugin for Anjuta DevStudio IDE.

%package glade
Summary: Glade support in Anjuta
Group: Development/GNOME and GTK+
Requires: %name = %version-%release
Obsoletes: %{name}2-glade < %version
Provides: %{name}2-glade

%description glade
Valgrind support plugin for Anjuta DevStudio IDE.

%package devhelp
Summary: DevHelp integration plugin for Anjuta
Group: Development/GNOME and GTK+
Requires: %name = %version-%release
Obsoletes: %{name}2-devhelp < %version
Provides: %{name}2-devhelp

%description devhelp
This plugin lets you run DevHelp from inside Anjuta.

%define schemasdir %_datadir/glib-2.0/schemas
%define anjuta_libdir %_libdir/%name
%define anjuta_datadir %_datadir/%name
%define anjuta_pixmapsdir %_pixmapsdir/%name

%add_findprov_lib_path %anjuta_libdir
%add_findreq_skiplist %anjuta_datadir/project/python/src/*.py
%add_findreq_skiplist %anjuta_datadir/project/pygtk/src/*.py

%prep
%setup -q
#%patch -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
    --disable-static \
    --disable-schemas-install \
    --disable-scrollkeeper \
    --disable-packagekit \
    --enable-plugin-devhelp \
%if_enabled glade
    --enable-plugin-glade \
%else
    --disable-plugin-glade \
%endif
    --enable-plugin-sourceview \
    --disable-plugin-subversion \
    --enable-gtk-doc

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang --with-gnome --output=global.lang %name %name-manual %name-build-tutorial %name-faqs

%files -f global.lang
%doc AUTHORS NEWS README THANKS TODO FUTURE ROADMAP doc/ScintillaDoc.html
%_bindir/*
%_libdir/*.so.*
%_typelibdir/*.typelib
%anjuta_libdir/
%exclude %anjuta_libdir/*.la
%exclude %anjuta_libdir/*cvs*
%if_enabled glade
%exclude %anjuta_libdir/*glade*
%endif
%exclude %anjuta_libdir/*devhelp*

%dir %anjuta_datadir
%anjuta_datadir/welcome.txt
%anjuta_datadir/layout.xml
%anjuta_datadir/languages.xml
%anjuta_datadir/snippets-global-variables.xml
%anjuta_datadir/snippets.anjuta-snippets
%anjuta_datadir/sources.list
%anjuta_datadir/class-templates/
%anjuta_datadir/build/
%anjuta_datadir/profiles/
%anjuta_datadir/gdb.init
%anjuta_datadir/tables.sql

%dir %anjuta_datadir/glade
%anjuta_datadir/glade/*.png
%anjuta_datadir/glade/*.ui
%exclude %anjuta_datadir/glade/*cvs*.ui

%anjuta_datadir/tools

%dir %anjuta_datadir/ui
%anjuta_datadir/ui/*.ui
%anjuta_datadir/ui/*.xml
%exclude %anjuta_datadir/ui/*cvs*.ui
%exclude %anjuta_datadir/ui/*devhelp*.ui

%anjuta_datadir/anjuta_project.template
%anjuta_datadir/project

%schemasdir/org.gnome.anjuta*gschema.xml
%exclude %schemasdir/org.gnome.anjuta.cvs.gschema.xml

%_iconsdir/hicolor/*/apps/anjuta.*
%_iconsdir/gnome/*/*/*
%anjuta_pixmapsdir/
%exclude %anjuta_pixmapsdir/*cvs*
%exclude %anjuta_pixmapsdir/*glade*
%exclude %anjuta_pixmapsdir/*devhelp*

%_desktopdir/%name.desktop
%_datadir/mime/packages/*

%_man1dir/*

%files devel
%_includedir/libanjuta*
%_libdir/*.so
%_girdir/*.gir
%_pkgconfigdir/*.pc
%_datadir/gtk-doc/html/lib%name

%files cvs
%anjuta_libdir/*cvs*
%exclude %anjuta_libdir/lib*.la
%anjuta_datadir/ui/*cvs*.ui
%anjuta_datadir/glade/*cvs*.ui
%schemasdir/org.gnome.anjuta.cvs.gschema.xml
%anjuta_pixmapsdir/*cvs*

%if_enabled glade
%files glade
%anjuta_libdir/*glade*
%exclude %anjuta_libdir/lib*.la
%_libdir/glade3/modules/libgladeanjuta.so
%_datadir/glade3/catalogs/anjuta-glade.xml
%exclude %_libdir/glade3/modules/*.la
%anjuta_pixmapsdir/*glade*
%endif

%files devhelp
%anjuta_libdir/*devhelp*
%_pixmapsdir/%name/*devhelp*
%exclude %anjuta_libdir/lib*.la
%exclude %anjuta_pixmapsdir/*devhelp*

%changelog
* Thu May 17 2012 Alexey Shabalin <shaba@altlinux.ru> 3.4.2-alt1
- 3.4.2

* Sat Mar 31 2012 Alexey Shabalin <shaba@altlinux.ru> 3.4.0-alt1
- 3.4.0

* Mon Nov 07 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.2.1-alt1.1
- Rebuild with Python-2.7

* Wed Oct 26 2011 Alexey Shabalin <shaba@altlinux.ru> 3.2.1-alt1
- 3.2.1

* Thu Sep 15 2011 Alexey Shabalin <shaba@altlinux.ru> 3.0.3-alt1
- 3.0.3
- rename anjuta2 to anjuta

* Sat Jan 15 2011 Valery Inozemtsev <shrek@altlinux.ru> 2.32.1.1-alt1
- 2.32.1.1

* Mon Nov 15 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.32.1-alt1
- 2.32.1

* Fri Oct 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.32.0-alt1
- 2.32.0

* Mon May 03 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.30.1-alt1
- 2.30.1

* Wed Mar 31 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.30.0-alt1
- 2.30.0

* Sun Feb 21 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.28.2-alt2
- fixed crash on create new project

* Sun Feb 21 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.28.2-alt1
- 2.28.2

* Sat Dec 19 2009 Alexey Rusakov <ktirf@altlinux.org> 2.28.1-alt1
- Switched to upstream branch 2.28.
- No more valgrind, class-inheritance and sample1 plugins in the main
  tree; upstream has moved them to a separate repository (anjuta-extras);
  upstream has also killed Kenny^W^Wmoved Scintilla editor from the main
  tree to anjuta-extras.
- Updated buildreqs and files list.
- Patch for compilation with NLS and underlinkage patch went upstream.

* Mon Nov 02 2009 Alexey Rusakov <ktirf@altlinux.org> 2.26.2.1-alt2.3
- Fixed some unowned files warnings issued by the install test of girar.
- Rebuilt with new libbfd.

* Mon Oct 26 2009 Alexey Rusakov <ktirf@altlinux.org> 2.26.2.1-alt2.2
- Rebuilt with new libdevhelp.

* Thu Aug 27 2009 Alexey Rusakov <ktirf@altlinux.org> 2.26.2.1-alt2.1
- Rebuilt with libbfd from newer binutils.

* Mon Aug 17 2009 Alexey Rusakov <ktirf@altlinux.org> 2.26.2.1-alt2
- Removed obsolete BuildRequires: libgnome-build.

* Mon Jun 22 2009 Alexey Rusakov <ktirf@altlinux.org> 2.26.2.1-alt1
- New version (2.26.2.1).
- BuildPreReq replaced with BuildRequires(pre) for rpm-build- packages.
- Moved 'Obsoletes: libgnome-build' to -core subpackage to avoid file
  conflicts when dist-upgrading without anjuta2 package installed.

* Wed Jun 10 2009 Alexey Rusakov <ktirf@altlinux.org> 2.26.2-alt3
- Updated from stable git branch (incl. Ukranian translation).
- Switched DevHelp and class inheritance plugins back on.

* Tue Jun 02 2009 Alexey Rusakov <ktirf@altlinux.org> 2.26.2-alt2.1
- Rebuild with new libvte.

* Tue May 26 2009 Alexey Rusakov <ktirf@altlinux.org> 2.26.2-alt2
- Merged with ldv's rebuild of 2.26.0.1.

* Tue May 26 2009 Alexey Rusakov <ktirf@altlinux.org> 2.26.2-alt1
- New version (2.26.2).
- Moved to git.
- Fixed building with Automake 1.11 (multiple install targets issue).

* Fri May 01 2009 Dmitry V. Levin <ldv@altlinux.org> 2.26.0.1-alt2.1
- NMU: rebuilt with libbfd-2.19.51.0.2.so.

* Thu Apr 16 2009 Alexey Rusakov <ktirf@altlinux.org> 2.26.0.1-alt2
- Temporarily disabled devhelp plugin (to allow a new libwebkit to pass to
  Sisyphus).

* Fri Apr 10 2009 Alexey Rusakov <ktirf@altlinux.org> 2.26.0.1-alt1
- New version (2.26.0.1).
- %name-docs subpackage is made noarch (thanks to repocop for a reminder).
- Enabled building DevHelp plugin back.
- Enabled building gtk-doc files.
- Build libgda4 plugin unconditionally (upstream no more gives an option).
- Disabled Graphviz plugin temporarily.
- Updated buildreqs, files list.
- Bzipped the ChangeLog (thanks to repocop for a hint).
- Added a patch to fix underlinkage in several places (GNOME Bug 578690).
- gnome-build module has been merged into Anjuta codebase.
- Fixed a bug that rendered anjuta2-core unable to install without
  anjuta2-cvs.

* Mon Dec 22 2008 Alexey Rusakov <ktirf@altlinux.org> 2.24.2-alt5
- Moved user documentation from -core to a separate package (-docs).
- Now anjuta2-core, not anjuta2, conflicts with Anjuta 1 (thanks to repocop
  for a hint).

* Thu Dec 18 2008 Alexey Rusakov <ktirf@altlinux.org> 2.24.2-alt4
- Fixed the conflict with Anjuta 1, fixing ALT Bug 18242.

* Mon Dec 15 2008 Alexey Rusakov <ktirf@altlinux.org> 2.24.2-alt3
- Merged in changes of aris@ that were accidentally overwritten.

* Mon Dec 15 2008 Alexey Rusakov <ktirf@altlinux.org> 2.24.2-alt2
- Fix .desktop file (thanks to repocop).
- Throw .la files from all packages.
- Switched on building with SMP.
- Fixed up dependencies of subpackages (s/%name/%name-core/).
- Updated buildreqs.
- Development documentation has moved from -devel to -devel-doc, thus
  fixing repocop whining about big /usr/share in arch-dependent package.
- Moved plugin-related pixmaps to corresponding subpackages.

* Sun Dec 14 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt1
- new version
- removed obsolete %%post{,un} scripts
- added lost postun/preun scripts for schemas {un,}install, updated reqs
- don't rebuilt documentation
- temporarily disabled devhelp plugin -- not ready for devhelp-0.22

* Mon Nov 10 2008 Alexey Rusakov <ktirf@altlinux.org> 2.24.1-alt1
- New version (2.24.1).
- Moved project templates and Scintilla editor properties (second largest
  noarch parts of anjuta2 package) to a separate noarch package.
- Added Packager tag.
- Added a workaround for missing Subversion configuration tools
  (svn-config or a .pc file).
- %name is now a virtual package, files moved to %name-core. Expect
  further moving of files out of -core to separate plugin subpackages.

* Wed Jun 18 2008 Alexey Rusakov <ktirf@altlinux.org> 2.4.2-alt1
- New version (2.4.2).
- Dropped the patch for anjuta-tags location (fixed upstream).
- Added BuildRequires on libldap-devel as a temporary workaround.

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt1.qa1
- NMU (by repocop), the following fixes applied:
 * update_menus for anjuta2

* Wed Dec 26 2007 Alexey Rusakov <ktirf@altlinux.org> 2.3.1-alt1
- New version (2.3.1).
- No need in autogen-devel, autogen is enough.
- Use license macro.
- Fix location of anjuta-tags (it goes to /usr/share, being an ELF binary).
- Removed a workaround for PKG_PATH in configure.in.
- Updated the files list.

* Mon Nov 05 2007 Alexey Rusakov <ktirf@altlinux.org> 2.3.0-alt1
- New version (2.3.0).
- Added (disabled) switch for libgda-3.0 for symbol DB plugin. There's no
  libgda3 in Sisyphus yet however, and there's no subpackage for this
  plugin either.

* Fri Oct 26 2007 Alexey Rusakov <ktirf@altlinux.org> 2.2.2-alt1
- new version (2.2.2)
- updated dependencies

* Sat Sep 22 2007 Alexey Rusakov <ktirf@altlinux.org> 2.2.1-alt1.1
- Rebuilt with new libgladeui.

* Fri Sep 07 2007 Alexey Rusakov <ktirf@altlinux.org> 2.2.1-alt1
- new version 2.2.1 (with rpmrb script)

* Wed Sep 05 2007 Alexey Rusakov <ktirf@altlinux.org> 2.2.0-alt1.1
- rebuild with new libgnome-build.

* Sun Jul 01 2007 Alexey Rusakov <ktirf@altlinux.org> 2.2.0-alt1
- new version (2.2.0)
- since Anjuta 1.2 and Anjuta 2 can't exist together, the executable's name
  from now on is anjuta, the former anjuta2 is a symlink to anjuta for legacy.
- added a workaround for incorrect usage of PKG_PATH macro in configure.in

* Mon May 21 2007 Alexey Rusakov <ktirf@altlinux.org> 2.1.3-alt2
- fixed typos (ALT Bug #11829)

* Fri May 11 2007 Alexey Rusakov <ktirf@altlinux.org> 2.1.3-alt1
- new version (2.1.3)
- updated dependencies
- linking patch from GNOME Bug #424121 went upstream.

* Mon May 07 2007 Alexey Rusakov <ktirf@altlinux.org> 2.1.2-alt2
- tell rpm-build that we have library dependencies in %%_libdir/anjuta
  (thanks to ldv@).

* Tue Apr 03 2007 Alexey Rusakov <ktirf@altlinux.org> 2.1.2-alt1
- new version (2.1.2)
- updated dependencies
- removed the clumsy workaround that once allowed anjuta 1.2 and anjuta 2 to
  co-exist - it's no more working, and for some time. Anjuta 1.2 stays in the
  repository, however, so the package name stays anjuta2.
- updated the patch that fixes linking, with the one proposed in
  GNOME Bug #424121
- enabled Glade3 plugin and (this time, for real) Valgrind plugin.
- forbid unpackaged files, updated files list.

* Mon Jan 22 2007 Alexey Rusakov <ktirf@altlinux.org> 2.0.2-alt2
- removed many Requires on library packages, let them be generated.
- dropped explicit dependency on libneon[-devel], because now we have several
  libneon-devel packages in Sisyphus, and subversion depends on another version
  than the one mentioned in this specfile. Better let subversion-devel choose
  appropriate libneon-devel.
- spec cleanup, updated buildreqs

* Wed May 17 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.0.2-alt1
- new version (2.0.2)
- fixed linking (thanks to damir@ for the patch)
- updated dependencies.
- class-inheritance plugin has been made optional ('graphviz' switch) and
  is disabled (waiting for Graphviz 2.6 to reach Sisyphus).

* Sun Apr 16 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.0.1-alt6
- added 'debug' switch.
- fixed crashing on start.

* Mon Apr 10 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.0.1-alt5
- fixed linking with --as-needed

* Sat Mar 04 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.0.1-alt4
- Updated buildreqs for X.org 7.0
- Removed Debian menu support
- Spec cleanup
- fixed double inclusion of subversion and class-inheritance plugins.

* Thu Oct 06 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.0.1-alt3
- Fixed Requires.

* Mon Oct 03 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.0.1-alt2
- Updated from CVS, fixing Bug #8077.
- Updated requirements from configure.in
- Urlified the source tag to favor etersoft-build-utils.

* Thu Jun 30 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.0.1-alt1
- New upstream version.
- Removed excess dependencies from the spec.

* Sat Jun 04 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.0.0-alt3
- Updated from CVS.
- Fixed Bug #6995.

* Sun May 22 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.0.0-alt2
- Sources updated from CVS.
- Several fixes and improvements in the spec (including Bug #6873).

* Fri May 13 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.0.0-alt1
- 2.0.0 release.
- The temporary name of the package is anjuta2 (this concerns all binaries
  and directories, but not libanjuta), to let anjuta-1.2 and anjuta-2.0
  coexist.

* Tue Feb 22 2005 Vladimir Lettiev <crux@altlinux.ru> 1.2.2-alt6
- version from cvs (2005-02-22)
- a lot of changes in spec

* Fri Jul 23 2004 Vital Khilko <vk@altlinux.ru> 1.2.2-alt5
- added icon for Anjuta submenu
- move anjuta_updatetags, tm_globals_tags to /usr/lib/anjuta
- remove /var/cache/anjuta only when package removed (not upgraded)

* Thu Jul 15 2004 Vital Khilko <vk@altlinux.ru> 1.2.2-alt4
- apply --disable-static to configure.
- do not list /usr/share/locale, /usr/share/omf/* and 
  /usr/share/gnome/help/* in %files (find-lang --with-gnome 
  treat these directories to find language specific files).
- use freedesktop2menu.pl to create menu file.
  Remove unusual icons from src.rpm
- remove unusual requires.
- updated buildreqs.
- other minor fixes, cleanups and .spec optimizatiions.
- fix #4766 (patch1)

* Thu May 20 2004 Vital Khilko <vk@altlinux.ru> 1.2.2-alt3
- minor fixes

* Wed Apr 28 2004 Vital Khilko <vk@altlinux.ru> 1.2.2-alt2
- fixed #3944

* Thu Apr 15 2004 Vital Khilko <vk@altlinux.ru> 1.2.2-alt1
- new version
- added menu entry

* Mon Feb 16 2004 Vital Khilko <vk@altlinux.ru> 1.2.1-alt1
- new version
- added ru, be, uk package description

* Sat Apr 12 2003 Alex Murygin <murygin@altlinux.ru> 1.0.2-alt2
- Added libanjuta obsoletes
- added icon in menu entry

* Mon Mar 31 2003 Alex Murygin <murygin@altlinux.ru> 1.0.2-alt1
- New version

* Tue Jan 21 2003 Stanislav Ievlev <inger@altlinux.ru> 0.1.9-alt2
- made rebuildable

* Tue Dec 18 2001 Stanislav Ievlev <inger@altlinux.ru> 0.1.8-alt1
- 0.1.8

* Thu Sep  6 2001 Stanislav Ievlev <inger@altlinux.ru> 0.1.7-alt1
- 0.1.7

* Mon Aug 13 2001 Stanislav Ievlev <inger@altlinux.ru> 0.1.6-alt1
- 0.1.6

* Fri Jul 27 2001 Stanislav Ievlev <inger@altlinux.ru> 0.1.5-alt2
- Update URLs

* Mon Jul  9 2001 Stanislav Ievlev <inger@altlinux.ru> 0.1.5-alt1
- 0.1.5

* Thu Jun 14 2001 Stanislav Ievlev <inger@altlinux.ru> 0.1.4-alt1
- 0.1.4

* Sat Jan 20 2001 AEN <aen@logic.ru>
- RE adaptation
- 1.1.2

* Thu Jan  4 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.1.1-2mdk
- new url

* Thu Nov  2 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.1.1-1mdk
- new in contribs
