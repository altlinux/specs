Name: gtans
Version: 1.99.0
Release: alt1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: gTans - a little puzzle game
License: GPLv2+
Group: Games/Puzzles

URL: http://gtans.sourceforge.net/
Source: http://downloads.sourceforge.net/gtans/gtans-%version.tar.gz
Source1: gtans.desktop

# Automatically added by buildreq on Tue Jan 13 2009
BuildRequires: intltool libgtk+2-devel

%description
Gtans is a tangram game that runs in X. Tangram is a kind of puzzle game where
the player has to arrange a set of pieces to match a given shape.

%prep
%setup

%build
%configure
%make_build CC="gcc %optflags"

%install
%make_install DESTDIR=%buildroot install
install -pD -m644 %SOURCE1 %buildroot%_desktopdir/gtans.desktop

%find_lang gtans

%files -f gtans.lang
%_sysconfdir/gtansrc
%_bindir/*
%_man6dir/*
%_datadir/gtans
%_miconsdir/*
%_niconsdir/*
%_liconsdir/*
%_iconsdir/hicolor/22x22/apps/*
%_iconsdir/hicolor/24x24/apps/*
%_iconsdir/hicolor/scalable/apps/*
%_desktopdir/*

%changelog
* Tue Jan 13 2009 Victor Forsyuk <force@altlinux.org> 1.99.0-alt1
- 1.99.0

* Tue Apr 24 2007 Victor Forsyuk <force@altlinux.org> 1.2-alt2
- Fix wrong paths in gtans configuration.
- Add URL.
- Refresh build requirements.
- Parallel build.
- Apply optflags.
- Include all localizations.
- Switch to freedesktop-style menu.

* Sun May 25 2003 Andrey Semenov <mitrofan@altlinux.ru> 1.2-alt1
- First version of RPM package.
