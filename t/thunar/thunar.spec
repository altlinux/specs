%def_disable docs
# Upstream tests are broken for now:
# new function thunarx_provider_module_unuse is not
# in the thunarx.symbols list.
%def_disable check

Name: thunar
Version: 4.19.3
Release: alt1

Summary: Thunar File Manager for the Xfce Desktop Environment
Summary (ru_RU.UTF-8): Файловый менеджер Thunar
Group: Graphical desktop/XFce
License: GPLv2+ and LGPLv2+
Url: https://docs.xfce.org/xfce/thunar/start
Packager: Xfce Team <xfce@packages.altlinux.org>

Vcs: https://gitlab.xfce.org/xfce/thunar.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-xfce4 >= 0.2.0

BuildRequires: xfce4-dev-tools
BuildRequires: libxfce4panel-gtk3-devel >= 4.12.0 libxfconf-devel >= 4.12.0 libexo-gtk3-devel >= 4.19.0
BuildRequires: libxfce4util >= 4.17.2 libxfce4ui-gtk3-devel >= 4.17.6
BuildRequires: libSM-devel libexif-devel libpcre2-devel
BuildRequires: libpango-devel
BuildRequires: libnotify-devel libgudev-devel
BuildRequires: libpolkit-devel
BuildRequires: desktop-file-utils
# NOTE: gtk-doc is required by build system even if docs are disabled.
BuildRequires: gtk-doc

%define _unpackaged_files_terminate_build 1

Requires: lib%name = %version-%release
Requires: eject
Requires: exo-utils
Requires: xfconf-utils

Obsoletes: Thunar < 1.3.1
Provides: Thunar = %version-%release

%description
Thunar File Manager for the Xfce desktop environment.

%description -l ru_RU.UTF-8
Файловый менеджер Thunar используемый в окружении рабочего стола Xfce.

%package -n lib%name-devel
Summary: Development files for %name
Group: Graphical desktop/XFce
License: LGPLv2+
Requires: lib%name = %version-%release
Obsoletes: libThunar-devel < 1.3.1
Provides: libThunar-devel = %version-%release

%description -n lib%name-devel
This package contains development files required to build
%name-based software.

%package -n lib%name
Summary: Shared libraries for %name
Group: Graphical desktop/XFce
License: LGPLv2+
Obsoletes: libThunar < 1.3.1
Provides: libThunar = %version-%release

%description -n lib%name
This package contains libraries for %name.

%if_enabled docs
%package -n lib%name-devel-doc
Summary: Development documentation for lib%name
Group: Development/Documentation
License: GFDL-1.1+
BuildArch: noarch

%description -n lib%name-devel-doc
This package contains development documentation for lib%name.
%endif

%prep
%setup
%patch -p1
%xfce4_cleanup_version

%build
%xfce4reconf
%configure \
	--disable-static \
	--enable-maintainer-mode \
	--enable-largefile \
	--enable-exif \
	--enable-pcre2 \
	--enable-gio-unix \
	--with-custom-thunarx-dirs-enabled=no \
%if_enabled docs
	--enable-gtk-doc \
%else
	--disable-gtk-doc \
%endif
	--enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang thunar
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Filesystem \
	--add-category=FileTools \
	%buildroot%_desktopdir/thunar-bulk-rename.desktop

%check
make check

%files -f thunar.lang
%doc README.md NEWS AUTHORS
%config(noreplace) %_sysconfdir/xdg/Thunar/
%_bindir/*
%_desktopdir/*
%_man1dir/*
%_datadir/dbus-1/services/*
%_datadir/polkit-1/actions/org.xfce.thunar.policy
%_datadir/metainfo/org.xfce.thunar.appdata.xml
%_datadir/Thunar
%_datadir/xfce4/panel/plugins/*.desktop
%_user_unitdir/thunar.service
%_libdir/xfce4/panel/plugins/*.so
%exclude %_libdir/xfce4/panel/plugins/*.la
%dir %_libdir/thunarx-*/
%_libdir/thunarx-*/*.so
%_libdir/Thunar/
%_iconsdir/hicolor/*/*/*
%_docdir/thunar

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_pkgconfigdir/*.pc
%_includedir/thunarx-*/
%_libdir/*.so

%if_enabled docs
%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/*
%endif

%exclude %_libdir/thunarx-*/*.la

%changelog
* Wed Jul 31 2024 Mikhail Efremov <sem@altlinux.org> 4.19.3-alt1
- Patch from upstream:
  + I18n: Update po/LINGUAS list.
- Used _user_unitdir macro.
- Updated to 4.19.3.

* Thu May 30 2024 Mikhail Efremov <sem@altlinux.org> 4.19.2-alt1
- Disabled tests.
- Use upstream Russian translation.
- Dropped html documentation.
- Updated to 4.19.2.

* Tue Jan 02 2024 Mikhail Efremov <sem@altlinux.org> 4.18.10-alt1
- Updated to 4.18.10.

* Fri Dec 29 2023 Mikhail Efremov <sem@altlinux.org> 4.18.9-alt1
- Updated to 4.18.9.

* Wed Oct 25 2023 Mikhail Efremov <sem@altlinux.org> 4.18.8-alt1
- Minor spec cleanup.
- Updated to 4.18.8.

* Mon Sep 04 2023 Mikhail Efremov <sem@altlinux.org> 4.18.7-alt1
- Updated to 4.18.7.

* Tue May 02 2023 Mikhail Efremov <sem@altlinux.org> 4.18.6-alt1
- Updated to 4.18.6.

* Tue Apr 18 2023 Mikhail Efremov <sem@altlinux.org> 4.18.4-alt2
- Don't use _user_unitdir macro.

* Mon Feb 27 2023 Mikhail Efremov <sem@altlinux.org> 4.18.4-alt1
- Updated to 4.18.4.

* Sat Jan 21 2023 Mikhail Efremov <sem@altlinux.org> 4.18.3-alt1
- Updated to 4.18.3.

* Tue Jan 10 2023 Mikhail Efremov <sem@altlinux.org> 4.18.2-alt1
- Updated to 4.18.2.

* Thu Dec 22 2022 Mikhail Efremov <sem@altlinux.org> 4.18.1-alt1
- Used our own Russian translation (merged with upstream translation).
- Updated to 4.18.1.

* Thu Dec 15 2022 Mikhail Efremov <sem@altlinux.org> 4.18.0-alt1
- thunar-thumbnailer: Check that pointer is not NULL.
- Updated to 4.18.0.

* Thu Dec 01 2022 Mikhail Efremov <sem@altlinux.org> 4.17.12-alt1
- Updated to 4.17.12.

* Tue Nov 01 2022 Mikhail Efremov <sem@altlinux.org> 4.17.11-alt1
- Updated to 4.17.11.

* Mon Oct 17 2022 Mikhail Efremov <sem@altlinux.org> 4.17.10-alt1
- Updated to 4.17.10.

* Mon Jul 11 2022 Mikhail Efremov <sem@altlinux.org> 4.17.9-alt1
- Dropped obsoleted patch.
- Updated to 4.17.9.

* Mon Apr 25 2022 Mikhail Efremov <sem@altlinux.org> 4.17.8-alt2
- Fixed plugin menu (patch from upstream git).
- Updated ALT Russian translation.

* Sun Apr 03 2022 Mikhail Efremov <sem@altlinux.org> 4.17.8-alt1
- Updated BR.
- Dropped libgamin-devel from BR.
- Updated to 4.17.8.

* Thu Jan 20 2022 Mikhail Efremov <sem@altlinux.org> 4.17.7-alt2
- Use our own Russian translation (closes: #41698).
- Use _user_unitdir macro.

* Tue Nov 23 2021 Mikhail Efremov <sem@altlinux.org> 4.17.7-alt1
- Updated to 4.17.7.

* Mon Sep 27 2021 Mikhail Efremov <sem@altlinux.org> 4.17.6-alt1
- Updated to 4.17.6.

* Mon Sep 13 2021 Mikhail Efremov <sem@altlinux.org> 4.17.5-alt1
- Updated to 4.17.5.

* Thu Jul 22 2021 Mikhail Efremov <sem@altlinux.org> 4.17.4-alt1
- Updated to 4.17.4.

* Wed May 12 2021 Mikhail Efremov <sem@altlinux.org> 4.16.8-alt1
- Updated to 4.16.8.

* Sun Mar 21 2021 Mikhail Efremov <sem@altlinux.org> 4.16.6-alt1
- Updated to 4.16.6.

* Wed Mar 10 2021 Mikhail Efremov <sem@altlinux.org> 4.16.5-alt1
- Updated to 4.16.5.

* Tue Feb 09 2021 Mikhail Efremov <sem@altlinux.org> 4.16.3-alt1
- Updated to 4.16.3.

* Wed Jan 13 2021 Mikhail Efremov <sem@altlinux.org> 4.16.2-alt1
- Updated to 4.16.2.

* Wed Dec 30 2020 Mikhail Efremov <sem@altlinux.org> 4.16.1-alt1
- Updated to 4.16.1.

* Wed Dec 23 2020 Mikhail Efremov <sem@altlinux.org> 4.16.0-alt1
- Updated to 4.16.0.

* Mon Nov 02 2020 Mikhail Efremov <sem@altlinux.org> 4.15.3-alt1
- Updated to 4.15.3.

* Thu Sep 03 2020 Mikhail Efremov <sem@altlinux.org> 4.15.2-alt1
- Updated url.
- Updated to 4.15.2.

* Mon May 25 2020 Mikhail Efremov <sem@altlinux.org> 1.8.15-alt1
- Updated Vcs tag.
- Updated to 1.8.15.

* Wed Mar 25 2020 Mikhail Efremov <sem@altlinux.org> 1.8.14-alt1
- Updated to 1.8.14.

* Tue Mar 24 2020 Mikhail Efremov <sem@altlinux.org> 1.8.13-alt1
- Updated to 1.8.13.

* Fri Jan 31 2020 Mikhail Efremov <sem@altlinux.org> 1.8.12-alt1
- Cleanup summary a bit.
- Drop unneded configure option.
- Enable development docs.
- Add Vcs tag.
- Fix license.
- Get rid of rpm-build-licenses.
- Updated to 1.8.12.

* Mon Nov 18 2019 Mikhail Efremov <sem@altlinux.org> 1.8.11-alt1
- Updated to 1.8.11.

* Mon Nov 11 2019 Mikhail Efremov <sem@altlinux.org> 1.8.10-alt1
- Updated to 1.8.10.

* Mon Aug 12 2019 Mikhail Efremov <sem@altlinux.org> 1.8.9-alt1
- Updated to 1.8.9.

* Sun Jul 21 2019 Mikhail Efremov <sem@altlinux.org> 1.8.8-alt1
- Updated to 1.8.8 (closes: #37025).

* Sun Jun 30 2019 Mikhail Efremov <sem@altlinux.org> 1.8.7-alt1
- Updated to 1.8.7.

* Tue May 21 2019 Mikhail Efremov <sem@altlinux.org> 1.8.6-alt1
- Updated to 1.8.6.

* Mon Jan 28 2019 Mikhail Efremov <sem@altlinux.org> 1.8.4-alt1
- Drop conflict with nautilus.
- Updated to 1.8.4.

* Fri Jan 25 2019 Mikhail Efremov <sem@altlinux.org> 1.8.3-alt1
- Add conflict with nautilus.
- Updated to 1.8.3.

* Thu Oct 25 2018 Mikhail Efremov <sem@altlinux.org> 1.8.2-alt2
- Fix systemd userdir location.

* Mon Oct 01 2018 Mikhail Efremov <sem@altlinux.org> 1.8.2-alt1
- Updated to 1.8.2.

* Tue Aug 07 2018 Mikhail Efremov <sem@altlinux.org> 1.8.1-alt1
- Fix description for libthunar-devel.
- Update url.
- Require exo-utils.
- Fix systemd userdir.
- thunarx.symbols: Add missing symbols.
- Updated to 1.8.1.

* Fri Apr 06 2018 Mikhail Efremov <sem@altlinux.org> 1.6.15-alt1
- Updated to 1.6.15.

* Fri Feb 16 2018 Mikhail Efremov <sem@altlinux.org> 1.6.14-alt1
- Updated to 1.6.14.

* Mon Nov 27 2017 Mikhail Efremov <sem@altlinux.org> 1.6.13-alt1
- Updated to 1.6.13.

* Mon Jul 03 2017 Mikhail Efremov <sem@altlinux.org> 1.6.12-alt1
- Disable silent rules.
- Fix changelog entry.
- Updated to 1.6.12.

* Tue Feb 14 2017 Mikhail Efremov <sem@altlinux.org> 1.6.11-alt1
- Drop obsoleted patch.
- Updated to 1.6.11.

* Fri Jul 22 2016 Mikhail Efremov <sem@altlinux.org> 1.6.10-alt3
- Patch from Xfce bugzilla (Xfce bug #12264, ALT bug #32271):
  + Take a reference to the ThunarFile before g_idle_add, release
    it after.

* Fri Feb 12 2016 Mikhail Efremov <sem@altlinux.org> 1.6.10-alt2
- Enable debug (minimum level).
- Fix potential buffer overflow (CVE-2013-7447).
- Updated translations from upstream git.
- Patches from upstream:
  + Fixing missing return value in standard view.
  + Fix crashes when reloading target file after move.

* Mon May 25 2015 Mikhail Efremov <sem@altlinux.org> 1.6.10-alt1
- Updated to 1.6.10.

* Mon May 18 2015 Mikhail Efremov <sem@altlinux.org> 1.6.9-alt1
- Updated to 1.6.9.

* Wed May 06 2015 Mikhail Efremov <sem@altlinux.org> 1.6.8-alt1
- Disable documentation build.
- Drop libstartup-notification-devel from BR.
- Updated to 1.6.8.

* Mon Apr 20 2015 Mikhail Efremov <sem@altlinux.org> 1.6.7-alt1
- Updated to 1.6.7.

* Fri Mar 06 2015 Mikhail Efremov <sem@altlinux.org> 1.6.6-alt1
- Updated to 1.6.6.

* Fri Feb 20 2015 Mikhail Efremov <sem@altlinux.org> 1.6.5-alt1
- Updated to 1.6.5.

* Mon Jan 12 2015 Mikhail Efremov <sem@altlinux.org> 1.6.4-alt1
- Fix Xfce name (XFce,XFCE -> Xfce).
- Drop obsoleted patch.
- Updated to 1.6.4.

* Mon May 06 2013 Mikhail Efremov <sem@altlinux.org> 1.6.3-alt1
- Updated to 1.6.3.

* Mon Mar 25 2013 Mikhail Efremov <sem@altlinux.org> 1.6.2-alt2
- Updated translations from upstream git.
- Fixes and improvements from upstream git:
  + Prepend and later reverse for collecting selection.
  + Allow keyboard shortcuts for user customizable actions
    (Xfce bug #1941).
  + Autotools updates.
  + Use utilities-terminal for default uca action
    (Xfce bug #9716).

* Thu Dec 27 2012 Mikhail Efremov <sem@altlinux.org> 1.6.2-alt1
- Updated to 1.6.2.

* Mon Dec 10 2012 Mikhail Efremov <sem@altlinux.org> 1.6.1-alt1
- Updated to 1.6.1.

* Mon Dec 03 2012 Mikhail Efremov <sem@altlinux.org> 1.6.0-alt1
- Drop obsoleted patches.
- Updated to 1.6.0.

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
