Name:		lastbash
Version: 	0.3.3
Release:	alt2
Source:		http://dl.sourceforge.net/sourceforge/lastbash/%name-%version.tar.gz
URL:		http://lastbash.sourceforge.net
License:	GPL
Group:		Sound
Summary:	Console/terminal based Last.fm player
Packager:	Fr. Br. George <george@altlinux.ru>
Buildarch:	noarch
Requires:	curl mplayer

%description
LastBASH is a console/terminal based Last.fm player. Although the default Last.fm player is a great one, it also is a graphical one and it could be somewhat inadequate for the die-hard terminal users, like some people I know. LastBASH tries to find its place among the other Last.fm players, filling this gap: the missing console player.

Note: this package suggests, athough not requires, the "notify-send" program.

%prep
%setup

%build

%install
%makeinstall DESTDIR=%buildroot
mv %buildroot%buildroot%_defaultdocdir doc.new
%files
%doc lastbash_template.html
%doc doc.new/%name-%version/*
%_sysconfdir/*
%_bindir/%name
%_man1dir/*

%changelog
* Sat Mar 21 2009 Fr. Br. George <george@altlinux.ru> 0.3.3-alt2
- Fix #18541, stupid buildroot in files section

* Sun Nov 23 2008 Fr. Br. George <george@altlinux.ru> 0.3.3-alt1
- Initial build from scratch

