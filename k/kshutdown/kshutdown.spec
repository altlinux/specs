Name: kshutdown
Version: 0.4.0
Release: alt3.1

Summary: A Shut Down Utility for KDE.
License: GPL
Group: Graphical desktop/KDE
Url: http://kshutdown.sourceforge.net
Packager: Ilya Mashkin <oddity at altlinux dot ru>

Source0: %name-%version.tar.bz2
#Source1: %name.mo
Patch0: %name-0.4.0-alt-DSO.patch


BuildRequires: xorg-libs fontconfig freetype2 gcc-c++ kde-settings kdelibs-devel  libjpeg-devel libpng-devel libqt3-devel libstdc++-devel  qt3-designer xml-utils zlib-devel libtqt-devel

%description
KShutDown is an advanced shut down utility for KDE.

%prep
%setup -q 
%patch0 -p2
sed -i 's,\.la,\.so,' configure

%build
%configure --disable-rpath --without-arts
%set_verify_elf_method textrel=relaxed
%make_build CXXFLAGS="-I%_includedir/tqtinterface"

%install
make DESTDIR=%buildroot install
#menu
mkdir -p %buildroot/%_menudir
install -p -m644 %buildroot/%_datadir/applnk/Utilities/%name.desktop %buildroot/%_menudir/%name 
#__mkdir_p %buildroot%_datadir/locale/ru/LC_MESSAGES
#__install -pD -m644 %%SOURCE1 %buildroot%_datadir/locale/ru/LC_MESSAGES/

%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog README TODO
%_bindir/%name
%_datadir/applnk/Utilities/%name.desktop
%_datadir/applnk/Utilities/kshutdownwizard.desktop
#%_datadir/locale/*/LC_MESSAGES/%name.mo
%_menudir/%name
%_datadir/apps/%name/
%doc %_docdir/HTML/en/%name
%_iconsdir/*/*/apps/%name.png

%changelog
* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt3.1
- Fixed build

* Thu Feb 23 2012 Roman Savochenko <rom_as@altlinux.ru> 0.4.0-alt3
- Build for TDE 3.5.13 release

* Wed May 25 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.4.0-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * altlinux-policy-obsolete-buildreq for kshutdown
  * postclean-03-private-rpm-macros for the spec file

* Sun Apr 17 2011 Ilya Mashkin <oddity at altlinux dot ru> 0.4.0-alt2
- fix build

* Thu Jan 14 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.4.0-alt1.2.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for kshutdown
  * postclean-05-filetriggers for spec file

* Tue May 27 2008 Ilya Mashkin <oddity at altlinux dot ru> 0.4.0-alt1.2
- spec cleanup

* Mon Jan 10 2005 Ilya Mashkin <oddity at altlinux dot ru> 0.4.0-alt1
- New version 0.4.0
- spec cleanup

* Fri Aug 27 2004 Dmitriy Porollo <spider@altlinux.ru> 0.3.0-alt1
- NEW: Ability to run a command before shut down (click "Configure", "Automation")
- NEW: Automatic screen locking after login (click "Configure", "Automation")
- NEW: Reorganized and improved settings dialog
- NEW: Colors in the "Setup" script
- NEW: Added help buttons
- NEW: Icons in tool tips
- NEW: Italian translation
- SYSTEM TRAY: Middle mouse button displays the actions menu
- SYSTEM TRAY: Added confirmations
- SYSTEM TRAY: Tear off handles in menus
- FIXED: Source code and API cleanup
- FIXED: Better usability
- FIXED: Added "now" argument to the command line options
- FIXED: Message window is now always on top
- Added new items to the "Extras" menu
