Name: wmpiki
Version: 0.2.1
Release: alt4.1

Summary: Hosts activity checker dockapp
License: GPL
Group: Graphical desktop/Window Maker

Url: http://clay.ll.pl/dockapps.html
Source0: http://clay.ll.pl/download/%name-%version.tar.gz
Source1: %name-%version-README.ALT
Patch: %name-%version-alt-cfpath.patch
Packager: Michael Shigorin <mike@altlinux.org>

Summary(pl):    Monitor aktywno╤ci hostСw
Summary(ru_RU.KOI8-R): Аплет-монитор удалённых хостов
Summary(uk_UA.KOI8-U): Аплет, що спостер╕га╓ в╕ддален╕ вузли

BuildRequires: libX11-devel libXpm-devel libXext-devel

%description
wmpiki is a dockapp which checks and displays small leds for indicate
hosts activity (up to eight hosts).

%description -l pl
wmpiki jest apletem, ktСry sprawdza i przy pomocy maЁych diod wskazuje
aktywno╤Ф hostСw w sieci (do o╤miu hostСw).

%description -l ru_RU.KOI8-R
wmpiki -- аплет, который проверяет доступность удалённых хостов (ping)
и отображает маленькие индикаторы (до восьми хостов).

%description -l uk_UA.KOI8-U
wmpiki -- аплет, що перев╕ря╓ досяжн╕сть в╕ддалених вузл╕в (п╕н╜)
та в╕добража╓ невеличк╕ ╕ндикатори (до восьми вузл╕в).

%prep
%setup
%patch -p1

%build
%make_build \
	CFLAGS="%optflags -Wall" \
	LIBS="-L%_x11libdir -lXpm -lXext -lX11"

%install
install -d %buildroot%_bindir
install %name %buildroot%_bindir
install -pm644 %SOURCE1 README.ALT
install -pm755 -d %buildroot%_menudir
cat << EOF > %buildroot%_menudir/%name
?package(wmpiki):\
	needs=wmaker \
	section="Window Maker/Accessibility" \
	title="wmpiki" \
	longtitle="Hosts activity checker dockapp" \
	command="EXEC /usr/bin/wmpiki"
EOF

%files
%doc AUTHORS README* ChangeLog
%_bindir/*
%_menudir/*

%changelog
* Thu Apr 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt4.1
- Fixed built

* Sat Aug 21 2010 Michael Shigorin <mike@altlinux.org> 0.2.1-alt4
- built for Sisyphus (closes: #23564)
  + thanks NotHAM

* Sat May 29 2010 Anatoly Chernov <aichernov@umail.ru> 0.2.1-alt3.1
- removed desktop-file (in spec %name.menu)

* Sat Dec 06 2008 Michael Shigorin <mike@altlinux.org> 0.2.1-alt3
- added Packager:
- replaced debian menufile with desktop one

* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 0.2.1-alt2
- applied repocop patch

* Sun Oct 17 2004 Michael Shigorin <mike@altlinux.ru> 0.2.1-alt1
- built for ALT Linux
- based on wmfire.spec and PLD's wmpiki.spec (somewhat, that is)
- moved config file to ~/.wmpiki (see README.ALT)
