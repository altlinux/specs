%define optflags_lto %nil
%define abiversion 4
Name: criterion
Version: 2.5.0
Release: alt1

Summary: A cross-platform C and C++ unit testing framework for the 21th century

License: MIT
Group: Development/C++
Url: https://github.com/Snaipe/Criterion

BuildRequires: gcc-c++
BuildRequires(pre): rpm-macros-meson
BuildRequires: cmake meson libnanomsg-devel libnanopb-devel libboxfort-devel libgit2-devel libffi-devel

ExcludeArch: armh ppc64le

# Source-url: https://github.com/Snaipe/Criterion/releases/download/v%version/criterion-%version.tar.xz
Source: %name-%version.tar

%description
A dead-simple, yet extensible, C and C++ unit testing framework.

%package -n lib%name-devel
Summary: A cross-platform C and C++ unit testing framework for the 21th century
Group: Development/C++
Requires: lib%name%abiversion = %EVR

%description -n lib%name-devel
A dead-simple, yet extensible, C and C++ unit testing framework.

%package -n lib%name%abiversion
Summary: A cross-platform C and C++ unit testing framework for the 21th century
Group: System/Libraries
Requires: lib%name-common >= %EVR
Provides: lib%name = %EVR
Obsoletes: lib%name < %EVR

%description -n lib%name%abiversion
A dead-simple, yet extensible, C and C++ unit testing framework.

%package -n lib%name-common
Summary: Common files (translations) for Criterion library
Group: System/Internationalization
BuildArch: noarch

%description -n lib%name-common
A dead-simple, yet extensible, C and C++ unit testing framework.

This package contains ABI independent files (translations).

%prep
%setup
subst 's|must_regenerate_pb =.*|must_regenerate_pb = false|' meson.build
subst 's|protobuf-nanopb-static|protobuf-nanopb|' meson.build

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

rm %buildroot%_libdir/libcriterion.a
#rm -rf %buildroot%_datadir/locale/
# FIXME
#rm -rf %buildroot/tmp/
# fix /usr/lib64
#[ -d %buildroot%_libdir ] || mv %buildroot%_prefix/lib %buildroot%_libdir

%files -n lib%name-common -f %name.lang

%files -n lib%name%abiversion
%_libdir/libcriterion.so.%abiversion
%_libdir/libcriterion.so.%abiversion.*

%files -n lib%name-devel
%_includedir/criterion/
%_libdir/libcriterion.so
%_pkgconfigdir/criterion.pc

%changelog
* Wed Oct 07 2026 Vitaly Lipatov <lav@altlinux.ru> 2.5.0-alt1
- new version 2.5.0
- soname bumped to libcriterion.so.4: rename libcriterion to libcriterion4 (Shared Libs Policy)
- move translations to noarch libcriterion-common subpackage

* Thu Mar 12 2026 Vitaly Lipatov <lav@altlinux.ru> 2.4.3-alt1
- new version 2.4.3

* Sun Jul 17 2022 Vitaly Lipatov <lav@altlinux.ru> 2.4.1-alt1
- new version 2.4.1 (with rpmrb script)

* Wed Mar 13 2019 Vitaly Lipatov <lav@altlinux.ru> 2.3.3-alt1
- initial build for ALT Sisyphus

