# vim: set ft=spec : -*- rpm-spec -*-

Name: yajl
Version: 2.0.4
Release: alt1

Summary: Yet Another JSON Library
Group: Development/C
License: BSD
Url: http://github.com/lloyd/yajl

Requires: lib%name = %version-%release

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake

%description
Yet Another JSON Library (YAJL).

%package -n lib%name
Summary: Yet Another JSON Library
Group: Development/C

%description -n lib%name
Yet Another JSON Library (YAJL).

%package -n lib%name-devel
Summary: Yet Another JSON Library (development headers)
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Development headers for Yet Another JSON Library (YAJL).

%prep
%setup
%patch -p1

%build
%cmake
%make_build -C BUILD VERBOSE=1

%install
%makeinstall_std -C BUILD
mkdir -p %buildroot%_pkgconfigdir
mv %buildroot%_datadir/pkgconfig/*.pc %buildroot%_pkgconfigdir/

%check
%make -C BUILD test

%files
%doc README TODO
%_bindir/json_reformat
%_bindir/json_verify

%files -n lib%name
%_libdir/libyajl.so.*

%files -n lib%name-devel
%_includedir/yajl
%_libdir/libyajl.so
%_pkgconfigdir/*.pc

%changelog
* Wed Jun 13 2012 Alexey Shabalin <shaba@altlinux.ru> 2.0.4-alt1
- 2.0.4

* Fri Apr 15 2011 Alexey Shabalin <shaba@altlinux.ru> 1.0.11-alt1
- 1.0.11
- rebuild for debuginfo

* Tue Jan 25 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt1.1
- rebuild for set:provides by request of mithraen

* Sun Apr 11 2010 Alexey I. Froloff <raorn@altlinux.org> 1.0.9-alt1
- Built for Sisyphus

