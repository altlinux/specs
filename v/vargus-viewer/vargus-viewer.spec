Name: vargus-viewer
Version: 1.0.1
Release: alt2

Summary: Qt4 client for vargus server

Group: Video
License: GPL
Url: http://git.etersoft.ru/projects/other/vargus-viewer.git

# Source-git: http://git.etersoft.ru/projects/other/vargus-viewer.git
Source: %name-%version.tar

# Automatically added by buildreq on Thu Apr 12 2012
# optimized out: fontconfig libqt4-core libqt4-devel libqt4-gui libqt4-network libstdc++-devel
BuildRequires: gcc-c++ libvlc-devel libqt4-devel

BuildPreReq: rpm-macros-qt4

Requires: vlc-mini vlc-plugin-ffmpeg

%description
Qt4 client for vargus server.

%prep
%setup

%build
%qmake_qt4
%make_build
lrelease-qt4 lang/lang_ru.ts

%install
install VargusViewer -D %buildroot%_bindir/VargusViewer
mkdir -p %buildroot%_datadir/%name/images
cp images/* %buildroot%_datadir/%name/images/
mkdir -p %buildroot%_datadir/%name/lang
cp lang/lang_ru.qm %buildroot%_datadir/%name/lang/

%files
#%doc README
%_bindir/VargusViewer
%_datadir/%name/

%changelog
* Mon Oct 07 2013 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt2
- build for ALT Linux Sisyphus

* Mon Oct 07 2013 Konstantin Kondratyuk <kondratyuk@etersoft.ru> 1.0.1-alt1
- set video source with libvlc_media_new_location() function

* Wed Mar 13 2013 Konstantin Kondratyuk <kondratyuk@etersoft.ru> 1.0.0-alt1
- fix bug with bad multiline info about cameras. Now read for one camera

* Wed Feb 06 2013 Konstantin Kondratyuk <kondratyuk@etersoft.ru> 0.9.14-alt1
- some bug fixes

* Wed Feb 06 2013 Konstantin Kondratyuk <kondratyuk@etersoft.ru> 0.9.13-alt2
- fix build with new gcc

* Tue Feb 05 2013 Konstantin Kondratyuk <kondratyuk@etersoft.ru> 0.9.13-alt1
- fix crashes in drag&drop video
- add local path for cross-compile

* Fri Feb 01 2013 Konstantin Kondratyuk <kondratyuk@etersoft.ru> 0.9.12-alt1
- refactoring of video vidget
- fix build of windows version
- add license information
- bug fixes

* Mon Dec 17 2012 Konstantin Kondratyuk <kondratyuk@etersoft.ru> 0.9.11-alt1
- fill black before show video
- some litle refactoring

* Fri Nov 23 2012 Konstantin Kondratyuk <kondratyuk@etersoft.ru> 0.9.10-alt1
- fix posible diagn error at reseived string
- fix bug with received string

* Thu Nov 15 2012 Konstantin Kondratyuk <kondratyuk@etersoft.ru> 0.9.9-alt1
- set check lenght reciived string and split it
- move name camera to screen

* Fri Nov 09 2012 Konstantin Kondratyuk <kondratyuk@etersoft.ru> 0.9.8-alt1
- change text output
- fix aspect ratio scheme

* Wed Oct 31 2012 Konstantin Kondratyuk <kondratyuk@etersoft.ru> 0.9.7-alt1
- add shadow background for text out
- add font settings
- update translation
- bug fixes

* Fri Oct 19 2012 Konstantin Kondratyuk <kondratyuk@etersoft.ru> 0.9.6-alt1
- change text output

* Mon Oct 08 2012 Konstantin Kondratyuk <kondratyuk@etersoft.ru> 0.9.5-alt1
- maximize main window at default

* Fri Oct 05 2012 Konstantin Kondratyuk <kondratyuk@etersoft.ru> 0.9.4-alt2
- fix compilation on new gcc

* Fri Oct 05 2012 Konstantin Kondratyuk <kondratyuk@etersoft.ru> 0.9.4-alt1
- fix requires
- add frames to views screen
- add command line options
- fix drag&drop from cameraList to widget
- cancelled bigSize call on widget which is not playing
- bug fixes

* Wed Sep 26 2012 Konstantin Kondratyuk <kondratyuk@etersoft.ru> 0.9.3-alt1
- bug fixes

* Tue Sep 25 2012 Konstantin Kondratyuk <kondratyuk@etersoft.ru> 0.9.2-alt1
- new build

* Tue Sep 25 2012 Konstantin Kondratyuk <kondratyuk@etersoft.ru> 0.9.1-alt1
- crashes fixed
- only lowlewel painting
- update translations, add backtrace function

* Thu Aug 16 2012 Konstantin Kondratyuk <kondratyuk@etersoft.ru> 0.9.0-alt1
- implement arhive call in browser
- changes for text on video
- fix uncorrect aspect ratio
- fix for new format sended string
- some bug fixes

* Mon Jul 16 2012 Konstantin Kondratyuk <kondratyuk@etersoft.ru> 0.5-alt1
- add vlc settings
- add reconnecting video after crash video
- some bug fixes

* Wed Jun 06 2012 Konstantin Kondratyuk <kondratyuk@etersoft.ru> 0.4-alt1
- add low level painting video mode
- add more settings
- add logs
- change work paths
- update translation
- some bug fixes
* Tue Apr 17 2012 Konstantin Kondratyuk <kondratyuk@etersoft.ru> 0.3-alt1
- add icons
- add trayIcon
- add russian translation
* Mon Apr 16 2012 Konstantin Kondratyuk <kondratyuk@etersoft.ru> 0.2-alt1
- add icons
- new parser of input parameters
- some bug fixes
* Wed Apr 11 2012 Konstantin Kondratyuk <kondratyuk@etersoft.ru> 0.1-alt1
- initial build
