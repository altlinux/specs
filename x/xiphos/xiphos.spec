%undefine __cmake_in_source_build

Name: xiphos
Version: 4.3.2.14
Release: alt1
Summary: Bible study and research tool
Url: http://xiphos.org/
Group: Text tools
License: GPL-2.0
Source: https://github.com/crosswire/xiphos/releases/download/%version/%name-%version.tar.xz
Source44: %name.watch
Patch: xiphos-4.2.1-glibc.patch
#Patch1:         find_biblesync.patch
Patch2:         xiphos-glib.patch
Patch3:         find_biblesync.patch

Requires: sword yelp
Provides: gnomesword
Obsoletes: gnomesword

BuildRequires(pre): rpm-macros-cmake
BuildRequires: biblesync-devel >= 2.0.1
BuildRequires: cmake desktop-file-utils intltool libGConf libdbus-glib-devel libdbus-devel 
BuildRequires: libappstream-glib libdbus-glib-devel libminizip-devel libwebkit2gtk-devel  libdatrie-devel libjpeg-devel 
BuildRequires: libsword-devel libwebkitgtk4-devel libxml2-devel yelp-tools zip bzip2-devel libbrotli-devel 
BuildRequires: gcc gcc-c++ 
BuildRequires:  pkgconfig(dbus-glib-1)

%description
Xiphos (formerly known as GnomeSword) is a Bible study application for GNOME,
a graphical desktop environment which is available for Linux and UNIX. Xiphos
is based on The SWORD Project by the CrossWire Bible Society, a framework for
providing tools useful for studying the Bible and additional information like
commentaries, dictionaries, and other texts using your computer.

%prep
%setup
#patch -p2
#patch1 -p2
#patch2 -p1
rm -rf src/biblesync

echo %{version} >cmake/source_version.txt

%patch3 -p1


%build
export CFLAGS="%{optflags} -Wno-dev -Wno-return-type"
export CXXFLAGS="%{optflags} -Wno-dev -Wno-return-type `pkg-config --cflags dbus-glib`"
export PYTHON="%{_bindir}/python3"
%cmake -DEPUB:BOOL=OFF -DCMAKE_INSTALL_DOCDIR:PATH=%{_docdir}/%{name} -DPOSTINST:BOOL=OFF
%cmake_build


%install
%cmake_install

desktop-file-install --delete-original         \
    --add-category=X-Bible                     \
    --add-category=X-Religion                  \
    --dir=%{buildroot}%{_datadir}/applications \
    --copy-name-to-generic-name                \
    %{buildroot}%{_datadir}/applications/xiphos.desktop


# package docs with macro
#rm -frv %{buildroot}%{_docdir}/%{name}

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README.md RELEASE-NOTES TODO COPYING
%_bindir/*
%_datadir/metainfo/%name.appdata.xml
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%_datadir/%name
%_datadir/help
%_datadir/doc/%name
%_datadir/locale/*/LC_MESSAGES/%name.mo
%_man1dir/%{name}*

%changelog
* Wed Nov 26 2025 Ilya Mashkin <oddity@altlinux.ru> 4.3.2.14-alt1
- 4.3.2.14

* Wed Apr 28 2021 Arseny Maslennikov <arseny@altlinux.org> 4.2.1-alt2.1
- NMU: spec: adapted to new cmake macros.

* Fri Apr 16 2021 Grigory Ustinov <grenka@altlinux.org> 4.2.1-alt2
- Fixed FTBFS.

* Sat Jul 04 2020 Grigory Ustinov <grenka@altlinux.org> 4.2.1-alt1
- Build new version.

* Fri Nov 30 2018 Grigory Ustinov <grenka@altlinux.org> 4.1.0-alt4
- Fixed FTBFS (Add BR on python-modules-multiprocessing).

* Tue Oct 16 2018 Ildar Mulyukov <ildar@altlinux.ru> 4.1.0-alt3
- rebuild with newer libicu

* Sun Jun 10 2018 Ildar Mulyukov <ildar@altlinux.ru> 4.1.0-alt2
- add dep on `sword` for in-sword localizaton

* Wed May 23 2018 Ildar Mulyukov <ildar@altlinux.ru> 4.1.0-alt1
- new version

* Fri Sep 15 2017 Ildar Mulyukov <ildar@altlinux.ru> 4.0.6a-alt1
- new version

* Tue Nov 20 2012 Ildar Mulyukov <ildar@altlinux.ru> 3.1.5-alt1
- new version

* Thu Oct 21 2010 Ildar Mulyukov <ildar@altlinux.ru> 3.1.3-alt2
- gtkhtml-editor requirement quick fix

* Thu Jun 24 2010 Ildar Mulyukov <ildar@altlinux.ru> 3.1.3-alt1
- new version 3.1.3
- disable GECKO
- clean up spec

* Sat Sep 05 2009 Vitaly Lipatov <lav@altlinux.ru> 3.1.1-alt1
- new version 3.1.1 (with rpmrb script)

* Wed Jun 17 2009 Vitaly Lipatov <lav@altlinux.ru> 3.1-alt1
- new version 3.1 (with rpmrb script)

* Fri Dec 19 2008 Vitaly Lipatov <lav@altlinux.ru> 2.4.1-alt1
- new version 2.4.1 (with rpmrb script)

* Thu Jul 10 2008 Vitaly Lipatov <lav@altlinux.ru> 2.3.5-alt1
- new version 2.3.5
- update buildreq, build with libgtkhtml

* Mon Dec 24 2007 Vitaly Lipatov <lav@altlinux.ru> 2.3.1-alt2
- rebuild with new xulrunner

* Tue Nov 13 2007 Vitaly Lipatov <lav@altlinux.ru> 2.3.1-alt1
- new version 2.3.1 (with rpmrb script)
- update buildreq
- build with xulrunner, new sword 1.5.10

* Sun Jun 24 2007 Vitaly Lipatov <lav@altlinux.ru> 2.2.3-alt1
- new version 2.2.3 (with rpmrb script)

* Sun Dec 10 2006 Vitaly Lipatov <lav@altlinux.ru> 2.1.10-alt0.1
- new version 2.1.10 (with rpmrb script)

* Sun Sep 03 2006 Vitaly Lipatov <lav@altlinux.ru> 2.1.7-alt0.1
- new version
- remove debian menu

* Tue Dec 27 2005 Vitaly Lipatov <lav@altlinux.ru> 2.1.2-alt0.1cvs20051113
- new version

* Sun Nov 13 2005 Vitaly Lipatov <lav@altlinux.ru> 2.1.2-alt0.3cvs20050716
- fix %_datadir/%name owner

* Thu Sep 08 2005 Vitaly Lipatov <lav@altlinux.ru> 2.1.2-alt0.2cvs20050716
- try 2

* Sat Jul 16 2005 Vitaly Lipatov <lav@altlinux.ru> 2.1.2-alt0.1cvs20050716
- new 2.1.2 from CVS
- build with new sword
- NOTE: remove ~/.gnomesword-2.0 if one crashed

* Sun Mar 20 2005 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt0.5
- rebuild with GNOME 2.10
- set name of executable as gnomesword

* Sun Jan 23 2005 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt0.4
- rebuild with gcc3.4

* Thu Nov 04 2004 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt0.3
- menu file fixed

* Sun Oct 31 2004 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt0.2
- rebuld with libgal 2.2.3

* Fri Jul 30 2004 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt0.1
- first build for Sisyphus (unstable 2.1.1)

* Fri Mar 12 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0.0-2mdk
- Rebuild with latest gtkhtml/gal

* Mon Jan 19 2004 Buchan Milne <bgmilne@linux-mandrake.com> 2.0.0-1mdk
- 2.0.0
- rebuild for sword

* Sun Apr 27 2003 Buchan Milne <bgmilne@linux-mandrake.com> 0.7.9-1mdk
 - 0.7.9
 - Rebuild for gal

* Thu Mar 13 2003 Buchan Milne <bgmilne@linux-mandrake.com> 0.7.8-1mdk
- 0.7.8
- Cleanups
- ->contrib

* Wed Oct 09 2002 David Abilleira <david1@abilleira.com> 0.7.6-1mdk
- Updated to 0.7.6

* Wed Oct 09 2002 David Abilleira <david1@abilleira.com> 0.7.5-1mdk
- First package
