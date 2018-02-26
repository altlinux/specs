Name: xjump
Version: 2.7.5
Release: alt2


Packager: Ilya Mashkin <oddity@altlinux.ru>
Summary: Jump-jump game for X
License: GPL
Group: Games/Arcade
Url: http://packages.debian.org/xjump

Source: %name-%version.tar.bz2

BuildRequires: libX11-devel libXaw-devel libICE-devel libXext-devel
BuildRequires: xpm-devel

%description
The way to play this game is very simple, but it is still nice game.
What you do in this game is only to jump, jump and jump up above.


%prep
%setup

%build
%make_build CDEBUGFLAGS="$RPM_OPT_FLAGS" RECORD_DIR="%_sysconfdir/%name"

%install
mkdir -p $RPM_BUILD_ROOT/%_usr/games
cp xjump $RPM_BUILD_ROOT/%_usr/games/

mkdir -p $RPM_BUILD_ROOT%_sysconfdir/%name
touch $RPM_BUILD_ROOT%_sysconfdir/%name/record

mkdir -p $RPM_BUILD_ROOT/%_sysconfdir/X11/app-defaults/
cp XJump.ad $RPM_BUILD_ROOT/%_sysconfdir/X11/app-defaults/XJump

%files
%attr(2711, root, games) %_usr/games/%name
%config(noreplace) %attr(774, games, games) %_sysconfdir/%name/*
%_sysconfdir/X11/app-defaults/XJump
%doc debian/copyright
%doc debian/changelog

%changelog
* Fri Dec 30 2011 Ilya Mashkin <oddity@altlinux.ru> 2.7.5-alt2
- fix build

* Thu Apr 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.5-alt1.3
- Fixed build

* Thu Dec 16 2010 Dmitry V. Levin <ldv@altlinux.org> 2.7.5-alt1.2
- Blind rebuild with libXaw.so.7.

* Thu Sep 25 2008 Ilya Mashkin <oddity@altlinux.ru> 2.7.5-alt1.1
- rebuild
- update requires

* Wed May 28 2003 Peter Novodvorsky <nidd@altlinux.com> 2.7.5-alt1
- Initial release.

