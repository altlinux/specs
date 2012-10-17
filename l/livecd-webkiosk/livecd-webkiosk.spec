Name: livecd-webkiosk
Version: 0.1
Release: alt3

Summary: start firefox for suitable webkiosk environment
License: Public domain
Group: System/X11

Url: http://www.altlinux.org/Mkimage/Profiles/m-p
Packager: Michael Shigorin <mike@altlinux.org>
BuildArch: noarch

Requires: livecd-firefox firefox-fullscreen-kiosk
Requires: ratpoison xinit

BuildArch: noarch

%define skeldir %_sysconfdir/skel
%define ifacedir %_sysconfdir/net/ifaces/eth0

%description
%summary
(livecd specific; also employs some ratpoison)

%prep

%build

%install
mkdir -p %buildroot{%skeldir,%ifacedir}

cat > %buildroot%skeldir/.xsession << _EOF_
ratpoison &
[ -f /image/index.html ] && url=/image/index.html
while :; do firefox \$url; done
_EOF_
chmod +x %buildroot%skeldir/.xsession

cat > %buildroot%skeldir/.ratpoisonrc << _EOF_
startup_message off
set border 0
set padding 0 0 0 0
set barpadding 0 0
escape F25
banish
_EOF_

cat > %buildroot%ifacedir/options << _EOF_
BOOTPROTO=dhcp
_EOF_

%files
%skeldir/.xsession
%skeldir/.ratpoisonrc
%ifacedir/options

%changelog
* Wed Oct 17 2012 Michael Shigorin <mike@altlinux.org> 0.1-alt3
- moved firefox prefs.js handling to livecd-firefox package

* Sun Mar 25 2012 Michael Shigorin <mike@altlinux.org> 0.1-alt2
- disable firefox' default browser check

* Tue Jan 24 2012 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release

