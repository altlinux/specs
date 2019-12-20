%def_enable snapshot
%set_verify_elf_method unresolved=relaxed

%define _libexecdir %_prefix/libexec

%define xdg_name org.gnome.FontManager
%define xdg_name1 org.gnome.FontViewer

%def_with nautilus

Name: font-manager
Version: 0.7.7
Release: alt1

Summary: A font management application for the GNOME desktop
License: GPL-3.0
Group: Graphical desktop/GNOME
Url: http://fontmanager.github.io/

%if_disabled snapshot
Source: https://github.com/FontManager/master/releases/download/%version/%name-%version.tar.bz2
%else
# VCS: https://github.com/FontManager/master.git
Source: %name-%version.tar
%endif
Patch: font-manager-0.7.5-alt-build.patch

Requires: file-roller

%define vala_ver 0.42

BuildRequires(pre): meson rpm-build-gir
BuildRequires: vala-tools >= %vala_ver
BuildRequires: libgtk+3-devel libjson-glib-devel
BuildRequires: libsqlite3-devel libxml2-devel
BuildRequires: yelp-tools desktop-file-utils libappstream-glib-devel
BuildRequires: gobject-introspection-devel libjson-glib-gir-devel libgtk+3-gir-devel
%if_with nautilus
BuildRequires(pre): rpm-build-gnome
BuildRequires: libnautilus-devel
%endif

%description
Font Manager is an application that allows users to easily manage fonts
on their system.

Font Manager is not intended to be a professional-grade font management
solution, but rather a simple application suitable for the needs of most
desktop users, and even graphics designers who may need to manage just a
few thousand font files.

Although designed with the GNOME desktop environment in mind, it should
work well with most major desktop environments such as XFCE,
Enlightenment, and even KDE.

%prep
%setup
%patch

%build
%meson \
	%{?_with_nautilus:-Dnautilus=true}
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%dir %_libexecdir/%name
%_libexecdir/%name/font-viewer
%_libdir/%name/
%_desktopdir/%xdg_name.desktop
%_desktopdir/%xdg_name1.desktop
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/dbus-1/services/%xdg_name1.service
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/glib-2.0/schemas/%xdg_name1.gschema.xml
%_man1dir/%name.1.*
%_datadir/metainfo/%xdg_name.appdata.xml
%_datadir/metainfo/%xdg_name1.appdata.xml
%{?_with_nautilus:%nautilus_extdir/*.so}
%doc README* CHANGELOG


%changelog
* Fri Dec 20 2019 Yuri N. Sedunov <aris@altlinux.org> 0.7.7-alt1
- updated to 0.7.7-2-g456d80b

* Sat Apr 27 2019 Yuri N. Sedunov <aris@altlinux.org> 0.7.5-alt2
- fixed build (ALT #36689)

* Sun Apr 21 2019 Yuri N. Sedunov <aris@altlinux.org> 0.7.5-alt1
- 0.7.5 (ported to Meson build system)
- built nautilus extension with python3 (nautilus-python-1.2.2-alt2)

* Tue Mar 19 2019 Yuri N. Sedunov <aris@altlinux.org> 0.7.4.3-alt1
- updated to 0.7.4.3-13-g96b3261

* Thu Jan 31 2019 Yuri N. Sedunov <aris@altlinux.org> 0.7.4.2-alt1
- 0.7.4.2

* Sat Sep 08 2018 Yuri N. Sedunov <aris@altlinux.org> 0.7.3.1-alt1
- 0.7.3.1

* Tue Apr 25 2017 Yuri N. Sedunov <aris@altlinux.org> 0.7.3-alt2
- updated to 0.7.3-11-gb4ee339

* Fri Oct 28 2016 Yuri N. Sedunov <aris@altlinux.org> 0.7.3-alt1
- 0.7.3

* Fri May 29 2015 Yuri N. Sedunov <aris@altlinux.org> 0.7.2-alt1
- 0.7.2 release (rev 425)

* Tue Apr 28 2015 Yuri N. Sedunov <aris@altlinux.org> 0.7.2-alt0.1
- 0.7.2, rev 422

* Sat Nov 29 2014 Yuri N. Sedunov <aris@altlinux.org> 0.7.1-alt1
- 0.7.1

* Sat Mar 17 2012 Yuri N. Sedunov <aris@altlinux.org> 0.5.7-alt2
- fixed build

* Fri Jan 06 2012 Yuri N. Sedunov <aris@altlinux.org> 0.5.7-alt1
- 0.5.7

* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.5-alt1.1
- Rebuild with Python-2.7

* Wed Jun 30 2010 Yuri N. Sedunov <aris@altlinux.org> 0.5.5-alt1
- 0.5.5

* Wed Jun 09 2010 Yuri N. Sedunov <aris@altlinux.org> 0.5.4-alt1
- 0.5.4

* Wed May 05 2010 Yuri N. Sedunov <aris@altlinux.org> 0.5.2-alt1
- 0.5.2

* Wed Mar 10 2010 Yuri N. Sedunov <aris@altlinux.org> 0.4.4-alt1
- first build for Sisyphus

