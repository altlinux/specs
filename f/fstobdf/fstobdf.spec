Name: fstobdf
Version: 1.0.5
Release: alt1
Summary: Generate BDF font from X font server
Group: System/X11
Source: %name-%version.tar.bz2
License: MIT

# Automatically added by buildreq on Thu Apr 14 2011
# optimized out: pkg-config xorg-fontsproto-devel xorg-xproto-devel
BuildRequires: libFS-devel libX11-devel

BuildRequires: libFS-devel
BuildRequires: libX11-devel
BuildRequires: xorg-util-macros

%description
The fstobdf program reads a font from a font server and generate BDF font.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall

%files
%doc ChangeLog README
%_bindir/%name
%_man1dir/%name.*

%changelog
* Thu May 03 2012 Fr. Br. George <george@altlinux.ru> 1.0.5-alt1
- Autobuild version bump to 1.0.5

* Tue Apr 12 2011 Fr. Br. George <george@altlinux.ru> 1.0.4-alt1.1
- Recalculate buildreq

* Fri Nov 05 2010 Fr. Br. George <george@altlinux.ru> 1.0.4-alt1
- Autobuild version bump to 1.0.4

* Sat Sep 30 2006 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1
- Initial build

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 25 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-25 20:17:57 (31598)
- X11R7.1

* Tue May 16 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-16 23:25:13 (27461)
- fix description

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository
