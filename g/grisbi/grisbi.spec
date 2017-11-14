Name: 	 grisbi
Version: 1.0.0
Release: alt2

Summary: Personal finance application
Summary(ru_RU.UTF-8): Программа персонального учёта финансов
License: GPL
Group:   Office 
URL:     http://www.grisbi.org

Source:  http://prdownloads.sourceforge.net/grisbi/%name-%version.tar.bz2
# VCS    git://git.code.sf.net/p/grisbi/code

BuildRequires: glib2-devel libatk-devel libgtk+2-devel libpango-devel libxml2-devel pkgconfig zlib-devel intltool

%description
Grisbi is a personal finance application for Linux, written
with Gnome and Gtk, and is released under the GPL licence.

%description -l ru_RU.UTF-8
Grisbi - это программа персонального учёта финансов для Linux,
написанная под Gnome и Gtk и распространяемая на условиях GPL.

%prep
%setup -q

%build
%autoreconf
%configure
%make_build 

%install
%makeinstall_std 

%find_lang %name

%files -f %name.lang
%doc ABOUT-NLS AUTHORS COPYING INSTALL NEWS OLDNEWS README
%_bindir/%name
%_datadir/%name/*
%_datadir/mime-info/%name.keys
%_datadir/mime-info/%name.mime
%_datadir/mime/packages
%_desktopdir/%name.desktop
%_pixmapsdir/%{name}*
%_iconsdir/hicolor/scalable/apps/grisbi.svg
%doc %_docdir/%name/*
%doc %_man1dir/%name.1*

%changelog
* Tue Nov 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.0-alt2
- Updated spec to allow any man pages compression.

* Thu Apr 17 2014 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- New version
- Build from upstream git

* Sat Apr 09 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.9-alt2.qa2
- NMU: menu converted to .desktop file

* Tue Feb 09 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.5.9-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for grisbi
  * postclean-05-filetriggers for spec file

* Sat Mar 01 2008 Grigory Batalov <bga@altlinux.ru> 0.5.9-alt2
- Fix build (config.rpath is missing).

* Sun Oct 08 2006 Grigory Batalov <bga@altlinux.ru> 0.5.9-alt1
- 0.5.9.
- Description typo ("personnal") was fixed (bug #3953).
- Fix linking with --as-needed

* Fri Jan 20 2006 Grigory Batalov <bga@altlinux.ru> 0.5.8-alt1
- 0.5.8

* Tue Jul 05 2005 Grigory Batalov <bga@altlinux.ru> 0.5.7-alt1
- 0.5.7

* Tue May 24 2005 Grigory Batalov <bga@altlinux.ru> 0.5.6-alt1
- 0.5.6

* Tue Mar 01 2005 Grigory Batalov <bga@altlinux.ru> 0.5.5-alt1
- 0.5.5
- Included gettext was removed
- Russian rouble support was added
- Toupper call on multibyte symbol was removed

* Mon Jul 05 2004 Pavel S. Khmelinsky <hmepas@altlinux.ru> 0.5.0-alt3
- BuildRequires updated 

* Sat Jul 03 2004 Pavel S. Khmelinsky <hmepas@altlinux.ru> 0.5.0-alt2
- Right Summary 

* Mon Jun 21 2004 Pavel S. Khmelinsky <hmepas@altlinux.ru> 0.5.0-alt1
- 0.5.0 


* Sat Mar 27 2004 Pavel S. Khmelinsky <hmepas@altlinux.ru> 0.4.4-alt1
- First Build for Sisyphus 
