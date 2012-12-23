Name: livecd-webkiosk
Version: 0.2
Release: alt1

Summary: start the browser for a suitable webkiosk environment
License: Public domain
Group: System/X11

Url: http://altlinux.org/m-p
Packager: Michael Shigorin <mike@altlinux.org>
BuildArch: noarch

Requires: ratpoison xinit

%define skeldir %_sysconfdir/skel
%define ifacedir %_sysconfdir/net/ifaces/eth0
%define xsfile %skeldir/.xsession
%define wrapper %_bindir/webkiosk-browser

%description
%summary
(livecd specific; also employs some ratpoison)

%package firefox
Summary: firefox webkiosk setup
Group: System/X11
Requires: %name = %version-%release
Requires: livecd-firefox firefox-fullscreen-kiosk

%description firefox
%summary
(the browser == firefox)

%package chromium
Summary: chromium webkiosk setup
Group: System/X11
Requires: %name = %version-%release
Requires: chromium

%description chromium
%summary
(the browser == chromium)

%prep

%build

%install
mkdir -p %buildroot{%skeldir,%ifacedir}

cat > %buildroot%xsfile << _EOF_
#!/bin/sh
ratpoison &
[ -f /image/index.html ] && url=/image/index.html
while :; do webkiosk-browser \$url; done
_EOF_
chmod +x %buildroot%xsfile

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

%post firefox
cat > %wrapper << _EOF_
#!/bin/sh
exec firefox "\$@"
_EOF_
chmod +x %wrapper

%post chromium
cat > %wrapper << _EOF_
#!/bin/sh
exec chromium --kiosk --start-maximized "\$@"
_EOF_
chmod +x %wrapper

%files
%skeldir/.ratpoisonrc
%ifacedir/options
%xsfile

%files firefox

%files chromium

%changelog
* Sun Dec 23 2012 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- introduced chromium support (as a separate subpackage)
- NB: firefox support moved to a subpackage as well,
  please pay attention if you're upgrading live images

* Wed Oct 17 2012 Michael Shigorin <mike@altlinux.org> 0.1-alt3
- moved firefox prefs.js handling to livecd-firefox package

* Sun Mar 25 2012 Michael Shigorin <mike@altlinux.org> 0.1-alt2
- disable firefox' default browser check

* Tue Jan 24 2012 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release

