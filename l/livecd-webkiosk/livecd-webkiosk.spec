Name: livecd-webkiosk
Version: 0.1
Release: alt2

Summary: start firefox for suitable webkiosk environment
License: Public domain
Group: System/X11

Url: http://www.altlinux.org/Mkimage/Profiles/m-p
Packager: Michael Shigorin <mike@altlinux.org>
BuildArch: noarch

Requires: firefox firefox-fullscreen-kiosk
Requires: ratpoison xinit

# it's *not* noarch

%define skeldir %_sysconfdir/skel
%define ifacedir %_sysconfdir/net/ifaces/eth0
%define prefsjs %_libdir/firefox/defaults/profile/prefs.js

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

%post
# http://permalink.gmane.org/gmane.linux.terminal-server.general/25696
[ ! -f %prefsjs ] || \
fgrep -q browser.rights %prefsjs || \
cat >> %prefsjs << _EOF_
user_pref("browser.rights.3.shown", true);
user_pref("browser.shell.checkDefaultBrowser", false);
user_pref("browser.download.manager.showWhenStarting", false);
user_pref("extensions.update.notifyUser", false);
_EOF_

%files
%skeldir/.xsession
%skeldir/.ratpoisonrc
%ifacedir/options

# TODO:
# - recheck prefs.js on x86_64

%changelog
* Sun Mar 25 2012 Michael Shigorin <mike@altlinux.org> 0.1-alt2
- disable firefox' default browser check

* Tue Jan 24 2012 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release

