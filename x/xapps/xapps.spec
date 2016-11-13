Name: xapps
Version: 1.0.2
Release: alt1

Summary: Libraries and common resources for XApps
License: %gpl3only
Group: Graphical desktop/GNOME
Url: https://github.com/linuxmint/xapps
Packager: Vladimir Didenko <cow@altlinux.org>

Source: %name-%version.tar

Requires: lib%name = %version-%release
BuildPreReq: rpm-build-licenses rpm-build-gnome

# From configure.in
BuildPreReq: intltool >= 0.35
BuildPreReq: libgtk+3-devel >= 3.3.6
BuildPreReq: glib2-devel >= 2.35.0
BuildPreReq: libgio-devel >= 2.28.0
BuildPreReq: gtk-doc >= 1.4
BuildPreReq: gnome-common >= 2.8.0
BuildPreReq: gsettings-desktop-schemas-devel >= 3.5.91

BuildRequires: gobject-introspection-devel libgtk+3-gir-devel libgnomekbd-devel

%description
Libraries and common resources for XApps

%package -n %name-schemas
Summary: A collection of GSettings schemas for XApps
Group: Graphical desktop/GNOME
BuildArch: noarch

%description -n %name-schemas
A collection of GSettings schemas for XApps

%package -n %name-utils
Summary: A collection of utils for XApps
Group: Graphical desktop/GNOME
BuildArch: noarch

%description -n %name-utils
A collection of utils for XApps

%package -n %name-icons
Summary: XApps icons
Group: Graphical desktop/GNOME
BuildArch: noarch

%description -n %name-icons
XApps icons.

%package -n lib%name
Summary: XApps core libraries
Group: Graphical desktop/GNOME

%description -n lib%name
XApps libraries.

%package -n lib%name-devel
Summary: XApps development libraries and includes
Group: Development/GNOME and GTK+
Requires: lib%name = %version-%release

%description -n lib%name-devel
XApps development libraries and includes

%package -n lib%name-gir
Summary: GObject introspection data for the %name library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the %name library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the %name
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the %name library

%prep
%setup -q -n %name-%version

%build
%autoreconf
%configure

%make_build

%install
%make_install DESTDIR=%buildroot install

%files -n %name-schemas
%_datadir/glib-2.0/schemas/org.x.apps.*.xml

%files -n %name-icons
%_datadir/icons/hicolor/scalable/actions/*

%files -n %name-utils
%_bindir/xfce4-set-wallpaper
# TODO: this scripts don't work without modifications in Alt Linux. Need to fix.
%exclude %_bindir/pastebin
%exclude %_bindir/upload-system-info


%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%files -n lib%name-gir
%_typelibdir/*

%files -n lib%name-gir-devel
%_girdir/*

%changelog
* Wed Nov 23 2016 Vladimir Didenko <cow@altlinux.org> 1.0.2-alt1
- 1.0.2-3-g4b700fe

* Tue Sep 27 2016 Vladimir Didenko <cow@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
