%define oname python-osmgpsmap
Name: python-module-osmgpsmap
Version: 0.7.3
Release: alt1

Summary: Python bindings for osm-gps-map GTK+ widget

Group: Development/Python
License: GPLv2
Url: http://nzjrs.github.com/osm-gps-map/

Packager: Vitaly Lipatov <lav@altlinux.ru>

%setup_python_module osmgpsmap

Source: http://www.johnstowers.co.nz/files/osm-gps-map/%oname-%version.tar

# Automatically added by buildreq on Mon May 28 2012
# optimized out: fontconfig fontconfig-devel glib2-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgtk+2-devel libosm-gps-map libpango-devel libsoup-devel pkg-config python-base python-devel python-module-distribute python-module-peak python-module-pygobject-devel python-module-zope python-modules python-modules-compiler python-modules-email
BuildRequires: libosm-gps-map-devel python-module-mwlib python-module-paste python-module-pygtk-devel

%description
Python bindings for a GTK+ widget that when given GPS co-ordinates,
draws a GPS track, and points of interest on a moving map
display. Downloads map data from a number of websites, including
openstreetmap.org.

%prep
%setup -n %oname-%version

%build
%python_build

%install
%python_install

%files
%doc AUTHORS ChangeLog COPYING NEWS
%python_sitelibdir/osmgpsmap.so
%python_sitelibdir/python_osmgpsmap-%version-py*.egg-info

%changelog
* Sat May 26 2012 Vitaly Lipatov <lav@altlinux.ru> 0.7.3-alt1
- initial build for ALT Linux Sisyphus (thanks, Fedora!)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep  9 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.7.3-5
- Drop README (only contains information on installing)

* Wed Sep 07 2011 Richard Shaw <hobbes1069@gmail.com> - 0.7.3-4
- Updated license in spec file to GPLv2.
- Update Source url in spec file to use %%{name} where appropriate.
- Added ChangeLog NEWS and README to package documentation.

* Sat Jul  2 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.7.3-3
- Filter private shared library provides
- use setup rather than setup0
- drop defattr
- Drop buildroot
- Drop clean section
- Use name of library rather than wildcard
- Add COPYING file to doc

* Wed May 11 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.7.3-2
- Add missing BRs

* Tue May  3 2011 Jeffrey C. Ollie <jeff@ocjtech.us> - 0.7.3-1
- First version for Fedora

