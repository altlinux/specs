Name: xload
Version: 1.1.1
Release: alt1
Summary: System load average display for X
Group: System/X11
Url: http://xorg.freedesktop.org
Source: %name-%version.tar.bz2
# check setuid return value to make sure we drop user privilegies
#Patch0: http://xorg.freedesktop.org/releases/X11R7.1/patches/xload-1.0.1-setuid.diff
License: MIT
Packager: Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Thu Apr 14 2011
# optimized out: libICE-devel libSM-devel libX11-devel libXmu-devel libXt-devel pkg-config xorg-xproto-devel
BuildRequires: libXaw-devel

BuildRequires: libXaw-devel libXt-devel xorg-util-macros

%description
The xload program displays a periodically updating histogram of the system
load average.

%prep
%setup -n %name-%version
#patch0 -p0 -b .setuid

%build
%autoreconf
%configure
%make

%install
%makeinstall appdefaultdir=%buildroot%_x11appconfdir

%files
%doc README
%_bindir/xload
%_x11appconfdir/XLoad
%_mandir/man1/xload.1.gz

%changelog
* Tue Apr 17 2012 Fr. Br. George <george@altlinux.ru> 1.1.1-alt1
- Autobuild version bump to 1.1.1

* Tue Apr 12 2011 Fr. Br. George <george@altlinux.ru> 1.1.0-alt1.1
- Recalculate buildreq

* Sat Oct 02 2010 Fr. Br. George <george@altlinux.ru> 1.1.0-alt1
- Autobuild version bump to 1.1.0

* Sat Nov 22 2008 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1
- Version up
- sync with upstream up to aw7 downgrade patch

* Sat Oct 21 2006 Fr. Br. George <george@altlinux.ru> 1.0.1-alt2
- __autoreconf added to correct manpage extension

* Sun Oct 01 2006 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1
- Initial build from MDV

* Fri Sep 01 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-09-01 01:24:44 (59277)
- Add a patch fixing setuid calls. The return value should be verified in order
  to make sure the user privilegies were dropped. (#24976)

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Tue May 30 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-30 21:30:11 (31769)
- better description

* Tue May 30 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-30 21:09:32 (31756)
- rebuild against new libXaw package\n- fixed description

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository
