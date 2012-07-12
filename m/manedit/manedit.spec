Name: manedit
Version: 1.2.1
Release: alt1.qa3

Summary: Manual page viewer and editor
Summary(ru_RU.CP1251): Программа для редактирования и просмотра документации
License: GPL
Group: Development/Other
Url: http://freshmeat.net/projects/manedit/
Packager: Eugene Ostapets <eostapets@altlinux.ru>

Source0: ftp://wolfpack.twu.net/users/wolfpask/%name-%version.tar.bz2
Source2: %{name}_48x48.xpm
Source3: %{name}_32x32.xpm
Source4: %{name}_16x16.xpm

Patch0: manedit-alt-fonts.patch
Patch1: manedit-alt-path.patch
Patch2: manedit-alt-bzip2_detection_fix.patch
Patch3: manedit-alt-x86_64.patch
Patch4: manedit-alt-manpage.patch
Patch5: manedit-1.2.1-alt-DSO.patch

# Automatically added by buildreq on Fri Mar 16 2007
BuildRequires: bzlib-devel gcc-c++ gtk+-devel zlib-devel

%description
ManEdit is a UNIX manual page editor and viewer. It can be used as a direct
editor for UNIX manual pages (with no manual conversion steps involved) or
a viewer/browser. ManEdit uses the GTK+ widget set and requires the X Window
Systems.

In the ManEdit editor you can load one or more manual pages and edit each
section using ManEdit's manual page format to XML translation feature. Each
manual page is broken down into sections and one header for easier recognition
of the manual page format. If you are unfamiliar with the XML or manual page
formats, you should go to help->How To Write ManPages.

In viewer mode, you can search for an manual page installed in the global
manual page directories on the file system ManEdit is running on. There is
also an index feature which creates a complete catagory index listing of all
the manual pages installed on the file system (see view->index).

ManEdit also supports full Drag and Drop features between its process windows,
you can run ManEdit with multiple editor and viewer windows in a single process.

%description -l ru_RU.CP1251
ManEdit это программа для редактирования и просмотра документации в UNIX. Она может
быть использована непосредственно для редактирования страниц документации в UNIX
(освобождая от конверсии вручную) или для их просмотра.
ManEdit использует набор виджетов GTK+ и требует для работы X Window Systems.

%prep
%setup
%patch0 -p2
%patch1 -p2
%patch2 -p2
%patch3 -p1
%patch4 -p1
%patch5 -p2

%build
./configure Linux --CFLAGS="%optflags"
%make_build

%install
%make_install install -C manedit \
		PREFIX=%buildroot%prefix \
		MAN_DIR="%buildroot%_man1dir"

# icons
install -D -m644 %SOURCE2 %buildroot%_miconsdir/%name.xpm
install -D -m644 %SOURCE3 %buildroot%_niconsdir/%name.xpm
install -D -m644 %SOURCE4 %buildroot%_liconsdir/%name.xpm

rm %buildroot%_iconsdir/%name.xpm
mv %buildroot%_iconsdir/manview.xpm %buildroot%_liconsdir/manview.xpm

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=ManEdit
Comment=Manual Page Viewer and Editor
Icon=%{name}
Exec=%name
Terminal=false
Categories=Development;Utility;TextTools;
EOF

%files
%_bindir/*
%_datadir/%name
%_man1dir/%name.1.*
%_desktopdir/%{name}.desktop
%_miconsdir/%name.xpm
%_niconsdir/%name.xpm
%_liconsdir/%name.xpm
%_liconsdir/manview.xpm
%doc AUTHORS README INSTALL LICENSE

%changelog
* Thu Jul 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1.qa3
- Fixed build

* Thu Apr 07 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1.qa2
- NMU: converted debian menu to freedesktop

* Tue Nov 17 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.1-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for manedit
  * postclean-05-filetriggers for spec file

* Sun Jul 12 2009 Slava Semushin <php-coder@altlinux.ru> 1.2.1-alt1
- NMU
- Updated to 1.2.1
  + Fixed segfault when New button pressed (Closes: #20754)
- Updated Url tag
- Removed obsolete %%update_menus/%%clean_menus calls

* Fri Mar 16 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.8.1-alt1
- new version
- fix 10929
- renew %name-filebrowser.patch
- clean buildrequires

* Tue Nov 07 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.7.1-alt2
- fix x86_64 build

* Wed Nov 01 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.7.1-alt1
- 0.7.1

* Sun Mar 27 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.6.1-alt1
- 0.6.1

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.5.12-alt1.1
- Rebuilt with libstdc++.so.6.

* Sun Nov 21 2004 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.5.12-alt1
- 0.5.12
- added %name-filebrowser.patch
- added optimisation
- updated BuildRequires

* Sat Jun 26 2004 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.5.11-alt2
- Changed Global man pages location

* Mon May 24 2004 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.5.11-alt1
- 0.5.11

* Wed May 07 2003 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 0.5.10-alt1
- 0.5.10

* Mon Mar 24 2003 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 0.5.9-alt1
- 0.5.9

* Sun Jan 26 2003 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.5.8-alt1
- 0.5.8

* Wed Dec 04 2002 Stanislav Ievlev <inger@altlinux.ru> 0.5.6-alt3
- rebuild to fix dep on groff

* Fri Oct 11 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.5.6-alt2
- rebuilded with gcc-3.2
- removed Summary & description in KOI8-R encoding

* Wed Mar 20 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.5.6-alt1
- 0.5.6

* Sat Mar 02 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.5.5-alt1
- 0.5.5

* Wed Jan 30 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.5.4-alt2
- added default path correction patch

* Sun Jan 20 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.5.4-alt1
- 0.5.4

* Wed Jan 09 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.5.3-alt4
- added Summary & description in CP1251 encoding

* Wed Dec 26 2001 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.5.3-alt3
- added fonts patch by Inger <inger@altlinux.ru>
- updated BuildRequires

* Sat Dec 8 2001 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.5.3-alt2
- fixed default fonts

* Fri Oct 26 2001 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.5.3-alt1
- 0.5.3

* Fri Oct 26 2001 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 0.5.2-alt1
- 0.5.2
- spec cleanup

* Fri Sep 21 2001 Aleksandr Blokhin 'Sass' <sass@uustoll.ee> 0.5.1-alt1
- 0.5.1

* Mon Feb 26 2001 AEN <aen@logic.ru> 0.4-ipl2
- 0.4i

* Tue Jan 16 2001 Dmitry V. Levin <ldv@fandra.org> 0.4-ipl1
- Initial revision.Name: manedit
