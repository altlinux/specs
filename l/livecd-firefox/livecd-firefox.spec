Name: livecd-firefox
Version: 0.1
Release: alt2

Summary: confiure firefox for a livecd environment
License: Public domain
Group: System/X11

Url: http://www.altlinux.org/Mkimage/Profiles/m-p
Packager: Michael Shigorin <mike@altlinux.org>

Requires: firefox
# it's *not* noarch
%define profdir %_libdir/firefox/defaults/profile
%define prefsjs %profdir/prefs.js

%description
%summary
(no need for defaultness check, really)

%prep

%install
mkdir -p %buildroot%profdir

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

# the build system's noarch check is a bit too smart, sigh
%files
%dir %profdir

%changelog
* Sun Nov 11 2012 Michael Shigorin <mike@altlinux.org> 0.1-alt2
- it's not really noarch of course

* Wed Oct 17 2012 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release (based on livecd-webkiosk-0.1-alt2)

