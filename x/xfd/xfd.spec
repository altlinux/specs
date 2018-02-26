Name: xfd
Version: 1.1.1
Release: alt1
Summary: Display all the characters in an X font
Group: System/X11
Url: http://xorg.freedesktop.org
Source: %name-%version.tar.bz2
Packager: Fr. Br. George <george@altlinux.ru>
License: MIT

# Automatically added by buildreq on Thu Apr 14 2011
# optimized out: fontconfig fontconfig-devel libICE-devel libSM-devel libX11-devel libXmu-devel libXrender-devel libXt-devel libfreetype-devel pkg-config xorg-renderproto-devel xorg-xproto-devel
BuildRequires: libXaw-devel libXft-devel

BuildRequires: xorg-util-macros

%description
The xfd utility creates a window containing the name of the font being
displayed, a row of command buttons, several lines of text for displaying
character metrics, and a grid containing one glyph per cell. The characters are
shown in increasing order from left to right, top to bottom.

%prep
#%setup -q -n %name-%version
%setup

%build
%autoreconf
%configure

%make

%install
%makeinstall appdefaultdir=%buildroot/%_x11appconfdir

%files
%_bindir/*
%_x11appconfdir/*
%_man1dir/*

%changelog
* Wed Feb 22 2012 Fr. Br. George <george@altlinux.ru> 1.1.1-alt1
- Autobuild version bump to 1.1.1

* Tue Apr 12 2011 Fr. Br. George <george@altlinux.ru> 1.1.0-alt1.1
- Recalculate buildreq

* Wed Nov 03 2010 Fr. Br. George <george@altlinux.ru> 1.1.0-alt1
- Autobuild version bump to 1.1.0

* Sat Nov 22 2008 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1
- Sync with upstream up to aw7 downgrade patch

* Wed Sep 06 2006 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1
- Initial build from mdk package

* Fri Sep 01 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-09-01 21:18:27 (59537)
- rebuild to fix libXaw.so.8 dependency

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Tue May 30 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-30 20:41:44 (31752)
- rebuild against new libXaw package

* Tue May 30 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-30 16:15:56 (31710)
- fill in a few more missing descriptions

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository
