Name: xcolors
Version: 1.5a
%define Level 6
Release: alt6.2

Summary: Display and select X11 named colors
Summary(ru_RU.KOI8-R): Показывает все именованные цвета X11
Group: Monitoring
License: BSD
Packager: Fr. Br. George <george@altlinux.ru>
Source: http://ftp.debian.org/debian/pool/main/x/xcolors/%{name}_%{version}.orig.tar.gz

Patch0: http://ftp.debian.org/debian/pool/main/x/xcolors/%{name}_%{version}-%Level.diff.gz

# Automatically added by buildreq on Tue Nov 11 2008
BuildRequires: imake libXaw-devel libXp-devel libXpm-devel xorg-cf-files libXext-devel

%description
Display all X11 named colors 
or select a subset of X11 colors near to the specified one

%prep
%setup -n %{name}-%{version}.orig
%patch0 -p1

%build
xmkmf
#make -f debian/rules RGB_TXT=/usr/share/X11/rgb.txt
%make

%install
%make_install install install.man DESTDIR="$RPM_BUILD_ROOT"

%files
%_x11bindir/%name
%_x11mandir/man?/%name.*
%_sysconfdir/X11/app-defaults/Xcolors


%changelog
* Thu Dec 04 2008 Fr. Br. George <george@altlinux.ru> 1.5a-alt6.2
- libXext-devel added

* Sat Nov 22 2008 Fr. Br. George <george@altlinux.ru> 1.5a-alt6.1
- aw7 downgrade rebuild

* Tue Nov 11 2008 Fr. Br. George <george@altlinux.ru> 1.5a-alt6
- New Buildrequires
- Debian patch freshened

* Sat May 17 2008 Fr. Br. George <george@altlinux.ru> 1.5a-alt5
- New Buildrequires
- Debian patch freshened

* Tue Jan 31 2006 Fr. Br. George <george@altlinux.ru> 1.5a-alt3
- GNU Debian upstream patchlevel sync
- XOrg.7 adaptation

* Fri Jan 23 2004 Fr. Br. George <george@altlinux.ru> 1.5a-alt2
- GNU Debian upstream patchlevel sync
- app-defaults provided

* Fri Jan 23 2004 Fr. Br. George <george@altlinux.ru> 1.5a-alt1
- ALT Linux port

