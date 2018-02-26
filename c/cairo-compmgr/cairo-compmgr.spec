%def_disable introspection
%def_enable gconf
%def_enable perf_plugin
%def_enable glade
%def_enable xrender

Name: cairo-compmgr
Version: 0.3.0
Release: alt7.git348f149
Summary: Cairo Composite Manager
License: GPL
Group: System/X11

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name-%version.tar

BuildRequires: intltool gtk-doc
BuildRequires: libXcomposite-devel libXdamage-devel libXext-devel libXi-devel libSM-devel
BuildRequires: libcairo-devel libpixman-devel
BuildRequires: libgtk+2-devel
BuildRequires: libvala-devel
%{?_enable_gconf:BuildRequires: libGConf-devel GConf}
%{?_enable_introspection:BuildRequires: gobject-introspection-devel}
%{?_enable_perf_plugin:BuildRequires: libgtop-devel libwnck-devel}
%{?_enable_glade:BuildRequires: libgladeui-devel}
%{?_enable_xrender:BuildRequires: libXrender-devel}
BuildRequires: desktop-file-utils

%description
Cairo Composite Manager is a versatile and extensible composite manager
which use cairo for rendering.

%package -n lib%name-devel
Summary: %summary
Group: System/X11
%description -n lib%name-devel
%summary

%package -n lib%name-gir
Summary: GObject introspection data for the cairo-compmgr library
Group: System/Libraries
Requires: %name = %version-%release

%description -n lib%name-gir
GObject introspection data for the cairo-compmgr library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the cairo-compmgr library
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the cairo-compmgr library

%package devel-doc
Summary: Development package for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
Contains developer documentation for %name.


%prep
%setup

%build
sed -i 's!libvala-0.14!libvala-0.16!' configure.ac
sed -i 's!libvala-0.14!libvala-0.16!' vapi/cairo-compmgr.deps

./autogen.sh
%configure \
	%{subst_enable gconf } \
	--disable-schemas-install \
	--enable-gtk-doc \
	%{?_enable_perf_plugin:--enable-perf-plugin} \
	%{?_enable_introspection:--enable-gobject-introspection}

%make
%make doc

%install
%make DESTDIR=%buildroot install
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=System \
	--add-category=X-Desktop \
	%buildroot%_desktopdir/cairo-compmgr.desktop

rm -f %buildroot%_libdir/*/*.la
rm -f %buildroot%_libdir/*/*/*.la

%define schemas ccm-automate ccm-decoration ccm-display ccm-fade ccm-freeze ccm-magnifier ccm-menu-animation ccm-mosaic ccm-opacity ccm-perf ccm-screen ccm-shadow ccm-snapshot ccm-vala-window-plugin ccm-window-animation

%post
%gconf2_install %schemas

%preun
if [ $1 = 0 ]; then
    %gconf2_uninstall %schemas
fi

%files
%_bindir/*
%_man1dir/*
%_libdir/libcairo_compmgr.so.*
%_libdir/cairo-compmgr
%config %_sysconfdir/gconf/schemas/*.schemas
%_desktopdir/*.desktop
%_datadir/cairo-compmgr
%_pixmapsdir/%name
%_libdir/glade3/modules/*.so
%_datadir/glade3/catalogs/*.xml

%files -n lib%name-devel
%_includedir/cairo-compmgr
%_libdir/libcairo_compmgr.so
%_pkgconfigdir/*.pc
%_datadir/vala/vapi/*

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/*.typelib

%files -n lib%name-gir-devel
%_girdir/*.gir
%endif

%files devel-doc
%_datadir/gtk-doc/html/*

%changelog
* Thu Mar 29 2012 Alexey Shabalin <shaba@altlinux.ru> 0.3.0-alt7.git348f149
- rebuild with vala-0.16

* Wed Oct 26 2011 Alexey Shabalin <shaba@altlinux.ru> 0.3.0-alt6.git348f149
- upstream snapshot 348f149af30bc829c2100d0e622c5dcaf43925b7

* Thu Jun 02 2011 Alexey Shabalin <shaba@altlinux.ru> 0.3.0-alt5.git711fc72
- upstream snapshot 711fc7275b79cc802dc69658eb714ddc50666c06

* Thu Jun 02 2011 Denis Smirnov <mithraen@altlinux.ru> 0.3.0-alt4
- fix build with vala-0.12

* Thu Jun 02 2011 Denis Smirnov <mithraen@altlinux.ru> 0.3.0-alt3
- rebuild

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.3.0-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for cairo-compmgr

* Mon Mar 14 2011 Denis Smirnov <mithraen@altlinux.ru> 0.3.0-alt2
- fix build

* Wed Jan 19 2011 Denis Smirnov <mithraen@altlinux.ru> 0.3.0-alt1
- first build for Sisyphus

