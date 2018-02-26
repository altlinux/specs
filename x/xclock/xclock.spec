Name: xclock
Version: 1.0.6
Release: alt1
Summary: analog / digital clock for X
Group: System/X11
Url: http://xorg.freedesktop.org
Source: %name-%version.tar.bz2
License: MIT
Packager: Fr. Br. George <george@altlinux.ru>

# Doesn't build withouth this
# Automatically added by buildreq on Thu Apr 14 2011
# optimized out: fontconfig fontconfig-devel libICE-devel libSM-devel libX11-devel libXmu-devel libXrender-devel libXt-devel libfreetype-devel pkg-config xorg-renderproto-devel xorg-xproto-devel
BuildRequires: libXaw-devel libXft-devel libxkbfile-devel

BuildRequires: xorg-util-macros

%description
The xclock program displays the time in analog or digital form. The time is
continuously updated at a frequency which may be specified by the user.

%prep
%setup -n %name-%version

%build
%autoreconf
%configure
%make

%install
%make install DESTDIR=%buildroot

%files
%doc README
%_bindir/xclock
%_x11appconfdir/*
%_mandir/man1/xclock.*

%changelog
* Wed Feb 22 2012 Fr. Br. George <george@altlinux.ru> 1.0.6-alt1
- Autobuild version bump to 1.0.6

* Tue Apr 12 2011 Fr. Br. George <george@altlinux.ru> 1.0.5-alt1.1
- Recalculate buildreq

* Sun Sep 26 2010 Fr. Br. George <george@altlinux.ru> 1.0.5-alt1
- Autobuild version bump to 1.0.5

* Fri Nov 21 2008 Fr. Br. George <george@altlinux.ru> 1.0.3-alt1
- Version up
- sync with upstream up to aw7 downgrade patch

* Sun Oct 01 2006 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1
- Initial build from MDV

* Fri Sep 01 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-09-01 20:52:41 (59459)
- rebuild to fix libXaw.so.8 dependency

* Thu Jun 01 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-06-01 20:13:15 (31864)
- fill in missing description & summaries

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Tue May 30 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-30 20:36:20 (31749)
- rebuild against new libXaw package

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 25 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-25 20:17:57 (31598)
- X11R7.1

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository
