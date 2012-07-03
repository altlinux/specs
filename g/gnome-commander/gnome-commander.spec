Name: gnome-commander
Version: 1.2.8.13
Release: alt3.1

Summary: A Gnome file manager similar to the Norton Commander (TM)
License: GPL
Group: File tools
Url: http://www.freesoftware.fsf.org/gcmd/
Packager: Radik Usupov <radik@altlinux.org>

Source0: %name-%version.tar.bz2
Patch: gnome-commander-alt-fix-su-mode.patch

Provides: libgcmd.so.0

Requires: gnome-vfs-module-smb
Requires: gnome-keyring
Requires: findutils grep
Requires: libunique yelp
Requires: beesu meld
Requires: nautilus-sendto

# Automatically added by buildreq on Fri Sep 26 2008
BuildRequires: flex gcc-c++ glibc-devel-static gnome-doc-utils-xslt libgnomeui-devel libunique-devel gnome-vfs-devel
BuildRequires: librarian perl-XML-Parser python-devel gnome-doc-utils intltool libpoppler-devel gettext perl-XML-Parser

%description
GNOME Commander is a nice and fast file manager for the GNOME desktop.
In addition to performing the basic file manager functions the program is
also an FTP-client and it can browse SMB-networks.


%prep
%setup -q
%patch -p2

%build
%autoreconf
%configure
%make_build RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO doc/*.txt 
%dir %_datadir/gnome
%dir %_datadir/omf
%_man1dir/*
%_bindir/*
%_libdir/%name
%_datadir/applications/%name.desktop
%_datadir/pixmaps/*
%_datadir/gnome/*
%_datadir/omf/*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.8.13-alt3.1
- Rebuild with Python-2.7

* Sun Oct 02 2011 Radik Usupov <radik@altlinux.org> 1.2.8.13-alt3
- Small fixed spec file
- Added meld to requires
- Added russian help

* Sun Oct 02 2011 Radik Usupov <radik@altlinux.org> 1.2.8.13-alt2
- Added reguires (Closes: 26327)
- Updated russian translations
- New upstream snapshot

* Mon Sep 19 2011 Radik Usupov <radik@altlinux.org> 1.2.8.13-alt1
- New version (1.2.8.13)

* Mon Feb 14 2011 Radik Usupov <radik@altlinux.org> 1.2.8.10-alt1
- New version (1.2.8.10) (Closes: 25083)
  + Bug fixes:
    + Fixed problem #448941 (numeric keypad arrows don't work in the main window)
    + Fixed problem #620275 (add menu item to copy full path and file name to clipboard)
    + Fixed problem #637501 (advrename: metatag popup menu shows wrong items)
    + Fixed problem with toggling path/basename/filename selections in copy/move dialogs
    + Fixed problem with searching path for devices
    + Updated translations: de
  gnome-commander 1.2.8.9
  + New features:
    + Support for shell-style wildcards in quick search
  gnome-commander 1.2.8.8
  + Bug fixes:
    + Fixed problem #610764 (menu item won't stay checked)
    + Fixed problem #626469 (add support for other su-like programs: xdg-su, gnomesu)
    + Fixed problem with broken Spanish translation
- Spec cleaned

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.7-alt4.1
- Rebuilt with python 2.6

* Tue Dec 16 2008 Vladimir Scherbaev <vladimir@altlinux.org> 1.2.7-alt4
- Some changes in spec file

* Fri Dec 12 2008 Vladimir Scherbaev <vladimir@altlinux.org> 1.2.7-alt3
- Add icons

* Thu Nov 20 2008 Vladimir Scherbaev <vladimir@altlinux.org> 1.2.7-alt2
- Apply repocop patch

* Fri Sep 26 2008 Vladimir Scherbaev <vladimir@altlinux.org> 1.2.7-alt1
- New version 1.2.7

* Fri May 14 2004 Andrey Semenov <mitrofan@altlinux.ru> 1.1.6-alt2
- bug fix compile with gtk 2.4

* Tue Jan 20 2004 Andrey Semenov <mitrofan@altlinux.ru> 1.1.6-alt1
- 1.1.6
- bugs fixes
- updated the cvs-plugin so that it can be used to diff and log files
- made the cwd label selectable (the one left of the cmdline)
- sorting column and direction is now remembered
- added button to the directory indicator to popup the directory history

* Sat Jan 17 2004 Andrey Semenov <mitrofan@altlinux.ru> 1.1.5-alt1
- 1.1.5
- the ext-column is now hidden when the extension is only showed together  with the filename
- fixed unnecessary redraws of the file-list when dragging files over it
- fixed problem with ftp-connections that didn't disappear from the connection toolbars when disconnected
- the program no longer tries to center itself on the desktop
- fixed problems when renaming directories

* Fri Nov 28 2003 Andrey Semenov <mitrofan@altlinux.ru> 1.1.4-alt1
- 1.1.4
- Fixed bug when selecting multiple files with shift+mouse button
- Cleaned up the file-popup menu
- Fixed possible async error when cancelling a xfer operation
- Reworked the layout tab and removed the colors tab in the options dialog
- Improved plugin-system

* Sat Nov 15 2003 Andrey Semenov <mitrofan@altlinux.ru> 1.1.3-alt1
- 1.1.3
- Bugs fixed
- Changed base class from GtkDialog to GnomeCmdDialog

* Sun Nov 2 2003 Andrey Semenov <mitrofan@altlinux.ru> 1.1.2-alt1
- 1.1.2
- SMB browsing
- Major rewrite of alot of code
- Bugs fixed

* Thu Oct 30 2003 Andrey Semenov <mitrofan@altlinux.ru> 1.0.1-alt2
- Update build requires

* Sat Jun 28 2003 Andrey Semenov <mitrofan@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Fri Jun 6 2003 Andrey Semenov <mitrofan@altlinux.ru> 1.0-alt1
- Realese 1.0

* Thu Apr 20 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.9.12-alt2
- Add requires to fam and cleanup spec

* Tue Mar 25 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.9.12-alt1
- First version of RPM package.

