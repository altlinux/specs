Name: livecd-firefox
Version: 0.1
Release: alt3

Summary: confiure firefox for a livecd environment
License: Public domain
Group: System/X11

Url: http://www.altlinux.org/Mkimage/Profiles/m-p
Packager: Michael Shigorin <mike@altlinux.org>

# it's *not* noarch, btw
%define prefsjs %_libdir/firefox/defaults/profile/prefs.js
Requires(post): %prefsjs

%description
%summary
(no need for defaultness check, really)

%prep

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

%changelog
* Mon Nov 12 2012 Michael Shigorin <mike@altlinux.org> 0.1-alt3
- dropped workarounds in favour of the proper arch-dependency solution
  suggested by at@

* Sun Nov 11 2012 Michael Shigorin <mike@altlinux.org> 0.1-alt2
- it's not really noarch of course

* Wed Oct 17 2012 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release (based on livecd-webkiosk-0.1-alt2)

