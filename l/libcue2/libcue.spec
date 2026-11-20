Name: libcue2
Version: 2.4.3
Release: alt1

Summary: Cue sheet parser library

# Files libcue/rem.{c,h} contains a BSD header
License: GPLv2 and BSD
Group: System/Libraries
Url: https://github.com/lipnitsk/libcue

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/lipnitsk/libcue/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: bison flex gcc-c++ rpm-build-cmake /usr/bin/ctest

%description
Libcue is intended for parsing a so-called cue sheet from a char string or
a file pointer. For handling of the parsed data a convenient API is available.

%package -n libcue-devel
Summary: Development files
Group: Development/C
Requires: %name = %EVR

%description -n libcue-devel
Development files for %name.

%prep
%setup

%build
# Keep assertions in upstream tests; optimization flags come from rpm.
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DBUILD_SHARED_LIBS=ON \
    -DCMAKE_C_FLAGS_RELWITHDEBINFO=
%cmake_build

%check
ctest --test-dir %_cmake__builddir --output-on-failure

%install
%cmake_install

%files
%_libdir/libcue.so.*
%doc README.md ChangeLog LICENSE

%files -n libcue-devel
%_includedir/libcue/
%_includedir/libcue.h
%_libdir/libcue.so
%_pkgconfigdir/libcue.pc

%changelog
* Fri Nov 20 2026 Vitaly Lipatov <lav@altlinux.ru> 2.4.3-alt1
- new version 2.4.3
- use rpm-build-cmake and enable shared libraries and upstream tests.
- add BuildRequires: bison, rpm-macros-cmake for the parser and macros.
- add BuildRequires: /usr/bin/ctest to run upstream tests.

* Wed Oct 11 2023 Vitaly Lipatov <lav@altlinux.ru> 2.3.0-alt1
- new version 2.3.0 (with rpmrb script)
- CVE-2023-43641

* Wed Feb 24 2021 Vitaly Lipatov <lav@altlinux.ru> 2.2.1-alt1
- new version 2.2.1 (with rpmrb script) (closes: #39700)

* Sun Aug 05 2012 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt2
- rebuild for enable debuginfo

* Wed Jul 25 2012 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt1
- new version 1.4.0 (with rpmrb script)

* Sat Dec 05 2009 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- initial build for ALT Linux Sisyphus

* Mon Nov 16 2009 Peter Lemenkov <lemenkov@gmail.com> - 1.3.0-2
- Changed %%description a bit
- Corrected license field
- Fixed Source0 value
- Fixed Group tag for main package

* Mon Nov  9 2009 Peter Lemenkov <lemenkov@gmail.com> - 1.3.0-1
- Initial package for Fedora

