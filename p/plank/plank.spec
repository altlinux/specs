%define ver_major 0.9
%def_disable dbusmenu

Name: plank
Version: %ver_major.1
Release: alt1

Summary: Elegant, simple, clean dock
License: GPLv3+
Group: Graphical desktop/Other
Url: https://launchpad.net/plank

Source: https://launchpad.net/%name/%ver_major/%version/+download/%name-%version.tar.xz

Packager: Igor Zubkov <icesik@altlinux.org>

Requires: bamfdaemon

BuildRequires: intltool libbamf3-devel libgee0.8-devel vala-tools xmllint
BuildRequires: xvfb-run dbus-tools-gui libgtk+3-devel libwnck3-devel
BuildRequires: libXi-devel libXfixes-devel
%{?_enable_dbusmenu:BuildRequires: libdbusmenu-glib-devel}

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
%configure \
  --enable-headless-tests \
  %{subst_enable dbusmenu}
%make_build V=1

%install
%makeinstall_std

%find_lang %name

%check
#make check || exit 1


%files -f %name.lang
%_sysconfdir/apport/crashdb.conf.d/plank-crashdb.conf
%_bindir/plank
%_datadir/icons/hicolor/*/apps/plank.*
%_man1dir/plank.*
%_desktopdir/plank.desktop
%_datadir/appdata/plank.appdata.xml
%exclude %_datadir/apport/package-hooks/source_plank.py

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

