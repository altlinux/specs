Name: fbreader
Version: 0.12.10
Release: alt3
Summary: E-Book Reader
Summary (ru_RU.UTF-8): Программа для чтения электронных книг (E-Book, Ebook)
License: GPL
Group: Text tools
URL: http://only.mawhrin.net/fbreader/
Source: %name-sources-%version.tar
Source1: watch
Source2: %{name}16.png
Source3: %{name}32.png
Source4: %{name}48.png
Source5: x-fb2.desktop
Patch1: %name-c++.patch

BuildRequires: bzlib-devel gcc-c++ libcurl-devel libexpat-devel libfribidi-devel liblinebreak-devel-static libqt4-devel libsqlite3-devel

%description
E-Book Reader. Supports several e-book formats: fb2 (fictionbook), html, plucker, palmdoc, zTxt, plain text.
--

%description -l ru_RU.UTF-8
Программа для чтения электронных книг (E-book, Ebook). Поддерживает форматы: fb2 (fictionbook), html, plucker, palmdoc, zTxt, plain text.
---

%prep
%setup -q
%patch1 -p1

%build
export QTDIR=%_qt4dir
%make LIBDIR=%_libdir INSTALLDIR=/usr TARGET_ARCH=desktop UI_TYPE=qt4 TARGET_STATUS=release MOC=%_qt4dir/bin/moc UILIBS="-L%_qt4dir/lib -lQtGui"


%install
%__subst "s,mozilla,firefox," fbreader/data/default/external.desktop.xml
%__subst "s,FBReader.png,fbreader.png," fbreader/desktop/desktop
%make LIBDIR=%_libdir DESTDIR=%buildroot INSTALLDIR=/usr TARGET_ARCH=desktop UI_TYPE=qt4 TARGET_STATUS=release MOC=%_qt4dir/bin/moc UILIBS="-L%_qt4dir/lib -lQtGui" install
ln -s FBReader %buildroot%_bindir/fbreader
%__install -pD -m644 %SOURCE2 %buildroot%_miconsdir/%name.png
%__install -pD -m644 %SOURCE3 %buildroot%_niconsdir/%name.png
%__install -pD -m644 %SOURCE4 %buildroot%_liconsdir/%name.png
%__install -pD -m644 %SOURCE4 %buildroot%_liconsdir/%name.png
%__install -pD -m644 %SOURCE5 %buildroot%_datadir/mimelnk/application/x-fb2.desktop
echo "MimeType=application/x-zip-compressed-fb2;application/x-fb2;application/rtf;application/x-chm;application/vnd.palm" >>%buildroot%_datadir/applications/FBReader.desktop


%files
%_bindir/*
%_datadir/FBReader
%_datadir/pixmaps/*
%_datadir/zlibrary
%_libdir/*.so.*
%_libdir/zlibrary
%_datadir/applications/FBReader.desktop
%_datadir/mimelnk/application/x-fb2.desktop
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%changelog
* Mon May 23 2011 Anton Farygin <rider@altlinux.ru> 0.12.10-alt3
- added application/x-zip-compressed-fb2  mime type (closes: #25604)
- removed text/plain from mime-types (closes: #21149)

* Tue Nov 30 2010 Anton Farygin <rider@altlinux.ru> 0.12.10-alt2
- fix for build in new environment

* Tue Sep 28 2010 Anton Farygin <rider@altlinux.ru> 0.12.10-alt1
- new version

* Tue Apr 07 2009 Anton Farygin <rider@altlinux.ru> 0.10.7-alt1
- new version

* Mon Feb 09 2009 Anton Farygin <rider@altlinux.ru> 0.10.3-alt1
- new version

* Wed Jan 28 2009 Anton Farygin <rider@altlinux.ru> 0.10.2-alt1
- new version

* Fri Jan 16 2009 Anton Farygin <rider@altlinux.ru> 0.10.0-alt1
- new version

* Tue Nov 25 2008 Anton Farygin <rider@altlinux.ru> 0.8.17-alt2
- post-scripts removed

* Mon Mar 24 2008 Anton Farygin <rider@altlinux.ru> 0.8.17-alt1
- new version

* Fri Mar 21 2008 Anton Farygin <rider@altlinux.ru> 0.8.16-alt1
- new version

* Tue Feb 26 2008 Anton Farygin <rider@altlinux.ru> 0.8.15-alt1
- new version

* Mon Feb 11 2008 Anton Farygin <rider@altlinux.ru> 0.8.14-alt1
- new version

* Sun Jan 27 2008 Anton Farygin <rider@altlinux.ru> 0.8.12-alt1
- new version

* Thu Jan 17 2008 Anton Farygin <rider@altlinux.ru> 0.8.11-alt1
- new version

* Sat Dec 29 2007 Anton Farygin <rider@altlinux.ru> 0.8.9-alt1
- new version

* Wed Dec 19 2007 Anton Farygin <rider@altlinux.ru> 0.8.8a-alt1
- new version (#13724 fixed by upstrem)

* Fri Nov 30 2007 Anton Farygin <rider@altlinux.ru> 0.8.8-alt1
- new version
- added watch file to sources

* Fri Nov 09 2007 Anton Farygin <rider@altlinux.ru> 0.8.7b-alt1
- new version

* Tue Nov 06 2007 Anton Farygin <rider@altlinux.ru> 0.8.7a-alt1
- new version

* Thu Aug 30 2007 Anton Farygin <rider@altlinux.ru> 0.8.6c-alt1
- new version

* Tue Aug 07 2007 Anton Farygin <rider@altlinux.ru> 0.8.6-alt1
- new version

* Thu Jul 19 2007 Anton Farygin <rider@altlinux.ru> 0.8.5a-alt1
- new version

* Thu Jul 05 2007 Anton Farygin <rider@altlinux.ru> 0.8.4a-alt1
- new version

* Wed Jun 06 2007 Anton Farygin <rider@altlinux.ru> 0.8.4-alt1
- new version

* Tue May 22 2007 Anton Farygin <rider@altlinux.ru> 0.8.3d-alt1
- new version

* Thu May 10 2007 Anton Farygin <rider@altlinux.ru> 0.8.3-alt1
- new version

* Thu May 03 2007 Anton Farygin <rider@altlinux.ru> 0.8.2b-alt1
- new version

* Wed Apr 18 2007 Anton Farygin <rider@altlinux.ru> 0.8.2a-alt1
- new version

* Sun Apr 15 2007 Anton Farygin <rider@altlinux.ru> 0.8.2-alt1
- new version

* Thu Apr 12 2007 Anton Farygin <rider@altlinux.ru> 0.8.1d-alt1
- new version

* Wed Apr 04 2007 Anton Farygin <rider@altlinux.ru> 0.8.1c-alt1
- new version

* Thu Mar 29 2007 Anton Farygin <rider@altlinux.ru> 0.8.1b-alt1
- new version
- build qt4 variant
- removed included to mainstream patches

* Fri Mar 23 2007 Anton Farygin <rider@altlinux.ru> 0.8.1a-alt2
- fixed build on x86_64
- added mime associations

* Fri Mar 23 2007 Anton Farygin <rider@altlinux.ru> 0.8.1a-alt1
- new version
- added fbreader to menu

* Thu Feb 01 2007 Anton Farygin <rider@altlinux.ru> 0.7.4s-alt1
- new version

* Sun Jan 14 2007 Anton Farygin <rider@altlinux.ru> 0.7.4r-alt1
- new version

* Fri Dec 22 2006 Anton Farygin <rider@altlinux.ru> 0.7.4q-alt1
- new version

* Fri Dec 01 2006 Anton Farygin <rider@altlinux.ru> 0.7.4p-alt1
- new version

* Fri Nov 03 2006 Anton Farygin <rider@altlinux.ru> 0.7.4m-alt1
- new version

* Wed Oct 11 2006 Anton Farygin <rider@altlinux.ru> 0.7.4k-alt1
- new version
- build QT instead of GTK variant

* Tue Jul 11 2006 Anton Farygin <rider@altlinux.ru> 0.7.4g-alt1
- new version

* Mon Jul 10 2006 Anton Farygin <rider@altlinux.ru> 0.7.4f-alt1
- new version

* Thu Jun 15 2006 Anton Farygin <rider@altlinux.ru> 0.7.4d-alt1
- new version

* Tue Jun 13 2006 Anton Farygin <rider@altlinux.ru> 0.7.4c-alt1
- new version

* Fri Jun 09 2006 Anton Farygin <rider@altlinux.ru> 0.7.4b-alt1
- new version

* Tue May 30 2006 Anton Farygin <rider@altlinux.ru> 0.7.4a-alt1
- new version

* Mon May 29 2006 Anton Farygin <rider@altlinux.ru> 0.7.4-alt1
- new version

* Sat May 13 2006 Anton Farygin <rider@altlinux.ru> 0.7.3d-alt1
- new version

* Sat May 13 2006 Anton Farygin <rider@altlinux.ru> 0.7.3-alt2
- fix build with gcc 4.1

* Sat Apr 29 2006 Anton Farygin <rider@altlinux.ru> 0.7.3-alt1
- first build for Sisyphus

