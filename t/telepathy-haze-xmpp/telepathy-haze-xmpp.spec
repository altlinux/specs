Name: telepathy-haze-xmpp
Version: 0.0.0
Release: alt1

Summary: XMPP profile for telepathy-haze
License: free
Group: Networking/Instant messaging
Url: http://developer.pidgin.im/wiki/Telepathy

Packager: Igor Zubkov <icesik@altlinux.org>

Source0: http://salami.ox.compsoc.net/~resiak/haze/profiles/xmpp.profile

BuildArch: noarch

Requires: telepathy-haze >= 0.1.3-alt1

%description
telepathy-haze is a connection manager built around libpurple, the
core of Pidgin (formerly Gaim), as a Summer of Code project under the
Pidgin umbrella.  Ultimately, any protocol supported by libpurple will
be supported by telepathy-haze; for now, XMPP, MSN and AIM are known to
work acceptably, and others will probably work too.

This is package contains XMPP profile for telepathy-haze.

%prep

%build

%install
mkdir -p %buildroot%_datadir/mission-control/profiles/

cp %SOURCE0 %buildroot%_datadir/mission-control/profiles/

%files
%_datadir/mission-control/profiles/*.profile

%changelog
* Fri Nov 16 2007 Igor Zubkov <icesik@altlinux.org> 0.0.0-alt1
- build for Sisyphus


