Name: font-manager
Version: 0.5.7
Release: alt2

Summary: A font management application for the GNOME desktop
License: GPLv3
Group: Graphical desktop/GNOME
Url: http://code.google.com/p/%name

Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: http://%name.googlecode.com/files/%name-%version.tar.bz2
Patch: %name-0.5.7-alt-include.patch

BuildRequires: glib2-devel fontconfig-devel libfreetype-devel libpango-devel
BuildRequires: libsqlite3-devel python-devel

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
%patch -p1

%build
%configure
%make_build

%install
%make DESTDIR=%buildroot install

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/*
%_libdir/%name/
%_datadir/%name/
%_datadir/applications/*
%doc AUTHORS NEWS README ChangeLog


%changelog
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

