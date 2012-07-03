Name: medit
Version: 1.1.0
Release: alt1

Summary: Multiplatform GTK+2 text editor
License: GPLv2+
Group: Editors

Url: http://mooedit.sourceforge.net/
Source0: http://prdownloads.sourceforge.net/mooedit/%name-%version.tar.bz2
Source1: medit16.png
Source2: medit32.png
Patch1: medit-1.0.1-docdir.patch

# Automatically added by buildreq on Fri Apr 01 2011
BuildRequires: gcc-c++ intltool libSM-devel libXext-devel libgamin-devel libxml2-devel python-module-pygtk-devel

%add_python_req_skip moo
%add_findreq_skiplist */xdg-open
%add_findreq_skiplist */xdg-email

%description
Medit is a multiplatform GTK+2 text editor.
Features:
- Configurable syntax highlighting
- Configurable keyboard accelerators
- Powerfull search system and file manager
- Multiplatform - works both on unix and windows

%prep
%setup
%patch1 -p1

%build
%configure
%make_build

%install
%makeinstall_std

install -pD -m644 %SOURCE1 %buildroot%_miconsdir/%name.png
install -pD -m644 %SOURCE2 %buildroot%_niconsdir/%name.png

%find_lang --output=medit.lang medit-1 medit-1-gsv

rm -f %buildroot%_iconsdir/hicolor/icon-theme.cache

%files -f medit.lang
%_bindir/%name
%_datadir/applications/%name.desktop
%_datadir/medit-1
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_man1dir/%name.*

%changelog
* Fri Mar 16 2012 Victor Forsiuk <force@altlinux.org> 1.1.0-alt1
- 1.1.0

* Mon Jan 09 2012 Victor Forsiuk <force@altlinux.org> 1.0.5-alt1
- 1.0.5

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.3-alt1.1
- Rebuild with Python-2.7

* Tue Apr 19 2011 Victor Forsiuk <force@altlinux.org> 1.0.3-alt1
- 1.0.3

* Fri Apr 01 2011 Victor Forsiuk <force@altlinux.org> 1.0.1-alt1
- 1.0.1

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4-alt10.1
- Rebuilt with python 2.6

* Thu Sep 24 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.9.4-alt10
- Removed depency for kdelibs.

* Wed Sep 23 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.9.4-alt9
- Russian translation updated.

* Tue Jun 30 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.9.4-alt8
- Added medit-l10n-fix.patch to fix some localization problems

* Mon Jun 29 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.9.4-alt7
- Russian translation updated

* Mon Jun 29 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.9.4-alt6
- Russian translation updated

* Sun May 24 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.9.4-alt5
- Fix build. Added russian translation

* Wed Nov 19 2008 Konstantin Baev <kipruss@altlinux.org> 0.9.4-alt4
- Fix repocop errors - remove update-desktop-database update_menus macroses
  update BuildRequires
  add icons 16x16 and 32x32

* Tue Oct 28 2008 Konstantin Baev <kipruss@altlinux.org> 0.9.4-alt3
- Fix repocop errors

* Mon Oct 27 2008 Konstantin Baev <kipruss@altlinux.org> 0.9.4-alt2
- Fixed bug ALT#17685. Remove dependencies on libexo, libgnome, kdebase-konqueror, kdebase-wm

* Tue Oct 21 2008 Konstantin Baev <kipruss@altlinux.org> 0.9.4-alt1
- Initial build for Sisyphus
