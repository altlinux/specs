Name: gala
Version: 0.2.0
Release: alt0.1

Summary: Pantheon Window Manager
Group: Graphical desktop/Other
License: GPLv3+
Url: https://launchpad.net/%name

# lp:gala
Source: %name-%version.tar

BuildRequires: intltool libbamf3-devel libclutter-gtk3-devel
BuildRequires: libgranite-devel libmutter-devel libgee0.8-devel
BuildRequires: libgnome-desktop3-devel libplank-devel
BuildRequires: libcanberra-gtk3-devel libnotify-devel libwayland-server-devel libgudev-devel
BuildRequires: vala-tools libgranite-vala libplank-vala libcanberra-vala

%description
gala is a window & compositing manager based on libmutter. It manages the
various windows a user has open.
It takes care of behaviors such as moving windows around, window switching,
window overview, animating windows, maximization, multiple workspaces,
providing accessibility features like zoom, and more.

%package -n lib%name
Summary: Shared library for Gala
Group: System/Libraries

%description -n lib%name
This package contains shared library needed to run Gala.

%package -n lib%name-devel
Summary: Development files for lib%name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains headers and development libraries for lib%name


%prep
%setup

%build
%autoreconf
%configure --disable-schemas-compile
%make_build V=1

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc HACKING INSTALL
%_bindir/%name
%_desktopdir/%name.desktop
%_desktopdir/%name-multitaskingview.desktop
%_desktopdir/%name-wayland.desktop
%_datadir/%name/
%_datadir/glib-2.0/schemas/org.pantheon.desktop.%name.gschema.xml
%_iconsdir/hicolor/*x*/apps/multitasking-view.svg

%files -n lib%name
%_libdir/lib%name.so.*
%dir %_libdir/%name/
%dir %_libdir/%name/plugins
%_libdir/%name/plugins/lib%name-maskcorners.so
%_libdir/%name/plugins/lib%name-notify.so
%_libdir/%name/plugins/lib%name-zoom.so

%exclude %_libdir/%name/plugins/*.la

%files -n lib%name-devel
%_includedir/%name/
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc
#%_vapidir/%name.deps
#%_vapidir/%name.vapi


%changelog
* Fri Sep 11 2015 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt0.1
- 0.2.0_r479

* Mon Nov 25 2013 Igor Zubkov <icesik@altlinux.org> 0.1-alt1.r363
- build for Sisyphus

