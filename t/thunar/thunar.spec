Name: thunar
Version: 1.4.0
Release: alt3

Summary: Thunar File Manager for the XFce Desktop Environment
Summary (ru_RU.UTF-8): Файловый менеджер Thunar
Group: Graphical desktop/XFce
License: %gpl2plus
Url: http://thunar.xfce.org
Packager: XFCE Team <xfce@packages.altlinux.org>

# Upstream: git://git.xfce.org/xfce/thunar
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 >= 0.1.0 xfce4-dev-tools
BuildPreReq: libxfce4panel-devel >= 4.8 libxfconf-devel >= 4.8 libexo-devel >= 0.6.0 libxfce4ui-devel >= 4.8
# Automatically added by buildreq on Thu Jan 22 2009
BuildRequires: gtk-doc intltool libSM-devel libdbus-glib-devel libexif-devel libgamin-devel libpcre-devel libstartup-notification-devel time
BuildRequires: libnotify4-devel libgudev-devel
BuildRequires: desktop-file-utils

Requires: lib%name = %version-%release
Requires: eject

Obsoletes: Thunar < 1.3.1
Provides: Thunar = %version-%release

%description
Thunar File Manager for the XFce desktop environment.

%description -l ru_RU.UTF-8
Файловый менеджер Thunar используемый в окружении рабочего стола Xfce.

%package -n lib%name-devel
Summary: devel files for Thunar
Group: Graphical desktop/XFce
Requires: lib%name = %version-%release
Obsoletes: libThunar-devel < 1.3.1
Provides: libThunar-devel = %version-%release

%description -n lib%name-devel
This package contains development files required to build build
%name-based software..

%package -n lib%name
Summary: Shared libraries for Thunar
Group: Graphical desktop/XFce
Obsoletes: libThunar < 1.3.1
Provides: libThunar = %version-%release

%description -n lib%name
This package contains libraries for Thunar.

%prep
%setup
%patch -p1

%build
%xfce4reconf
%configure \
	--disable-static \
	--enable-maintainer-mode \
	--enable-largefile \
	--enable-startup-notification \
	--enable-xml2po \
	--enable-dbus \
	--enable-gtk-doc \
	--enable-gen-doc \
	--enable-exif \
	--enable-pcre \
	--enable-gio-unix \
	--enable-debug=no
%make_build

%install
%makeinstall_std
%find_lang Thunar
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Filesystem \
	--add-category=FileTools \
	%buildroot%_desktopdir/Thunar-bulk-rename.desktop

%check
make check

%files -f Thunar.lang
%doc README NEWS AUTHORS
%config(noreplace) %_sysconfdir/xdg/Thunar/
%_bindir/*
%_desktopdir/*
%_man1dir/*
%_pixmapsdir/*
%_datadir/dbus-1/services/*
%_datadir/Thunar
%_datadir/xfce4/panel/plugins/*.desktop
%_libdir/xfce4/panel/plugins/*.so
%exclude %_libdir/xfce4/panel/plugins/*.la
%dir %_libdir/thunarx-*/
%_libdir/thunarx-*/*.so
%_libdir/Thunar/
%_iconsdir/hicolor/*/*/*
%_docdir/Thunar

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_datadir/gtk-doc/html/*
%_pkgconfigdir/*.pc
%_includedir/thunarx-*/
%_libdir/*.so
%exclude %_libdir/thunarx-*/*.la

%changelog
* Mon May 21 2012 Mikhail Efremov <sem@altlinux.org> 1.4.0-alt3
- Fix DSO linking.

* Thu May 03 2012 Mikhail Efremov <sem@altlinux.org> 1.4.0-alt2
- Patch from Xfce bug #7110:
  + Sorting files, switching to g_utf8_collate_key_for_filename().
- Fix panel plugin's desktop file path.

* Sun Apr 29 2012 Mikhail Efremov <sem@altlinux.org> 1.4.0-alt1
- Updated to 1.4.0.

* Tue Apr 17 2012 Mikhail Efremov <sem@altlinux.org> 1.3.2-alt1
- Updated to 1.3.2.

* Mon Apr 09 2012 Mikhail Efremov <sem@altlinux.org> 1.3.1-alt1
- Rename package: Thunar -> thunar.
- Drop obsoleted patches.
- Updated to 1.3.1.

* Wed Mar 07 2012 Mikhail Efremov <sem@altlinux.org> 1.3.0-alt12
- Patches from upstream:
  + Fix handling %%U when launching multiple files with an app.
  + Improve sorting of file names that include numbers
    (closes: #26282).
  + Fix crash when removing an ancestor of the current folder.

* Mon Jan 16 2012 Mikhail Efremov <sem@altlinux.org> 1.3.0-alt11
- Don't create trash on nfs and cifs filesystems too.

* Wed Jan 11 2012 Mikhail Efremov <sem@altlinux.org> 1.3.0-alt10
- Rebuild with xfce4-panel-4.9.

* Fri Dec 30 2011 Mikhail Efremov <sem@altlinux.org> 1.3.0-alt9
- Build with libexo-0.7.0.

* Tue Dec 06 2011 Mikhail Efremov <sem@altlinux.org> 1.3.0-alt8
- Patches from upstream:
  + Fix segfault when plugin returns a NULL suffix.
  + Fix sorting of filenames with large numbers.
- Don't try create trash on Windows filesystems (closes: #26662).

* Fri Oct 07 2011 Mikhail Efremov <sem@altlinux.org> 1.3.0-alt7
- Patches from upstream:
  + Allow exec bit of MS-DOS executables and MSI to be changed.
  + Show translated names of desktop files.
  + Prevent falling back to an unexpected locale.
  + Fix non-initialized variable.
  + Fix segfaults in case icons are missing or not found.
- Drop obsoleted patch.
- Update fix-crash-opening-mountable-drive.patch.
- Drop fix-thunar-settings-icon.patch.

* Wed Aug 31 2011 Mikhail Efremov <sem@altlinux.org> 1.3.0-alt6
- Fix format strings of display names (CVE-2011-1588).
- Updated Russian translation.
- Rename russian-translation.patch -> russian-documentation.patch.
- Fix thunar-settings icon.

* Fri Jun 10 2011 Mikhail Efremov <sem@altlinux.org> 1.3.0-alt5
- Require eject (closes: #25736).

* Wed May 25 2011 Mikhail Efremov <sem@altlinux.org> 1.3.0-alt4
- Update Russian documentation translation (by Artem Zolochevskiy).
- bulk-rename.desktop: Change category: Filesystem -> FileTools
    (patch from repocop).

* Fri May 20 2011 Mikhail Efremov <sem@altlinux.org> 1.3.0-alt3
- Add fix-smb.patch (closes: #25629).

* Sun Apr 17 2011 Mikhail Efremov <sem@altlinux.org> 1.3.0-alt2
- Build with libnotify-0.7.
- Patches from upstream git (fixes various crashes).
- Don't recognize empty 'http:' and 'https:' as URI (closes: #25443).

* Tue Feb 15 2011 Mikhail Efremov <sem@altlinux.org> 1.3.0-alt1
- Enable tests.
- Own forgotten dirs.
- Updated to 1.3.0.

* Tue Jan 25 2011 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1
- Drop thunar-remove-shorcuts-view-min-len.patch (obsolete).
- Drop thunar-vfs-get_eject.diff (obsolete).
- Remove Thunar-0.9.0-missing-audio-cds-for-volman.patch.
- Spec cleanup, tar.bz2 -> tar.
- Updated to 1.2.0 (closes: #22728).

* Tue May 25 2010 Denis Koryavov <dkoryavov@altlinux.org> 1.0.2-alt1
- New version.

* Wed Dec 23 2009 Denis Koryavov <dkoryavov@altlinux.org> 1.0.1-alt4
- Fix build width gtkdoc.

* Sun Jul 05 2009 Denis Koryavov <dkoryavov@altlinux.org> 1.0.1-alt3
- Added patch that removes minimal length limitation for width of shortcuts view pane.

* Mon May 25 2009 Denis Koryavov <dkoryavov@altlinux.org> 1.0.1-alt2
- Added autoconf and automake requirements. This is resolve problem with translation for item Make Link for some systems.

* Mon Apr 20 2009 Denis Koryavov <dkoryavov@altlinux.org> 1.0.1-alt1
- Xfce 4.6.1

* Sun Apr 12 2009 Denis Koryavov <dkoryavov@altlinux.org> 1.0.0-alt1
- Xfce 4.6.0

* Tue Jan 27 2009 Eugene Ostapets <eostapets@altlinux.ru> 0.9.99.1-alt1
- Xfce 4.6rc1

* Thu Jan 22 2009 Eugene Ostapets <eostapets@altlinux.ru> 0.9.93-alt1
- Xfce 4.6 beta 3

* Fri Oct 24 2008 Eugene Ostapets <eostapets@altlinux.org> 0.9.91-alt1
- Xfce 4.6 beta1

* Wed Dec 12 2007 Eugene Ostapets <eostapets@altlinux.org> 0.9.0-alt2
- fix "Eject" menu for ejectable device
- fix detect audio cd

* Mon Nov 19 2007 Eugene Ostapets <eostapets@altlinux.org> 0.9.0-alt1
- Xfce 4.4.2 release

* Mon Jan 22 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.8.0-alt0.1
- Xfce 4.4 release

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.5.0-alt1.1
- Rebuilt due to libdbus-1.so.2 -> libdbus-1.so.3 soname change.

* Sun Nov 05 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.5.0-alt1
- Xfce 4.4rc2

* Mon Oct 30 2006 Eugene Ostapets <eostapets@altlinux.ru>  0.4.0rc1-alt2
- Fix buildreq and cleanup spec

* Tue Nov 15 2005 Eugene Ostapets <eostapets@altlinux.ru> 0.4.0rc1-alt1
- 4.4rc1
