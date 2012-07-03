Name: libxfce4ui
Version: 4.10.0
Release: alt1

Summary: Various Gtk+2 widgets for XFce
Summary (ru_RU.UTF-8): Набор виджетов GTK 2 для Xfce
License: %lgpl2plus
Group: Graphical desktop/XFce
Url: http://www.xfce.org/

Packager: XFCE Team <xfce@packages.altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildRequires: gtk-doc intltool libSM-devel libgladeui-devel libstartup-notification-devel libxfce4util-devel libxfconf-devel xorg-cf-files

# Due xfce4-about
Conflicts: xfce-utils < 4.8.3-alt3

%description
Various Gtk+2 widgets for XFce.

%description -l ru_RU.UTF-8
Набор виджетов GTK 2 для Xfce.

%package devel
Summary: Development files for %name
Group: Development/C
PreReq: %name = %version-%release

%description devel
Header files for the %name library.

%prep
%setup
%patch -p1

%build
%xfce4reconf
%configure \
	--disable-static \
	--enable-maintainer-mode \
	--enable-gtk-doc \
	--enable-startup-notification \
	--enable-gladeui \
	--enable-debug=no
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README NEWS AUTHORS
%_bindir/*
%_desktopdir/*.desktop
%_liconsdir/*
%_libdir/*.so.*
%_datadir/glade3/catalogs/*.xml
%exclude %_datadir/glade3/catalogs/*.xml.in
%_datadir/glade3/pixmaps/*/*/*/*
%_libdir/glade3/modules/*.so
%config(noreplace) %_sysconfdir/xdg/xfce4/xfconf/xfce-perchannel-xml/*.xml
%exclude %_libdir/glade3/modules/*.la

%files devel
%_includedir/xfce4/libxfce4kbd-private-2
%_includedir/xfce4/libxfce4ui-1
%_pkgconfigdir/*.pc
%_libdir/*.so
%doc %_datadir/gtk-doc/html/%name

%changelog
* Sun Apr 29 2012 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt1
- Updated to 4.10.0.

* Tue Apr 17 2012 Mikhail Efremov <sem@altlinux.org> 4.9.2-alt1
- Updated to 4.9.2.

* Fri Apr 06 2012 Mikhail Efremov <sem@altlinux.org> 4.9.1-alt1
- Updated to 4.9.1.

* Tue Jan 10 2012 Mikhail Efremov <sem@altlinux.org> 4.9.0-alt2
- Add conflict with xfce-utils < 4.8.3-alt3.

* Tue Jan 10 2012 Mikhail Efremov <sem@altlinux.org> 4.9.0-alt1
- Updated to 4.9.0.

* Thu Dec 29 2011 Mikhail Efremov <sem@altlinux.org> 4.8.1-alt1
- Don't build static libraries.
- Use maintainer mode.
- Updated to 4.8.1.

* Tue Nov 08 2011 Mikhail Efremov <sem@altlinux.org> 4.8.0-alt4
- Replace <Primary> shortcut with <Control>.

* Mon Aug 29 2011 Mikhail Efremov <sem@altlinux.org> 4.8.0-alt3
- Updated Russian translation.

* Wed Jan 19 2011 Mikhail Efremov <sem@altlinux.org> 4.8.0-alt2
- Own xfce4-keyboard-shortcuts.xml file.
- Fix group.
- Fix license.
- Added keyboard-shortcuts patch from FC.

* Mon Jan 17 2011 Mikhail Efremov <sem@altlinux.org> 4.8.0-alt1
- Updated to 4.8.0.
- Spec cleanup.

* Sun May 16 2010 Denis Koryavov <dkoryavov@altlinux.org> 4.7.2-alt1
- First build for sisyphus. Spec based on libxfcegui4 spec file.

