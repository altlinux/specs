Name: typespeed
Version: 0.6.5
Release: alt1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: A typing speed tester
License: GPLv2+
Group: Games/Educational

Url: http://tobias.eyedacor.org/typespeed/
Source: %url/%name-%version.tar.gz

# Automatically added by buildreq on Tue Nov 13 2007
BuildRequires: libncurses-devel

%description
Typespeed is a tool and game for testing your typing speed. It displays your
CPS (total and correct), typo ratio, and some points to compare with your
friends. It is a clone of 'ztspeed', and features a network play mode for
challenging your friends.

%prep
%setup

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install
%find_lang %name

%files -f %name.lang
%attr(2711,root,games) %_bindir/*
%config %_sysconfdir/typespeedrc
%_datadir/typespeed
%_man6dir/*
%config(noreplace) %attr(664,root,games) %_localstatedir/games/typespeed.score
%exclude %_datadir/doc

%changelog
* Sun Aug 17 2008 Victor Forsyuk <force@altlinux.org> 0.6.5-alt1
- 0.6.5

* Tue Dec 11 2007 Victor Forsyuk <force@altlinux.org> 0.6.4-alt1
- 0.6.4 (fixes vulnerability that can cause DoS).

* Tue Nov 13 2007 Victor Forsyuk <force@altlinux.org> 0.6.3-alt1
- Initial build.
