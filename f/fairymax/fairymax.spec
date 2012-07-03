Name: fairymax
Version: 4.8j
Release: alt1

Summary: Fairy-Max, a sub-2KB (source) micro-Max Chess program
License: Public domain
Group: Games/Boards

Url: http://home.hccnet.nl/h.g.muller/
Source0: %url/fmax4_8w.c
Source1: %url/fmax.ini
Source2: %name.6
Packager: Michael Shigorin <mike@altlinux.org>

%define inidir %_gamesdatadir/%name

%description
Fairymax is a program that plays chess and chess variants.
It uses the xboard/winboard chess-engine protocol to communicate.
Apart from 'regular' chess (also known as the Mad-Queen variant),
it can play Capablanca chess, gothic chess, knightmate, cylinder
chess, berolina chess, superchess and courier chess.

%prep
#mkdir -p $RPM_BUILD_DIR
sed 's,fmax.ini",%inidir/&,' < %SOURCE0 > %name.c

%build
%make CFLAGS="%optflags" %name

%install
install -pDm755 %name %buildroot%_bindir/%name
install -pDm644 %SOURCE1 %buildroot%_gamesdatadir/%name/fmax.ini
install -pDm644 %SOURCE2 %buildroot%_man6dir/%name.6

%files
%_bindir/*
%_gamesdatadir/%name/
%_man6dir/*

# TODO:
# - zip seems to also contain some docs
# - consider -DSHATRANJ

%changelog
* Wed Oct 21 2009 Michael Shigorin <mike@altlinux.org> 4.8j-alt1
- built for ALT Linux (current xboard defaults to fairymax engine)
  + ini file location, manpage and description borrowed from Debian
