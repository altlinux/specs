Name: luvcview
Version: 0.2.6
Release: alt1

Summary: SDL-based video grabber
License: GPLv2+
Group: Video

Url: http://www.quickcamteam.net/software/linux/v4l2-software/luvcview
Source: %name-%version.tar.lzma
Source1: dynctrl-logitech.h
Source2: uvcvideo.h
Source3: uvc_compat.h
Patch: linuxvideodev2.patch
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: libSDL-devel

%description
luvcview is a small video capture program ideal for webcam testing
and problem debugging.

%prep
%setup
cp -a %SOURCE1 .
cp -a %SOURCE2 .
cp -a %SOURCE3 .
%patch -p0
# debug spam :-/
sed -i '/printf("find DRI \\n");/d' utils.c

%build
%make

%install
install -pDm755 %name %buildroot%_bindir/%name

%files
%doc README Changelog COPYING ToDo
%_bindir/%name

%changelog
* Mon Nov 14 2016 Michael Shigorin <mike@altlinux.org> 0.2.6-alt1
- initial build for ALT Linux Sisyphus (based on mageia package)

* Fri Feb 12 2016 umeabot <umeabot> 0.2.6-8.mga6
+ Revision: 956098
- Mageia 6 Mass Rebuild

* Wed Oct 21 2015 daviddavid <daviddavid> 0.2.6-7.mga6
+ Revision: 893587
- do not strip binary to fix empty debuginfo

* Wed Oct 15 2014 umeabot <umeabot> 0.2.6-6.mga5
+ Revision: 742821
- Second Mageia 5 Mass Rebuild

* Tue Sep 16 2014 umeabot <umeabot> 0.2.6-5.mga5
+ Revision: 682054
- Mageia 5 Mass Rebuild

* Fri Oct 18 2013 umeabot <umeabot> 0.2.6-4.mga4
+ Revision: 507627
- Mageia 4 Mass Rebuild

* Sat Jan 12 2013 umeabot <umeabot> 0.2.6-3.mga3
+ Revision: 359140
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild

* Fri Dec 07 2012 dams <dams> 0.2.6-2.mga3
+ Revision: 327852
- update %%group

* Wed Jun 08 2011 dams <dams> 0.2.6-1.mga2
+ Revision: 101784
- Fix linux/videodev2.h with a patch
- imported package luvcview

* Fri Aug 28 2009 Lev Givon <lev@mandriva.org> 0.2.6-1mdv2010.0
+ Revision: 422031
- Update to 0.2.6.

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.2.4-2mdv2009.0
+ Revision: 268095
- rebuild early 2009.0 package (before pixel changes)

* Fri Jun 13 2008 Lev Givon <lev@mandriva.org> 0.2.4-1mdv2009.0
+ Revision: 218647
- import luvcview

* Wed May 28 2008 Lev Givon <lev@mandriva.org> 0.2.4-1mdv2008.1
- Package for Mandriva.
