Name:		last.fm
Version:	1.5.1.31879
Release:	alt4
Packager:	Fr. Br. George <george@altlinux.ru>
Summary:	Free Last.fm internet radio player on demand

Source0: http://cdn.last.fm/client/src/last.fm-%version.tar.bz2
Source1: lastfm-icons.tar.bz2
Source2: trayicons22.tar.bz2
Source3: %name.png
# gw these patches come from the unofficial Debian package at:
# http://mehercule.net/staticpages/index.php/lastfm
Patch0: build-fixes.diff
Patch1: reduce-linkage.diff
Patch2: gcc-4.3.patch
Patch3: no-fingerprint-lib.diff
Patch4: alsa-uses-qdebug.diff
Patch5: check-soundcard-errors.diff
Patch6: tray-icon-size.diff
Patch7: hide-scrobbledir-option.diff
Patch8: hide-crashreport-option.diff
Patch9: tray-volume.diff
Patch10: set-locale.diff
Patch11: cheaper-save-geometry.diff
Patch12: set-firstrun-status.diff
Patch13: dirpaths.diff
Patch52: browser-select.diff
Patch53: last.fm-1.5.1.31879-alt-glib2-2.32.0.patch
Patch54: last.fm-1.5.1.31879-alt-DSO-linkage.patch

License: GPL
Group: Sound
Url: http://www.last.fm/tools/downloads/

# Automatically added by buildreq on Sat Oct 18 2008
BuildRequires: gcc-c++ libalsa-devel libfftw3-devel libgpod-devel libmad-devel libqt4-devel libreadline libsamplerate-devel glib2-devel libportaudio2-devel

%description
With Last.fm on your computer you can scrobble your tracks, share your
music taste, listen to personalised radio streams, and discover new
music and people.

This is "official" version of http://last.fm client.

%prep
%setup -q -a 1 -n last.fm-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch52 -p1
%patch53 -p2
%patch54 -p1
##sed -i 's/ -lMoose/ -lmad -lMoose/' definitions.pro.inc
##sed -i 's@/usr/lib/glib@%_libdir/glib@g' src/mediadevices/ipod/ipod.pro
##sed -i 's@/usr/lib/glib@%_libdir/glib@g' src/mediadevices/gpod/gpod.pro

bzcat %SOURCE2 | tar -C bin/data/icons -xf -

chmod -R +r .
perl -pi -e "s|\r\n|\n|" ChangeLog

%build
qmake-qt4 -config release
%make_build CXX="g++ -fPIC $(pkg-config --cflags libgpod-1.0)"

cd i18n
lrelease-qt4 *.ts
mkdir -p ../bin/data/i18n
cp *.qm ../bin/data/i18n
cd ..

%install
mkdir -p %buildroot{%_bindir,%_libdir/}
cp -r bin %buildroot%_libdir/%name
for L in %buildroot%_libdir/%name/lib*; do
  mv $L %buildroot%_libdir/; \
  ln -s ../`basename $L` $L; \
done
cat << EOF > %buildroot%_bindir/%name
#!/bin/sh
export LD_LIBRARY_PATH=\$LD_LIBRARY_PATH:%_libdir/%name
%_libdir/%name/last.fm \$*
EOF
install -d -m 755 %buildroot%_datadir/services
cat > %buildroot%_datadir/services/lastfm.protocol << EOF
[Protocol]
 exec=%_bindir/%name "%%u"
 protocol=lastfm
 input=none
 output=none
 helper=true
 listing=
 reading=false
 writing=false
 makedir=false
 deleting=false
EOF

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Name=Last.FM Player
Comment=Play the last.fm internet radio
Exec=%name %%U
Icon=lastfm
Terminal=false
Type=Application
StartupNotify=true
Categories=Qt;AudioVideo;Audio;Player;
EOF

mkdir -p %buildroot%_datadir/icons
cp -r icons/crystalsvg %buildroot%_datadir/icons/hicolor
find %buildroot -name .svn |xargs rm -rf

rm -f %buildroot%_libdir/%name/*.{lib,dylib}
#gw the dirpaths patch expects the data files there:
mv %buildroot%_libdir/%name/data %buildroot%_datadir/lastfm

install -D %SOURCE3 %buildroot%_iconsdir/hicolor/64x64/apps/%name.png

%files
%doc ChangeLog README
%attr(755,root,root) %_bindir/%name
%_desktopdir/*
%_iconsdir/hicolor/*/apps/last*
%dir %_libdir/%name
%_libdir/%name
%_libdir/lib*
%_datadir/lastfm
%_datadir/services/lastfm.protocol

%changelog
* Sun May 20 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.5.1.31879-alt4
- fix DSO linking

* Fri Apr 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1.31879-alt3.1
- Fixed build with new glib2

* Mon Apr 18 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.1.31879-alt3
- fix build

* Mon Dec 21 2009 Fr. Br. George <george@altlinux.ru> 1.5.1.31879-alt2
- New libgpod rebuild

* Sun Mar 29 2009 Fr. Br. George <george@altlinux.ru> 1.5.1.31879-alt1
- Version up
- Renew package from MDV


* Mon Jan 19 2009 Götz Waschk <waschk@mandriva.org> 1:1.5.1.31879-3mdv2009.1
+ Revision: 331122
- rebuild for new libgpod

* Thu Jul 24 2008 Götz Waschk <waschk@mandriva.org> 1:1.5.1.31879-2mdv2009.0
+ Revision: 245080
- move icons to the right dir

  + Funda Wang <fundawang@mandriva.org>
    - clearify the license

* Thu Jul 17 2008 Funda Wang <fundawang@mandriva.org> 1:1.5.1.31879-1mdv2009.0
+ Revision: 236740
- New version 1.5.1.31879
- synch patches

  + Götz Waschk <waschk@mandriva.org>
    - fix source URL

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Tue Apr 15 2008 Götz Waschk <waschk@mandriva.org> 1:1.4.2.58240-3mdv2009.0
+ Revision: 194163
- fix typo in startup script

* Tue Apr 15 2008 Götz Waschk <waschk@mandriva.org> 1:1.4.2.58240-2mdv2009.0
+ Revision: 194054
- fix wrapper script (Moobyfr)

* Mon Apr 14 2008 Götz Waschk <waschk@mandriva.org> 1:1.4.2.58240-1mdv2009.0
+ Revision: 193156
- fix build on x86_64
- *** empty log message ***
- new version
- sync patches with the debian package
- update buildrequires
- fix build and installation

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Oct 05 2007 Götz Waschk <waschk@mandriva.org> 1:1.3.2.13-1mdv2008.1
+ Revision: 95558
- new version
- update patches

* Tue Sep 11 2007 Götz Waschk <waschk@mandriva.org> 1:1.3.1.0-2mdv2008.0
+ Revision: 84577
- fix browser selection patch
- fix menu category
- drop patch 20, fixing bug #33463
- remove unused patches

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Tue Jul 24 2007 Funda Wang <fundawang@mandriva.org> 1:1.3.1.0-1mdv2008.0
+ Revision: 54883
- Enable browser selection patch
- refresh patches
- New version

* Sat May 19 2007 Olivier Blin <oblin@mandriva.com> 1:1.1.3-2mdv2008.0
+ Revision: 28409
- add back menu macros

* Tue Apr 03 2007 Götz Waschk <waschk@mandriva.org> 1.1.3-1mdv2007.1
+ Revision: 150239
- fix buildrequires
- no more update-menus

  + Frederic Crozat <fcrozat@mandriva.com>
    - Release 1.1.3
    - Remove patches 0 (no longer needed), 10 (merged)
    - Update patches 2, 3, 4, 5, 6, 9, 13
    - Patch0 (mehercule): fix user config path
    - Patch14 (mehercule): fix translations support
    - Patch15 (mehercule): Add 22x22 tray icon

* Tue Jan 23 2007 Götz Waschk <waschk@mandriva.org> 1:1.0.9.6-1mdv2007.1
+ Revision: 112420
- Import lastfm-player

* Tue Jan 23 2007 Götz Waschk <waschk@mandriva.org> 1.0.9.6-1mdv2007.1
- synchronize patches with Debian
- new version

* Thu Aug 03 2006 Götz Waschk <waschk@mandriva.org> 1.0.0.1-0.2113.2mdv2007.0
- fix crash on play by switching to oss

* Tue Jul 25 2006 Götz Waschk <waschk@mandriva.org> 1:1.0.0.1-0.2113.1mdv2007.0
- drop patch
- new version

* Thu Jun 29 2006 Götz Waschk <waschk@mandriva.org> 1.1.90-0.2099.3mdv2007.0
- fix xdg menu

* Wed Jun 28 2006 Götz Waschk <waschk@mandriva.org> 1.1.90-0.2099.2mdv2007.0
- fix build with gcc 4.1
- xdg menu

* Fri Apr 07 2006 Götz Waschk <waschk@mandriva.org> 1.1.90-0.2099.1mdk
- drop patch
- change license to GPL
- new snapshot

* Fri Feb 10 2006 Götz Waschk <waschk@mandriva.org> 1.1.5-0.1988.1mdk
- fix build on x86_64
- new version

* Tue Jan 31 2006 Götz Waschk <waschk@mandriva.org> 1.1.4-0.1933.1mdk
- new version

* Tue Dec 20 2005 Götz Waschk <waschk@mandriva.org> 1.1.3-0.1907.1mdk
- new version

* Mon Dec 12 2005 Götz Waschk <waschk@mandriva.org> 1.1.1-0.1892.3mdk
- fix buildrequires

* Sun Dec 11 2005 Anssi Hannula <anssi.hannula@gmail.com> 1.1.1-0.1892.2mdk
- fix lib64 build

* Wed Dec 07 2005 Götz Waschk <waschk@mandriva.org> 1.1.1-0.1892.1mdk
- fix build
- ne version

* Sat Oct 01 2005 Götz Waschk <waschk@mandriva.org> 1.0.4-1mdk
- New release 1.0.4

* Fri Aug 26 2005 Götz Waschk <waschk@mandriva.org> 1.0.3-1mdk
- new version

* Tue Aug 16 2005 Götz Waschk <waschk@mandriva.org> 1.0.1-1mdk
- fix qmake call
- fix the version number

* Sat Aug 13 2005 Götz Waschk <waschk@mandriva.org> 0-0.20050812.4mdk
- fix the program icons

* Sat Aug 13 2005 Götz Waschk <waschk@mandriva.org> 0-0.20050812.3mdk
- add KDE protocol handler (Nick Brown)

* Sat Aug 13 2005 Götz Waschk <waschk@mandriva.org> 0-0.20050812.2mdk
- rename from player

* Sat Aug 13 2005 Götz Waschk <waschk@mandriva.org> 0-0.20050812.1mdk
- initial package

