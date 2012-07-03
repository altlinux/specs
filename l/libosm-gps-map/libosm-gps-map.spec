%define oname osm-gps-map
Name: libosm-gps-map
Version: 0.7.3
Release: alt1

Summary: Gtk+ widget for displaying OpenStreetMap tiles

Group: System/Libraries
License: GPLv2
Url: http://nzjrs.github.com/osm-gps-map/
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.johnstowers.co.nz/files/osm-gps-map/%oname-%version.tar

# Automatically added by buildreq on Sat May 26 2012
# optimized out: fontconfig fontconfig-devel glib2-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libpango-devel libwayland-client libwayland-server pkg-config
BuildRequires: glibc-devel gtk-doc libgtk+2-devel libsoup-devel

%description
A Gtk+ widget that when given GPS co-ordinates, draws a GPS track, and
points of interest on a moving map display. Downloads map data from a
number of websites, including openstreetmap.org.

%package devel
Summary: Development files for the osm-gps-map Gtk+ widget
Group: Development/Other
Requires: %name = %version-%release

%description devel
The development files for the osm-gps-map Gtk+ widget

%prep
%setup -n %oname-%version

%build
%configure --disable-static --disable-introspection
%make_build

%install
%makeinstall_std
rm -rf %buildroot/usr/doc/osm-gps-map
rm -rf %buildroot%_libdir/libosmgpsmap.la

%files
%doc AUTHORS COPYING README NEWS
%_libdir/libosmgpsmap.so.*

%files devel
%doc %_datadir/gtk-doc/html/libosmgpsmap
%_includedir/osmgpsmap/
%_libdir/libosmgpsmap.so
%_pkgconfigdir/osmgpsmap.pc

%changelog
* Sat May 26 2012 Vitaly Lipatov <lav@altlinux.ru> 0.7.3-alt1
- initial build for ALT Linux Sisyphus (thanks, Fedora!)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.7.3-4
- Rebuild for new libpng

* Tue May 10 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.7.3-3
- Drop unecessary BR cairo-gobject-devel

* Fri May  6 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.7.3-2
- Fix issues noted in review:
- - grammatical issues
- - drop reference to python bindings
- - use GPLv2 license
- - add/remove doc files
- - use verbose build
- - disable gobject introspection

* Tue May  3 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.7.3-1
- First version for Fedora
