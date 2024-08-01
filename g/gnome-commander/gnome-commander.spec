%def_disable snapshot

%define ver_major 1.18
%def_with exiv2
%def_with taglib
%def_with poppler
%def_with libgsf
%def_with samba

%def_enable check

Name: gnome-commander
Version: %ver_major.1
Release: alt1

%define xdg_name org.gnome.%name

Summary: A Gnome file manager similar to the Norton Commander (TM)
License: GPL-2.0
Group: File tools
Url: https://gcmd.github.io

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Vcs: https://gitlab.gnome.org/GNOME/gnome-commander.git
Source: %name-%version.tar
%endif

%define gtk_ver 3.24

Requires: dconf xdg-utils
Requires: %_bindir/gio gvfs-backends
Requires: file-roller

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson flex gcc-c++
BuildRequires: yelp-tools desktop-file-utils /usr/bin/appstreamcli
BuildRequires: libgtk+3-devel >= %gtk_ver libgnome-keyring-devel
%{?_with_exiv2:BuildRequires: libexiv2-devel}
%{?_with_taglib:BuildRequires: libtag-devel}
%{?_with_poppler:BuildRequires: libpoppler-glib-devel}
%{?_with_libgsf:BuildRequires: libgsf-devel}
%{?_with_samba:BuildRequires: libsmbclient-devel}
%{?_enable_check:BuildRequires: xvfb-run libgtest-devel}

%description
GNOME Commander is a two-pane graphical file manager for the GNOME
desktop environment. It features separate tabs for each pane,
setting up custom device buttons, bookmark manager, fully integrated
commandline, file quick search, an internal image viewer, a powerful
batch renaming tool, and FTP and Samba access.

%prep
%setup
%ifarch %e2k
# workaround for EDG frontend
sed -i.e2k "/g_autofree gchar/{s|g_autofree gchar|g_autofree_edg(gchar)|;s|\*||g}" src/gnome-cmd-data.cc
%endif

%build
%meson
%meson_build

%install
%meson_install
rm -f %buildroot%_libdir/libgcmd.a

%find_lang --with-gnome %name

%check
xvfb-run %__meson_test

%files -f %name.lang
%_bindir/*
%_libdir/%name/
%_datadir/%name/
%_desktopdir/%xdg_name.desktop
%_datadir/glib-2.0/schemas/%xdg_name.enums.xml
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_iconsdir/hicolor/*/apps/*.svg
%_datadir/pixmaps/%name/
%_datadir/metainfo/%xdg_name.appdata.xml
%_man1dir/*
%doc AUTHORS NEWS README* TODO doc/*.txt

%exclude %_datadir/%name/internal_viewer_hacking.txt
%exclude %_datadir/%name/keys.txt


%changelog
* Thu Aug 01 2024 Yuri N. Sedunov <aris@altlinux.org> 1.18.1-alt1
- 1.18.1

* Thu Jul 25 2024 Yuri N. Sedunov <aris@altlinux.org> 1.18.0-alt1
- updated to 1.18.0-6-g00e234a1

* Fri May 17 2024 Yuri N. Sedunov <aris@altlinux.org> 1.16.2-alt1
- 1.16.2

* Sat Jul 08 2023 Yuri N. Sedunov <aris@altlinux.org> 1.16.1-alt1
- 1.16.1

* Mon Jan 23 2023 Yuri N. Sedunov <aris@altlinux.org> 1.16.0-alt1
- 1.16.0 (ported to Meson build system)

* Tue Dec 06 2022 Yuri N. Sedunov <aris@altlinux.org> 1.14.3-alt2
- 1.14.3-11-g3169f4d5 (updated translations,
  fixed calculation of total bytes to be transfered)

* Sat Jun 18 2022 Yuri N. Sedunov <aris@altlinux.org> 1.14.3-alt1
- 1.14.3

* Sun Mar 27 2022 Yuri N. Sedunov <aris@altlinux.org> 1.14.2-alt1
- 1.14.2

* Thu Mar 03 2022 Yuri N. Sedunov <aris@altlinux.org> 1.14.1-alt1
- 1.14.1

* Mon Feb 28 2022 Yuri N. Sedunov <aris@altlinux.org> 1.14.0-alt1
- 1.14.0

* Sun Nov 21 2021 Yuri N. Sedunov <aris@altlinux.org> 1.12.3.1-alt1
- 1.12.3.1

* Sun Nov 21 2021 Yuri N. Sedunov <aris@altlinux.org> 1.12.3-alt1
- 1.12.3 (fixed ALT #41354)

* Thu Sep 16 2021 Yuri N. Sedunov <aris@altlinux.org> 1.12.2-alt2
- fixed build for %%e2k (ilyakurdyukov@)

* Sun May 30 2021 Yuri N. Sedunov <aris@altlinux.org> 1.12.2-alt1
- 1.12.2

* Sat Apr 17 2021 Yuri N. Sedunov <aris@altlinux.org> 1.12.1-alt1
- 1.12.1

* Thu Mar 25 2021 Yuri N. Sedunov <aris@altlinux.org> 1.12.0-alt1
- 1.12.0

* Fri Jun 19 2020 Yuri N. Sedunov <aris@altlinux.org> 1.10.3-alt1
- 1.10.3

* Thu May 23 2019 Yuri N. Sedunov <aris@altlinux.org> 1.10.2-alt1
- 1.10.2

* Sun May 12 2019 Yuri N. Sedunov <aris@altlinux.org> 1.10.1-alt1
- 1.10.1

* Sun Mar 31 2019 Yuri N. Sedunov <aris@altlinux.org> 1.10.0-alt1
- 1.10.0

* Sun Mar 04 2018 Yuri N. Sedunov <aris@altlinux.org> 1.8.1-alt1
- 1.8.1

* Sun Oct 08 2017 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0

* Sun May 28 2017 Yuri N. Sedunov <aris@altlinux.org> 1.6.4-alt1
- 1.6.4

* Sun May 07 2017 Yuri N. Sedunov <aris@altlinux.org> 1.6.3-alt2
- rebuilt against libexiv2.so.26

* Mon Feb 27 2017 Yuri N. Sedunov <aris@altlinux.org> 1.6.3-alt1
- 1.6.3

* Sun Nov 06 2016 Yuri N. Sedunov <aris@altlinux.org> 1.6.2-alt1
- 1.6.2

* Tue Oct 18 2016 Yuri N. Sedunov <aris@altlinux.org> 1.6.1-alt1
- 1.6.1

* Tue Oct 04 2016 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Sun Sep 18 2016 Yuri N. Sedunov <aris@altlinux.org> 1.4.9-alt1
- 1.4.9

* Tue Mar 15 2016 Yuri N. Sedunov <aris@altlinux.org> 1.4.8-alt1
- 1.4.8

* Sun Jun 28 2015 Yuri N. Sedunov <aris@altlinux.org> 1.4.7-alt2
- rebuilt against libexiv2.so.14

* Fri Jun 19 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.4.7-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Sat May 30 2015 Yuri N. Sedunov <aris@altlinux.org> 1.4.7-alt1
- 1.4.7

* Thu May 28 2015 Yuri N. Sedunov <aris@altlinux.org> 1.4.6-alt1
- 1.4.6
- built with gcc-4.9

* Sun Jan 25 2015 Yuri N. Sedunov <aris@altlinux.org> 1.4.5-alt1
- 1.4.5

* Wed Nov 12 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.4-alt1
- 1.4.4

* Fri Jun 27 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.3-alt1
- 1.4.3

* Fri May 23 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.2-alt1
- 1.4.2

* Sat Apr 05 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt1
- 1.4.1

* Mon Mar 17 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Sun Jan 12 2014 Yuri N. Sedunov <aris@altlinux.org> 1.2.8.17-alt1
- 1.2.8.17

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

* Sun Apr 20 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.9.12-alt2
- Add requires to fam and cleanup spec

* Tue Mar 25 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.9.12-alt1
- First version of RPM package.

