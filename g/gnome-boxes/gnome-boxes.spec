%define _libexecdir %_prefix/libexec
%def_disable ovirt
%def_enable usbredir
%def_enable smartcard

Name: gnome-boxes
Version: 3.10.0
Release: alt1
Summary: A simple GNOME 3 application to access remote or virtual systems
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>
Group: Emulators
License: LGPLv2+
Url: https://live.gnome.org/Boxes

Source: %name-%version.tar
Source2: libgd.tar

# From configure.ac
%define clutter_gtk_ver 1.3.2
%define clutter_ver 1.11.14
%define govirt_ver 0.2.0
%define glib_ver 2.32.0
%define gtk_ver 3.9
%define gtk_vnc_ver 0.4.4
%define libvirt_glib_ver 0.1.7
%define libxml2_ver 2.7.8
%define spice_gtk_ver 0.15
%define gudev_ver 165
%define osinfo_ver 0.2.6
%define tracker_ver 0.13.1
%define uuid_ver 1.41.3
%define libsoup_ver 2.38

BuildRequires: intltool >= 0.40.0
BuildRequires: yelp-tools
BuildRequires: gobject-introspection-devel >= 0.9.6
BuildRequires: libvala-devel >= 0.21.1
BuildRequires: vala-tools
BuildRequires: libclutter-gtk3-devel >= %clutter_gtk_ver
BuildRequires: libclutter-devel >= %clutter_ver
BuildRequires: glib2-devel >= %glib_ver libgio-devel >= %glib_ver
BuildRequires: libgtk+3-devel >= %gtk_ver libgtk+3-gir-devel
BuildRequires: libgtk3vnc-devel >= %gtk_vnc_ver
BuildRequires: libvirt-gobject-devel >= %libvirt_glib_ver
BuildRequires: libvirt-gconfig-devel >= %libvirt_glib_ver
BuildRequires: libxml2-devel >= %libxml2_ver
BuildRequires: libspice-gtk3-devel >= %spice_gtk_ver
BuildRequires: libgudev-devel >= %gudev_ver
BuildRequires: libosinfo-devel >= %osinfo_ver
BuildRequires: tracker-devel >= %tracker_ver
BuildRequires: libuuid-devel >= %uuid_ver
BuildRequires: libsoup-devel >= %libsoup_ver
%{?_enable_ovirt:BuildRequires: pkgconfig(govirt-1.0) >= %govirt_ver}


# Need libvirtd and an hypervisor to do anything useful
Requires: libvirt-daemon
Requires: qemu-kvm

# Needed for unattended installations
Requires: fuseiso
Requires: mtools

# gnome-boxes uses a dark theme
Requires: gnome-icon-theme

%description
gnome-boxes lets you easily create, setup, access, and use:
  * remote machines
  * remote virtual machines
  * local virtual machines
  * When technology permits, set up access for applications on
    local virtual machines

%prep
%setup
tar -xf %SOURCE2 -C libgd
echo %version > .tarball-version

%build
%autoreconf
intltoolize -f
%configure \
	%{subst_enable usbredir} \
	%{subst_enable smartcard} \
	--enable-vala

%make_build

%install
%makeinstall_std
%find_lang %name --with-gnome

%files -f %name.lang
%doc AUTHORS COPYING README NEWS TODO
%_bindir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%_datadir/glib-2.0/schemas/org.gnome.boxes.gschema.xml
%_iconsdir/hicolor/*/apps/gnome-boxes.*
%_libexecdir/gnome-boxes-search-provider
%_datadir/dbus-1/services/org.gnome.Boxes.SearchProvider.service
%_datadir/gnome-shell/search-providers/gnome-boxes-search-provider.ini
%_datadir/appdata/*.xml

%changelog
* Wed Oct 30 2013 Alexey Shabalin <shaba@altlinux.ru> 3.10.0-alt1
- 3.10.0
- disable govirt support

* Thu Sep 19 2013 Alexey Shabalin <shaba@altlinux.ru> 3.9.92-alt1
- 3.9.92

* Tue Sep 03 2013 Alexey Shabalin <shaba@altlinux.ru> 3.9.91-alt1
- 3.9.91

* Tue Jul 30 2013 Alexey Shabalin <shaba@altlinux.ru> 3.8.4-alt1
- 3.8.4

* Tue May 14 2013 Alexey Shabalin <shaba@altlinux.ru> 3.8.2-alt1
- 3.8.2

* Mon May 06 2013 Alexey Shabalin <shaba@altlinux.ru> 3.8.1.2-alt2
- update to upstream/gnome-3-8 branch
- build with oVirt support

* Fri Apr 19 2013 Alexey Shabalin <shaba@altlinux.ru> 3.8.1.2-alt1
- 3.8.1.2

* Wed Mar 27 2013 Alexey Shabalin <shaba@altlinux.ru> 3.8.0-alt1
- 3.8.0

* Fri Mar 22 2013 Alexey Shabalin <shaba@altlinux.ru> 3.7.92-alt1
- 3.7.92

* Mon Feb 25 2013 Alexey Shabalin <shaba@altlinux.ru> 3.7.90-alt1
- 3.7.90

* Mon Feb 25 2013 Alexey Shabalin <shaba@altlinux.ru> 3.6.3-alt1
- 3.6.3

* Tue Nov 13 2012 Alexey Shabalin <shaba@altlinux.ru> 3.6.2-alt1
- 3.6.2

* Mon Oct 15 2012 Alexey Shabalin <shaba@altlinux.ru> 3.6.1-alt1
- 3.6.1

* Wed Sep 26 2012 Alexey Shabalin <shaba@altlinux.ru> 3.6.0-alt1
- 3.6.0

* Tue Sep 11 2012 Alexey Shabalin <shaba@altlinux.ru> 3.4.3-alt1.1
- rebuild with new libspice-client-glib-2.0.so.1, libspice-client-gtk-3.0.so.1

* Thu Jun 14 2012 Alexey Shabalin <shaba@altlinux.ru> 3.4.3-alt1
- 3.4.3

* Wed May 16 2012 Alexey Shabalin <shaba@altlinux.ru> 3.4.2-alt1
- 3.4.2

* Tue Apr 24 2012 Alexey Shabalin <shaba@altlinux.ru> 3.4.1-alt1
- 3.4.1

* Wed Apr 04 2012 Alexey Shabalin <shaba@altlinux.ru> 3.4.0.1-alt1
- Initial build.

