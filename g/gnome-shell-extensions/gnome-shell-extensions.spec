%define ver_major 3.4
%define domain gcampax.github.com

Name: gnome-shell-extensions
Version: %ver_major.0
Release: alt1

Summary: GNOME Shell Extensions
Group: Graphical desktop/GNOME
License: GPLv2+
Url: http://live.gnome.org/GnomeShell
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

BuildArch: noarch

Source: http://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar

Requires: gnome-shell >= %version

BuildRequires: gnome-common intltool libgnome-desktop3-devel libgtop-devel

%description
GNOME Shell Extensions is a collection of extensions providing additional
and optional functionality to GNOME Shell.
See %_docdir/%name-%version/README for more information.

%prep
%setup -q -n %name-%version

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
    --disable-schemas-compile \
    --enable-extensions=all
%make_build

%check
%make check

%install
%make DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%dir %_datadir/gnome-shell/extensions
# alternate-tab
%dir %_datadir/gnome-shell/extensions/alternate-tab@gnome-shell-extensions.%domain
%_datadir/gnome-shell/extensions/alternate-tab@gnome-shell-extensions.%domain/extension.js
%_datadir/gnome-shell/extensions/alternate-tab@gnome-shell-extensions.%domain/metadata.json
%_datadir/gnome-shell/extensions/alternate-tab@gnome-shell-extensions.%domain/stylesheet.css
%_datadir/gnome-shell/extensions/alternate-tab@gnome-shell-extensions.%domain/convenience.js
%_datadir/gnome-shell/extensions/alternate-tab@gnome-shell-extensions.%domain/prefs.js
%_datadir/glib-2.0/schemas/org.gnome.shell.extensions.alternate-tab.gschema.xml

# alternative status menu
%dir %_datadir/gnome-shell/extensions/alternative-status-menu@gnome-shell-extensions.%domain
%_datadir/gnome-shell/extensions/alternative-status-menu@gnome-shell-extensions.%domain/extension.js
%_datadir/gnome-shell/extensions/alternative-status-menu@gnome-shell-extensions.%domain/metadata.json
%_datadir/gnome-shell/extensions/alternative-status-menu@gnome-shell-extensions.%domain/stylesheet.css
%_datadir/gnome-shell/extensions/alternative-status-menu@gnome-shell-extensions.%domain/convenience.js

# dock
%dir %_datadir/gnome-shell/extensions/dock@gnome-shell-extensions.%domain
%_datadir/gnome-shell/extensions/dock@gnome-shell-extensions.%domain/extension.js
%_datadir/gnome-shell/extensions/dock@gnome-shell-extensions.%domain/metadata.json
%_datadir/gnome-shell/extensions/dock@gnome-shell-extensions.%domain/stylesheet.css
%_datadir/gnome-shell/extensions/dock@gnome-shell-extensions.%domain/convenience.js
%_datadir/glib-2.0/schemas/org.gnome.shell.extensions.dock.gschema.xml

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

# xrandr-indicator
%dir %_datadir/gnome-shell/extensions/xrandr-indicator@gnome-shell-extensions.%domain
%_datadir/gnome-shell/extensions/xrandr-indicator@gnome-shell-extensions.%domain/extension.js
%_datadir/gnome-shell/extensions/xrandr-indicator@gnome-shell-extensions.%domain/metadata.json
%_datadir/gnome-shell/extensions/xrandr-indicator@gnome-shell-extensions.%domain/stylesheet.css
%_datadir/gnome-shell/extensions/xrandr-indicator@gnome-shell-extensions.%domain/convenience.js


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

%if 0
# gajim integration
%dir %_datadir/gnome-shell/extensions/gajim@gnome-shell-extensions.%domain
%_datadir/gnome-shell/extensions/gajim@gnome-shell-extensions.%domain/extension.js
%_datadir/gnome-shell/extensions/gajim@gnome-shell-extensions.%domain/metadata.json
%_datadir/gnome-shell/extensions/gajim@gnome-shell-extensions.%domain/stylesheet.css
%_datadir/gnome-shell/extensions/gajim@gnome-shell-extensions.%domain/convenience.js

# example
%dir %_datadir/gnome-shell/extensions/example@gnome-shell-extensions.%domain
%_datadir/gnome-shell/extensions/example@gnome-shell-extensions.%domain/extension.js
%_datadir/gnome-shell/extensions/example@gnome-shell-extensions.%domain/metadata.json
%_datadir/gnome-shell/extensions/example@gnome-shell-extensions.%domain/stylesheet.css
%_datadir/gnome-shell/extensions/example@gnome-shell-extensions.%domain/convenience.js
%_datadir/gnome-shell/extensions/example@gnome-shell-extensions.%domain/prefs.js
%_datadir/glib-2.0/schemas/org.gnome.shell.extensions.example.gschema.xml
%endif

%doc README

%changelog
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
