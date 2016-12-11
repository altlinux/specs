%define ver_major 0.11
%def_enable dbusmenu
%def_disable apport

Name: plank
Version: %ver_major.3
Release: alt1

Summary: Elegant, simple, clean dock
License: GPLv3+
Group: Graphical desktop/Other
Url: https://launchpad.net/plank

Source: https://launchpad.net/%name/1.0/%version/+download/%name-%version.tar.xz

Requires: bamfdaemon dconf

%define gtk_ver 3.10
%define glib_ver 2.40
%define bamf_ver 0.2.92

BuildRequires: intltool xmllint
BuildRequires: libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver
BuildRequires: libbamf3-devel >= %bamf_ver libgee0.8-devel
BuildRequires: libwnck3-devel libXi-devel libXfixes-devel
BuildRequires: xvfb-run dbus-tools-gui
BuildRequires: vala-tools
%{?_enable_dbusmenu:BuildRequires: libdbusmenu-gtk3-devel}

%description
Plank is a dock enabling you to start applications and manage your windows.

%package -n lib%name
Summary: Library to build a elegant, simple, clean dock
Group: System/Libraries

Requires: lib%name-common = %version-%release

%description -n lib%name
Plank is a dock enabling you to start applications and manage your windows.

%package -n lib%name-devel
Summary: Library to build a elegant, simple, clean dock (development files)
Group: Development/C

%description -n lib%name-devel
Plank is a dock enabling you to start applications and manage your windows.

%package -n lib%name-common
Summary: Library to build a elegant, simple, clean dock
Group: Graphical desktop/Other
BuildArch: noarch

# TODO:
# Depends: plank-theme-pantheon

%description -n lib%name-common
Plank is a dock enabling you to start applications and manage your windows.

%package -n lib%name-doc
Summary: Library to build a elegant, simple, clean dock - documentation
Group: Documentation
BuildArch: noarch
Conflicts: lib%name < %version

%description -n lib%name-doc
Plank is a dock enabling you to start applications and manage your windows.

This package contains the documentation.

%package -n lib%name-vala
Summary: Vala language bindings for plank library
Group: Development/Other
BuildArch: noarch
Requires: lib%name = %version-%release

%description -n lib%name-vala
This package provides Vala language bindings for plank library.

%prep
%setup

%build
%autoreconf
%configure \
  --enable-headless-tests \
  %{subst_enable dbusmenu} \
  %{subst_enable apport}
%make_build

%install
%makeinstall_std

%find_lang %name

%check
#make check || exit 1


%files -f %name.lang
%_bindir/%name
%_datadir/icons/hicolor/*/apps/plank.*
%_man1dir/plank.*
%_desktopdir/plank.desktop
%dir %_libdir/plank
%dir %_libdir/plank/docklets
%_libdir/plank/docklets/libdocklet-clippy.so
%_libdir/plank/docklets/libdocklet-clock.so
%_libdir/plank/docklets/libdocklet-cpumonitor.so
%_libdir/plank/docklets/libdocklet-desktop.so
%_libdir/plank/docklets/libdocklet-trash.so
%_datadir/glib-2.0/schemas/net.launchpad.plank.gschema.xml
%_datadir/appdata/plank.appdata.xml

%if_enabled apport
%_sysconfdir/apport/crashdb.conf.d/plank-crashdb.conf
%_datadir/apport/package-hooks/source_plank.py
%endif

%exclude %_libdir/plank/docklets/*.la

%files -n lib%name
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_libdir/lib%name.so
%_includedir/plank
%_pkgconfigdir/plank.pc

%files -n lib%name-common
%_datadir/plank/themes

%files -n lib%name-doc

%files -n lib%name-vala
%_datadir/vala/vapi/plank.deps
%_datadir/vala/vapi/plank.vapi

%changelog
* Sun Dec 11 2016 Yuri N. Sedunov <aris@altlinux.org> 0.11.3-alt1
- 0.11.3

* Mon Jun 13 2016 Yuri N. Sedunov <aris@altlinux.org> 0.11.2-alt1
- 0.11.2

* Tue May 31 2016 Yuri N. Sedunov <aris@altlinux.org> 0.11.1-alt1
- 0.11.1

* Sat Mar 19 2016 Yuri N. Sedunov <aris@altlinux.org> 0.11.0-alt1
- 0.11.0

* Sat Oct 31 2015 Yuri N. Sedunov <aris@altlinux.org> 0.10.1-alt1
- 0.10.1

* Thu Sep 17 2015 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt1
- 0.10.0

* Mon Sep 07 2015 Yuri N. Sedunov <aris@altlinux.org> 0.9.1-alt1
- 0.9.1

* Mon Nov 25 2013 Igor Zubkov <icesik@altlinux.org> 0.5.0-alt5
- Built with --disable-gee-0.8

* Sat Nov 23 2013 Igor Zubkov <icesik@altlinux.org> 0.5.0-alt4
- Add vala bindings

* Thu Nov 21 2013 Igor Zubkov <icesik@altlinux.org> 0.5.0-alt3
- Rebuilt with libbamf3.so.2

* Wed Nov 20 2013 Igor Zubkov <icesik@altlinux.org> 0.5.0-alt2
- Enable headless tests

* Wed Nov 20 2013 Igor Zubkov <icesik@altlinux.org> 0.5.0-alt1
- 0.5.0

* Mon Oct 21 2013 Igor Zubkov <icesik@altlinux.org> 0.4.0-alt1
- 0.4.0

* Wed Oct 09 2013 Igor Zubkov <icesik@altlinux.org> 0.3.0-alt1.bzr857
- build for Sisyphus

