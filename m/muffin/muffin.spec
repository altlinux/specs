# typelibs/girs dependencies (see below) added manually because of conflict with gnome-shell names

%global _internal_version 10abba0

Name: muffin
Version: 1.0.3
Release: alt2

Summary: Window and compositing manager based on Clutter
License: GPLv2+
Group: Graphical desktop/GNOME

Url: https://github.com/linuxmint/muffin
# To generate tarball
# wget https://github.com/linuxmint/muffin/tarball/1.0.2 -O muffin-1.0.2.tar.gz
Source: %name-%version.tar.gz
Patch: %name-XKeycodeToKeySum-fix.patch

Requires: lib%name = %version-%release
Requires(post,preun): GConf
Requires: zenity

BuildPreReq: libclutter-devel >= 1.7.5
BuildPreReq: libgtk+3-devel >= 3.3.3
BuildRequires: GConf libGConf-devel libcanberra-gtk3-devel libstartup-notification-devel
BuildRequires: libXrandr-devel libXcursor-devel libXcomposite-devel
BuildRequires: libXinerama-devel libXext-devel libSM-devel
BuildRequires: gtk-doc gnome-common intltool gnome-doc-utils
BuildRequires: zenity
BuildRequires: gobject-introspection-devel libclutter-gir-devel libgtk+3-gir-devel

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

%prep
%setup -n linuxmint-%name-%_internal_version
%patch -p1

%build
%autoreconf
%configure --disable-static \
	--disable-schemas-install

SHOULD_HAVE_DEFINED="HAVE_SM HAVE_XINERAMA HAVE_XFREE_XINERAMA HAVE_SHAPE HAVE_RANDR HAVE_STARTUP_NOTIFICATION HAVE_COMPOSITE_EXTENSION"

for I in $SHOULD_HAVE_DEFINED; do
  if ! grep -q "define $I" config.h; then
    echo "$I was not defined in config.h"
    grep "$I" config.h
    exit 1
  else
    echo "$I was defined as it should have been"
    grep "$I" config.h
  fi
done

%make_build

%install
%makeinstall_std

%find_lang %name

%post
%gconf2_install %name

%preun
if [ $1 = 0 ]; then
    %gconf2_uninstall %name
fi


%files -f %name.lang
%_man1dir/muffin.1*
%_man1dir/muffin-message.1*
%_bindir/muffin
%_bindir/muffin-message
%_desktopdir/*.desktop
%_datadir/gnome/wm-properties/muffin-wm.desktop
%config %_sysconfdir/gconf/schemas/muffin.schemas
%_datadir/muffin
%doc README AUTHORS NEWS HACKING doc/theme-format.txt

%files utils
%_bindir/muffin-theme-viewer
%_bindir/muffin-window-demo
%_man1dir/muffin-theme-viewer.1*
%_man1dir/muffin-window-demo.1*

%files -n lib%name
%_libdir/lib*.so.*
%dir %_libdir/%name
%_libdir/%name/Meta-3.0.typelib
%dir %_libdir/%name/plugins
%_libdir/%name/plugins/default.so

%files -n lib%name-devel
%_includedir/*
%_libdir/lib*.so
%_libdir/%name/Meta-3.0.gir
%_pkgconfigdir/*

%changelog
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
