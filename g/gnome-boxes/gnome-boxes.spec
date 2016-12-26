%define _libexecdir %_prefix/libexec
%def_disable ovirt

Name: gnome-boxes
Version: 3.22.3
Release: alt1
Summary: A simple GNOME 3 application to access remote or virtual systems
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>
Group: Emulators
License: LGPLv2+
Url: https://wiki.gnome.org/Apps/Boxes

Source: %name-%version.tar
Source2: libgd.tar

# From configure.ac
%define govirt_ver 0.2.0
%define glib_ver 2.38.0
%define gtk_ver 3.13.2
%define gtk_vnc_ver 0.4.4
%define libvirt_glib_ver 0.2.2
%define libxml2_ver 2.7.8
%define libusb_ver 1.0.9
%define spice_gtk_ver 0.27
%define gudev_ver 165
%define osinfo_ver 0.2.12
%define tracker_ver 0.13.1
%define uuid_ver 1.41.3
%define libsoup_ver 2.38
%define libarchive_ver 3.0.0

BuildRequires: intltool >= 0.40.0
BuildRequires: yelp-tools
BuildRequires: gobject-introspection-devel >= 0.9.6
BuildRequires: libvala-devel >= 0.28.0.16
BuildRequires: vala-tools
BuildRequires: glib2-devel >= %glib_ver libgio-devel >= %glib_ver
BuildRequires: libgtk+3-devel >= %gtk_ver libgtk+3-gir-devel
BuildRequires: libgtk3vnc-devel >= %gtk_vnc_ver
BuildRequires: libvirt-gobject-devel >= %libvirt_glib_ver
BuildRequires: libvirt-gconfig-devel >= %libvirt_glib_ver
BuildRequires: libxml2-devel >= %libxml2_ver
BuildRequires: libusb-devel >= %libusb_ver
BuildRequires: libspice-gtk3-devel >= %spice_gtk_ver
BuildRequires: libgudev-devel >= %gudev_ver
BuildRequires: libosinfo-devel >= %osinfo_ver
BuildRequires: tracker-devel >= %tracker_ver
BuildRequires: libuuid-devel >= %uuid_ver
BuildRequires: libsoup-devel >= %libsoup_ver
BuildRequires: libarchive-devel >= %libarchive_ver
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
	--enable-vala

%make_build

%install
%makeinstall_std
%find_lang %name --with-gnome

%files -f %name.lang
%doc AUTHORS COPYING README NEWS TODO
%_bindir/%name
%_datadir/%name
%_desktopdir/*.desktop
%_datadir/glib-2.0/schemas/org.gnome.boxes.gschema.xml
%_iconsdir/hicolor/*/apps/gnome-boxes*
%_libexecdir/gnome-boxes-search-provider
%_datadir/dbus-1/services/*.service
%_datadir/gnome-shell/search-providers/gnome-boxes-search-provider.ini
%_datadir/appdata/*.xml

%changelog
* Mon Dec 26 2016 Alexey Shabalin <shaba@altlinux.ru> 3.22.3-alt1
- 3.22.3

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 3.22.1-alt1
- 3.22.1

* Mon Jun 27 2016 Alexey Shabalin <shaba@altlinux.ru> 3.20.2-alt2
- rebuild with spice-gtk-0.32-alt1

* Tue May 10 2016 Alexey Shabalin <shaba@altlinux.ru> 3.20.2-alt1
- 3.20.2

* Mon Apr 25 2016 Alexey Shabalin <shaba@altlinux.ru> 3.20.1-alt1
- 3.20.1

* Fri Apr 01 2016 Alexey Shabalin <shaba@altlinux.ru> 3.20.0-alt1
- 3.20.0

* Tue Oct 20 2015 Alexey Shabalin <shaba@altlinux.ru> 3.18.1-alt1
- 3.18.1

* Wed Apr 15 2015 Alexey Shabalin <shaba@altlinux.ru> 3.16.1-alt1
- 3.16.1

* Mon Mar 30 2015 Alexey Shabalin <shaba@altlinux.ru> 3.16.0-alt1
- 3.16.0

* Wed Nov 12 2014 Alexey Shabalin <shaba@altlinux.ru> 3.14.2-alt1
- 3.14.2

* Tue Sep 30 2014 Alexey Shabalin <shaba@altlinux.ru> 3.14.0-alt1
- 3.14.0

* Tue May 13 2014 Alexey Shabalin <shaba@altlinux.ru> 3.12.2-alt1
- 3.12.2

* Fri Apr 25 2014 Alexey Shabalin <shaba@altlinux.ru> 3.12.1-alt1
- 3.12.1

* Tue Mar 25 2014 Alexey Shabalin <shaba@altlinux.ru> 3.12.0-alt1
- 3.12.0

* Mon Feb 24 2014 Alexey Shabalin <shaba@altlinux.ru> 3.11.90.1-alt1.git.58bb18
- upstream snapshot 58bb18a328c2f3db3c3b656edcc8bd93630a2084

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

