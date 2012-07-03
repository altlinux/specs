Name: viewres
Version: 1.0.3
Release: alt1.1
Summary: graphical class browser for Xt
Group: System/X11
Url: http://xorg.freedesktop.org
Source: %name-%version.tar.bz2
License: MIT
Packager: Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Thu Apr 14 2011
# optimized out: libICE-devel libSM-devel libX11-devel libXmu-devel libXt-devel pkg-config xorg-xproto-devel
BuildRequires: libXaw-devel

BuildRequires: libXaw-devel libXt-devel xorg-util-macros

%description
The viewres program displays a tree showing the widget class hierarchy
of the Athena Widget Set.

%prep
%setup -q -n %name-%version

%build
%autoreconf
%configure
%make_build

%install
%make install DESTDIR=%buildroot

%files
%doc README
%_bindir/viewres
%_x11appconfdir/Viewres*
%_mandir/man1/viewres.*

%changelog
* Tue Apr 12 2011 Fr. Br. George <george@altlinux.ru> 1.0.3-alt1.1
- Recalculate buildreq

* Wed Nov 03 2010 Fr. Br. George <george@altlinux.ru> 1.0.3-alt1
- Autobuild version bump to 1.0.3

* Fri Sep 24 2010 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1
- Autobuild version bump to 1.0.2

* Tue Nov 25 2008 Fr. Br. George <george@altlinux.ru> 1.0.1-alt3
- Sync with upstream up to aw7 downgrade patch

* Sat Oct 21 2006 Fr. Br. George <george@altlinux.ru> 1.0.1-alt2
- __autoreconf added to correct manpage extension

* Sun Oct 01 2006 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1
- Initial build from MDV

* Fri Sep 01 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-09-01 20:47:59 (59448)
- rebuild to fix libXaw.so.8 dependency

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Tue May 30 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-30 20:26:44 (31744)
- rebuild against new libXaw package

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Wed May 17 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-17 00:19:51 (27491)
- fix description

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository
