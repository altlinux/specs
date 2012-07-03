# project is stollen. revised at 06.08.2007
Name: kxmleditor
Version: 1.1.4
Release: alt4.qa3

Packager: Vitaly Lipatov <lav@altlinux.ru>

Summary: KXML Editor for KDE
Summary(ru_RU.KOI8-R): Редактор файлов XML для KDE

Group: Development/Other
License: GPL
Url: http://kxmleditor.sourceforge.net

Source: http://prdownloads.sf.net/%name/%name-%version.tar.bz2
Patch: kxmleditor-1.1.4-alt-DSO.patch

%define desktop_file_utils_ver 0.8
Requires(post,postun): desktop-file-utils >= %desktop_file_utils_ver

# manually removed: imake kde-i18n-ru qt3-designer xorg-cf-files
# Automatically added by buildreq on Mon Nov 24 2008
BuildRequires: gcc-c++ imake kde-i18n-ru kdepim-devel libXt-devel libjpeg-devel qt3-designer xml-utils xorg-cf-files

%description
KXML Editor is a program that lets you browse and edit XML files.

%description -l ru_RU.KOI8-R
KXML Editor предназначен для просмотра и редактирования файлов XML.

%prep
%setup -q
%patch -p2
#%__subst 's,\.la\>,.so,' configure
%__subst 's,\$(kde_appsdir)/Applications,%_desktopdir,' %name/Makefile.in

%build
export KDEDIR=%prefix
export QTDIR=%_qt3dir
%add_optflags -I%_includedir/tqtinterface -fpermissive
%configure \
	--disable-rpath \
	--enable-shared \
	--disable-static \
	--with-qt-dir=%_qt3dir \
	--with-xinerama \
	 --without-arts \
	--program-prefix=""

%make_build

%install
%makeinstall_std
%find_lang --with-kde %name

%files -f %name.lang
%_bindir/%name
%_libdir/*.so*
%_datadir/apps/%name
%_datadir/services/*.desktop
%_iconsdir/*/*/apps/%name.png
%_desktopdir/%name.desktop
%doc ChangeLog AUTHORS KXMLEditor.flw README

%changelog
* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.4-alt4.qa3
- Fixed build

* Wed Apr 20 2011 Andrey Cherepanov <cas@altlinux.org> 1.1.4-alt4.qa2
- Build without aRts
- Adapt to new KDE3 placement

* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.1.4-alt4.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for kxmleditor
  * postun_ldconfig for kxmleditor
  * update_menus for kxmleditor
  * postclean-05-filetriggers for spec file

* Sun Nov 23 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.4-alt4
- fix build

* Sat Mar 08 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.4-alt3
- update buildreqs
- (close #12580)

* Sun Jul 02 2006 Vitaly Lipatov <lav@altlinux.ru> 1.1.4-alt2
- change packager
- update buildreqs, fix Source URL, small cleanup spec

* Fri Apr 21 2006 Sergey V Turchin <zerg at altlinux dot org> 1.1.4-alt1.1
- spec cleanup
- fix build on current Sisyphus

* Mon Jan 17 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.1.4-alt1
- 1.1.4

* Sat Nov 27 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.1.3-alt1
- 1.1.3

* Thu Apr 15 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Sat Jan 03 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.9.1-alt1
- 0.9.1

* Mon Dec 22 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.8.5-alt1
- 0.8.5

* Fri Sep 12 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.8.1-alt2
- updated buildreqs.

* Wed May 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Fri Oct 04 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.8-alt0.2.beta
- Rebuild with new QT3/KDE3

* Fri Sep 20 2002 Sergey V Turchin <zerg@altlinux.ru> 0.8-alt0.1.beta
- new version
- rebuild with gcc.3.2

* Tue May 14 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.7.2-alt2
- BuildConflicts on libqt2-devel <= 2.3.1-alt10
- rebuild

* Sat May 11 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.7.2-alt1
- First KDE3 version.

* Mon Jan 28 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.7.1-alt3
- cleanups

* Tue Dec 4 2001 Yuri N. Sedunov <aris@altlinux.ru> 0.7.1-alt2
- Menu, russian summary and description added.

* Fri Nov 30 2001 Yuri N. Sedunov <aris@altlinux.ru> 0.7.1-alt1
- first build for Sisyphus
