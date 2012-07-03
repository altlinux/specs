
Name:  tuxkart
Version: 0.4.0
Release: alt2.qa1

Summary: Tuxedo T Penguin stars in Tuxkart
License: GPL
Group: Games/Arcade
Source: http://tuxkart.sourceforge.net/dist/%{name}-%{version}.tar.gz

Packager: Ilya Mashkin <oddity@altlinux.ru>

URL: http://tuxkart.sourceforge.net/

# Automatically added by buildreq on Mon Oct 06 2003 (-bi)
BuildRequires: xorg-cf-files libX11-devel libXi-devel libXext-devel libXmu-devel gcc-c++ libGLU-devel libaudio-devel libglut-devel libstdc++-devel plib-devel

%description
This is another game that stars your Favorite Hero: Tux, the Linux Penguin.

%prep
%setup -q
find . -type f|xargs chmod -x
#%__subst 's/-O6//g' configure.in
#aclocal
#autoconf
#automake
chmod a+x ./configure

%build
%configure
%make_build

%install
%makeinstall

install -m755 -d %buildroot%_desktopdir/
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Tuxkart
Comment=Karting with tux
Exec=%name
# TODO!!!
#Icon=%name
Terminal=false
StartupNotify=false
Categories=Game;Simulation;
EOF

%files
%doc README COPYING
%_bindir/*
%_datadir/games/tuxkart
%_datadir/tuxkart
%_desktopdir/%{name}.desktop

%changelog
* Mon Apr 18 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt2.qa1
- NMU: converted menu to desktop file

* Mon Dec 22 2008 Ilya Mashkin <oddity at altlinux dot ru> 0.4.0-alt2
- rebuild

* Mon Oct 06 2003 Sergey V Turchin <zerg at altlinux dot org> 0.2.0-alt2
- rebuild

* Wed Oct 02 2002 Stanislav Ievlev <inger@altlinux.ru> 0.2.0-alt1
- 0.2.0

* Tue Feb 12 2002 Sergey V Turchin <zerg@altlinux.ru> 0.1.0-alt1
- new version

* Fri Sep 28 2001 Stefan van der Eijk <stefan@eijk.nu> 0.0.6-2mdk
- BuildRequires: Mesa-common-devel

* Fri Jul 27 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.0.6-1mdk
- updated to 0.0.6

* Sat Nov 18 2000 Daouda Lo <daouda@mandrakesoft.com> 0.0.3-3mdk
- build against new libstdc++
- rm hardcoded path to binary in menu 
- rpmlint 100%% happy

* Tue Sep 19 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.0.3-2mdk
- menu

* Thu Aug 24 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.0.3-1mdk
- 0.0.3
- added Packager tag
- removed hardcoded -O6

* Mon Jul  3 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.0.2-1mdk
- 0.0.2

* Mon Jul  3 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.0.1-1mdk
- first Mandrake Package

