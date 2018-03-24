
Name: libgaiagraphics
Version: 0.5
Release: alt1
Summary: Graphics canvas for GIS rendering

Group: System/Libraries
License: LGPLv3+
Packager: Ilya Mashkin <oddity@altlinux.ru>
Url: https://www.gaia-gis.it/fossil/libgaiagraphics
Source0: http://www.gaia-gis.it/gaia-sins/%name-%version.tar.gz

BuildRequires: libcairo-devel
BuildRequires: libgeotiff-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libxml2-devel
# Is only checked for, but not actually used
BuildRequires: libproj-devel

%description
Libgaiagraphics wraps raster- and vector graphics, to implement a reasonably
abstract and platform independent graphics canvas for GIS rendering.

%package devel
Summary: Development files for %name
Group: System/Libraries
Requires: %name%{?_isa} = %version-%release
Requires: pkgconfig

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup

%build
%configure --disable-static

# Remove links to unused libraries
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

%make_build

%install
%makeinstall_std

# Delete libtool archives, because we don't ship them
find %buildroot -name '*.la' -exec rm -f {} ';'

%files
%doc AUTHORS COPYING
%_libdir/%name.so.*

%files devel
%_includedir/gaiagraphics.h
%_libdir/%{name}*.so
%_libdir/pkgconfig/gaiagraphics.pc

%changelog
* Thu Feb 04 2016 Andrey Cherepanov <cas@altlinux.org> 0.5-alt1
- New version

* Sat Feb 02 2013 Ilya Mashkin <oddity@altlinux.ru> 0.4b-alt1
- Build for Sisyphus

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 0.4b-4
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 0.4b-3
- rebuild against new libjpeg

* Wed Jan 11 2012 Volker Frohlich <volker27@gmx.at> - 0.4b-1
- Update for new release
- Update URL and source URL
- Drop LGPL source, upstream includes the proper license now
- Drop libgeotiff patch, configure now searches in  include/libgeotiff now as well
- Subsequently drop BR autoconf

* Wed Nov 23 2011 Volker Frohlich <volker27@gmx.at> - 0.4-3
- Replace wrong license file

* Sun Oct 30 2011 Volker Frohlich <volker27@gmx.at> - 0.4-2
- Place isa in devel package's Requires
- Correct license to LPGLv3+
- Correct spelling of the name in description
- More specific file list
- Add Requires for pkgconfig to devel sub-package (EPEL 5)
- Switch to name and version macro in source URL
- Remove zlib-devel as BR; libpng-devel already requires it

* Tue Jan 18 2011 Volker Frohlich <volker27@gmx.at> - 0.4-1
- Initial packaging
