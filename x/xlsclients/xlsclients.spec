Name: xlsclients
Version: 1.1.2
Release: alt1
Summary: List client applications running on a display
Group: System/X11
Url: http://cgit.freedesktop.org/xorg/app/xlsclients
Source: %name-%version.tar.bz2
License: MIT
Packager: Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Fri Jun 04 2010
BuildRequires: libxcbutil-devel

BuildRequires: xorg-util-macros

%description
Xlsclients is a utility for listing information about the client appli- cations running on a display.  It may be used to generate scripts  representing a snapshot of the user's current session.

%prep
%setup -n %name-%version

%build
%autoreconf
%configure
%make

%install
%makeinstall

%files
%_bindir/*
%_man1dir/*

%changelog
* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.1.2-alt1
- Autobuild version bump to 1.1.2

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.1.1-alt2
- Synchronize with http://cgit.freedesktop.org/xorg/app/xlsclients/commit/?id=41689f150904be690f3aa96c283a7ee632d566ce
   (Drop dependency on xcb-atom/xcb-util)

* Tue Apr 12 2011 Fr. Br. George <george@altlinux.ru> 1.1.1-alt1.1
- Recalculate buildreq

* Thu Nov 04 2010 Fr. Br. George <george@altlinux.ru> 1.1.1-alt1
- Autobuild version bump to 1.1.1

* Fri Jun 04 2010 Fr. Br. George <george@altlinux.ru> 1.1.0-alt1
- Version up

* Tue May 18 2010 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1
- New version

* Sun Oct 01 2006 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1
- Initial build from MDV

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository
