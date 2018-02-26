Name: vacuum
Version: 0.13a
Release: alt1
Summary: Vacuum Magic is a fast-paced action game
License: GPL
Url: http://apocalypse.rulez.org/vacuum
Group: Games/Arcade
Source0: http://downloads.sourceforge.net/vacuum/%name-%version.tar.gz
Source1: %name.png
Packager: Fr. Br. George <george@altlinux.ru>
BuildArch: noarch

# Automatically added by buildreq on Fri Jan 09 2009
BuildRequires: perl-Compress-Zlib perl-SDL perl-SDL-OpenGL

%description
Vacuum Magic is a fast-paced action game.

The point of the game is using your magical vacuum field to
collect food and defend against monsters. Food and certain
monsters can also be spat out and used as a projectile
against other monsters. Vacuum Magic can be played by up to
six players, either cooperatively or against each other.

%set_perl_req_method relaxed

%prep
%setup -q -n %name-%version
# ULGY HACK to prevent findreq fail
#sed -i 's@ /usr/share/vacuum @ /usr/share/vacuum /usr/src/tmp/vacuum-buildroot/usr/share/vacuum @' bin/vacuum

%build
%autoreconf
%configure
%make

%install
%makeinstall

install -dm 755 %buildroot%_pixmapsdir
install -m 644 %SOURCE1 %buildroot%_pixmapsdir/

# menu-entries
cat > %name.desktop << EOF
[Desktop Entry]
Comment=Vacuum Magic is a fast-paced action game
Name=Vacuum Magic
GenericName=
Type=Application
Exec=%name
Icon=%name
Terminal=false
Categories=Game;ActionGame;
EOF
install -D  %name.desktop %buildroot/%_desktopdir/%name.desktop

%files
%doc AUTHORS ChangeLog README NEWS TODO
%_bindir/%name
%dir %_datadir/%name
%_datadir/%name/*
%_man6dir/%name.6*
%_desktopdir/*.desktop
%_pixmapsdir/*.png

%changelog
* Thu Aug 06 2009 Fr. Br. George <george@altlinux.ru> 0.13a-alt1
- Version up (closes #20729)

* Fri Jul 03 2009 Fr. Br. George <george@altlinux.ru> 0.12-alt1
- Version up

* Tue Mar 31 2009 Fr. Br. George <george@altlinux.ru> 0.11-alt1
- Version up

* Sat Feb 14 2009 Fr. Br. George <george@altlinux.ru> 0.9-alt1
- Version up

* Fri Jan 09 2009 Fr. Br. George <george@altlinux.ru> 0.7-alt1
- Initial build fropm OpenSuSE

* Mon Nov 10 2008 Toni Graffy <toni@links2linux.de> - 0.7-0.pm.1
- update to 0.7
* Thu Oct 02 2008 Toni Graffy <toni@links2linux.de> - 0.6-0.pm.1
- update to 0.6
* Sat Sep 27 2008 Toni Graffy <toni@links2linux.de> - 0.5-0.pm.1
- Initial build 0.5
