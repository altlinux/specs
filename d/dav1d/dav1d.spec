Name: dav1d
Version: 1.4.3
Release: alt1
%define soversion 7

Summary: AV1 cross-platform Decoder
License: BSD
Group: Video

Url: https://code.videolan.org/videolan/dav1d
VCS: https://code.videolan.org/videolan/dav1d.git/
Source: %name-%version.tar
BuildRequires: gcc
BuildRequires: nasm
BuildRequires: doxygen
BuildRequires: meson >= 0.47.0

%description
dav1d is a new AV1 cross-platform Decoder, open-source, and focused on speed
and correctness.

%package -n libdav1d_%soversion
Group: Video
Summary: Library files for dav1d

%description -n libdav1d_%soversion
Library files for dav1d, the AV1 cross-platform Decoder.

%package -n libdav1d-devel
Group: Video
Summary: Development files for dav1d
Requires: libdav1d_%soversion = %EVR

%description -n libdav1d-devel
Development files for dav1d, the AV1 cross-platform Decoder.

%prep
%setup

%build
%meson

%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc COPYING doc/PATENTS
%doc CONTRIBUTING.md NEWS README.md
%_bindir/dav1d

%files -n libdav1d_%soversion
%doc COPYING doc/PATENTS
%_libdir/libdav1d.so.%soversion
%_libdir/libdav1d.so.%soversion.*

%files -n libdav1d-devel
#doc %_target_platform/doc/html
%_includedir/%name
%_libdir/libdav1d.so
%_pkgconfigdir/%name.pc

%changelog
* Mon Jul 01 2024 Anton Farygin <rider@altlinux.ru> 1.4.3-alt1
- 1.4.3

* Sun Jun 09 2024 Anton Farygin <rider@altlinux.ru> 1.4.2-alt1
- 1.4.2

* Mon Apr 01 2024 Anton Farygin <rider@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Thu Feb 22 2024 Anton Farygin <rider@altlinux.ru> 1.4.0-alt1
- 1.4.0
- a package with the library was renamed in accordance with SharedLibsPolicy

* Fri Jun 30 2023 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- new version 1.2.1 (with rpmrb script)

* Tue May 30 2023 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- new version 1.2.0 (with rpmrb script)

* Sun Apr 23 2023 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- new version 1.1.0 (with rpmrb script)

* Mon Dec 13 2021 Vitaly Lipatov <lav@altlinux.ru> 0.9.2-alt1
- new version 0.9.2 (with rpmrb script)

* Sun Jan 26 2020 Vitaly Lipatov <lav@altlinux.ru> 0.5.2-alt1
- new version 0.5.2 (with rpmrb script)

* Thu May 30 2019 Vitaly Lipatov <lav@altlinux.ru> 0.3.1-alt1
- new version 0.3.1 (with rpmrb script)

* Wed May 08 2019 Michael Shigorin <mike@altlinux.org> 0.3.0-alt2
- fixed build on e2k
- minor spec cleanup

* Mon May 06 2019 Vitaly Lipatov <lav@altlinux.ru> 0.3.0-alt1
- new version 0.3.0 (with rpmrb script)

* Mon Apr 01 2019 Vitaly Lipatov <lav@altlinux.ru> 0.2.1-alt1
- initial build for ALT Sisyphus

* Tue Mar 26 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.1-2
- Rebuild with -Db_ndebug=true

* Tue Mar 12 2019 Robert-André Mauchin - 0.2.1-1
- Release 0.2.1

* Tue Mar 05 2019 Robert-André Mauchin - 0.2.0-1
- Release 0.2.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 11 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.0-1
- Initial build
