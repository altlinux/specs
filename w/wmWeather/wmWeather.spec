Name: wmWeather
Version: 1.31
Release: alt4

Summary: Applet that displays the weather
License: GPL
Group: Graphical desktop/Window Maker

#Url: http://nis-www.lanl.gov/~mgh/WindowMaker/DockApps.shtml
Url: http://www.dockapps.org/file.php/id/17
Source: %name-%version.tar.gz
Source1: %name.menu
Source2: %name-README.ALT
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Thu May 15 2008
BuildRequires: libXext-devel libXpm-devel

Summary(ru_RU.KOI8-R): Апплет, показывающий погоду
Summary(uk_UA.KOI8-U): Аплет, що показу╓ погоду
Summary(pl): Aplet wy╤wietlaj╠cy informacje o pogodzie

%description
wmWeather is a WindowMaker dockapp that displays the current weather
conditions for a given location, in an easy to read icon.

%description -l ru_RU.KOI8-R
wmWeather -- докапп для WindowMaker, который показывает текущую погоду 
в окрестности заданного датчика METAR в удобном виде.

%description -l uk_UA.KOI8-U
wmWeather -- докап для WindowMaker, що показу╓ поточну погоду 
неподал╕к в╕д завданого давача METAR в зручному вигляд╕.

%description -l pl
wmWeather jest dokowalnym apletem dla WindowMakera, wy╤wietlaj╠cym
informacje o aktualnych warunkach atmosferycznych dla wybranego
miejsca.

%prep
%setup

%build
make -C Src CFLAGS="%optflags"

%install
install -d %buildroot{%_x11bindir,%_bindir,%_menudir,%_man1dir}

install Src/%name %buildroot%_x11bindir/
install Src/GrabWeather %buildroot%_bindir/
install Src/%name.1 %buildroot%_man1dir/

install -m644 %SOURCE1 %buildroot%_menudir/%name
install -m644 %SOURCE2 $RPM_BUILD_DIR/%name-%version/README.ALT

%files
%doc HINTS BUGS CHANGES README.ALT
%_x11bindir/%name
%_bindir/GrabWeather
%_man1dir/*
%_menudir/*

# TODO: try to analyse /etc/localtime to get location?

%changelog
* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 1.31-alt4
- applied repocop patch

* Thu May 15 2008 Michael Shigorin <mike@altlinux.org> 1.31-alt3
- buildreq
- minor spec cleanup

* Wed Jan 25 2006 Michael Shigorin <mike@altlinux.org> 1.31-alt2
- updated package Url (fixes #8921)

* Wed Dec 18 2002 Michael Shigorin <mike@altlinux.ru> 1.31-alt1
- built for ALT Linux
- added METAR site code list
- default site is Amundsen-Scott South Pole Station, Antarctica
  which should be reasonable for most Linux systems (sic!)
- spec based on PLD; credits:
    Rod Cordova <rcordova@ethernet.org>
    baggins@pld.org.pl
    blues@pld.org.pl
    kloczek@pld.org.pl
    pius@pld.org.pl
    qboosh@pld.org.pl
    wiget@pld.org.pl
    wrobell@pld.org.pl

