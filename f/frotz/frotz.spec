Name: frotz
Version: 2.43
Release: alt1

Summary: a curses-based Z-Machine interpreter for interactive fiction games
License: GPL v2
Group: Games/Other
Url: http://www.ifarchive.org/indexes/if-archiveXinfocomXinterpretersXfrotz.html

Source: ftp://ftp.ifarchive.org/if-archive/infocom/interpreters/frotz/%name-%version.tar.gz

# Automatically added by buildreq on Tue Oct 25 2005
BuildRequires: libncurses-devel libtinfo-devel

%description
Frotz is an interpreter for playing all of Infocom's text adventures and
newer games using the same format. Frotz complies with Graham Nelson's
Z-Machine standard v1.0.

%prep
%setup

%build
%make PREFIX=%prefix CONFIG_DIR=%_sysconfdir \
	SOUND_DEFS=-DOSS_SOUND SOUND_DEV=/dev/dsp \
	CURSES=-lncurses CURSES_DEF=-DUSE_NCURSES_H

%install
%make PREFIX=%buildroot%prefix MAN_PREFIX=%buildroot%_datadir install

%files
%_bindir/%name
%_man6dir/*
%doc AUTHORS BUGS ChangeLog HOW_TO_PLAY README TODO doc/%name.conf*

%changelog
* Tue Oct 25 2005 Alex V. Myltsev <avm@altlinux.ru> 2.43-alt1
- Initial build for ALT Linux.

