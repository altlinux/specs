%define gtk2_ver 2.14.0

Name: gtk-xfce-engine
Summary: Xfce gtk theme engine with various different themes
Version: 3.1.0
Release: alt1
License: %gpl2plus
Url: http://www.xfce.org/
# Upstream: git://git.xfce.org/xfce/gtk-xfce-engine
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Group: Graphical desktop/XFce
Packager: Xfce Team <xfce@packages.altlinux.org>

BuildRequires(pre): rpm-build-licenses

BuildRequires: rpm-build-xfce4 >= 0.1.1 xfce4-dev-tools
BuildRequires: libICE-devel libXt-devel xorg-cf-files
BuildRequires: libgtk+2-devel >= %gtk2_ver libgtk+3-devel

%description
This package provides the Xfce Gtk+-2.0 and Gtk+-3.0 engines,
which allows for homogeneity in applications for both business and
personal desktops.

%package -n gtk2-themes-xfce4
Summary: Xfce Gtk+-2.0 engine and themes
Group: Graphical desktop/XFce
Obsoletes: gtk-engines-xfce < 2.8.1
Provides: gtk-engines-xfce = %version-%release
Obsoletes: libgtk-engines-xfce4 < 2.8.1
Provides: libgtk-engines-xfce4 = %version-%release

%description -n gtk2-themes-xfce4
This package provides the Xfce Gtk+-2.0 engine, which allows for
homogeneity in applications for both business and personal desktops.

%prep
%setup
%patch -p1

# Don't use git tag in version.
%xfce4_drop_gitvtag gtk_xfce_engine_version_tag configure.ac.in

%build
%xfce4reconf
touch ChangeLog
%configure \
	--disable-static \
	--enable-gtk2 \
	--disable-gtk3 \
	--enable-debug=no
%make_build

%install
%makeinstall_std

%files -n gtk2-themes-xfce4
%exclude %_libdir/gtk-2.0/*/engines/*.la
%_libdir/gtk-2.0/*/engines/*.so
%dir %_datadir/themes/*
%_datadir/themes/*/gtk-2.0
%doc AUTHORS

%changelog
* Thu Feb 19 2015 Mikhail Efremov <sem@altlinux.org> 3.1.0-alt1
- Drop gtk3 theme engine.
- Fix Xfce name (XFCE -> Xfce).
- Updated to 3.1.0.

* Tue Aug 28 2012 Mikhail Efremov <sem@altlinux.org> 3.0.0-alt2
- Patch from upstream:
  + Don't leak a graduent pattern at each draw (bug #8521).

* Sat Apr 28 2012 Mikhail Efremov <sem@altlinux.org> 3.0.0-alt1
- Updated to 3.0.0.

* Tue Apr 17 2012 Mikhail Efremov <sem@altlinux.org> 2.99.3-alt1
- Updated to 2.99.3.

* Wed Apr 11 2012 Mikhail Efremov <sem@altlinux.org> 2.99.2-alt1
- Updated to 2.99.2.

* Sat Feb 11 2012 Mikhail Efremov <sem@altlinux.org> 2.99.1-alt1
- Updated to 2.99.1.

* Thu Dec 29 2011 Mikhail Efremov <sem@altlinux.org> 2.99.0-alt1
- Updated to 2.99.0.

* Thu Nov 17 2011 Mikhail Efremov <sem@altlinux.org> 2.9.0-alt1
- Updated to 2.9.0.

* Wed Mar 09 2011 Mikhail Efremov <sem@altlinux.org> 2.8.1-alt1
- Rename package (closes: #11695).
- Updated to 2.8.1.

* Wed Jan 19 2011 Mikhail Efremov <sem@altlinux.org> 2.8.0-alt1
- Fix license.
- rename spec.
- Spec cleanup.
- Updated to 2.8.0.

* Wed Apr 29 2009 Denis Koryavov <dkoryavov@altlinux.org> 2.6.0-alt2
- Technical update for easy upgrade from Desktop 5.0

* Tue Apr 28 2009 Denis Koryavov <dkoryavov@altlinux.org> 2.6.0-alt1.M50.1
- Backport to Desktop 5.0

* Sun Apr 12 2009 Denis Koryavov <dkoryavov@altlinux.org> 2.6.0-alt1
Xfce 4.6.0

* Tue Jan 27 2009 Eugene Ostapets <eostapets@altlinux.ru> 2.5.99.1-alt1
- Xfce 4.6rc1

* Thu Jan 22 2009 Eugene Ostapets <eostapets@altlinux.ru> 2.5.93-alt1
- Xfce 4.6 beta 3

* Fri Oct 24 2008 Eugene Ostapets <eostapets@altlinux.org> 2.5.91-alt1
- Xfce 4.6 beta1

* Mon Nov 19 2007 Eugene Ostapets <eostapets@altlinux.org> 2.4.2-alt1
- Xfce 4.4.2 release

* Sat Apr 14 2007 Eugene Ostapets <eostapets@altlinux.ru> 2.4.1-alt1
- Xfce 4.4.1 release

* Mon Jan 22 2007 Eugene Ostapets <eostapets@altlinux.ru> 2.4.0-alt0.1
- Xfce 4.4 release

* Sun Nov 05 2006 Eugene Ostapets <eostapets@altlinux.ru> 2.3.99.2-alt1
- new version

* Sat Sep 30 2006 Eugene Ostapets <eostapets@altlinux.ru> 2.3.99.1-alt1
- new version

* Fri Apr 28 2006 Eugene Ostapets <eostapets@altlinux.ru> 2.3.90.1-alt0.1
- new version

* Fri Sep 02 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.2.1-alt1
- New upstream version.

* Thu Mar 18 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.1.1-alt2.4
- rebuild against gtk-2.4.0.

* Wed Jun 11 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.1-alt1.4
- new version.

* Wed Dec 18 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.8-alt1.4
- Rebuilt with gtk-2.1.5

* Fri Dec 06 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.8-alt1.3
- Rebuilt with gtk-2.1.3.

* Sun Nov 03 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.8-alt1.2
- Rebuilt with new gtk2.

* Thu Oct 24 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.8-alt1.1
- Rebuilt with new gtk2.

* Wed Oct 09 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.8-alt1
- First build for Sisyphus.
