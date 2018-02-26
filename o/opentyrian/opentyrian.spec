Name: opentyrian
Version: 2.1
Release: alt2.rev628c01aadaa7
Summary: OpenTyrian is a port of the DOS shoot-em-up Tyrian
License: GPLv2
Group: Games/Arcade
Url: http://code.google.com/p/opentyrian/
Source: %name.tar.gz
Source1: %name-installer
Source2: %name.png

# Automatically added by buildreq on Thu Dec 24 2009
BuildRequires: gcc-c++ libSDL-devel libSDL_net-devel

%description
OpenTyrian is a port of the DOS shoot-em-up Tyrian. Jason Emery generously gave the OpenTyrian developers
a copy of the Tyrian 2.1 source code, which has since been ported from Turbo Pascal to C. The port uses SDL,
making it easily cross-platform.
Tyrian is an arcade-style vertical scrolling shooter. The story is set in 20,031 where you play as 
Trent Hawkins, a skilled fighter-pilot employed to fight Microsol and save the galaxy.

%prep
%setup -qn %name

%build
%make release

%install
install -Dpm 755 opentyrian %buildroot%_bindir/opentyrian
install -Dpm 755 %SOURCE1 %buildroot%_bindir/opentyrian-installer

mkdir -p %buildroot%_liconsdir
install -m644 %SOURCE2 %buildroot%_liconsdir/%name.png

mkdir -p %buildroot%_datadir/applications
cat > %buildroot%_datadir/applications/%name.desktop  <<EOF
[Desktop Entry]
Name=OpenTyrian
Comment=%summary
Exec=%name-installer
Icon=%name
Type=Application
Terminal=false
Categories=Qt;Game;ArcadeGame;
EOF


%files
%doc COPYING README CREDITS NEWS
%_bindir/*
%_liconsdir/*
%_datadir/applications/%name.desktop

%changelog
* Sun May 27 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.1-alt2.rev628c01aadaa7
- Update to revision 628c01aadaa7

* Sun Feb 21 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 2.1-alt1.r953
- Build for ALT
