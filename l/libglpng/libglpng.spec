Name: libglpng
Version: 1.45
Release: alt1.1
Summary: Toolkit for loading PNG images as OpenGL textures
Group: System/Libraries
License: MIT
Url: https://admin.fedoraproject.org/pkgdb/packages/name/libglpng
# Upstream's dead
Source0: http://ftp.de.debian.org/debian/pool/main/libg/%name/%{name}_%version.orig.tar.gz
# From Debian - a Makefile. Yay.
Source1: libglpng-1.45-makefile
# Debian patch, couple of small fixes.
Patch0: libglpng-1.45-debian.patch
Packager: Fr. Br. George <george@altlinux.ru>

BuildRequires: libpng-devel libGL-devel

%description
glpng is a small toolkit to make loading PNG image files as an OpenGL
texture as easy as possible.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -q -n %name-%version.orig
%patch0 -p1
cp %SOURCE1 Makefile

%build
%make_build CFLAGS="$RPM_OPT_FLAGS -fPIC -Iinclude" libglpng.so.1.45

%install
%makeinstall DESTDIR=$RPM_BUILD_ROOT%prefix LIB=%_lib

%files
%doc glpng.htm
%_libdir/%name.so.*

%files devel
%doc Example glpng.htm
%_includedir/GL/*
%_libdir/%name.so

%changelog
* Tue Nov 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.45-alt1.1
- Rebuilt for soname set-versions

* Mon Jul 05 2010 Fr. Br. George <george@altlinux.ru> 1.45-alt1
- Initial build from FC

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 17 2009 Hans de Goede <hdegoede@redhat.com> 1.45-1
- Initial Fedora package, based on Mandriva package
