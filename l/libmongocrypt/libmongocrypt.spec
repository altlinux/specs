%define sover 0

%ifnarch i586
%def_enable check
%endif

Name: libmongocrypt
Version: 1.19.2
Release: alt1

Summary: The companion C library for client side encryption in drivers

License: Apache-2.0
Group: System/Libraries
Url: https://github.com/mongodb/libmongocrypt
VCS: https://github.com/mongodb/libmongocrypt

# Source-url: https://github.com/mongodb/libmongocrypt/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar
Patch0: %name-%version-%release.patch
Patch1: libmongocrypt-1.15.1-fedora-static-libbson.patch

BuildRequires: cmake gcc-c++ git-core libbson-devel libssl-devel python3
%if_enabled check
BuildRequires: ctest
%endif

%description
%summary.

%package common
Summary: The common files for %name
Group: Documentation
BuildArch: noarch

%description common
This package provides the common files for %name.

%package -n libkms_message-common
Summary: The common files for libkms_message
Group: Documentation
BuildArch: noarch

%description -n libkms_message-common
This package provides the common files for libkms_message.

%package -n %name%sover
Summary: The companion C library for client side encryption in drivers
Group: System/Libraries

%description -n %name%sover
This package provides libmongocrypt library.

%package -n libkms_message%sover
Summary: The kms-message C library
Group: System/Libraries

%description -n libkms_message%sover
This package provides libkms_message library.

%package devel
Summary: The development files for %name
Group: Development/C

%description devel
This package provides development files for %name.

%package -n libkms_message-devel
Summary: The development files for libkms_message
Group: Development/C

%description -n libkms_message-devel
This package provides development files for libkms_message.

%prep
%setup
%if "%(rpmquery --qf '%%{VERSION}' libbson-devel)" < "2"
%patch0 -p1
%endif
%patch1 -p1

%build
%cmake \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DBUILD_VERSION=%version \
  -DENABLE_PIC=ON \
  -DUSE_SHARED_LIBBSON=ON \
  -DMONGOCRYPT_MONGOC_DIR=USE-SYSTEM \
  -DENABLE_ONLINE_TESTS=OFF \
  -DENABLE_STATIC=OFF \
#
%ifarch %e2k
sed -i 's/_M_AMD64/__e2k__/' %_cmake__builddir/_deps/intel_dfp-src/LIBRARY/float128/architecture.h
%endif
%cmake_build

%install
%cmake_install

%if_enabled check
%check
cd %_cmake__builddir
ctest
%endif

%files common
%doc CHANGELOG.md LICENSE README.md

%files -n libkms_message-common
%doc kms-message/{COPYING,README.md,THIRD_PARTY_NOTICES}

%files -n %name%sover
%_libdir/libmongocrypt.so.%{sover}*

%files -n libkms_message%sover
%_libdir/libkms_message.so.%{sover}*

%files devel
%_includedir/mongocrypt/
%_libdir/libmongocrypt.so
%_libdir/cmake/mongocrypt/
%_pkgconfigdir/libmongocrypt.pc

%files -n libkms_message-devel
%_includedir/kms_message/
%_libdir/libkms_message.so
%_libdir/cmake/kms_message/
%_pkgconfigdir/libkms_message.pc

%changelog
* Wed Jun 24 2026 Leontiy Volodin <lvol@altlinux.org> 1.19.2-alt1
- New version 1.19.2.

* Thu Jun 18 2026 Leontiy Volodin <lvol@altlinux.org> 1.19.1-alt1
- New version 1.19.1.

* Wed Jun 17 2026 Leontiy Volodin <lvol@altlinux.org> 1.19.0-alt1
- New version 1.19.0.

* Tue Jun 02 2026 Leontiy Volodin <lvol@altlinux.org> 1.18.2-alt1
- New version 1.18.2.

* Wed May 13 2026 Leontiy Volodin <lvol@altlinux.org> 1.18.1-alt1
- New version 1.18.1.

* Wed May 06 2026 Leontiy Volodin <lvol@altlinux.org> 1.18.0-alt1
- New version 1.18.0.

* Wed Apr 08 2026 Leontiy Volodin <lvol@altlinux.org> 1.17.3-alt1
- New version 1.17.3.

* Thu Feb 05 2026 Leontiy Volodin <lvol@altlinux.org> 1.17.2-alt1
- New version 1.17.2.

* Mon Jan 12 2026 Leontiy Volodin <lvol@altlinux.org> 1.17.1-alt1
- New version 1.17.1.

* Tue Nov 11 2025 Leontiy Volodin <lvol@altlinux.org> 1.17.0-alt1
- New version 1.17.0.

* Wed Oct 01 2025 Leontiy Volodin <lvol@altlinux.org> 1.16.0-alt1
- New version 1.16.0.

* Wed Sep 17 2025 Leontiy Volodin <lvol@altlinux.org> 1.15.2-alt1
- New version 1.15.2.

* Mon Sep 15 2025 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.15.1-alt2
- e2k build fix

* Tue Aug 12 2025 Leontiy Volodin <lvol@altlinux.org> 1.15.1-alt1
- Initial commit for ALT Sisyphus (for mongo-php-driver).
