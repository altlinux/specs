Name: spatialindex
Version: 1.8.0
Release: alt1
Summary: Spatial index library
Group: System/Libraries
Packager: Ilya Mashkin <oddity@altlinux.ru>
License: MIT
Url: http://libspatialindex.org
Source0: http://download.osgeo.org/lib%name/%name-src-%version.tar.bz2

# Create proper soname symlinks and versioned libspatialindex_c
# https://github.com/libspatialindex/libspatialindex/issues/9
# Autotools do it automatically
Patch0: %name-1.8.0-soname.patch

BuildRequires: cmake gcc gcc-c++ gcc-fortran

%description
Spatialindex provides a general framework for developing spatial indices.
Currently it defines generic interfaces, provides simple main memory and
disk based storage managers and a robust implementation of an R*-tree,
an MVR-tree and a TPR-tree.

%package devel
Summary: Development files for %name
Group: System/Libraries
Requires: %name%{?_isa} = %version-%release

%description devel
Development files for %name.

%prep
%setup -n %name-src-%version
%patch0 -p1 -b .soname~

%build
%cmake ../
cd BUILD
make %{?_smp_mflags}

%install
cd BUILD
make install DESTDIR=%buildroot

# Tests must be run manually and seemingly are not built yet
# See changelog 2011-10-11


%files
%doc AUTHORS ChangeLog COPYING README
%_libdir/lib%{name}*.so.*

%files devel
%_includedir/%name
%_libdir/lib%{name}*.so

%changelog
* Mon Dec 24 2012 Ilya Mashkin <oddity@altlinux.ru> 1.8.0-alt1
- Build for Sisyphus

* Thu Dec 13 2012 Volker Frohlich <volker27@gmx.at> - 1.8.0-1
- New upstream release
- New URL
- License is now MIT

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr  9 2012 Volker Frohlich <volker27@gmx.at> - 1.7.1-2
- Patch build system to install to the expected include dir
  and produce proper soname symlinks and fully versioned C
  API library

* Sun Apr  8 2012 Volker Frohlich <volker27@gmx.at> - 1.7.1-1
- Update for new release
- Drop 64 bit patch
- Header permissions are correct now
- Move header files to spatialindex sub-directory
- Correct FSF address in all files
- Update URL
- Upstream switched to Cmake
- No more issues with rpath, libtool archives or undefined symbols

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-5
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Aug 04 2011 Volker Frohlich <volker27@gmx.at> - 1.6.1-3
- Preserve timestamps by using install -p

* Thu Aug 04 2011 Volker Frohlich <volker27@gmx.at> - 1.6.1-2
- Generalized file list to avoid specifying so-version
- Adapt Require in sub-package to guidelines
- Removed BR chrpath; using approach from
  http://fedoraproject.org/wiki/Packaging:Guidelines#Removing_Rpath
- Correct FSF postal address

* Thu Jun 02 2011 Volker Frohlich <volker27@gmx.at> - 1.6.1-1
- Initial packaging
