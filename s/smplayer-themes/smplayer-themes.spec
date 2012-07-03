Name:		smplayer-themes
Summary:	Themes icons for SMPlayer
License:	%gpl2plus %lgpl3only CCPL_Attribution_2.5 CCPL_Attribution-ShareAlike_2.5 (see README.txt for themes)
Group:		Video
Url:		http://smplayer.sourceforge.net/
Version:	0.1.20
Release:	alt1
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Source0:	http://smplayer.sourceforge.net/uk/linux/download/%name-%version.tar.bz2
BuildArch:	noarch
Requires:	smplayer >= 0.5.29
BuildPreReq:	rpm-build-licenses

%description
This package provides icon themes for SMPlayer.
SMPlayer intends to be a complete front-end for Mplayer, from basic features
like playing videos, DVDs, and VCDs to more advanced features like support
for Mplayer filters and more. One of the main features is the ability to
remember the state of a played file, so when you play it later it will resume
at the same point and with the same settings. smplayer is developed with
the Qt toolkit, so it's multi-platform.

%prep
%setup -q

%install
mkdir -p %buildroot%_datadir/smplayer/themes
cp -r ./themes/* %buildroot%_datadir/smplayer/themes/

%files
%_datadir/smplayer/themes

%changelog
* Tue Feb 23 2010 Motsyo Gennadi <drool@altlinux.ru> 0.1.20-alt1
- 0.1.20

* Sun Apr 12 2009 Motsyo Gennadi <drool@altlinux.ru> 0.1.19-alt1
- 0.1.19
  + Updated the Gnome theme
- added packager tag

* Tue Nov 11 2008 Motsyo Gennadi <drool@altlinux.ru> 0.1.18-alt1
- 0.1.18

* Mon Sep 29 2008 Motsyo Gennadi <drool@altlinux.ru> 0.1.17-alt1
- 0.1.17

* Sun Jul 27 2008 Motsyo Gennadi <drool@altlinux.ru> 0.1.16-alt1
- 0.1.16

* Sat Feb 02 2008 Motsyo Gennadi <drool@altlinux.ru> 0.1.15-alt1
- 0.1.15
- add all licenses

* Tue Nov 06 2007 Motsyo Gennadi <drool@altlinux.ru> 0.1.14-alt1
- 0.1.14

* Fri Sep 21 2007 Motsyo Gennadi <drool@altlinux.ru> 0.1.12-alt1
- 0.1.12

* Fri Sep 07 2007 Motsyo Gennadi <drool@altlinux.ru> 0.1.11-alt1
- 0.1.11

* Wed Sep 05 2007 Motsyo Gennadi <drool@altlinux.ru> 0.1.10-alt1
- 0.1.10

* Tue Sep 04 2007 Motsyo Gennadi <drool@altlinux.ru> 0.1.9-alt1
- 0.1.9

* Mon Sep 03 2007 Motsyo Gennadi <drool@altlinux.ru> 0.1.8-alt1
- 0.1.8

* Sat Sep 01 2007 Motsyo Gennadi <drool@altlinux.ru> 0.1.7-alt1
- 0.1.7

* Thu Aug 30 2007 Motsyo Gennadi <drool@altlinux.ru> 0.1.6-alt1
- 0.1.6

* Wed Aug 29 2007 Motsyo Gennadi <drool@altlinux.ru> 0.1.5-alt1
- 0.1.5

* Mon Aug 27 2007 Motsyo Gennadi <drool@altlinux.ru> 0.1.4-alt1
- 0.1.4

* Mon Jul 09 2007 Motsyo Gennadi <drool@altlinux.ru> 0.1.3-alt0.M40.1
- 0.1.3

* Fri Jun 29 2007 Motsyo Gennadi <drool@altlinux.ru> 0.1.2-alt0.M40.1
- 0.1.2

* Tue May 29 2007 Motsyo Gennadi <drool@altlinux.ru> 0.1.1-alt0.M24.1
- 0.1.1

* Sun May 06 2007 Motsyo Gennadi <drool@altlinux.ru> 0.1-alt0.M24.1
- initial build for ALT Linux

* Sat May 05 2007 Ricardo Villalba <rvm@escomposlinux.org>
  - first spec file
