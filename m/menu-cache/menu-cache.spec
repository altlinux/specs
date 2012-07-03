Name: menu-cache
Version: 0.3.3
Release: alt1

Summary: Library and utils to speed up the manipulation for freedesktop.org menu
License: GPL
Group: Graphical desktop/Other
Url: http://lxde.sf.net
Packager: LXDE Development Team <lxde at packages.altlinux.org>

Source: %name-%version.tar.gz

# Automatically added by buildreq on Fri Jan 09 2009
BuildRequires: gcc-c++ libgio-devel

%description
Libmenu-cache is a library creating and utilizing caches to speed up
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
Libmenu-cache is a library creating and utilizing caches to speed up
the manipulation for freedesktop.org defined application menus.
It can be used as a replacement of libgnome-menu of gnome-menus.

Advantages:
1. Shorten time for loading menu entries.
2. Ease of use. (API is very similar to that of libgnome-menu)
3. Lightweight runtime library. (Parsing of the menu definition files 
   are done by menu-cache-gen when the menus are really changed.)
4. Less unnecessary and complicated file monitoring.
5. Heavily reduced disk I/O.

%package -n lib%name-devel
Summary: Library and utils to speed up the manipulation for freedesktop.org menu
License: LGPL
Group: System/Libraries
%description -n lib%name-devel
Libmenu-cache is a library creating and utilizing caches to speed up
the manipulation for freedesktop.org defined application menus.
It can be used as a replacement of libgnome-menu of gnome-menus.

Advantages:
1. Shorten time for loading menu entries.
2. Ease of use. (API is very similar to that of libgnome-menu)
3. Lightweight runtime library. (Parsing of the menu definition files 
   are done by menu-cache-gen when the menus are really changed.)
4. Less unnecessary and complicated file monitoring.
5. Heavily reduced disk I/O.

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
%doc ChangeLog INSTALL README
%_libexecdir/%name
%files -n lib%name
%_libdir/*.so.*
%files -n lib%name-devel
%_libdir/*.so
%exclude %_libdir/*.a
%_pkgconfigdir/*.pc
%_includedir/%name

%changelog
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
