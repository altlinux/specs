Name: libjpeg8
Version: 2.1.5.1
Release: alt1
Summary: The MMX/SSE accelerated JPEG compression/decompression library
License: IJG and BSD-3-Clause and Zlib
Group: System/Libraries
Url: http://sourceforge.net/projects/libjpeg-turbo

Source: https://sourceforge.net/projects/libjpeg-turbo/files/%version/libjpeg-turbo-%version.tar.gz
Patch: libjpeg-turbo14-noinst.patch
Patch1: libjpeg-turbo-header-files.patch
Patch11: libjpeg-turbo-alt-header-files.patch

BuildRequires(pre): rpm-build-ninja
BuildRequires: cmake gcc

%description
The libjpeg8 package contains a library of functions for manipulating JPEG images.

%prep
%setup -n libjpeg-turbo-%version
%patch11 -p2
chmod -x README.md

%build
%cmake \
    -GNinja \
    -DENABLE_STATIC=false \
    -DWITH_TURBOJPEG=false \
    -DWITH_JPEG8=true \
#
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install
find %buildroot -name "*.la" -delete

# We need only shared library for this package, so we will remove
# all other installed by default make sequence files.
rm -f %buildroot%_bindir/{cjpeg,djpeg,jpegtran,rdjpgcom,wrjpgcom}
rm -f %buildroot%_libdir/libjpeg.so
rm -rf %buildroot%_pkgconfigdir
rm -rf %buildroot%_includedir
rm -rf %buildroot%_mandir
# Packaged using %%doc
rm -rf %buildroot%_datadir/doc/libjpeg-turbo
rm -rf %buildroot%_libdir/cmake/libjpeg-turbo/*.cmake

%files
%doc README.md ChangeLog.md LICENSE.md README.ijg
%_libdir/libjpeg.so.8*

%changelog
* Thu Feb 09 2023 Leontiy Volodin <lvol@altlinux.org> 2.1.5.1-alt1
- New version (2.1.5.1) with rpmgs script.

* Wed Feb 01 2023 Leontiy Volodin <lvol@altlinux.org> 2.1.5-alt1
- New version (2.1.5) with rpmgs script.

* Tue Aug 16 2022 Leontiy Volodin <lvol@altlinux.org> 2.1.4-alt1
- New version (2.1.4) with rpmgs script.

* Mon Feb 28 2022 Leontiy Volodin <lvol@altlinux.org> 2.1.3-alt1
- New version (2.1.3) with rpmgs script.

* Wed Nov 24 2021 Leontiy Volodin <lvol@altlinux.org> 2.1.2-alt1
- New version (2.1.2) with rpmgs script.

* Mon Aug 16 2021 Leontiy Volodin <lvol@altlinux.org> 2.1.1-alt1
- New version (2.1.1) with rpmgs script.

* Thu May 20 2021 Leontiy Volodin <lvol@altlinux.org> 2.1.0-alt1.1
- NMU: spec: adapted to new cmake macros (altlinux.org/CMakeMigration2021).

* Mon Apr 26 2021 Leontiy Volodin <lvol@altlinux.org> 2.1.0-alt1
- New version (2.1.0) with rpmgs script.
- Fixes:
  + CVE-2021-20205.

* Tue Nov 17 2020 Leontiy Volodin <lvol@altlinux.org> 2.0.6-alt1
- New version (2.0.6) with rpmgs script.
- Built with ninja instead make.

* Thu Jun 25 2020 Leontiy Volodin <lvol@altlinux.org> 2.0.5-alt1
- New version (2.0.5) with rpmgs script.
- Updated license tag.
- Fixes:
  + CVE-2020-13790.

* Tue Feb 04 2020 Leontiy Volodin <lvol@altlinux.org> 2.0.4-alt1
- New version (2.0.4) with rpmgs script.
- Built with cmake.
- Updated source link.

* Mon Feb 03 2020 Leontiy Volodin <lvol@altlinux.org> 1.5.3-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
