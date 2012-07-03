%define _name frippery

Name: gnome-shell-extensions-%_name
Version: 0.4.0
Release: alt1

Summary: GNOME Shell extensions for GNOME 2 user experience
Group: Graphical desktop/GNOME
License: GPLv2+
Url: http://intgat.tigress.co.uk/rmy/extensions/index.html

Source: gnome-shell-%_name-%version.tgz

BuildArch: noarch
Requires: gnome-shell >= 3.2
BuildRequires: rpm-build-gir

%description
The gnome-shell-extensions-%_name package contains a set extensions for the GNOME
Shell that provide a user experience more akin to that of GNOME 2. The
extensions:

 * move the clock to the right of the panel
 * add launchers for favourite applications to the panel
 * replace the Activities button with an Applications menu
 * restore static workspaces
 * replace Suspend menu item with Shut Down
 * add a bottom panel with window list and workspace switcher

%prep
%setup -n %_name -c
mv .local/share/gnome-shell/* ./ && rm -rf .local

%install
mkdir -p %buildroot%_datadir/gnome-shell
find . -name '*.po' -delete
cp -R extensions %buildroot%_datadir/gnome-shell/

%files
%_datadir/gnome-shell/extensions/*/
%doc gnome-shell-%_name/*

%changelog
* Wed Apr 18 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0

* Sun Jan 01 2012 Yuri N. Sedunov <aris@altlinux.org> 0.3.6-alt1
- 0.3.6

* Sat Dec 03 2011 Yuri N. Sedunov <aris@altlinux.org> 0.3.4-alt1
- adapted for Sisyphus

* Sun Nov 27 2011 Ron Yorston <rmy@tigress.co.uk> 0.3.4-1
- Fix bugs in workspace switching
- Add workspace switching popup that understands the grid layout

* Tue Nov 22 2011 Ron Yorston <rmy@tigress.co.uk> 0.3.3-1
- Allow workspaces to be arranged in a grid
- Allow the mouse scroll wheel to change workspace
- Fix a bug in handling of translations

* Sun Nov 13 2011 Ron Yorston <rmy@tigress.co.uk> 0.3.2-1
- Add icon to Applications menu
- Reinstate top-left hot corner

* Mon Nov  7 2011 Ron Yorston <rmy@tigress.co.uk> 0.3.1-1
- Only show the '!' in the message button if notifications are present
- Increase height of children of the bottom panel

* Mon Oct 17 2011 Ron Yorston <rmy@tigress.co.uk> 0.3.0-1
- Update for GNOME 3.2

* Thu Aug 18 2011 Ron Yorston <rmy@tigress.co.uk> 0.2.5-1
- Improve positioning of bottom panel on systems with multiple monitors.

* Sun Aug  7 2011 Ron Yorston <rmy@tigress.co.uk> 0.2.4-1
- Fix bug in bottom panel that stopped Alt+Tab from working.
- Remove conflict with alternative-status-menu:  different users may wish
  to enable different combinations of installed extensions.

* Fri Jun 17 2011 Ron Yorston <rmy@tigress.co.uk> 0.2.3-1
- Another attempt at fixing the window list bug.

* Mon Jun 13 2011 Ron Yorston <rmy@tigress.co.uk> 0.2.2-1
- Fix bug in updating of window list as windows are added/removed.

* Wed Jun  8 2011 Ron Yorston <rmy@tigress.co.uk> 0.2.1-1
- Make the width of the clock more stable as the time changes.

* Thu Jun  2 2011 Ron Yorston <rmy@tigress.co.uk> 0.2.0-1
- Add bottom panel

* Tue May 31 2011 Ron Yorston <rmy@tigress.co.uk> 0.1.1-1
- Fix stylesheet problem due to user-theme extension
- Fix launcher tooltips for applications without comments

* Wed May 25 2011 Ron Yorston <rmy@tigress.co.uk> 0.1.0-1
- Add Shut Down menu extension

* Sun May 22 2011 Ron Yorston <rmy@tigress.co.uk> 0.0.4-1
- Initial RPM release
