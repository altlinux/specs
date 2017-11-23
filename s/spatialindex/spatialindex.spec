# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:      spatialindex
Version:   1.8.5
Release:   alt1_7
Summary:   Spatial index library 
Group:     System/Libraries
License:   MIT
URL:       http://libspatialindex.org
Source0:   http://download.osgeo.org/lib%{name}/%{name}-src-%{version}.tar.bz2

BuildRequires:    ctest cmake
Source44: import.info

%description
Spatialindex provides a general framework for developing spatial indices.
Currently it defines generic interfaces, provides simple main memory and
disk based storage managers and a robust implementation of an R*-tree,
an MVR-tree and a TPR-tree.

%package devel
Summary: Development files for %{name}
Group: Development/Other
Requires: %{name} = %{version}-%{release}

%description devel
Development files for %{name}.


%prep
%setup -qn %{name}-src-%{version}


%build
%{fedora_cmake} .
%make_build


%install
make install DESTDIR=%{buildroot}


# Tests must be run manually and seemingly are not built yet
# See changelog 2011-10-11


%files 
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/lib%{name}*.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}*.so


%changelog
* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 1.8.5-alt1_7
- new version

* Thu Feb 27 2014 Ilya Mashkin <oddity@altlinux.ru> 1.8.1-alt1
- 1.8.1

* Mon Dec 24 2012 Ilya Mashkin <oddity@altlinux.ru> 1.8.0-alt1
- Build for Sisyphus

* Thu Dec 13 2012 Volker Frohlich <volker27@gmx.at> - 1.8.0-1
- New upstream release
- New URL
- License is now MIT

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
