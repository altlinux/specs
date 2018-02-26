%define base gtk-engines

Name: %base-cleanice
Version: 2.4.0
Release: alt2

Summary: A GTK+2 theme engine - Clean Ice
License: GPL
Group: Graphical desktop/GNOME
Url: http://art.gnome.org

Source: %url/download/themes/gtk2/156/%name-%version.tar.gz

%define gtk_ver 2.10.0
%define gtk_binary_ver 2.10.0

Requires: libgtk+2 >= %gtk_ver
BuildPreReq: libgtk+2-devel >= %gtk_ver

%description
Simple, clean theme engine...

%prep
%setup -q

%build
%configure
%make_build

%install
%makeinstall

%files
%_libdir/gtk-2.0/%gtk_binary_ver/engines/*.so
%doc AUTHORS ChangeLog NEWS README TODO

%exclude %_libdir/gtk-2.0/%gtk_binary_ver/engines/*.la

%changelog
* Sun Aug 13 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.4.0-alt2
- rebuilt with Gtk+ 2.10
- spec cleanup

* Sun Mar 13 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Thu Mar 18 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.2.6-alt2.4
- 1.2.6

* Wed Dec 18 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.1.6.2-alt1.4
- Rebuilt with gtk-2.1.5

* Fri Dec 06 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.1.6.2-alt1.3
- Rebuilt with gtk-2.1.3

* Sun Nov 03 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.1.6.2-alt1.2
- Rebuilt with new gtk2.

* Thu Oct 24 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.1.6.2-alt1.1
- Rebuilt with new gtk2.

* Wed Oct 09 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.1.6.2-alt1
- First build forSisyphus.
