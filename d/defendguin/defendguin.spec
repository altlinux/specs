Name: defendguin
Version: 0.0.12
Release: alt1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Defender clone
License: GPLv2+
Group: Games/Arcade

Url: http://newbreedsoftware.com/defendguin/
Source: ftp://ftp.tuxpaint.org/unix/x/defendguin/src/defendguin-%version.tar.gz
Patch: defendguin-0.0.5-fix-CFLAGS.patch

# Automatically added by buildreq on Tue Aug 04 2009
BuildRequires: libSDL-devel libSDL_mixer-devel

Requires: %name-gamedata = %version

%description
Defendguin is going to be a clone of the arcade game "Defender" but with a
Linux theme. Your mission is to defend little penguinoids from being captured
and mutated by... well, you know who.

%package gamedata
Summary: Data files for defendguin game
Group: Games/Arcade
BuildArch: noarch

%description gamedata
Data files for defendguin game.

%prep
%setup
%patch -p1

subst 's|/usr/local/share|/usr/share|' src/defendguin.6

%define _optlevel 3
%add_optflags %optflags_kernel %optflags_notraceback %optflags_fastmath

%build
%make_build PREFIX=/usr CFLAGS="%optflags"

%install
install -d %buildroot{%_bindir,%_man6dir}
%makeinstall PREFIX=%buildroot%prefix MAN_PREFIX=%buildroot%_datadir

%files
%doc docs/AUTHORS.txt docs/CHANGES.txt docs/README.txt
%_bindir/*
%_man6dir/*

%files gamedata
%_datadir/%name

%changelog
* Wed Dec 23 2009 Victor Forsyuk <force@altlinux.org> 0.0.12-alt1
- 0.0.12

* Tue Aug 04 2009 Victor Forsyuk <force@altlinux.org> 0.0.11-alt2
- Move architecture-independent game data files to noarch subpackage.
- Refresh build requirements (removes esound dependency, hooray!).

* Wed Nov 01 2006 Victor Forsyuk <force@altlinux.org> 0.0.11-alt1
- 0.0.11
- Fix and package man-page.
- Updated buildreqs.

* Thu Oct 24 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.0.10-alt1
- 0.0.10
- Rebuilt in new environment

* Fri Aug 09 2002 Stanislav Ievlev <inger@altlinux.ru> 0.0.9-alt1
- 0.0.9

* Fri Aug 17 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.0.6-ipl7mdk
- Rebuild with new SDL
- Fixed CFLAGS
- Some spec cleanup

* Fri Apr  6 2001 Kostya Timoshenko <kt@altlinux.ru> 0.0.6-ipl6mdk
- Rebuild with SDL-1.2.0

* Wed Mar 14 2001 Kostya Timoshenko <kt@petr.kz> 0.0.6-ipl5mdk
- fix BuildPreReq

* Mon Feb  5 2001 Kostya Timoshenko <kt@petr.kz> 0.0.6-ipl4mdk
- rebuild for RE

* Tue Dec 19 2000 Pixel <pixel@mandrakesoft.com> 0.0.6-3mdk
- rebuild for new libSDL_mixer

* Wed Nov 29 2000 Pixel <pixel@mandrakesoft.com> 0.0.6-2mdk
- rebuild, build req

* Sun Nov 26 2000 Pixel <pixel@mandrakesoft.com> 0.0.6-1mdk
- new version

* Tue Nov  7 2000 Pixel <pixel@mandrakesoft.com> 0.0.5-3mdk
- capitalize summary

* Tue Nov  7 2000 Pixel <pixel@mandrakesoft.com> 0.0.5-2mdk
- rebuild

* Thu Nov  2 2000 Pixel <pixel@mandrakesoft.com> 0.0.5-1mdk
- initial spec
