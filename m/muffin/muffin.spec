# typelibs/girs dependencies (see below) added manually because of conflict with gnome-shell names

Name: muffin
Version: 2.0.4
Release: alt1

Summary: Window and compositing manager based on Clutter
License: GPLv2+
Group: Graphical desktop/GNOME

Url: https://github.com/linuxmint/muffin
# To generate tarball
# wget https://github.com/linuxmint/muffin/tarball/1.0.2 -O muffin-1.0.2.tar.gz
Source: %name-%version.tar
#Patch: %name-%version-%release.patch

Requires: lib%name = %version-%release
Requires(post,preun): GConf
Requires: zenity

BuildPreReq: rpm-build-gir >= 0.7.1-alt6
BuildPreReq: libclutter-devel >= 1.7.5
BuildPreReq: libgtk+3-devel >= 3.3.3
BuildRequires: GConf libGConf-devel libcanberra-gtk3-devel libstartup-notification-devel
BuildRequires: libXrandr-devel libXcursor-devel libXcomposite-devel
BuildRequires: libXinerama-devel libXext-devel libSM-devel
BuildRequires: gtk-doc gnome-common intltool gnome-doc-utils
BuildRequires: zenity
BuildRequires: gobject-introspection-devel libclutter-gir-devel libgtk+3-gir-devel
BuildRequires: libcinnamon-desktop-devel libcinnamon-desktop-gir-devel


%description
Muffin is a window and compositing manager that displays and manages
your desktop via OpenGL. Muffin combines a sophisticated display engine
using the Clutter toolkit with solid window-management logic inherited
from the Metacity window manager.

While Muffin can be used stand-alone, it is primarily intended to be
used as the display core of a larger system such as Cinnamon.
For this reason, Muffin is very extensible via plugins, which
are used both to add fancy visual effects and to rework the window
management behaviors to meet the needs of the environment.

%package utils
Summary: Additional utilities for %name
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description utils
Utilities for testing Metacity/Muffin themes.

%package -n lib%name
Summary: Shared libraries for %name
Group: System/Libraries
# manual dependencies
Requires: typelib(Clutter) = 1.0 typelib(Gtk) = 3.0

%description -n lib%name
Shared libraries for Muffin and its plugins.

%package -n lib%name-devel
Summary: Development package for %name
Group: Development/C
Requires: lib%name = %version-%release
# manual dependencies
Requires: gir(Clutter) = 1.0 gir(Gtk) = 3.0

%description -n lib%name-devel
Header files and libraries for developing Muffin plugins.

%package -n lib%name-gir
Summary: GObject introspection data for the Muffin library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the Muffin library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the Muffin library
Group: System/Libraries
Requires: lib%name-devel = %version-%release lib%name-gir = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the Muffin library

%set_typelibdir %_libdir/%name
%set_girdir %_libdir/%name

%prep
%setup -n %name-%version
#%patch -p1

%build
%autoreconf
%configure --disable-static \
	--disable-schemas-compile

%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_man1dir/muffin.1*
%_man1dir/muffin-message.1*
%_bindir/muffin
%_bindir/muffin-message
%_desktopdir/*.desktop
%_datadir/muffin
%_datadir//GConf/gsettings/muffin-schemas.convert
%_datadir/glib-2.0/schemas/org.cinnamon.muffin.gschema.xml
%doc README AUTHORS NEWS HACKING doc/theme-format.txt

%files utils
%_bindir/muffin-theme-viewer
%_bindir/muffin-window-demo
%_man1dir/muffin-theme-viewer.1*
%_man1dir/muffin-window-demo.1*

%files -n lib%name
%_libdir/lib*.so.*
%dir %_libdir/%name
%dir %_libdir/%name/plugins
%_libdir/%name/plugins/default.so

%files -n lib%name-devel
%_includedir/*
%_libdir/lib*.so
%_pkgconfigdir/*

%files -n lib%name-gir
%_libdir/%name/*.typelib

%files -n lib%name-gir-devel
%_libdir/%name/*.gir


%changelog
* Tue Nov 12 2013 Vladimir Didenko <cow@altlinux.org> 2.0.4-alt1
- 2.0.4

* Tue Oct 29 2013 Vladimir Didenko <cow@altlinux.org> 2.0.3-alt1
- 2.0.3

* Mon Oct 21 2013 Vladimir Didenko <cow@altlinux.org> 2.0.2-alt1
- 2.0.2

* Thu Oct 10 2013 Vladimir Didenko <cow@altlinux.org> 2.0.1-alt1
- 2.0.1

* Wed Sep 25 2013 Yuri N. Sedunov <aris@altlinux.org> 1.8.2-alt4
- rebuild for GNOME-3.10

* Thu Aug 29 2013 Vladimir Didenko <cow@altlinux.org> 1.8.2-alt3
- v1.8.2-58-gc13a698

* Mon Aug 5 2013 Vladimir Didenko <cow@altlinux.org> 1.8.2-alt2
- 1.8.2-51-gd05c4c6

* Tue May 21 2013 Vladimir Didenko <cow@altlinux.org> 1.8.2-alt1
- 1.8.2

* Fri May 17 2013 Vladimir Didenko <cow@altlinux.org> 1.8.1-alt1
- 1.8.1

* Mon May 6 2013 Vladimir Didenko <cow@altlinux.org> 1.8.0-alt1
- 1.8.0

* Wed Apr 24 2013 Vladimir Didenko <cow@altlinux.org> 1.7.3-alt2
- 1.7.3-16-ge0ad43f
- created gir and gir-devel subpackages
- use set_typelibdir and set_girdir macroses. 

* Tue Apr 16 2013 Vladimir Didenko <cow@altlinux.org> 1.7.3-alt1
- 1.7.3

* Tue Mar 12 2013 Vladimir Didenko <cow@altlinux.org> 1.7.1-alt2
- add support for gtk-3.7 enum values

* Fri Feb 22 2013 Vladimir Didenko <cow@altlinux.org> 1.7.1-alt1
- 1.7.1-3-g2f496ac

* Fri Nov 16 2012 Vladimir Didenko <cow@altlinux.org> 1.1.2-alt2
- rebuilt for Sisyphus

* Wed Oct 31 2012 Vladimir Didenko <vladimir.didenko@gmail.com> 1.1.2-alt1
- 1.1.2

* Wed Oct 03 2012 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt1
- 1.1.1

* Wed May 30 2012 Michael Shigorin <mike@altlinux.org> 1.0.3-alt2
- rebuilt for Sisyphus

* Wed May 23 2012 Vladimir Didenko <vladimir.didenko@gmail.com> 1.0.3-alt1
- update to 1.0.3

* Thu Apr 12 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt2
- removed obsolete configure option
- added lost %%post, %%preun scripts
- simplified buildreqs, fixed reqs
- more cleanups

* Wed Apr 11 2012 Michael Shigorin <mike@altlinux.org> 1.0.2-alt1
- rebuilt for Sisyphus
- libification
- spec cleanup

* Mon Apr 09 2012 Vyacheslav Dikonov <slava@altlinux.ru> 1.0.2-slava1
- ALTLinux build
- linuxmint-muffin-a5935f8
- muffin-XKeycodeToKeySum-fix.patch

* Tue Mar 13 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.0.2-1
- update to 1.0.2

* Thu Feb 17 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.0.1-1
- update version to 1.0.1

* Thu Feb 02 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-2
- make review changes

* Wed Jan 04 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-1
- initial package based on fedora mutter srpm
