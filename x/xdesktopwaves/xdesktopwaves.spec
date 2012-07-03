# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: xdesktopwaves
Version: 1.3
Release: alt7.qa1

Summary: Simulation of water waves on the X Windows desktop

License: GPL
Group: Toys
Url: http://xdesktopwaves.sourceforge.net
Packager: Slava Semushin <php-coder@altlinux.ru>

Source0: http://dl.sourceforge.net/%name/%name-%version.tar.gz
Source1: %name-16.xpm
Source2: %name-32.xpm
Patch: %name-1.3-alt-makefile-destdir_support.patch

BuildRequires: libXext-devel libX11-devel

%description
xdesktopwaves is a cellular automata setting the background of your X
Windows desktop under water. Windows and mouse are like ships on the
sea. Each movement of these ends up in moving water waves. You can
even have rain and/or storm stirring up the water.

To see what xdesktopwaves is able to do, start it by running
'xdesktopwaves' and then run 'xdwapidemo'. You should see the
supported effects on your desktop.

%prep
%setup
%patch -p1

%build
%make_build \
	CC="%__cc" \
	LINK="%__cc" \
	CFLAGS="%optflags -Werror"

%make_build -C xdwapi \
	CC="%__cc" \
	LINK="%__cc" \
	CFLAGS="%optflags -Werror"

%install
%make_install install \
	DESTDIR=%buildroot \
	BINDIR=%_gamesbindir \
	MAN1DIR=%_man1dir

install -pD -m 644 %SOURCE1 %buildroot%_miconsdir/%name.xpm
install -pD -m 644 %SOURCE2 %buildroot%_niconsdir/%name.xpm
install -pD -m 644 %name.xpm %buildroot%_liconsdir/%name.xpm
install -pD -m 755 xdwapi/xdwapidemo %buildroot%_gamesbindir/xdwapidemo

install -m755 -d %buildroot%_desktopdir/
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=xdesktopwaves
Comment=Simulation of water waves on the X Windows desktop
Exec=%_gamesbindir/%name
Icon=%name
Terminal=false
Categories=Game;Amusement;
EOF
cat > %buildroot%_desktopdir/%{name}-exit.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=xdesktopwaves exit
Comment=Simulation of water waves on the X Windows desktop
Exec=%_gamesbindir/%name -end
Icon=%name
Terminal=false
Categories=Game;Amusement;
EOF



%files
%doc README
%_gamesbindir/%name
%_gamesbindir/xdwapidemo
%_man1dir/%name.1.*
%_miconsdir/%name.xpm
%_niconsdir/%name.xpm
%_liconsdir/%name.xpm
%_desktopdir/%{name}.desktop
%_desktopdir/%{name}-exit.desktop

%changelog
* Mon Apr 18 2011 Igor Vlasenko <viy@altlinux.ru> 1.3-alt7.qa1
- NMU: converted menu to desktop file

* Tue Dec 09 2008 Slava Semushin <php-coder@altlinux.ru> 1.3-alt7
- Fixed build (added libX11-devel to BuildRequires)

* Sat Nov 29 2008 Slava Semushin <php-coder@altlinux.ru> 1.3-alt6
- Removed obsolete %%update_menus/%%clean_menus calls (noted by repocop)

* Wed Oct 10 2007 Slava Semushin <php-coder@altlinux.ru> 1.3-alt5
- Show icons in menu
- Imported into git and built with gear

* Wed Jun 13 2007 Slava Semushin <php-coder@altlinux.ru> 1.3-alt4
- New maintainer
- Changes in package:
  + Relocate from /usr/X11R6 to /usr/games (idea from Debian)
  + Add xdwapidemo to package (idea from Gentoo/PLD)
  + Catalog with documentation now belongs to package
  + Put icons with size 32x32 to appropriate catalog
  + Added patch for DESTDIR support (inspired by Debian)
  + Provide values for compiler options (idea from PLD)
  + Using -Werror flag for compiler by default
  + Exclude COPYING file from package
- Spec cleanup:
  + Added Url tag (#9385)
  + Removed package name from Summary
  + Removed trailing spaces in %%description
  + More complete %%description
  + s/%%setup -q/%%setup/
  + Added full url to Source tag
  + Updated BuildRequires
  + More strict names in %%files section
- Changes in menu file:
  + Change section from "Toys" to "Amusement/Toys" (#6309)
  + Specify full path to program in command
  + Minor whitespace fixes
- Enable _unpackaged_files_terminate_build

* Fri Dec 24 2004 Denis Klykvin <nikon@altlinux.ru> 1.3-alt3
- version 1.3

* Sat Dec 11 2004 Denis Klykvin <nikon@altlinux.ru> 1.2-alt2
- version 1.2
- Exit from menu is added

* Thu Nov 18 2004 Denis Klykvin <nikon@altlinux.ru> 1.0-alt1
- Initial build

