Name: font-manager
Version: 0.7.1
Release: alt1

Summary: A font management application for the GNOME desktop
License: GPLv3
Group: Graphical desktop/GNOME
Url: http://code.google.com/p/%name

Source: http://%name.googlecode.com/files/%name-%version.tar.bz2

BuildRequires: libgtk+3-devel libjson-glib-devel libgee0.8-devel
BuildRequires: libgucharmap-devel libsqlite3-devel libxml2-devel
BuildRequires: intltool yelp-tools
BuildRequires: vala-tools
BuildRequires: gobject-introspection-devel libgucharmap-gir-devel

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
export ac_cv_prog_HAVE_FILE_ROLLER="yes"
%configure
# SMP-incompatible build
%make

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/glib-2.0/schemas/org.gnome.FontManager.gschema.xml
%_datadir/appdata/%name.appdata.xml
%doc README


%changelog
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

