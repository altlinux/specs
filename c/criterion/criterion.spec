%define optflags_lto %nil
Name: criterion
Version: 2.4.1
Release: alt1

Summary: A cross-platform C and C++ unit testing framework for the 21th century

License: MIT
Group: Development/C++
Url: https://github.com/Snaipe/Criterion

BuildRequires: gcc-c++
BuildRequires(pre): rpm-macros-meson
BuildRequires: cmake meson libnanomsg-devel libnanopb-devel libboxfort-devel libgit2-devel libffi-devel

ExcludeArch: armh ppc64le

# Source-url: https://github.com/Snaipe/Criterion/archive/v%version.tar.gz
Source: %name-%version.tar

# Source1-script: .gear/criterion-postsubmodules/copy-source.sh
Source1: %name-postsubmodules-%version.tar

%description
A dead-simple, yet extensible, C and C++ unit testing framework.

%package -n lib%name-devel
Summary: A cross-platform C and C++ unit testing framework for the 21th century
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
A dead-simple, yet extensible, C and C++ unit testing framework.

%package -n lib%name
Summary: A cross-platform C and C++ unit testing framework for the 21th century
Group: Development/C++

%description -n lib%name
A dead-simple, yet extensible, C and C++ unit testing framework.

%prep
%setup -a1
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

%files -n lib%name -f %name.lang
%_libdir/libcriterion.so.*

%files -n lib%name-devel
%_includedir/criterion/
%_libdir/libcriterion.so
%_pkgconfigdir/criterion.pc

%changelog
* Sun Jul 17 2022 Vitaly Lipatov <lav@altlinux.ru> 2.4.1-alt1
- new version 2.4.1 (with rpmrb script)

* Wed Mar 13 2019 Vitaly Lipatov <lav@altlinux.ru> 2.3.3-alt1
- initial build for ALT Sisyphus

