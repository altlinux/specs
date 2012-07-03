%define games_list chess chinese-checkers combat dots ggzcards hastings reversi spades tictactoe

Name: ggz-gtk-games
Version: 0.0.14.1
Release: alt2

Summary: GGZ Games for GTK+ user interface
License: GPL
Group: Games/Other
URL: http://www.ggzgamingzone.org/
Source0: http://ftp.belnet.be/packages/ggzgamingzone/ggz/%version/%name-%version.tar.gz

Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Tue Apr 15 2008
BuildRequires: ggz-client-libs-devel libgtk+2-devel

%description
The complete set of GGZ Gaming Zone games for GTK+ user interface.
Includes all of the following:
Chess
Chinese Checkers
Combat
Connect the Dots
GGZCards
Hastings
La Pocha
Reversi
Spades
Tic-Tac-Toe

%prep
%setup -q

%build
%configure \
	--disable-debug
%make_build

%install
%make_install DESTDIR=%buildroot install

bzip2 -9k ChangeLog

rm %buildroot%_sysconfdir/ggz.modules
rmdir %buildroot%_sysconfdir/

# Get a copy of all of our .dsc files
mkdir -p %buildroot%_datadir/ggz/ggz-config
for i in %games_list; do
	install -m 0644 $i/module.dsc %buildroot%_datadir/ggz/ggz-config/gtk-$i.dsc
done

%find_lang chess
%find_lang chinese-checkers
%find_lang combat
%find_lang common
%find_lang dots
%find_lang ggzcards
%find_lang hastings
%find_lang reversi
%find_lang spades
%find_lang tictactoe

cat chess.lang chinese-checkers.lang combat.lang common.lang dots.lang \
ggzcards.lang hastings.lang reversi.lang spades.lang tictactoe.lang >> all.lang

%post
# Run ggz-config vs. all installed games
if [ -f %_sysconfdir/ggz.modules ]; then
	for i in %games_list; do
		ggz-config --install --modfile=%_datadir/ggz/ggz-config/gtk-$i.dsc --force
	done
fi

%preun
# Run ggz-config to uninstall all the games
if [ "$1" = "0" ]; then
	if [ -f %_sysconfdir/ggz.modules ]; then
		for i in %games_list; do
			ggz-config --remove --modfile=%_datadir/ggz/ggz-config/gtk-$i.dsc
		done
	fi
fi

%files -f all.lang
%doc AUTHORS ChangeLog.bz2 NEWS QuickStart.GGZ README README.GGZ TODO
%_libdir/ggz/*
%_datadir/ggz/

%changelog
* Wed Mar 25 2009 Igor Zubkov <icesik@altlinux.org> 0.0.14.1-alt2
- bzip2 ChangeLog

* Tue Apr 15 2008 Igor Zubkov <icesik@altlinux.org> 0.0.14.1-alt1
- 0.0.14 -> 0.0.14.1
- disable debug

* Thu May 24 2007 Igor Zubkov <icesik@altlinux.org> 0.0.14-alt1
- build for Sisyphus

