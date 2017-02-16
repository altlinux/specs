#%%set_automake_version 1.11

%define upstreamname lxappearance
%define gtkver 2
Name: lxde-%upstreamname
Version: 0.6.3
Release: alt1

Summary: %name is desktop-independent theme swither for GTK+.
License: GPL
Group: Graphical desktop/Other
Url: https://git.lxde.org/gitweb/?p=lxde/lxappearance.git
Packager: LXDE Development Team <lxde at packages.altlinux.org>

Source: %upstreamname-%version.tar
Patch1: lxappearance-0.5.2-alt-fixbuild.patch

BuildPreReq: libgtk+%gtkver-devel intltool gtk-doc xsltproc libdbus-glib-devel

%description
LXAppearance is part of LXDE project.
It's a desktop-independent theme swither for GTK+.

%package devel
Summary: devel files for lxappearance
Group: Development/Other

%description devel
This package contains files needed to build plugins for lxappearance

%prep
%setup -n %upstreamname-%version
%patch1 -p2

%build
%autoreconf
%configure --enable-man \
           --enable-dbus \
%if %gtkver==3
           --enable-gtk3
%endif

#touch -r po/Makefile po/stamp-it
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_libdir/%upstreamname/plugins

%find_lang %upstreamname

%files -f %upstreamname.lang
%doc ChangeLog README AUTHORS COPYING
%_bindir/*
%_desktopdir/*
%_datadir/%upstreamname
%_libdir/%upstreamname
%_man1dir/*

%files devel
%dir %_includedir/%upstreamname
%_includedir/%upstreamname/*.h
%_pkgconfigdir/*.pc

%changelog
* Wed Feb 15 2017 Anton Midyukov <antohami@altlinux.org> 0.6.3-alt1
- new version 0.6.3

* Wed Jun 29 2016 Anton Midyukov <antohami@altlinux.org> 0.6.2-alt2
- Enable dbus support.

* Tue May 17 2016 Anton Midyukov <antohami@altlinux.org> 0.6.2-alt1
- New version (0.6.2).

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt1.1
- Fixed build

* Thu May 24 2012 Radik Usupov <radik@altlinux.org> 0.5.2-alt1
- New version (0.5.2)

* Mon Feb 13 2012 Radik Usupov <radik@altlinux.org> 0.5.1-alt2
- new upstream snapshot

* Fri Aug 26 2011 Radik Usupov <radik@altlinux.org> 0.5.1-alt1.11524650
- new upstream snapshot

* Thu Jun 02 2011 Mykola Grechukh <gns@altlinux.ru> 0.5.0-alt3.g4619e8a
- new upstream snapshot

* Mon Feb 14 2011 Mykola Grechukh <gns@altlinux.ru> 0.5.0-alt2.g7f14ba7
- merged upstream git

* Tue Aug 10 2010 Mykola Grechukh <gns@altlinux.ru> 0.5.0-alt1
- new upstream version

* Mon Jan 11 2010 Mykola Grechukh <gns@altlinux.ru> 0.4.0-alt0.1
- new version

* Wed Dec 09 2009 Mykola Grechukh <gns@altlinux.ru> 0.3.0-alt1
- new version

* Fri Jul 17 2009 Nick S. Grechukh <gns@altlinux.org> 0.2.1-alt3
- build fixed (infinite loop in po/)

* Thu Jul 16 2009 Nick S. Grechukh <gns@altlinux.org> 0.2.1-alt2
- packager fixed

* Thu Jul 16 2009 Nick S. Grechukh <gns@altlinux.org> 0.2.1-alt1
- new version. post/preun update_menus removed

* Fri Jul 18 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.2-alt1
- new version

* Fri May 23 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.1-alt1
- First version of RPM package for Sisyphus.
