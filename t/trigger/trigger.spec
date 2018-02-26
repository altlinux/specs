Name: trigger
Version: 0.5.2.1
Release: alt3.1
Summary: Free rally car racing game
URL: http://sourceforge.net/projects/trigger-rally/

License: GPL
Group: Games/Sports
Requires: trigger-data
Source0: %name-%version-src.tar.bz2
Source1: %name.desktop
Patch0: %name-0.5.2-gcc4.patch
Packager: Ilya Mashkin <oddity@altlinux.ru>

# Automatically added by buildreq on Sat Mar 03 2007
BuildRequires: esound gcc-c++ imake libSDL-devel libSDL_image-devel libX11-devel libopenal-devel libphysfs-devel xorg-cf-files zlib-devel jam libalut-devel

BuildRequires: libGL-devel libGLU-devel

#uildRequires: boost-jam

%description
Trigger is a free rally car racing game. Fun for all the family!
You race a sequence of 6 courses, with increasing levels of difficulty.

%prep
%setup -q -n %name-%version-src
#%patch0 -p0

%build
%configure --enable-optimize --datadir=%_gamesdatadir/%{name} --bindir=%_gamesbindir
jam

%install
%__mkdir_p %buildroot%_gamesbindir/
%__install -D -pm 755 %{name} %buildroot%_gamesbindir/
%__mkdir_p %buildroot%_desktopdir
%__install %SOURCE1 %buildroot%_desktopdir


%files
%_gamesbindir/*
%_desktopdir/*
%doc doc/*

%changelog
* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2.1-alt3.1
- Rebuilt with libphysfs 2.0.2
- BuildRequires: replaced libmesa-devel by libGL-devel and libGLU-devel

* Sat May 08 2010 Ilya Mashkin <oddity@altlinux.ru> 0.5.2.1-alt3
- fix requires
- fix .desktop

* Sun Jan 11 2009 Ilya Mashkin <oddity@altlinux.ru> 0.5.2.1-alt2
- fix requires
- fix url
- apply repocop patch

* Sat Mar 03 2007 Eugene V. Horohorin <genix@altlinux.ru> 0.5.2.1-alt1
- 0.5.2.1

* Fri May 19 2006 Eugene V. Horohorin <genix@altlinux.ru> 0.5.2-alt3
- gcc4.1 compatible

* Sun Feb 26 2006 Eugene V. Horohorin <genix@altlinux.ru> 0.5.2-alt2
- x86_64 support:
  * wrong buildreq removed

* Wed Feb 15 2006 Eugene V. Horohorin <genix@altlinux.ru> 0.5.2-alt1
- 0.5.2
- trigger.desktop added

* Mon Nov 07 2005 Eugene V. Horohorin <genix@altlinux.ru> 0.5.1c-alt1.1
- beer-to-drink update

* Thu Mar 31 2005 Eugene V. Horohorin <genix@altlinux.ru> 0.5.1c-alt1
- Initial build.
