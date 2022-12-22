Name: opentyrian
Version: 2.1.20221123
Release: alt1
Summary: OpenTyrian is a port of the DOS shoot-em-up Tyrian
License: GPLv2
Group: Games/Arcade
Url: https://github.com/opentyrian/opentyrian
Source: %name.tar
Source1: %name-installer
Source2: %name.png

# Automatically added by buildreq on Thu Dec 24 2009
BuildRequires: gcc-c++ libSDL2-devel libSDL2_net-devel

%description
OpenTyrian is a port of the DOS shoot-em-up Tyrian. Jason Emery generously gave
the OpenTyrian developers a copy of the Tyrian 2.1 source code, which has since
been ported from Turbo Pascal to C. The port uses SDL, making it easily
cross-platform.

Tyrian is an arcade-style vertical scrolling shooter. The
story is set in 20,031 where you play as Trent Hawkins, a skilled fighter-pilot
employed to fight Microsol and save the galaxy.

%prep
%setup -qn %name

%build
prefix=%_prefix CPPFLAGS="%optflags" %make %name

%install
install -Dpm 755 %name %buildroot%_bindir/%name
install -Dpm 755 %SOURCE1 %buildroot%_bindir/%name-installer

mkdir -p %buildroot{%_liconsdir,%_desktopdir,%_man6dir}
install -m644 %SOURCE2 %buildroot%_liconsdir/%name.png
install -m644 linux/man/*.6 %buildroot%_man6dir/

cat > %buildroot%_desktopdir/%name.desktop  <<EOF
[Desktop Entry]
Name=OpenTyrian
Comment=%summary
Exec=%name-installer
Icon=%name
Type=Application
Terminal=false
Categories=Game;ArcadeGame;
EOF


%files
%doc COPYING README NEWS
%_bindir/*
%_liconsdir/*
%_man6dir/*
%_desktopdir/%name.desktop

%changelog
* Thu Dec 22 2022 L.A. Kostis <lakostis@altlinux.ru> 2.1.20221123-alt1
- Updated to v2.1.20221123.

* Fri Mar 25 2022 L.A. Kostis <lakostis@altlinux.ru> 2.1.20220318-alt1
- Updated to v2.1.20220318.
- SDL->SDL2.

* Sun May 27 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.1-alt2.rev628c01aadaa7
- Update to revision 628c01aadaa7

* Sun Feb 21 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 2.1-alt1.r953
- Build for ALT
