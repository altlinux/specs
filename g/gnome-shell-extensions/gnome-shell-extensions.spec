%def_disable snapshot

%define ver_major 44
%define beta %nil
%define domain gcampax.github.com
%define _libexecdir %_prefix/libexec

%def_enable classic_mode

Name: gnome-shell-extensions
Version: %ver_major.0
Release: alt1%beta

Summary: GNOME Shell Extensions
Group: Graphical desktop/GNOME
License: GPLv2+
Url: https://wiki.gnome.org/Projects/GnomeShell

BuildArch: noarch

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz
%else
Source: %name-%version%beta.tar
%endif

Requires: gnome-shell >= %version

# extensions/apps-menu/extension.js
# const {
#     Atk, Clutter, Gio, GLib, GMenu, GObject, Gtk, Meta, Shell, St
# } = imports.gi;
%{?_enable_classic_mode:Requires: typelib(GMenu) = 3.0}

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: meson libgjs-devel libmozjs78-tools sassc

%description
GNOME Shell Extensions is a collection of extensions providing additional
and optional functionality to GNOME Shell.
See %_docdir/%name-%version/README for more information.

%prep
%setup -n %name-%version%beta

%build
%meson \
    %{?_enable_classic_mode:-Dclassic_mode=true} \
    -Dextension_set=all
%meson_build

%check
%meson_test

%install
%meson_install
%find_lang %name

%files -f %name.lang
# Classic mode
%if_enabled classic_mode
%_datadir/xsessions/gnome-classic.desktop
%_datadir/wayland-sessions/gnome-classic-wayland.desktop
%_datadir/wayland-sessions/gnome-classic.desktop
%_datadir/xsessions/gnome-classic-xorg.desktop
%_datadir/gnome-shell/modes/classic.json
%_datadir/gnome-shell/theme/classic-process-working.svg
%_datadir/gnome-shell/theme/gnome-classic.css
%_datadir/gnome-shell/theme/gnome-classic-high-contrast.css
%_datadir/glib-2.0/schemas/00_org.gnome.shell.extensions.classic.gschema.override
%endif

## Extensions
%dir %_datadir/gnome-shell/extensions
# windowsNavigator
%dir %_datadir/gnome-shell/extensions/windowsNavigator@gnome-shell-extensions.%domain
%_datadir/gnome-shell/extensions/windowsNavigator@gnome-shell-extensions.%domain/extension.js
%_datadir/gnome-shell/extensions/windowsNavigator@gnome-shell-extensions.%domain/metadata.json
%_datadir/gnome-shell/extensions/windowsNavigator@gnome-shell-extensions.%domain/stylesheet.css

# auto-move-windows
%dir %_datadir/gnome-shell/extensions/auto-move-windows@gnome-shell-extensions.%domain
%_datadir/gnome-shell/extensions/auto-move-windows@gnome-shell-extensions.%domain/extension.js
%_datadir/gnome-shell/extensions/auto-move-windows@gnome-shell-extensions.%domain/metadata.json
%_datadir/gnome-shell/extensions/auto-move-windows@gnome-shell-extensions.%domain/prefs.js
%_datadir/glib-2.0/schemas/org.gnome.shell.extensions.auto-move-windows.gschema.xml

# user theme loading
%dir %_datadir/gnome-shell/extensions/user-theme@gnome-shell-extensions.%domain
%_datadir/gnome-shell/extensions/user-theme@gnome-shell-extensions.%domain/extension.js
%_datadir/gnome-shell/extensions/user-theme@gnome-shell-extensions.%domain/prefs.js
%_datadir/gnome-shell/extensions/user-theme@gnome-shell-extensions.%domain/util.js
%_datadir/gnome-shell/extensions/user-theme@gnome-shell-extensions.%domain/metadata.json
%_datadir/glib-2.0/schemas/org.gnome.shell.extensions.user-theme.gschema.xml

# removable drives menu
%dir %_datadir/gnome-shell/extensions/drive-menu@gnome-shell-extensions.%domain
%_datadir/gnome-shell/extensions/drive-menu@gnome-shell-extensions.%domain/extension.js
%_datadir/gnome-shell/extensions/drive-menu@gnome-shell-extensions.%domain/metadata.json
%_datadir/gnome-shell/extensions/drive-menu@gnome-shell-extensions.%domain/stylesheet.css

# apps-menu
%dir %_datadir/gnome-shell/extensions/apps-menu@gnome-shell-extensions.%domain
%_datadir/gnome-shell/extensions/apps-menu@gnome-shell-extensions.%domain/extension.js
%_datadir/gnome-shell/extensions/apps-menu@gnome-shell-extensions.%domain/metadata.json
%_datadir/gnome-shell/extensions/apps-menu@gnome-shell-extensions.%domain/stylesheet.css
%_datadir/glib-2.0/schemas/org.gnome.shell.extensions.apps-menu.gschema.xml

# native-window-placement
%dir %_datadir/gnome-shell/extensions/native-window-placement@gnome-shell-extensions.%domain
%_datadir/gnome-shell/extensions/native-window-placement@gnome-shell-extensions.%domain/extension.js
%_datadir/gnome-shell/extensions/native-window-placement@gnome-shell-extensions.%domain/metadata.json
%_datadir/glib-2.0/schemas/org.gnome.shell.extensions.native-window-placement.gschema.xml

# places-menu
%dir %_datadir/gnome-shell/extensions/places-menu@gnome-shell-extensions.%domain
%_datadir/gnome-shell/extensions/places-menu@gnome-shell-extensions.%domain/extension.js
%_datadir/gnome-shell/extensions/places-menu@gnome-shell-extensions.%domain/metadata.json
%_datadir/gnome-shell/extensions/places-menu@gnome-shell-extensions.%domain/stylesheet.css
%_datadir/gnome-shell/extensions/places-menu@gnome-shell-extensions.%domain/placeDisplay.js

# workspace indicator
%dir %_datadir/gnome-shell/extensions/workspace-indicator@gnome-shell-extensions.%domain
%_datadir/gnome-shell/extensions/workspace-indicator@gnome-shell-extensions.%domain/extension.js
%_datadir/gnome-shell/extensions/workspace-indicator@gnome-shell-extensions.%domain/metadata.json
%_datadir/gnome-shell/extensions/workspace-indicator@gnome-shell-extensions.%domain/stylesheet.css
%_datadir/gnome-shell/extensions/workspace-indicator@gnome-shell-extensions.%domain/prefs.js

# launch-new-instance
%dir %_datadir/gnome-shell/extensions/launch-new-instance@gnome-shell-extensions.%domain
%_datadir/gnome-shell/extensions/launch-new-instance@gnome-shell-extensions.%domain/extension.js
%_datadir/gnome-shell/extensions/launch-new-instance@gnome-shell-extensions.%domain/metadata.json

# window-list
%dir %_datadir/gnome-shell/extensions/window-list@gnome-shell-extensions.%domain
%_datadir/gnome-shell/extensions/window-list@gnome-shell-extensions.%domain/classic.css
%_datadir/gnome-shell/extensions/window-list@gnome-shell-extensions.%domain/extension.js
%_datadir/gnome-shell/extensions/window-list@gnome-shell-extensions.%domain/metadata.json
%_datadir/gnome-shell/extensions/window-list@gnome-shell-extensions.%domain/prefs.js
%_datadir/gnome-shell/extensions/window-list@gnome-shell-extensions.%domain/stylesheet.css
%_datadir/gnome-shell/extensions/window-list@gnome-shell-extensions.%domain/windowPicker.js
%_datadir/gnome-shell/extensions/window-list@gnome-shell-extensions.%domain/workspaceIndicator.js
%_datadir/glib-2.0/schemas/org.gnome.shell.extensions.window-list.gschema.xml

# screenshot-window-sizer
%dir %_datadir/gnome-shell/extensions/screenshot-window-sizer@gnome-shell-extensions.%domain
%_datadir/glib-2.0/schemas/org.gnome.shell.extensions.screenshot-window-sizer.gschema.xml
%_datadir/gnome-shell/extensions/screenshot-window-sizer@gnome-shell-extensions.%domain/extension.js
%_datadir/gnome-shell/extensions/screenshot-window-sizer@gnome-shell-extensions.%domain/metadata.json
%_datadir/gnome-shell/extensions/screenshot-window-sizer@gnome-shell-extensions.%domain/stylesheet.css

%doc NEWS README.md

%changelog
* Sun Mar 19 2023 Yuri N. Sedunov <aris@altlinux.org> 44.0-alt1
- 44.0

* Thu Nov 10 2022 Yuri N. Sedunov <aris@altlinux.org> 43.1-alt1
- 43.1

* Tue Sep 20 2022 Yuri N. Sedunov <aris@altlinux.org> 43.0-alt1
- 43.0

* Mon Jul 04 2022 Yuri N. Sedunov <aris@altlinux.org> 42.3-alt1
- 42.3

* Sun May 29 2022 Yuri N. Sedunov <aris@altlinux.org> 42.2-alt1
- 42.2

* Fri May 06 2022 Yuri N. Sedunov <aris@altlinux.org> 42.1-alt1
- 42.1

* Sun Mar 13 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1
- 42.0

* Sun Feb 27 2022 Yuri N. Sedunov <aris@altlinux.org> 41.2-alt1
- 41.2

* Mon Dec 13 2021 Yuri N. Sedunov <aris@altlinux.org> 41.1-alt1
- 41.1

* Sun Sep 19 2021 Yuri N. Sedunov <aris@altlinux.org> 41.0-alt1
- 41.0

* Wed Aug 18 2021 Yuri N. Sedunov <aris@altlinux.org> 40.4-alt1
- 40.4

* Mon Jul 12 2021 Yuri N. Sedunov <aris@altlinux.org> 40.3-alt1
- 40.3

* Thu Jun 10 2021 Yuri N. Sedunov <aris@altlinux.org> 40.2-alt1
- 40.2

* Fri May 14 2021 Yuri N. Sedunov <aris@altlinux.org> 40.1-alt1
- 40.1

* Sat Mar 20 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- 40.0

* Mon Mar 15 2021 Yuri N. Sedunov <aris@altlinux.org> 40-alt0.8.rc
- 40.rc

* Thu Dec 03 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.2-alt1
- 3.38.2

* Sat Oct 24 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.1-alt1
- 3.38.1

* Tue Sep 15 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Fri Aug 21 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.3-alt1
- 3.36.3

* Thu Apr 30 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.2-alt1
- 3.36.2

* Tue Mar 31 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.1-alt1
- 3.36.1

* Sun Mar 08 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0

* Thu Dec 12 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.2-alt1
- 3.34.2

* Wed Oct 09 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt1
- 3.34.1

* Sat Sep 28 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt2
- updated to 3.34.0-4-g6462af3 (fixed classic mode with new g-s-d)

* Mon Sep 09 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Wed Jul 10 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt3
- requires typelib(GMenu) if classic_mode enabled (ALT #36997)

* Tue Jul 09 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt2
- updated to 3.32.1-1-g13372e7 (fixed apps-menu (ALT #36997))

* Wed Apr 17 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Tue Mar 12 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Tue Oct 09 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Tue Sep 04 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Sat Apr 14 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Tue Mar 13 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Thu Nov 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt1
- 3.26.2

* Wed Oct 04 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Tue Sep 12 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Thu Jul 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.3-alt1
- 3.24.3

* Thu May 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.2-alt1
- 3.24.2

* Tue Apr 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Mon Mar 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Thu Nov 10 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt1
- 3.22.2

* Tue Oct 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Wed May 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Tue Mar 08 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.4-alt1
- 3.18.4

* Sat Jan 09 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.3-alt1
- 3.18.3

* Thu Nov 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Fri Oct 16 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Wed Oct 14 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt2
- removed /usr/bin/startgnome-classic

* Tue Sep 22 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Thu Jul 02 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Wed Apr 15 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.14.4-alt1
- 3.14.4

* Sat Dec 20 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.3-alt1
- 3.14.3

* Wed Dec 10 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt2
- disabled alt-specific mechanism for run gnome-classic session,
  packaged standard xsessions/gnome-classic.desktop instead

* Wed Nov 12 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Wed Oct 15 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Wed May 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

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

