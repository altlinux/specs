# vim: set ft=spec : -*- rpm-spec -*-
%define        _unpackaged_files_terminate_build 1
%define        nomen yajl

Name:          lib%nomen
Version:       2.1.0.6
Release:       alt0.1

Summary:       Yet Another JSON Library
Group:         Development/C
License:       BSD
Url:           https://github.com/lloyd/yajl
Vcs:           https://github.com/lloyd/yajl.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: ctest

%description
Yet Another JSON Library (YAJL).

%package       -n %nomen
Summary:       Yet Another JSON Library
Group:         Development/C

%description   -n %nomen
Yet Another JSON Library (YAJL).

%package       devel
Summary:       Yet Another JSON Library (development headers)
Group:         Development/C

%description   devel
Development headers for Yet Another JSON Library (YAJL).

%prep
%setup

%build
%cmake \
   -DBUILD_SHARED_LIBS=ON \
   -DCMAKE_BUILD_TYPE=RelWithDebInfo \
   %nil
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%doc README TODO
%_libdir/libyajl.so.*

%files         -n %nomen
%doc README TODO
%_bindir/json_reformat
%_bindir/json_verify

%files         devel
%doc README
%_includedir/yajl
%_libdir/libyajl.so
%_pkgconfigdir/*.pc

%changelog
* Wed Jul 23 2025 Pavel Skrylev <majioa@altlinux.org> 2.1.0.6-alt0.1
- ^ 2.1.0 -> 2.1.0p6
- ! fixed FTBFS

* Wed Jun 14 2023 Alexander Danilov <admsasha@altlinux.org> 2.1.0-alt3
- fixes CVE-2023-33460.

* Tue Oct 26 2021 Alexey Shabalin <shaba@altlinux.org> 2.1.0-alt2
- Fix build.

* Wed Apr 28 2021 Arseny Maslennikov <arseny@altlinux.org> 2.1.0-alt1.1
- NMU: spec: adapted to new cmake macros.

* Mon May 12 2014 Alexey Shabalin <shaba@altlinux.ru> 2.1.0-alt1
- 2.1.0

* Wed Jun 13 2012 Alexey Shabalin <shaba@altlinux.ru> 2.0.4-alt1
- 2.0.4

* Fri Apr 15 2011 Alexey Shabalin <shaba@altlinux.ru> 1.0.11-alt1
- 1.0.11
- rebuild for debuginfo

* Tue Jan 25 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt1.1
- rebuild for set:provides by request of mithraen

* Sun Apr 11 2010 Alexey I. Froloff <raorn@altlinux.org> 1.0.9-alt1
- Built for Sisyphus

