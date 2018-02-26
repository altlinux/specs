Name: xkbutils
Version: 1.0.3
Release: alt1
Summary: XKB utilities: xkbbell, xkbvleds, and xkbwatch
Group: System/X11
Url: http://xorg.freedesktop.org
Source: %name-%version.tar.bz2
License: MIT

# Automatically added by buildreq on Thu Dec 04 2008
BuildRequires: libXaw-devel libxkbfile-devel xorg-inputproto-devel

BuildRequires: xorg-util-macros

%description
Xkbutils accumulates some XKB utilities such as xkbbell, xkbvleds, and xkbwatch.

%prep
%setup -q -n %name-%version

%build
%autoreconf
%configure
%make_build

%install
%makeinstall

%files
%doc README
%_bindir/xkbbell
%_bindir/xkbvleds
%_bindir/xkbwatch
%_man1dir/*

%changelog
* Wed Nov 03 2010 Fr. Br. George <george@altlinux.ru> 1.0.3-alt1
- Autobuild version bump to 1.0.3

* Tue Sep 28 2010 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1
- Autobuild version bump to 1.0.2

* Thu Dec 04 2008 Fr. Br. George <george@altlinux.ru> 1.0.1-alt3
- Implement upstream synchronization
- libXext-devel issue

* Sat Nov 22 2008 Fr. Br. George <george@altlinux.ru> 1.0.1-alt2
- Sync with upstream up to aw7 downgrade patch
- Manpages added

* Sun Oct 01 2006 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1
- Initial build from MDV

* Fri Sep 01 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-09-01 20:56:41 (59477)
- rebuild to fix libXaw.so.8 dependency

* Thu Jun 01 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-06-01 20:13:15 (31864)
- fill in missing description & summaries

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Tue May 30 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-30 21:08:28 (31755)
- rebuild against new libXaw package

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository
