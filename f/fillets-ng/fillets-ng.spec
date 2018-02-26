Name: fillets-ng
Version: 1.0.1
Release: alt1
Summary: puzzle game about witty fish saving the world sokoban-style
Group: Games/Puzzles
License: GPLv2+
Url: http://fillets.sourceforge.net/
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

Source0: %name-%version.tar.gz
Source1: %name.png

Requires: fillets-ng-data

# Automatically added by buildreq on Wed Mar 25 2009
BuildRequires: gcc-c++ libSDL-devel libSDL_image-devel libSDL_mixer-devel libSDL_ttf-devel libX11-devel libfribidi-devel liblua5-devel libsmpeg-devel

%description
Fish Fillets is strictly a puzzle game. The goal in every of the seventy
levels is always the same: find a safe way out. The fish utter witty remarks
about their surroundings, the various inhabitants of their underwater realm
quarrel among themselves or comment on the efforts of your fish. The whole
game is accompanied by quiet, comforting music.

%prep
%setup -q

%build
%configure --datadir=%_datadir/fillets-ng
%make_build

%install
%make_install DESTDIR=%buildroot install

#Menu and icons
mkdir -p %buildroot%_niconsdir
install -m644 %SOURCE1 %buildroot%_niconsdir/%name.png
mkdir -p %buildroot%_datadir/applications
cat > %buildroot%_datadir/applications/%name.desktop  <<EOF
[Desktop Entry]
Name=Fillets
Comment=%summary
Exec=fillets
Icon=%name
Type=Application
Terminal=false
Categories=Game;LogicGame;
EOF


%files
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%_bindir/*
%_man6dir/*
%_datadir/applications/*
%_niconsdir/*


%changelog
* Sat Oct 29 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.1-alt1
- New version (bugfix release)

* Sat Dec 25 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.0-alt1
- New version

* Sat Feb 27 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.3-alt1
- New version
- Add SOURCE1

* Mon Dec 28 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.2-alt1
- New version
- Remove patch
- Add desktop file and icon

* Wed Mar 25 2009 Igor Zubkov <icesik@altlinux.org> 0.8.1-alt1
- 0.8.0 -> 0.8.1

* Tue Dec 02 2008 Igor Zubkov <icesik@altlinux.org> 0.8.0-alt2
- fix build with gcc 4.3

* Wed Mar 05 2008 Igor Zubkov <icesik@altlinux.org> 0.8.0-alt1
- build for Sisyphus

