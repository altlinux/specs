# vim: set ft=spec : -*- rpm-spec -*-

Name: libyajl1
Version: 1.0.11
Release: alt2

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

%prep
%setup
%patch -p1

%build
%cmake
%make_build -C BUILD VERBOSE=1

%install
%makeinstall_std -C BUILD

%files
%_libdir/libyajl.so.*

%changelog
* Wed Jun 13 2012 Alexey Shabalin <shaba@altlinux.ru> 1.0.11-alt2
- build as legacy libraries "libyajl1" for compat

* Fri Apr 15 2011 Alexey Shabalin <shaba@altlinux.ru> 1.0.11-alt1
- 1.0.11
- rebuild for debuginfo

* Tue Jan 25 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt1.1
- rebuild for set:provides by request of mithraen

* Sun Apr 11 2010 Alexey I. Froloff <raorn@altlinux.org> 1.0.9-alt1
- Built for Sisyphus

