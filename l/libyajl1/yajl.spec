# vim: set ft=spec : -*- rpm-spec -*-
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

Name: libyajl1
Version: 1.0.11
Release: alt3.2

Summary: Yet Another JSON Library
Group: System/Legacy libraries
License: BSD
Url: http://github.com/lloyd/yajl

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake

%description
Yet Another JSON Library (YAJL).

%package -n %name-devel
Summary: Yet Another JSON Library (development headers)
Group: Development/C
Requires: %name = %version-%release
Conflicts: libyajl-devel

%description -n %name-devel
Development headers for Yet Another JSON Library (YAJL).


%prep
%setup
%patch -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_libdir/libyajl.so.*

%files -n %name-devel
%_includedir/yajl
%_libdir/libyajl.so

%changelog
* Fri Oct 29 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.0.11-alt3.2
- FTBFS: fix build with LTO

* Tue Apr 27 2021 Arseny Maslennikov <arseny@altlinux.org> 1.0.11-alt3.1
- NMU: spec: adapted to new cmake macros.

* Tue Jun 04 2013 Sergey Y. Afonin <asy@altlinux.ru> 1.0.11-alt3
- return devel package (ALT #27558)

* Wed Jun 13 2012 Alexey Shabalin <shaba@altlinux.ru> 1.0.11-alt2
- build as legacy libraries "libyajl1" for compat

* Fri Apr 15 2011 Alexey Shabalin <shaba@altlinux.ru> 1.0.11-alt1
- 1.0.11
- rebuild for debuginfo

* Tue Jan 25 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt1.1
- rebuild for set:provides by request of mithraen

* Sun Apr 11 2010 Alexey I. Froloff <raorn@altlinux.org> 1.0.9-alt1
- Built for Sisyphus

