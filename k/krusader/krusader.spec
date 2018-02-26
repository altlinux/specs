%define version 1.90.0
%define altrelease 9

%define appname krusader
%define srcname %appname-%{?cvs:cvs-%cvs}%{!?cvs:%version%{?pre:-%pre}}

%define qtdir %_qt3dir
%define kdedir %_K3prefix

Name: %appname
Version: %version
Release: alt%{?pre:0.%altrelease.%pre}%{!?pre:%altrelease}%{?cvs:.cvs%cvs}

Source0: %srcname.tar.gz

Patch10: krusader-cvs-20060412-makefile-kutils.patch
Patch11: tde-3.5.13-build-defdir-autotool.patch
Patch12: cvs-auto_version_check.patch

Group: File tools
Summary: A twin panel file manager for kde %{?cvs:- unstable version from cvs}
License: GPL
Url: http://krusader.sourceforge.net

# Automatically added by buildreq on Mon Sep 29 2008
BuildRequires: gcc-c++ imake kdebase-devel kjsembed-devel libXt-devel libjpeg-devel libqt3-devel xml-utils xorg-cf-files

%description
Krusader is an advanced twin-panel (commander-style) file-manager for KDE 3.x (similar to Midnight or Total Commander) but with many extras.
It provides all the file-management features you could possibly want. Plus: extensive archive handling, mounted filesystem support, FTP, advanced search module, viewer/editor, directory synchronisation, file content comparisons, powerful batch renaming and much much more.
Krusader supports the following archive formats: tar, zip, bzip2, gzip, rar, ace, arj and rpm and can handle other KIOSlaves such as smb:// or fish://.
It is (almost) completely customizable, very user friendly, fast and looks great on your desktop! :-) You should give it a try.

%prep
%setup -q -n %srcname
%patch10
%patch11
%patch12

cp -Rp /usr/share/libtool/aclocal/libtool.m4 admin/libtool.m4.in
cp -Rp /usr/share/libtool/config/ltmain.sh admin/ltmain.sh
make -f admin/Makefile.common

%build
rm -rf %buildroot
export QTDIR=%qtdir
export KDEDIR=%kdedir

export PATH=$QTDIR/bin:$KDEDIR/bin:$PATH

%K3configure \
        --disable-rpath \
	--disable-debug \
	--disable-static \
	--enable-shared

### SMP build is buggy! don't use make_build
%make

%install
%K3install

cp %buildroot/%_kde3_iconsdir/locolor/16x16/apps/%appname.png %buildroot/%_kde3_iconsdir

%find_lang %appname --with-kde

%files -f %appname.lang
%_K3bindir/%appname
%_K3lib/*
#%exclude %_libdir/kde3/kio_iso.*
#exclude %_libdir/kde3/kio_tar.*
# %_datadir/apps/konqueror/servicemenus/*.desktop
# %_datadir/config/*
###%%_menudir/%appname
%_K3apps/%appname
%_K3xdg_apps/*.desktop
%doc README ChangeLog TODO CVSNEWS
%doc %_K3doc/*/krusader/
%_K3iconsdir/crystalsvg/*/apps/%{appname}*
%_kde3_iconsdir/*/*/*/*.png
%_kde3_iconsdir/%name.png
%_K3srv/*.protocol
%_K3i18n/*
# %_man1dir/*

%changelog
* Wed May 23 2012 Roman Savochenko <rom_as@altlinux.ru> 1.90.0-alt9
- Direct link to -lkjs is added for build fix.

* Thu Apr 26 2012 Roman Savochenko <rom_as@altlinux.ru> 1.90.0-alt8
- Automake version is fixed to 1.11.5 detect.

* Thu Feb 23 2012 Roman Savochenko <rom_as@altlinux.ru> 1.90.0-alt7
- Build for TDE 3.5.13 release

* Wed Nov 19 2008 Konstantin Baev <kipruss@altlinux.org> 1.90.0-alt6
- fix repocop warnings - remove update_menus macros

* Wed Oct 29 2008 Konstantin Baev <kipruss@altlinux.org> 1.90.0-alt5
- fix repocop warnings

* Mon Sep 29 2008 Konstantin Baev <kipruss@altlinux.org> 1.90.0-alt4
- Cleanup BuildRequires

* Mon Sep 15 2008 Konstantin Baev <kipruss@altlinux.org> 1.90.0-alt3
- fix BuildRequires

* Fri Mar 28 2008 Nick S. Grechukh <gns@altlinux.org> 1.90.0-alt2
- built with kjsembed

* Fri Mar 28 2008 Nick S. Grechukh <gns@altlinux.org> 1.90.0-alt1
- new version

* Thu Jul 26 2007 Nick S. Grechukh <gns@altlinux.org> 1.80.0-alt1
- yeah, they did it! ;) stable 1.80 release

* Fri May 11 2007 Nick S. Grechukh <gns@altlinux.org> 1.80.0-alt0.05.beta2.cvs20070509
- new snapshot

* Fri Apr 13 2007 Nick S. Grechukh <gns@altlinux.org> 1.80.0-alt0.03.beta1.cvs20070413
- new snapshot

* Wed Feb 07 2007 Nick S. Grechukh <gns@altlinux.ru> 1.80.0-alt0.03.beta1.cvs20070207
- new snapshot

* Sat Jan 13 2007 Nick S. Grechukh <gns@altlinux.org> 1.80.0-alt0.02.beta1
- new version
- package naming policy changed

* Sat Oct 28 2006 Nick S. Grechukh <gns@altlinux.ru> 1.70.0-alt3.beta0.cvs20061027.1
- fresh snapshot
- New major features: atomic extension, extensions known to be atomic (tar.gz, tar.bz2). full screen terminal (mc style). keeping the directory structure of copying/moving from.
- patch11 removed (#1519955)

* Tue Jul 11 2006 Nick S. Grechukh <gns@altlinux.ru> 1.70.0-alt3.beta0.cvs20060626.4
- fixed build on i586 (-lkutils), spec cleanup

* Thu Jul 06 2006 Nick S. Grechukh <gns@altlinux.ru> 1.70.0-alt3.beta0.cvs20060626.2
- cvs date in about dialog. fixed supplementary groups support in vfs::vfs_calcSpaceLocal (patch11).

* Mon Jun 26 2006 Nick S. Grechukh <gns@altlinux.org> 1.70.0-alt3.beta0.cvs20060626.1
- fresh snapshot

* Thu May 04 2006 Nick S. Grechukh <gns@altlinux.org> 1.70.0-alt3.beta0.cvs20060501.1
- fresh snapshot

* Tue Feb 14 2006 Nick S. Grechukh <gns@altlinux.org> 1.70.0-alt2.stable
- stable release

* Mon Feb 06 2006 Nick S. Grechukh <gns@altlinux.org> 1.70.0-alt1.beta2.cvs20060204.2
- fresh snapshot

* Wed Jan 18 2006 Nick S. Grechukh <gns@altlinux.org> 1.70.0-alt1.beta2.cvs20060116.1
- fresh snapshot

* Sun Dec 18 2005 Nick S. Grechukh <gns@altlinux.ru> 1.70.0-alt1.beta2.cvs20051129.2
- new beta release

* Wed Oct 05 2005 Nick S. Grechukh <gns@altlinux.ru> 1.70.0-alt1.beta1.cvs20051005.1
- new release

* Mon Aug 08 2005 Nick S. Grechukh <gns@altlinux.ru> 1.60.0-alt1.beta2.cvs20050807.1
- 2005-08-07 (see changelog for details):
    ADDED: right click menu -> trash, delete, shred options
    ADDED: column types can be changed and saved individually to each panel
    (each side)
    --architecture-- refactoring in the view. things might be a bit unstable
    ADDED: select remote encoding menu for fish, ftp and sftp protocols
    ADDED: clear-location-bar button a-la konqueror (configurable)
    ADDED: permissions column as octal numbers
    ADDED: right-click menu now has a "create new..." submenu
    ADDED: ctrl-alt-enter opens the current folder in a new tab
    ADDED: calculate space in archives and remote FS (KDE >= 3.3.0)
    ADDED: synchronize selected files
    ADDED: colorful synchronizer :-)

* Fri Jul 22 2005 Nick S. Grechukh <gns@altlinux.ru> 1.60.0-alt1.beta2.cvs20050721.1
- 20050721: see changelog. AFAIK speed on big directories VERY improved.

* Thu Apr 07 2005 Nick S. Grechukh <gns@altlinux.ru> 1.60.0-alt1.beta2.cvs20050406
- new snapshot (unstable branch)

* Thu Jan 20 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.51-alt1.stable.1
- Rebuilt with libstdc++.so.6.

* Wed Dec 15 2004 Nick S. Grechukh <gns@altlinux.ru> 1.51-alt1.stable
- 1.51. thanks to Valery Inozemtsev aka shrek@ for help!

* Tue Oct 19 2004 Nick S. Grechukh <gns@altlinux.ru> 1.50-alt1.beta1
- new beta version

* Wed Oct 13 2004 Nick S. Grechukh <gns@altlinux.ru> 1.40-alt2.5.cvs.20041011
- new snapshot

* Tue Aug 31 2004 Nick S. Grechukh <gns@altlinux.ru> 1.40-alt2.4.cvs.20040831
new snapshot. Features:
- when closing krusader, the tabs are saved and restored.
- new delete dialog box: lists the file names to be deleted
- iso protocol for viewing .iso cd/dvd images
- .. and more.

* Mon Aug 16 2004 Nick S. Grechukh <gns@altlinux.ru> 1.40-alt2.4.cvs.20040815
- new snapshot. fixed #4495

* Fri Aug 06 2004 Nick S. Grechukh <gns@altlinux.ru> 1.40-alt2.3stable
- rollback to stable version... (for M2.4)

* Thu Aug 05 2004 Nick S. Grechukh <gns@altlinux.ru> 1.40-alt2.2.cvs.20040801
- added comment and dirty workaround about buggy SMP build

* Wed Aug 04 2004 Nick S. Grechukh <gns@altlinux.ru> 1.40-alt2.1.cvs.20040801
- fixed build on SMP

* Tue Aug 03 2004 Nick S. Grechukh <gns@altlinux.ru> 1.40-alt1.2.cvs.20040801
- export KDEDIR and QTDIR - as temporary workaround

* Tue Aug 03 2004 Nick S. Grechukh <gns@altlinux.ru> 1.40-alt1.1.cvs.20040801
- fixed libpng buildreq

* Mon Aug 02 2004 Nick S. Grechukh <gns@altlinux.ru> 1.40-alt1.cvs.20040801
- new cvs snapshot. Specfile cleaned, according to ALT specfiles policy. Buildreq regenerated.

* Sun Jun 13 2004 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.40-alt0.2.beta1
- new description
- fix requires

* Tue Apr 13 2004 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.40-alt0.1.beta1
- 1.40-beta1

* Mon Mar 29 2004 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.30-alt3
- fix bugs

* Tue Jan 27 2004 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.30-alt2
- fix builrequires

* Tue Dec 09 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.30-alt1
- 1.30

* Wed Oct 01 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.20-alt2
- new buildrequires and rebuilding in hasher

* Sun Jun 22 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.20-alt1
- 1.20

* Mon Feb 03 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.11-alt3
- rebuild in new kde

* Sun Jan 26 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.11-alt2
- new requires and buildrequires

* Sat Nov 16 2002 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.11-alt1
- 1.11
- rebuild for kde-3.1

* Fri Sep 20 2002 Sergey V Turchin <zerg@altlinux.ru> 1.10-alt1
- new version
- build with gcc3.2

* Thu Jun 04 2002 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Thu Jan 03 2002 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.0-alt1
- 1.0

* Tue Jan 01 2002 Shie Erlich & Rafi Yanai <krusader@users.sourceforge.net> Releaze version 1.0
- 1.0
