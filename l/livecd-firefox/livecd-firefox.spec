Name: livecd-firefox
Version: 0.1
Release: alt6

Summary: configure firefox for a livecd environment
License: Public domain
Group: System/X11

Url: http://altlinux.org/m-p
Packager: Michael Shigorin <mike@altlinux.org>

# it's *not* noarch, btw
%define prefix %_libdir/firefox/browser/defaults
Requires(post): %_bindir/firefox
Requires(post): %_libdir

%description
%summary
(no need for defaultness check, really)

%prep

%post
# http://permalink.gmane.org/gmane.linux.terminal-server.general/25696
[ -d %prefix ] || exit 0

prefs=%prefix/preferences/all-altlinux.js
[ ! -f $prefs ] || \
fgrep -q browser.rights $prefs || \
cat >> $prefs << _EOF_
user_pref("browser.rights.3.shown", true);
user_pref("browser.shell.checkDefaultBrowser", false);
user_pref("browser.download.manager.showWhenStarting", false);
user_pref("extensions.update.notifyUser", false);
_EOF_

%files

%changelog
* Mon Dec 04 2017 Michael Shigorin <mike@altlinux.org> 0.1-alt6
- dropped prefs.js references

* Tue May 03 2016 Michael Shigorin <mike@altlinux.org> 0.1-alt5
- adapted for Firefox 46 (prefs.js is no more, legion@ advised
  to use all-altlinux.js; the prefix has changed yet again)

* Fri Jun 07 2013 Michael Shigorin <mike@altlinux.org> 0.1-alt4
- adapted for Firefox 21 (prefs.js path now includes "browser/",
  thanks legion@ for heads-up)
- pretty Url:

* Mon Nov 12 2012 Michael Shigorin <mike@altlinux.org> 0.1-alt3
- dropped workarounds in favour of the proper arch-dependency solution
  suggested by at@

* Sun Nov 11 2012 Michael Shigorin <mike@altlinux.org> 0.1-alt2
- it's not really noarch of course

* Wed Oct 17 2012 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release (based on livecd-webkiosk-0.1-alt2)

