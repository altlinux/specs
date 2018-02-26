%define _pseudouser_user     _teeworlds
%define _pseudouser_group    _teeworlds
%define _pseudouser_home     %_localstatedir/teeworlds

%define svnrev 78

Name: teeworlds-tdtw
Version: 0.5.2
Release: alt1

Packager: Vladimir V. Kamarzin <vvk@altlinux.org>

Summary: Cute little buggers with guns (RTC version)
License: distributable
Group: Games/Arcade

Url: http://code.google.com/p/tdtw
Source: %name-%version.tar

Requires: teeworlds-tdtw-gamedata = %version-%release
# Automatically added by buildreq on Wed Jan 14 2009
BuildRequires: gcc-c++ libGL-devel libSDL-devel libX11-devel python-modules zlib-devel

%description
Cute little buggers with guns. Online multi-player platform 2D shooter.

This is RTC version of teeworlds. Some features:
Client:
- cool HUD
- some effects
- autoswitch weapon when out of ammo
Server:
- zombie gametype
- laser push
- hammer push

And some other features...

%package gamedata
Summary: Game data for teeworlds
License: distributable
Group: Games/Arcade
BuildArch: noarch

%description gamedata
Game data for teeworlds 2D shooter.

%package server
Summary: Teeworlds dedicated server
Group: System/Servers
Requires: %name-gamedata = %version-%release

%description server
Teeworlds dedicated server

%prep
%setup

%build
cd bam
./make_unix.sh
cd ..
bam/src/bam release

%install
# dirs
install -d %buildroot{%_bindir,%_datadir/teeworlds-tdtw}
install -d %buildroot%_var/run/%name
install -d %buildroot%_var/log/%name

# binaries
install -pm755 teeworlds %buildroot%_bindir/%name
install -pm755 teeworlds_srv %buildroot%_bindir/teeworlds_srv_tdtw
install -m755 altlinux/teeworlds_srv_tdtw_wrapper %buildroot%_bindir/

# data
cp -a data/* %buildroot%_datadir/teeworlds-tdtw/

# desktop-stuff
install -pDm644 teeworlds.desktop %buildroot%_desktopdir/teeworlds-tdtw.desktop
install -pDm644 teeworlds.png %buildroot%_liconsdir/teeworlds-tdtw.png
install -pDm644 teeworlds16.png %buildroot%_miconsdir/teeworlds-tdtw.png
install -pDm644 teeworlds32.png %buildroot%_niconsdir/teeworlds-tdtw.png

# logrotate
install -pDm644 altlinux/teeworlds-tdtw.logrotate %buildroot%_sysconfdir/logrotate.d/%name

# initscript and config
install -pDm755 altlinux/teeworlds-tdtw-zm.init %buildroot%_initdir/teeworlds-tdtw-zm
install -pDm644 altlinux/teeworlds-tdtw-zm.sysconfig %buildroot%_sysconfdir/sysconfig/teeworlds-tdtw-zm
install -pDm644 altlinux/server-zm.cfg %buildroot%_sysconfdir/%name/server-zm.cfg

%pre server
/usr/sbin/groupadd -r -f %_pseudouser_group ||:
/usr/sbin/useradd -g %_pseudouser_group -c 'The teeworlds daemon' \
        -d %_pseudouser_home -s /dev/null -r %_pseudouser_user >/dev/null 2>&1 ||:

%post server
%post_service %name-zm

%preun server
%preun_service %name-zm

%files
%_bindir/%name
%_desktopdir/*
%_miconsdir/*
%_niconsdir/*
%_liconsdir/*

%files server
%_bindir/teeworlds_srv*
%_initdir/%name-zm
%config(noreplace) %_sysconfdir/sysconfig/%name-zm
%config(noreplace) %_sysconfdir/%name/server-zm.cfg
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/logrotate.d/%name
%dir %attr(0770,root,%_pseudouser_group) %_var/run/%name
%dir %attr(0770,root,%_pseudouser_group) %_var/log/%name

%files gamedata
%_datadir/%name

%changelog
* Tue Oct 27 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 0.5.2-alt1
- Update to git 58b4e5ac1cf774918323fd188cf8add2a0c1bef9
- Sync with upstream 0.5.2.

* Fri Jun 05 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 0.5.1-alt1.svn.78
- Update to 78 rev.

* Wed May 13 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 0.5.1-alt1.svn.74
- Update to 74 rev.

* Mon Apr 27 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 0.5.1-alt1.svn.67
- Update to 67 rev.

* Wed Apr 15 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 0.5.1-alt1.svn.53
- Initial build for Sisyphus
