Name: oclock
Version: 1.0.3
Release: alt1
Summary: Round X clock
Group: System/X11
Url: http://xorg.freedesktop.org
Source: %name-%version.tar.bz2
License: MIT
Packager: Fr. Br. George <george@altlinux.ru>

BuildRequires: xorg-util-macros

# Automatically added by buildreq on Thu Mar 01 2012
# optimized out: libICE-devel libSM-devel libX11-devel libXt-devel pkg-config xorg-xextproto-devel xorg-xproto-devel
BuildRequires: libXext-devel libXmu-devel libxkbfile-devel

%description
Oclock simply displays the current time on an analog display.

%prep
%setup -n %name-%version

%build
%autoreconf
%configure
%make_build

%install
%make install DESTDIR=%buildroot

%files
%doc README
%_bindir/oclock
%_x11appconfdir/Clock-color
%_mandir/man1/oclock.1.gz

%changelog
* Thu Mar 01 2012 Fr. Br. George <george@altlinux.ru> 1.0.3-alt1
- Autobuild version bump to 1.0.3
- BuildRequires updated

* Fri Sep 24 2010 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1
- Autobuild version bump to 1.0.2

* Tue Dec 02 2008 Fr. Br. George <george@altlinux.ru> 1.0.1-alt3
- Implement upstream synchronization

* Thu Oct 19 2006 Fr. Br. George <george@altlinux.ru> 1.0.1-alt2
- Autoreconf added to correct manpage extension

* Sun Oct 01 2006 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1
- Initial build from MDV

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Wed May 17 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-17 00:13:06 (27483)
- fix description

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository
