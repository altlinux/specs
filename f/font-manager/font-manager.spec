%define _libexecdir %_prefix/libexec

%define xdg_name org.gnome.FontManager
%define xdg_name1 org.gnome.FontViewer

%def_with file_roller
%def_with nautilus

Name: font-manager
Version: 0.7.3
Release: alt1

Summary: A font management application for the GNOME desktop
License: GPLv3
Group: Graphical desktop/GNOME
Url: http://fontmanager.github.io/

# VCS: https://github.com/FontManager/master.git
Source: https://github.com/FontManager/master/releases/download/%version/%name-%version.tar.bz2

%{?_with_file_roller:Requires: file-roller}

BuildRequires: libgtk+3-devel libjson-glib-devel libgee0.8-devel
BuildRequires: libgucharmap-devel libsqlite3-devel libxml2-devel
BuildRequires: intltool yelp-tools libappstream-glib-devel
BuildRequires: vala-tools
BuildRequires: gobject-introspection-devel libgucharmap-gir-devel
%{?_with_nautilus:BuildRequires: nautilus-python}

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

%build
%autoreconf
%{?_with_file_roller:export ac_cv_prog_HAVE_FILE_ROLLER="yes"}
%configure %{?_with_file_roller:--with-file-roller} \
	%{subst_with nautilus}
%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%dir %_libexecdir/%name
%_libexecdir/%name/font-viewer
%_libdir/%name/
%_desktopdir/%xdg_name.desktop
%_desktopdir/%xdg_name1.desktop
%_datadir/%name/
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/dbus-1/services/%xdg_name1.service
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/glib-2.0/schemas/%xdg_name1.gschema.xml
%_man1dir/%name.1.*
%_datadir/appdata/%xdg_name.appdata.xml
%{?_with_nautilus:%_datadir/nautilus-python/extensions/font-manager.py*}
%doc README

%exclude %_libdir/%name/*.la

%changelog
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

