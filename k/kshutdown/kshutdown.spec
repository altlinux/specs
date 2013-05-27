Name: kshutdown
Version: 0.6.1
Release: alt1
Summary: A Shut Down Utility for KDE
License: GPLv2+
Group: Graphical desktop/KDE
Url: http://%name.sourceforge.net
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: rpm-macros-kde-common-devel kdelibs-devel
BuildRequires: gcc-c++ libdnet-devel libjpeg-devel libpng-devel zlib-devel xml-utils

%description
KShutDown is an advanced shut down utility for KDE.


%prep
%setup -q
%patch -p1
sed -i 's|\.la|.so|g' configure


%build
%add_optflags -I%_includedir/tqtinterface
export KDEDIR="$(dirname %_K3bindir)"
%configure --disable-rpath --without-arts
%make_build


%install
%makeinstall_std
%find_lang %name


%files -f %name.lang
%doc AUTHORS ChangeLog README TODO
%doc %_docdir/HTML/en/%name
%_bindir/*
%_datadir/applnk/Utilities/*
%_datadir/apps/*
%_niconsdir/*
%_liconsdir/*
%_iconsdir/locolor/*/apps/*


%changelog
* Mon May 27 2013 Led <led@altlinux.ru> 0.6.1-alt1
- 0.6.1

* Sun May 26 2013 Led <led@altlinux.ru> 0.4.0-alt4
- removed unneeded file
- build with %%optflags
- fixed License
- updated BuildRequires

* Fri Apr 12 2013 Andrey Cherepanov <cas@altlinux.org> 0.4.0-alt3.2
- Fix build with new xorg

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
