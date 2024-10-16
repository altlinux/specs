%def_enable introspection
%def_enable vala
%def_disable docs

Name: xfce4-panel
Version: 4.19.5
Release: alt1

Summary: Panel for Xfce
Summary(ru_RU.UTF-8): Панель для окружения рабочего стола Xfce
License: GPLv2+
Group: Graphical desktop/XFce
Url: https://docs.xfce.org/xfce/xfce4-panel/start

Vcs: https://gitlab.xfce.org/xfce/xfce4-panel.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Packager: Xfce Team <xfce@packages.altlinux.org>

BuildRequires: rpm-build-xfce4 >= 0.1.0 xfce4-dev-tools
BuildRequires: libxfce4util-devel >= 4.17.2-alt1
BuildRequires: libxfce4ui-gtk3-devel >= 4.17.1-alt1 libexo-gtk3-devel >= 0.11.2 libgarcon-gtk3-devel >= 4.17.0
Buildrequires: libxfce4windowing-devel >= 4.19.6-alt1
BuildRequires: libX11-devel libXext-devel libwnck3-devel
BuildRequires: libgtk+3-devel
BuildRequires: libwayland-client-devel libgtk-layer-shell-devel
BuildRequires: libdbusmenu-gtk3-devel
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgtk+3-gir-devel libxfce4util-gir-devel >= 4.15.6-alt1}
%{?_enable_vala:BuildRequires: vala-tools libxfce4util-vala >= 4.15.6-alt1}
# NOTE: gtk-doc is required by build system even if docs are disabled.
BuildRequires: gtk-doc

Requires: xfce4-common

Obsoletes: xfce4-showdesktop-plugin, xfce4-windowlist-plugin

# libxfce4windowing >= 4.19.6 breaks API/ABI whithout soname change
Conflicts: libxfce4windowing < 4.19.6

%define libxfce4panel_name_gtk3 libxfce4panel-2.0
%define wrapper_name_gtk3 wrapper-2.0

%define _unpackaged_files_terminate_build 1

%description
%name is the panel for the Xfce desktop environment.

%description -l ru_RU.UTF-8
Данный пакет содержит в себе панель для окружения рабочего стола Xfce.

%if_enabled docs
%package -n libxfce4panel-devel-doc
Summary: Documentation files to build Xfce panel plugins
Group: Development/Documentation
Provides: %name-devel-doc = %version-%release
Obsoletes: %name-devel-doc < 4.8.0
Conflicts: libxfce4panel-gtk3-devel < %version-%release
BuildArch: noarch

%description -n libxfce4panel-devel-doc
This package contains files to develop plugins for Xfce panel.
%endif

%package -n libxfce4panel-gtk3
Summary: Library for Xfce panel (GTK+3)
License: LGPLv2.1+
Group: Development/C

%description -n libxfce4panel-gtk3
This package contains library for Xfce panel plugins
(GTK+3 variant).

%package -n libxfce4panel-gtk3-devel
Summary: Development files to build Xfce panel plugins (GTK+3)
License: LGPLv2.1+
Group: Development/C
Requires: libxfce4panel-gtk3 = %version-%release

%description -n libxfce4panel-gtk3-devel
This package contains files to develop plugins for Xfce panel
(GTK+3 variant).

%if_enabled introspection
%package -n libxfce4panel-gtk3-gir
Summary: GObject introspection data for libxfce4panel-gtk3
Group: System/Libraries
Requires: libxfce4panel-gtk3 = %EVR

%description -n libxfce4panel-gtk3-gir
GObject introspection data for libxfce4panel-gtk3.

%package -n libxfce4panel-gtk3-gir-devel
Summary: GObject introspection devel data for libxfce4panel-gtk3
Group: System/Libraries
BuildArch: noarch
Requires: libxfce4panel-gtk3-gir = %EVR
Requires: libxfce4panel-gtk3-devel = %EVR

%description -n libxfce4panel-gtk3-gir-devel
GObject introspection devel data for libxfce4panel-gtk3.
%endif

%if_enabled vala
%package -n libxfce4panel-gtk3-vala
Summary: Vala bindings for libxfce4panel-gtk3
Group: System/Libraries
Requires: libxfce4panel-gtk3-devel = %EVR
BuildArch: noarch

%description -n libxfce4panel-gtk3-vala
Vala bindings for libxfce4panel-gtk3.
%endif


%prep
%setup
%patch -p1

%build
%xfce4reconf
%configure \
	--disable-static \
	--enable-maintainer-mode \
	--enable-x11 \
	--enable-wayland \
	%{subst_enable introspection} \
	%{subst_enable vala} \
%if_enabled docs
	--enable-gtk-doc \
%else
	--disable-gtk-doc \
%endif
	--enable-debug=minimum
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc AUTHORS NEWS README.md
%config(noreplace) %_sysconfdir/xdg/xfce4/*
%_bindir/*
%_libdir/xfce4/panel/
%exclude %_libdir/xfce4/panel/%wrapper_name_gtk3
%_iconsdir/hicolor/*/apps/*
%_datadir/xfce4/panel/
%_desktopdir/*.desktop
%exclude %_libdir/xfce4/panel/plugins/*.la

%if_enabled docs
%files -n libxfce4panel-devel-doc
%doc %_datadir/gtk-doc/html/libxfce4panel-*/
%endif

%files -n libxfce4panel-gtk3
%_libdir/%libxfce4panel_name_gtk3.so.*
%_libdir/xfce4/panel/%wrapper_name_gtk3

%files -n libxfce4panel-gtk3-devel
%_libdir/pkgconfig/%libxfce4panel_name_gtk3.pc
%_libdir/%libxfce4panel_name_gtk3.so
%_includedir/xfce4/%libxfce4panel_name_gtk3/

%if_enabled introspection
%files -n libxfce4panel-gtk3-gir
%_libdir/girepository-1.0/*.typelib

%files -n libxfce4panel-gtk3-gir-devel
%_datadir/gir-1.0/*.gir
%endif

%if_enabled vala
%files -n libxfce4panel-gtk3-vala
%_datadir/vala/vapi/libxfce4panel-*
%endif

%changelog
* Wed Oct 16 2024 Mikhail Efremov <sem@altlinux.org> 4.19.5-alt1
- Updated to 4.19.5.

* Mon Jun 10 2024 Mikhail Efremov <sem@altlinux.org> 4.19.4-alt2
- Dropped non-existent plugin from default panel configuration
  (closes: #50585).
- Explicitly enabled both Wayland and X11 support.

* Tue May 28 2024 Mikhail Efremov <sem@altlinux.org> 4.19.4-alt1
- Dropped html documentation.
- Updated to 4.19.4.

* Thu Feb 29 2024 Mikhail Efremov <sem@altlinux.org> 4.18.6-alt1
- Updated to 4.18.6.

* Wed Sep 27 2023 Mikhail Efremov <sem@altlinux.org> 4.18.5-alt1
- Dropped %%xfce4_drop_gitvtag macro.
- Updated to 4.18.5.

* Tue May 23 2023 Mikhail Efremov <sem@altlinux.org> 4.18.4-alt1
- Updated to 4.18.4.

* Wed Mar 29 2023 Mikhail Efremov <sem@altlinux.org> 4.18.3-alt1
- Updated to 4.18.3.

* Thu Feb 09 2023 Mikhail Efremov <sem@altlinux.org> 4.18.2-alt1
- Updated to 4.18.2.

* Wed Jan 11 2023 Mikhail Efremov <sem@altlinux.org> 4.18.1-alt1
- Updated to 4.18.1.

* Fri Dec 16 2022 Mikhail Efremov <sem@altlinux.org> 4.18.0-alt2
- Fixed Russian "File Manager" translation.

* Thu Dec 15 2022 Mikhail Efremov <sem@altlinux.org> 4.18.0-alt1
- Updated to 4.18.0.

* Wed Nov 30 2022 Mikhail Efremov <sem@altlinux.org> 4.17.5-alt1
- Updated to 4.17.5.

* Tue Nov 01 2022 Mikhail Efremov <sem@altlinux.org> 4.17.4-alt1
- Updated to 4.17.4.

* Mon Aug 22 2022 Mikhail Efremov <sem@altlinux.org> 4.17.3-alt1
- Updated to 4.17.3.

* Mon Jul 11 2022 Mikhail Efremov <sem@altlinux.org> 4.17.2-alt1
- Updated to 4.17.2.

* Mon May 23 2022 Mikhail Efremov <sem@altlinux.org> 4.17.1-alt1
- Updated Url tag.
- Updated to 4.17.1 (closes: #41835).

* Mon Apr 18 2022 Mikhail Efremov <sem@altlinux.org> 4.17.0-alt1
- Use upstream Russian translation.
- Updated to 4.17.0.

* Mon Apr 11 2022 Mikhail Efremov <sem@altlinux.org> 4.16.3-alt3.g1870071c
- Upstream git snapshot (xfce-4.16 branch) (closes: #42398).

* Thu Jan 20 2022 Mikhail Efremov <sem@altlinux.org> 4.16.3-alt2
- Use our own Russian translation.

* Wed May 12 2021 Mikhail Efremov <sem@altlinux.org> 4.16.3-alt1
- Updated to 4.16.3.

* Thu Feb 25 2021 Mikhail Efremov <sem@altlinux.org> 4.16.2-alt1
- Updated to 4.16.2.

* Wed Jan 27 2021 Mikhail Efremov <sem@altlinux.org> 4.16.1-alt1
- Updated to 4.16.1.

* Wed Dec 23 2020 Mikhail Efremov <sem@altlinux.org> 4.16.0-alt1
- Updated to 4.16.0.

* Wed Dec 16 2020 Mikhail Efremov <sem@altlinux.org> 4.15.6-alt1
- Added libxfce4util-vala to BR for vala bindings.
- Updated BR.
- Updated to 4.15.6.

* Tue Nov 03 2020 Mikhail Efremov <sem@altlinux.org> 4.15.5-alt1
- Updated to 4.15.5.

* Wed Sep 02 2020 Mikhail Efremov <sem@altlinux.org> 4.15.4-alt1
- Dropped GTK+2 support.
- Updated Vcs tag.
- Updated to 4.15.4.

* Tue Apr 28 2020 Mikhail Efremov <sem@altlinux.org> 4.14.4-alt1
- Dropped bogus patch.
- Updated to 4.14.4.

* Tue Mar 17 2020 Mikhail Efremov <sem@altlinux.org> 4.14.3-alt3.g95d18aa4
- Enable Vala bindings again.
- Fix remote_event signal.

* Mon Mar 16 2020 Mikhail Efremov <sem@altlinux.org> 4.14.3-alt2.g95d18aa4
- Disable Vala bindings for now.
- Upstream git snapshot (xfce-4.14 branch).

* Mon Jan 13 2020 Mikhail Efremov <sem@altlinux.org> 4.14.3-alt1
- Use Vcs rpm tag.
- Don't use rpm-build-licenses.
- Updated to 4.14.3.

* Thu Sep 26 2019 Mikhail Efremov <sem@altlinux.org> 4.14.1-alt1
- Updated to 4.14.1.

* Mon Sep 23 2019 Mikhail Efremov <sem@altlinux.org> 4.14.0-alt2
- Fix systray icons drawing w/o compositing (by Ivan A. Melnikov).

* Mon Aug 12 2019 Mikhail Efremov <sem@altlinux.org> 4.14.0-alt1
- Updated to 4.14.0.

* Mon Jul 29 2019 Mikhail Efremov <sem@altlinux.org> 4.13.7-alt1
- Updated to 4.13.7.

* Fri Jul 05 2019 Mikhail Efremov <sem@altlinux.org> 4.13.6-alt2
- Enable vala support.
- Enable GObject introspection support.
- Fix changelog entry.

* Mon Jul 01 2019 Mikhail Efremov <sem@altlinux.org> 4.13.6-alt1
- Don't use deprecated PreReq.
- Updated to 4.13.6.

* Fri May 17 2019 Mikhail Efremov <sem@altlinux.org> 4.13.5-alt1
- Updated to 4.13.5.
- Drop no longer used directories.

* Wed Jan 02 2019 Mikhail Efremov <sem@altlinux.org> 4.13.4-alt1
- Updated to 4.13.4.

* Tue Aug 07 2018 Mikhail Efremov <sem@altlinux.org> 4.13.3-alt1
- Update url.
- Enable debug (minimum level).
- Updated to 4.13.3.

* Thu Dec 14 2017 Mikhail Efremov <sem@altlinux.org> 4.12.2-alt1
- Updated to 4.12.2.

* Wed Oct 26 2016 Mikhail Efremov <sem@altlinux.org> 4.12.1-alt1
- Updated to 4.12.1.

* Fri Feb 12 2016 Mikhail Efremov <sem@altlinux.org> 4.12.0-alt3
- Don't try to use panel-desktop-handler in the KDE (closes: #31542).

* Thu Mar 12 2015 Mikhail Efremov <sem@altlinux.org> 4.12.0-alt2
- Package GTK+3 variant of the library.

* Thu Mar 05 2015 Mikhail Efremov <sem@altlinux.org> 4.12.0-alt1
- Updated to 4.12.0.

* Mon Jan 12 2015 Mikhail Efremov <sem@altlinux.org> 4.11.2-alt1
- Updated to 4.11.2.

* Wed Jun 25 2014 Mikhail Efremov <sem@altlinux.org> 4.11.1-alt1
- Updated to 4.11.1.

* Mon Feb 17 2014 Mikhail Efremov <sem@altlinux.org> 4.11.0-alt1
- Fix Xfce name (XFce,XFCE -> Xfce).
- Updated to 4.11.0.

* Mon May 06 2013 Mikhail Efremov <sem@altlinux.org> 4.10.1-alt1.git20130506
- Bump version (this snapshot is newer then %name-4.10.1 release).
- Upstream git snapshot.

* Mon Dec 03 2012 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt3
- applicationsmenu plugin: Skip empty GenericName.
- Require xfce4-common.
- Own %%_libexecdir/xfce4.

* Tue May 22 2012 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt2
- Fix BR.
- Drop %%_datadir/xfce4/panel-plugins directory.

* Sun Apr 29 2012 Mikhail Efremov <sem@altlinux.org> 4.10.0-alt1
- Updated to 4.10.0.

* Tue Apr 17 2012 Mikhail Efremov <sem@altlinux.org> 4.9.2-alt1
- Updated to 4.9.2.

* Mon Apr 09 2012 Mikhail Efremov <sem@altlinux.org> 4.9.1-alt1
- Updated to 4.9.1.

* Sat Dec 31 2011 Mikhail Efremov <sem@altlinux.org> 4.9.0-alt1
- Drop old Russan manual translation.
- Updated to 4.9.0.

* Fri Oct 07 2011 Mikhail Efremov <sem@altlinux.org> 4.8.6-alt1
- Drop obsoleted patches.
- Updated to 4.8.6.

* Wed Aug 31 2011 Mikhail Efremov <sem@altlinux.org> 4.8.5-alt3
- Updated Russian translation.

* Tue Aug 16 2011 Mikhail Efremov <sem@altlinux.org> 4.8.5-alt2
- Add Russian documentation (by Artem Zolochevskiy).
- Updated Russian translation (by Artem Zolochevskiy).

* Thu Jun 23 2011 Mikhail Efremov <sem@altlinux.org> 4.8.5-alt1
- Updated to 4.8.5.

* Mon May 30 2011 Mikhail Efremov <sem@altlinux.org> 4.8.3-alt2
- Add patches from upstream git:
   + Sleep on startup until a window manager is detected.
   + Fix menu positioning for moved external plugins.

* Mon Apr 11 2011 Mikhail Efremov <sem@altlinux.org> 4.8.3-alt1
- Drop obsoleted patches.
- Updated to 4.8.3.

* Mon Mar 21 2011 Mikhail Efremov <sem@altlinux.org> 4.8.2-alt3
- Fix build requires.

* Tue Mar 01 2011 Mikhail Efremov <sem@altlinux.org> 4.8.2-alt2
- Patch from upstream:
    Fix work with grouped windows (closes: #25174).

* Sun Feb 27 2011 Mikhail Efremov <sem@altlinux.org> 4.8.2-alt1
- Drop obsoleted patch.
- Updated to 4.8.2.

* Mon Feb 21 2011 Mikhail Efremov <sem@altlinux.org> 4.8.1-alt3
- Fix Russian translation.

* Fri Feb 18 2011 Mikhail Efremov <sem@altlinux.org> 4.8.1-alt2
- Patch from upstream: Initialize viewport if screen is connected.
- Fix Russian translation (closes: #25107).

* Tue Feb 15 2011 Mikhail Efremov <sem@altlinux.org> 4.8.1-alt1
- Updated to 4.8.1.

* Fri Jan 21 2011 Mikhail Efremov <sem@altlinux.org> 4.8.0-alt1
- Move libxfce4panel to separate subpackage.
- Spec cleanup, tar.bz2 -> tar.
- Remove exo-0.5.1.patch.
- Updated to 4.8.0.

* Tue Jan 26 2010 Denis Koryavov <dkoryavov@altlinux.org> 4.6.3-alt1
- New version.

* Tue Jan 26 2010 Denis Koryavov <dkoryavov@altlinux.org> 4.6.3-alt0.M51.1
- Backport to branch 5.1.

* Mon Jan 04 2010 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt4
- Fix build with gtkdocize.

* Sun Oct 25 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt3
- Russian translation updated.

* Tue May 12 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt0.M50.2
- Backport to Desktop 5.0

* Sat May 09 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt2
- Updated russian translation

* Mon Apr 20 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.1-alt1
Xfce 4.6.1

* Sun Apr 12 2009 Denis Koryavov <dkoryavov@altlinux.org> 4.6.0-alt1
- Xfce 4.6.0

* Tue Jan 27 2009 Eugene Ostapets <eostapets@altlinux.ru> 4.5.99.1-alt1
- Xfce 4.6rc1

* Thu Jan 22 2009 Eugene Ostapets <eostapets@altlinux.ru> 4.5.93-alt1
- Xfce 4.6 beta 3

* Fri Oct 24 2008 Eugene Ostapets <eostapets@altlinux.org> 4.5.91-alt1
- Xfce 4.6 beta1

* Mon Nov 19 2007 Eugene Ostapets <eostapets@altlinux.org> 4.4.2-alt1
- Xfce 4.4.2 release

* Sun Jun 17 2007 Eugene Ostapets <eostapets@altlinux.ru> 4.4.1-alt2
- fix 12007

* Sat Apr 14 2007 Eugene Ostapets <eostapets@altlinux.ru> 4.4.1-alt1
- Xfce 4.4.1 release

* Mon Jan 22 2007 Eugene Ostapets <eostapets@altlinux.ru> 4.4.0-alt0.1
- Xfce 4.4 release

* Sun Nov 05 2006 Eugene Ostapets <eostapets@altlinux.ru> 4.3.99.2-alt1
- Xfce 4.4rc2

* Mon Oct 30 2006 Eugene Ostapets <eostapets@altlinux.ru>  4.3.99.1-alt2
- Fix buildreq and cleanup spec

* Tue Sep 12 2006 Eugene Ostapets <eostapets@altlinux.ru> 4.3.99.1-alt1
- new version 4.4rc1

* Tue Nov 15 2005 Eugene Ostapets <eostapets@altlinux.ru> 4.2.3-alt1
- 4.2.3

* Wed May 18 2005 Andrey Astafiev <andrei@altlinux.ru> 4.2.2-alt1
- 4.2.2

* Wed Mar 23 2005 Andrey Astafiev <andrei@altlinux.ru> 4.2.1-alt2
- Fixed panel settings saving.

* Thu Mar 17 2005 Andrey Astafiev <andrei@altlinux.ru> 4.2.1-alt1
- 4.2.1

* Sat Jan 15 2005 Andrey Astafiev <andrei@altlinux.ru> 4.2.0-alt1
- 4.2.0

* Fri Dec 24 2004 Andrey Astafiev <andrei@altlinux.ru> 4.1.99.3-alt1
- 4.1.99.3

* Mon Nov 01 2004 Andrey Astafiev <andrei@altlinux.ru> 4.1.91-alt1
- 4.1.91

* Wed Jul 21 2004 Andrey Astafiev <andrei@altlinux.ru> 4.0.6-alt1
- 4.0.6

* Sat Apr 17 2004 Andrey Astafiev <andrei@altlinux.ru> 4.0.5-alt1
- 4.0.5

* Tue Mar 16 2004 Andrey Astafiev <andrei@altlinux.ru> 4.0.4-alt1
- 4.0.4

* Wed Jan 21 2004 Andrey Astafiev <andrei@altlinux.ru> 4.0.3-alt1
- 4.0.3

* Mon Dec 22 2003 Andrey Astafiev <andrei@altlinux.ru> 4.0.2-alt1
- 4.0.2

* Tue Nov 18 2003 Andrey Astafiev <andrei@altlinux.ru> 4.0.1-alt1
- 4.0.1

* Fri Sep 26 2003 Andrey Astafiev <andrei@altlinux.ru> 4.0.0-alt1
- 4.0.0

* Fri Sep 12 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.4-alt1
- 3.99.4

* Fri Aug 29 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.3-alt0.9
- 3.99.3

* Sun Aug 17 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.2-alt0.9
- 3.99.2

* Mon Jul 14 2003 Andrey Astafiev <andrei@altlinux.ru> 3.99.1-alt0.9
- 3.99.1

* Fri Jun 13 2003 Andrey Astafiev <andrei@altlinux.ru> 3.90.0-alt0.9
- First version of RPM package for Sisyphus.
- Spec derived from original version.
