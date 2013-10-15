%define ver_major 3.10
%define domain gcampax.github.com
%define _libexecdir %_prefix/libexec

Name: gnome-shell-extensions
Version: %ver_major.1
Release: alt1

Summary: GNOME Shell Extensions
Group: Graphical desktop/GNOME
License: GPLv2+
Url: https://live.gnome.org/GnomeShell
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

BuildArch: noarch

Source: http://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

Requires: gnome-shell >= 3.9.91

BuildRequires: gnome-common intltool libgnome-desktop3-devel libgtop-devel

%description
GNOME Shell Extensions is a collection of extensions providing additional
and optional functionality to GNOME Shell.
See %_docdir/%name-%version/README for more information.

%prep
%setup -n %name-%version

%build
#NOCONFIGURE=1 ./autogen.sh
%configure \
    --disable-schemas-compile \
    --enable-extensions=all
%make_build

%check
%make check

%install
%make DESTDIR=%buildroot install

cat <<__START_GNOME__ >startgnome
#!/bin/sh

. %_datadir/gnome-session/startgnome-common

exec %_bindir/gnome-session --session gnome-classic "\$@"
__START_GNOME__

install -pD -m755 startgnome %buildroot%_bindir/startgnome-classic

mkdir -p %buildroot%_sysconfdir/X11/wmsession.d/
cat << __EOF__ > %buildroot%_sysconfdir/X11/wmsession.d/03Gnome-classic
NAME=Gnome-classic
ICON=%_iconsdir/gnome.svg
DESC=Gnome Classic Mode
EXEC=%_bindir/startgnome-classic
SCRIPT:
exec %_bindir/startgnome-classic
__EOF__


%find_lang %name

%files -f %name.lang
## Classic mode
%_bindir/startgnome-classic
%_sysconfdir/X11/wmsession.d/03Gnome-classic
%_datadir/applications/gnome-shell-classic.desktop
%_datadir/gnome-session/sessions/gnome-classic.session
%_datadir/gnome-shell/modes/classic.json
%_datadir/gnome-shell/theme/classic-toggle-off-intl.svg
%_datadir/gnome-shell/theme/classic-toggle-off-us.svg
%_datadir/gnome-shell/theme/classic-toggle-on-intl.svg
%_datadir/gnome-shell/theme/classic-toggle-on-us.svg
%_datadir/gnome-shell/theme/classic-process-working.svg
%_datadir/gnome-shell/theme/gnome-classic.css
%_datadir/glib-2.0/schemas/org.gnome.shell.extensions.classic-overrides.gschema.xml
%exclude %_datadir/xsessions/gnome-classic.desktop

## Extensions
%dir %_datadir/gnome-shell/extensions
# alternate-tab
%dir %_datadir/gnome-shell/extensions/alternate-tab@gnome-shell-extensions.%domain
%_datadir/gnome-shell/extensions/alternate-tab@gnome-shell-extensions.%domain/extension.js
%_datadir/gnome-shell/extensions/alternate-tab@gnome-shell-extensions.%domain/metadata.json
%_datadir/gnome-shell/extensions/alternate-tab@gnome-shell-extensions.%domain/stylesheet.css
%_datadir/gnome-shell/extensions/alternate-tab@gnome-shell-extensions.%domain/convenience.js
%_datadir/gnome-shell/extensions/alternate-tab@gnome-shell-extensions.%domain/prefs.js


# windowsNavigator
%dir %_datadir/gnome-shell/extensions/windowsNavigator@gnome-shell-extensions.%domain
%_datadir/gnome-shell/extensions/windowsNavigator@gnome-shell-extensions.%domain/extension.js
%_datadir/gnome-shell/extensions/windowsNavigator@gnome-shell-extensions.%domain/metadata.json
%_datadir/gnome-shell/extensions/windowsNavigator@gnome-shell-extensions.%domain/stylesheet.css
%_datadir/gnome-shell/extensions/windowsNavigator@gnome-shell-extensions.%domain/convenience.js

# auto-move-windows
%dir %_datadir/gnome-shell/extensions/auto-move-windows@gnome-shell-extensions.%domain
%_datadir/gnome-shell/extensions/auto-move-windows@gnome-shell-extensions.%domain/extension.js
%_datadir/gnome-shell/extensions/auto-move-windows@gnome-shell-extensions.%domain/metadata.json
%_datadir/gnome-shell/extensions/auto-move-windows@gnome-shell-extensions.%domain/stylesheet.css
%_datadir/gnome-shell/extensions/auto-move-windows@gnome-shell-extensions.%domain/convenience.js
%_datadir/gnome-shell/extensions/auto-move-windows@gnome-shell-extensions.%domain/prefs.js
%_datadir/glib-2.0/schemas/org.gnome.shell.extensions.auto-move-windows.gschema.xml

# user theme loading
%dir %_datadir/gnome-shell/extensions/user-theme@gnome-shell-extensions.%domain
%_datadir/gnome-shell/extensions/user-theme@gnome-shell-extensions.%domain/extension.js
%_datadir/gnome-shell/extensions/user-theme@gnome-shell-extensions.%domain/metadata.json
%_datadir/gnome-shell/extensions/user-theme@gnome-shell-extensions.%domain/stylesheet.css
%_datadir/gnome-shell/extensions/user-theme@gnome-shell-extensions.%domain/convenience.js
%_datadir/glib-2.0/schemas/org.gnome.shell.extensions.user-theme.gschema.xml

# removable drives menu
%dir %_datadir/gnome-shell/extensions/drive-menu@gnome-shell-extensions.%domain
%_datadir/gnome-shell/extensions/drive-menu@gnome-shell-extensions.%domain/extension.js
%_datadir/gnome-shell/extensions/drive-menu@gnome-shell-extensions.%domain/metadata.json
%_datadir/gnome-shell/extensions/drive-menu@gnome-shell-extensions.%domain/stylesheet.css
%_datadir/gnome-shell/extensions/drive-menu@gnome-shell-extensions.%domain/convenience.js


# apps-menu
%dir %_datadir/gnome-shell/extensions/apps-menu@gnome-shell-extensions.%domain
%_datadir/gnome-shell/extensions/apps-menu@gnome-shell-extensions.%domain/extension.js
%_datadir/gnome-shell/extensions/apps-menu@gnome-shell-extensions.%domain/metadata.json
%_datadir/gnome-shell/extensions/apps-menu@gnome-shell-extensions.%domain/stylesheet.css
%_datadir/gnome-shell/extensions/apps-menu@gnome-shell-extensions.%domain/convenience.js

# native-window-placement
%dir %_datadir/gnome-shell/extensions/native-window-placement@gnome-shell-extensions.%domain
%_datadir/gnome-shell/extensions/native-window-placement@gnome-shell-extensions.%domain/extension.js
%_datadir/gnome-shell/extensions/native-window-placement@gnome-shell-extensions.%domain/metadata.json
%_datadir/gnome-shell/extensions/native-window-placement@gnome-shell-extensions.%domain/stylesheet.css
%_datadir/gnome-shell/extensions/native-window-placement@gnome-shell-extensions.%domain/convenience.js
%_datadir/glib-2.0/schemas/org.gnome.shell.extensions.native-window-placement.gschema.xml

# places-menu
%dir %_datadir/gnome-shell/extensions/places-menu@gnome-shell-extensions.%domain
%_datadir/gnome-shell/extensions/places-menu@gnome-shell-extensions.%domain/extension.js
%_datadir/gnome-shell/extensions/places-menu@gnome-shell-extensions.%domain/metadata.json
%_datadir/gnome-shell/extensions/places-menu@gnome-shell-extensions.%domain/stylesheet.css
%_datadir/gnome-shell/extensions/places-menu@gnome-shell-extensions.%domain/convenience.js
%_datadir/gnome-shell/extensions/places-menu@gnome-shell-extensions.%domain/placeDisplay.js

# system monitor
%dir %_datadir/gnome-shell/extensions/systemMonitor@gnome-shell-extensions.%domain
%_datadir/gnome-shell/extensions/systemMonitor@gnome-shell-extensions.%domain/extension.js
%_datadir/gnome-shell/extensions/systemMonitor@gnome-shell-extensions.%domain/metadata.json
%_datadir/gnome-shell/extensions/systemMonitor@gnome-shell-extensions.%domain/stylesheet.css
%_datadir/gnome-shell/extensions/systemMonitor@gnome-shell-extensions.%domain/convenience.js

# workspace indicator
%dir %_datadir/gnome-shell/extensions/workspace-indicator@gnome-shell-extensions.%domain
%_datadir/gnome-shell/extensions/workspace-indicator@gnome-shell-extensions.%domain/extension.js
%_datadir/gnome-shell/extensions/workspace-indicator@gnome-shell-extensions.%domain/metadata.json
%_datadir/gnome-shell/extensions/workspace-indicator@gnome-shell-extensions.%domain/stylesheet.css
%_datadir/gnome-shell/extensions/workspace-indicator@gnome-shell-extensions.%domain/convenience.js
%_datadir/gnome-shell/extensions/workspace-indicator@gnome-shell-extensions.%domain/prefs.js

# launch-new-instance
%dir %_datadir/gnome-shell/extensions/launch-new-instance@gnome-shell-extensions.gcampax.github.com
%_datadir/gnome-shell/extensions/launch-new-instance@gnome-shell-extensions.gcampax.github.com/convenience.js
%_datadir/gnome-shell/extensions/launch-new-instance@gnome-shell-extensions.gcampax.github.com/extension.js
%_datadir/gnome-shell/extensions/launch-new-instance@gnome-shell-extensions.gcampax.github.com/metadata.json
%_datadir/gnome-shell/extensions/launch-new-instance@gnome-shell-extensions.gcampax.github.com/stylesheet.css

# window-list
%dir %_datadir/gnome-shell/extensions/window-list@gnome-shell-extensions.gcampax.github.com
%_datadir/gnome-shell/extensions/window-list@gnome-shell-extensions.gcampax.github.com/classic.css
%_datadir/gnome-shell/extensions/window-list@gnome-shell-extensions.gcampax.github.com/convenience.js
%_datadir/gnome-shell/extensions/window-list@gnome-shell-extensions.gcampax.github.com/extension.js
%_datadir/gnome-shell/extensions/window-list@gnome-shell-extensions.gcampax.github.com/metadata.json
%_datadir/gnome-shell/extensions/window-list@gnome-shell-extensions.gcampax.github.com/prefs.js
%_datadir/gnome-shell/extensions/window-list@gnome-shell-extensions.gcampax.github.com/stylesheet.css
%_datadir/glib-2.0/schemas/org.gnome.shell.extensions.window-list.gschema.xml


%doc README

# example
%exclude %_datadir/gnome-shell/extensions/example@gnome-shell-extensions.%domain/
%exclude %_datadir/glib-2.0/schemas/org.gnome.shell.extensions.example.gschema.xml

%if 0
# xrandr-indicator incompatible with the new DisplayConfig mutter API
%dir %_datadir/gnome-shell/extensions/xrandr-indicator@gnome-shell-extensions.%domain
%_datadir/gnome-shell/extensions/xrandr-indicator@gnome-shell-extensions.%domain/extension.js
%_datadir/gnome-shell/extensions/xrandr-indicator@gnome-shell-extensions.%domain/metadata.json
%_datadir/gnome-shell/extensions/xrandr-indicator@gnome-shell-extensions.%domain/stylesheet.css
%_datadir/gnome-shell/extensions/xrandr-indicator@gnome-shell-extensions.%domain/convenience.js
%endif

%changelog
* Tue Oct 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Wed Sep 11 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.4-alt1
- 3.8.4

* Sat Jun 22 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.3.1-alt1
- 3.8.3.1

* Sat Jun 08 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.3-alt1
- 3.8.3

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Wed Apr 17 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Sat Nov 24 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2

* Fri Oct 05 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Wed Apr 18 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0 snapshot

* Wed Mar 21 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.90-alt1
- 3.3.90 snapshot

* Mon Oct 31 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt2
- updated from upstream git

* Mon Oct 03 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Thu Apr 28 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Sun Apr 10 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt2
- don't package buggy xrandr-indicator

* Thu Apr 07 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- first build for people/gnome
- don't package gajim integration and example plugins

