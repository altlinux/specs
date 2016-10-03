Name: menu-cache
Version: 1.0.1
Release: alt1

Summary: Library and utils to speed up the manipulation for freedesktop.org menu
License: GPL
Group: Graphical desktop/Other

Url: http://lxqt.org
Source: %name-%version.tar
Packager: LXDE Development Team <lxde at packages.altlinux.org>

# Automatically added by buildreq on Wed Jan 23 2013
# optimized out: glib2-devel pkg-config
BuildRequires: gtk-doc libfm-devel libgio-devel

%description
libmenu-cache is a library creating and utilizing caches to speed up
the manipulation for freedesktop.org defined application menus.
It can be used as a replacement of libgnome-menu of gnome-menus.

Advantages:
1. Shorten time for loading menu entries.
2. Ease of use. (API is very similar to that of libgnome-menu)
3. Lightweight runtime library. (Parsing of the menu definition files
   are done by menu-cache-gen when the menus are really changed.)
4. Less unnecessary and complicated file monitoring.
5. Heavily reduced disk I/O.

%package -n lib%name
Summary: Library and utils to speed up the manipulation for freedesktop.org menu
License: LGPL
Group: System/Libraries

%description -n lib%name
libmenu-cache is a library creating and utilizing caches to speed up
the manipulation for freedesktop.org defined application menus.
It can be used as a replacement of libgnome-menu of gnome-menus.

This package contains shared libraries for libmenu-cache.

%package -n lib%name-devel
Summary: Library and utils to speed up the manipulation for freedesktop.org menu
License: LGPL
Group: Development/C

%description -n lib%name-devel
libmenu-cache is a library creating and utilizing caches to speed up
the manipulation for freedesktop.org defined application menus.
It can be used as a replacement of libgnome-menu of gnome-menus.

This package contains development headers for libmenu-cache.

%prep
%setup

%build
%autoreconf
%configure --libexecdir=%_libexecdir/%name
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc ChangeLog README
%_libexecdir/%name

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_pkgconfigdir/*.pc
%_includedir/%name
%exclude %_libdir/*.a

%changelog
* Mon Oct 03 2016 Michael Shigorin <mike@altlinux.org> 1.0.1-alt1
- 1.0.1

* Mon Nov 02 2015 Michael Shigorin <mike@altlinux.org> 1.0.0-alt1
- 1.0.0

* Tue Oct 14 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- 0.7.0

* Wed Aug 27 2014 Michael Shigorin <mike@altlinux.org> 0.6.1-alt1
- 0.6.1

* Thu May 08 2014 Michael Shigorin <mike@altlinux.org> 0.5.1-alt1
- 0.5.1
- reworked upstream git use scheme
- spec cleanup
- updated Url:

* Wed Jan 23 2013 Mykola Grechukh <gns@altlinux.ru> 0.4.1.10-alt1.g1a48be7
- updated from upstream git

* Tue Jun 12 2012 Radik Usupov <radik@altlinux.org> 0.3.3-alt1
- new version (0.3.3)

* Fri Mar 11 2011 Radik Usupov <radik@altlinux.org> 0.3.2-alt2
- rebuild for debuginfo
- change packager

* Fri Mar 12 2010 Nick S. Grechukh <gns@altlinux.ru> 0.3.2-alt1
- new version from upstream

* Mon Jan 04 2010 Mykola Grechukh <gns@altlinux.ru> 0.2.6-alt1
- new upstream version

* Fri Jan 09 2009 Eugene Ostapets <eostapets@altlinux.ru> 0.2.2-alt1
- First version of RPM package for Sisyphus.
