%define ver_major 3.4
%def_disable packagekit
%def_enable magic

%define nau_api_ver 3.0

Name: file-roller
Version: %ver_major.2
Release: alt1

Summary: An archive manager for GNOME
Summary (ru_RU.UTF-8): Архиватор для GNOME 2
License: %gpl2plus
Group: File tools
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz
Patch: %name-2.28.2-alt-7z.patch
Patch1: %name-3.3.90-alt-zip_command.patch

# From configure.in
%define glib_ver 2.29.14
%define gtk_ver 3.0.2
%define nautilus_ver 2.91.91

%define desktop_file_utils_ver 0.8

Requires: tar gzip bzip2 ncompress lzop binutils arj lha unrar zip unzip p7zip lzma-utils
# Requires: cdrecord # for .iso support

BuildPreReq: rpm-build-gnome rpm-build-licenses
# From configure.in
BuildPreReq: gnome-doc-utils
BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: libgio-devel >= %glib_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libnautilus-devel >= %nautilus_ver
BuildPreReq: intltool >= 0.35.0
BuildPreReq: desktop-file-utils >= %desktop_file_utils_ver
BuildRequires: scrollkeeper libSM-devel
%{?_enable_magic:BuildRequires: libmagic-devel}

%description
File Roller is an archive manager for the GNOME environment.  This means that
you can : create and modify archives; view the content of an archive; view a
file contained in the archive; extract files from the archive.
File Roller is only a front-end (a graphical interface) to archiving programs
like tar and zip. The supported file types are :
    * Tar archives uncompressed (.tar) or compressed with
          * gzip (.tar.gz, .tgz)
          * bzip (.tar.bz, .tbz)
          * bzip2 (.tar.bz2, .tbz2)
          * compress (.tar.Z, .taz)
          * lzop (.tar.lzo, .tzo)
    * Ar archives (.ar)
    * Arj archives (.arj)
    * Jar archives (.jar, .ear, .war)
    * Lha archives (.lzh)
    * Rar archives (.rar)
    * Zip archives (.zip)
    * 7-Zip archives (.7z)
    * Single files compressed with gzip, bzip, bzip2, compress, lzop

%description -l ru_RU.UTF-8
File Roller - архиватор для рабочего стола GNOME. С его помощью можно:
создавать архивы и изменять их содержимое, читать оглавление архивов,
просматривать и распаковывать заключенные в архив файлы.
File Roller является графической оболочкой к различным средствам сжатия
данных. В число поддерживаемых программой типов архивов входят:
    * Архивы Tar как несжатые (.tar), так и сжатые посредством
          * gzip (.tar.gz, .tgz)
          * bzip (.tar.bz, .tbz)
          * bzip2 (.tar.bz2, .tbz2)
          * compress (.tar.Z, .taz)
          * lzop (.tar.lzo, .tzo)
    * Ar архивы (.ar)
    * Arj архивы (.arj)
    * Jar архивы (.jar, .ear, .war)
    * Lha архивы (.lzh)
    * Rar архивы (.rar)
    * Zip архивы (.zip)
    * 7-Zip архивы (.7z)
    * Отдельные файлы сжатые при помощи gzip, bzip, bzip2, compress, lzop.

%prep
%setup -q
%patch
%patch1

rm -f data/%name.desktop{,.in}

%build
%configure \
    --enable-nautilus-actions \
    --disable-schemas-compile \
    --disable-scrollkeeper \
    --disable-static \
    %{subst_enable magic} \
    %{subst_enable packagekit}

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/*
%_libdir/nautilus/extensions-%nau_api_ver/*.so
%_libexecdir/file-roller-server
%dir %_libexecdir/%name
%_libexecdir/%name/*.sh
%_libexecdir/%name/rpm2cpio
%dir %_datadir/%name
%_datadir/%name/*
%_datadir/dbus-1/services/org.gnome.FileRoller.service
%_desktopdir/*
%_iconsdir/hicolor/*/apps/%name.png
%config %_datadir/glib-2.0/schemas/*
%_datadir/GConf/gsettings/%name.convert
%doc AUTHORS NEWS README


%exclude %_libdir/nautilus/extensions-%nau_api_ver/*.la

%changelog
* Tue May 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Tue Apr 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Tue Mar 20 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.92-alt1
- 3.3.92

* Thu Mar 01 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt2
- fixed command line for zip (ALT #27011)

* Tue Nov 15 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Mon Oct 17 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Sun Oct 16 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Fri Sep 09 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.91-alt1
- 3.1.91

* Tue May 24 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Tue Apr 26 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.2-alt1
- 2.32.2

* Tue Nov 16 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Tue Oct 19 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Tue Sep 14 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.92-alt1
- 2.31.92

* Mon Jun 21 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2

* Tue Apr 27 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1.1-alt1
- 2.30.1

* Tue Mar 30 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Tue Mar 09 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.92-alt1
- 2.29.92

* Thu Feb 25 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.91-alt1
- 2.29.91

* Tue Feb 09 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.90-alt1
- 2.29.90

* Tue Jan 26 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.5-alt1
- 2.29.5

* Sun Jan 17 2010 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt2
- don't allow to use 7z for read/write zip archives (closes #21150)

* Tue Jan 12 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.4-alt1
- 2.29.4

* Tue Dec 22 2009 Yuri N. Sedunov <aris@altlinux.org> 2.29.3-alt1
- 2.29.3

* Tue Dec 15 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt1
- 2.28.2

* Tue Oct 20 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Tue Sep 22 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Tue Aug 25 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.91-alt1
- 2.27.91

* Tue Jun 30 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.3-alt1
- 2.26.3

* Tue May 19 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2

* Tue Apr 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Sat Mar 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0
- updated buildreqs

* Tue Jan 13 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.3-alt1
- 2.24.3

* Mon Nov 24 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt1
- 2.24.2
- removed obsolete %%post* scripts

* Tue Oct 21 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1

* Sun Sep 28 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.0-alt1
- new version (2.24.0)

* Sat May 03 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.2-alt1
- new version (2.22.2)
- add Packager

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 2.22.1-alt1.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for file-roller

* Tue Apr 08 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.1-alt1
- new version (2.22.1)

* Sun Mar 30 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- new version (2.22.0)

* Wed Oct 17 2007 Alexey Rusakov <ktirf@altlinux.org> 2.20.1-alt1
- new version (2.20.1)
- added intltoolize invocation to fix building with new intltool.

* Mon Jul 23 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.4-alt2
- fixed packaging on x86_64.

* Thu Jul 19 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.4-alt1
- new version (2.18.4)
- use macros from rpm-build-gnome; replaced %%__autoreconf macro with a plain
  autoreconf call
- updated files list

* Tue Feb 06 2007 Alexey Rusakov <ktirf@altlinux.org> 2.16.3-alt1
- new version (2.16.3)
- dropped zoo support, as zoo is no more in Sisyphus

* Sat Oct 07 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.0-alt1
- new version (2.16.0)
- updated dependencies

* Sun Jun 04 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.3-alt1
- new version (2.14.3)

* Sun Apr 16 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.1-alt1
- new version (2.14.1)
- spec cleanup

* Tue Feb 28 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.92-alt1
- new version (2.13.92)
- updated dependencies, cleaned up the spec.
- removed Debian menu support

* Fri Sep 30 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.0-alt1
- 2.12.0

* Sat Apr 23 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.3-alt1
- 2.10.3

* Wed Apr 13 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.2-alt1
- 2.10.2

* Thu Mar 31 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.1-alt1
- 2.10.1

* Mon Mar 07 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Wed Dec 08 2004 Vyacheslav Dikonov <slava@altlinux.ru> 2.9.0-alt3
- requires GConf2, scrollkeeper, desktop-file-utils
- run %%{update,clean}_desktopdb in %%post{un,}
  desktop-file-utils >= 0.8 required for build.

* Sun Dec 05 2004 Vyacheslav Dikonov <slava@altlinux.ru> 2.9.0-alt2
- removed broken *desktopdb macros

* Wed Nov 24 2004 Vyacheslav Dikonov <slava@altlinux.ru> 2.9.0-alt1
- 2.9.0
- requires all backends

* Sat Nov 20 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.8.3-alt1
- Updated to 2.8.3
- Spec cleanup

* Thu Jun 24 2004 Vyacheslav Dikonov <slava@altlinux.ru> 2.6.2-alt1
- new version

* Sat May 15 2004 Sergey N. Yatskevich <syatskevich@altlinux.ru> 2.6.1-alt2
- new version

* Fri Oct 17 2003 Vyacheslav Dikonov <slava@altlinux.ru> 2.4.0.1-alt1
- new version

* Sat Nov 02 2002 Vyacheslav Dikonov <slava@altlinux.ru> 2.0.3-alt2
- translation update, missing docs fixed

* Mon Oct 14 2002 AEN <aen@altlinux.ru> 2.0.3-alt1
- new version

* Wed Oct 09 2002 AEN <aen@altlinux.ru> 2.0.2-alt1
- first build for Sisyphus
