%define _name nemo
%define ver_major 1.1
%define api_ver 3.0

%def_enable exempi
%def_disable packagekit
%def_enable tracker
%def_enable introspection
%def_enable selinux

Name: nemo
Version: %ver_major.2
Release: alt1

Summary: default file manager for Cinnamon
License: GPLv2+
Group: Graphical desktop/GNOME
URL: https://github.com/linuxmint/nemo

Source: %name-%version.tar

Patch: %name-%version-%release.patch

Provides: %_name = %version-%release
Obsoletes: gnome-volume-manager
Provides: gnome-volume-manager

%define pkgconfig_ver 0.8
%define icon_theme_ver 2.10.0
%define desktop_file_utils_ver 0.8

# From configure.in
%define glib_ver 2.31.9
%define desktop_ver 3.3.3
%define pango_ver 1.28.3
%define gtk_ver 3.3.18
%define libxml2_ver 2.4.7
%define exif_ver 0.5.12
%define exempi_ver 2.1.0
%define gir_ver 0.10.2
%define notify_ver 0.7.0
%define tracker_ver 0.12

PreReq: lib%name = %version-%release
PreReq: gnome-icon-theme >= %icon_theme_ver

Requires: shared-mime-info
Requires: common-licenses
Requires: gvfs >= 1.9.1

BuildPreReq: pkgconfig >= %pkgconfig_ver
BuildPreReq: desktop-file-utils >= %desktop_file_utils_ver
BuildPreReq: rpm-build-gnome rpm-build-licenses
# for %%check
BuildPreReq: xvfb-run dbus-tools-gui /proc

# From configure.in
BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: libgio-devel >= %glib_ver
BuildPreReq: libgnome-desktop3-devel >= %desktop_ver
BuildPreReq: libpango-devel >= %pango_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: gsettings-desktop-schemas-devel
BuildPreReq: libgail3-devel
BuildPreReq: libxml2-devel >= %libxml2_ver
BuildPreReq: intltool >= 0.40.1
BuildPreReq: libexif-devel >= %exif_ver
BuildPreReq: libnotify-devel >= %notify_ver
BuildRequires: libX11-devel xorg-xproto-devel
BuildRequires: docbook-utils gtk-doc
%{?_enable_exempi:BuildPreReq: libexempi-devel >= %exempi_ver}
%{?_enable_tracker:BuildPreReq: tracker-devel >= %tracker_ver}
%{?_enable_introspection:BuildPreReq: gobject-introspection-devel >= %gir_ver libgtk+3-gir-devel}
%{?_enable_selinux:BuildRequires: libselinux-devel}

%description
Nemo integrates access to files, applications, media, Internet-based
resources and the Web.  Nemo delivers a dynamic and rich user
experience.  Nemo is an free software project developed under the
GNU General Public License and is a core component of the Cinnamon desktop
project.

%package -n lib%name
Summary: Shared libraries needed to run Nemo
Group: System/Libraries

%description -n lib%name
This package contains shared libraries needed to run Nemo and its
components.

%package -n lib%name-devel
Summary: Libraries and include files for developing Nemo components
Group: Development/GNOME and GTK+
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package provides the necessary development libraries and include
files to allow you to develop Nemo components.

%package -n lib%name-devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
Conflicts: lib%name-devel < %version-%release
BuildArch: noarch

%description -n lib%name-devel-doc
This package contains development documentation for the %name.

%package -n lib%name-gir
Summary: GObject introspection data for the nemo-extension library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the nemo-extension library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the nemo-extension library
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the nemo-extension library

%define _bonobo_servers_dir %_libdir/bonobo/servers

%prep
%setup -q
%patch0 -p1 

rm -f data/*.desktop

# make check using xvfb-run
subst 's@\.\/@xvfb-run -a ./@' eel/check-eel src/check-nemo

%build
%autoreconf
%configure \
    --disable-update-mimedb \
    --disable-schemas-compile \
    %{subst_enable packagekit}

%make_build

%if 0
%check
for d in eel src; do
pushd $d
make check
popd
done
%endif

%install
%make_install install DESTDIR=%buildroot
mkdir -p %buildroot%_libdir/%name-%api_ver/components
bzip2 -9fk NEWS

# The license
ln -sf %_licensedir/LGPL-2 COPYING

%find_lang %name

%files -f %name.lang
%_bindir/*
%_libexecdir/nemo-convert-metadata
%dir %_libdir/%name-%api_ver
%dir %_libdir/%name-%api_ver/components
%_datadir/mime/packages/nemo.xml
%_datadir/applications/*.desktop
%_sysconfdir/xdg/autostart/nemo-autostart.desktop
%_datadir/%name
%_iconsdir/hicolor/*/apps/*.png
%_iconsdir/hicolor/*/apps/*.svg
%_iconsdir/hicolor/*/actions/*.svg
%_datadir/dbus-1/services/org.Nemo.service
%_datadir/dbus-1/services/org.freedesktop.NemoFileManager1.service
# gsettings schemas
%config %_datadir/glib-2.0/schemas/org.nemo.gschema.xml
%_datadir/GConf/gsettings/nemo.convert
# docs
%doc --no-dereference COPYING
%doc AUTHORS MAINTAINERS NEWS.bz2 README THANKS TODO
%_man1dir/*

%files -n lib%name
%_libdir/libnemo-extension.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%files -n lib%name-devel-doc
%doc docs/*.{txt,html} README.commits

%if_enabled introspection
%files -n lib%name-gir
%_libdir/girepository-1.0/*

%files -n lib%name-gir-devel
%_datadir/gir-1.0/*
%endif


%changelog
* Thu Nov 15 2012 Vladimir Didenko <cow@altlinux.org> 1.1.2-alt1
- update to 1.1.2
- fixed Open in terminal functionality

* Tue Nov 13 2012 Vladimir Didenko <vladimir.didenko@gmail.com> 1.1.1-alt1
- update to 1.1.1

* Tue Nov 6 2012 Vladimir Didenko <vladimir.didenko@gmail.com> 1.1.0-alt1
- update to 1.1.0

* Thu Nov 1 2012 Vladimir Didenko <vladimir.didenko@gmail.com> 1.0.7-alt1
- update to 1.0.7

* Mon Oct 8 2012 Vladimir Didenko <vladimir.didenko@gmail.com> 1.0.3-alt1
- update to 1.0.3

* Thu Oct 4 2012 Vladimir Didenko <vladimir.didenko@gmail.com> 1.0.2-alt1
- First build
