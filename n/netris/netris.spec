# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: netris
Version: 0.52
Release: alt5.2

Summary: A free network version of Tetris
Summary(ru_RU.CP1251): Свободная версия сетевого тетриса

License: GPLv2
Group: Games/Other
Url: ftp://ftp.netris.org/pub/netris/
Packager: Slava Semushin <php-coder@altlinux.ru>

Source0: ftp://ftp.netris.org/pub/netris/%name-%version.tar.gz

# http://www.openbsd.org/cgi-bin/cvsweb/~checkout~/ports/games/netris/files/netris.1
# http://www.freebsd.org/cgi/cvsweb.cgi/~checkout~/ports/games/netris/files/netris.1
Source2: %name.6

Patch0: %name-0.52-alt-warnings-Wall_fix.patch
Patch1: %name-0.52-alt-configure-tests_fix.patch

# http://www.openbsd.org/cgi-bin/cvsweb/ports/games/netris/patches/patch-game_c
Patch2: netris-openbsd-src-snprintf.patch

BuildRequires: libncurses-devel

%description
A free version of Tetris. This game uses ncurses library and can work
in console or pseudo-terminal. You can play against computer or on the
network against your friends.

%description -l ru_RU.CP1251
Свободная версия тетриса. Игра использует библиотеку ncurses и может
работать как в консоли так и в псевдотерминале. Играть можно против
компьютера или по сети, против друг друга.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2

%build
./Configure -O%_optlevel --cextra "%optflags -Werror"
%make_build

%install
install -pD -m 755 %name %buildroot%_gamesbindir/%name
install -pD -m 755 sr %buildroot%_gamesbindir/sample-robot
install -pD -m 644 %SOURCE2 %buildroot%_man6dir/%name.6

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=%name
Comment=A free network version of Tetris
Comment[ru]=РЎРІРѕР±РѕРґРЅР°СЏ РІРµСЂСЃРёСЏ СЃРµС‚РµРІРѕРіРѕ С‚РµС‚СЂРёСЃР°
Icon=%{name}
Exec=%_gamesbindir/%name
#Exec=%name
Terminal=false
Categories=Game;BlocksGame;
EOF

%files
%doc README FAQ robot_desc
%_gamesbindir/%name
%_gamesbindir/sample-robot
%_desktopdir/%{name}.desktop
%_man6dir/%name.6.*

%changelog
* Sat Apr 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.52-alt5.2
- NMU: desktop file cleanup (thanks to php-coder@)

* Wed Apr 06 2011 Igor Vlasenko <viy@altlinux.ru> 0.52-alt5.1
- NMU: converted debian menu to freedesktop

* Fri Dec 05 2008 Slava Semushin <php-coder@altlinux.ru> 0.52-alt5
- Removed obsolete %%update_menus/%%clean_menus calls (noted by repocop)

* Sun May 18 2008 Slava Semushin <php-coder@altlinux.ru> 0.52-alt4
- Added manual page (from OpenBSD/FreeBSD)
- Install sample-robot program (like OpenBSD/FreeBSD does)
- Added patch to use snprintf() instead of sprintf() (from OpenBSD)
- Spec cleanup

* Sat Sep 09 2006 Slava Semushin <php-coder@altlinux.ru> 0.52-alt3
- Fixed build with gcc4 and -Werror
- Separate warnings-fix patch to configure-tests_fix and
  warnings-Wall_fix patches
- Enable _unpackaged_files_terminate_build
- Give compiler flags via Configure options
- Formatted %%description
- Changed my name in Packager tag

* Wed Jan 18 2006 php-coder <php-coder@altlinux.ru> 0.52-alt2
- Removed useless Summary and %%description in koi8-r and utf8 charsets
- Use %%def_enable instead of %%add_optflags for enable -Werror flag
- Dont use --silent and --no-print-directory options for make

* Mon Jan 02 2006 php-coder <php-coder@altlinux.ru> 0.52-alt1
- Initial build for ALT Linux Sisyphus
- Using -Werror flag for compiler by default

