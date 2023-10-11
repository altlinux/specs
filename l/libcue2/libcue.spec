Name: libcue2
Version: 2.3.0
Release: alt1

Summary: Cue sheet parser library

# Files libcue/rem.{c,h} contains a BSD header
License: GPLv2 and BSD
Group: System/Libraries
Url: https://github.com/lipnitsk/libcue

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/lipnitsk/libcue/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: flex gcc-c++ cmake

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
subst "s|\(ADD_LIBRARY(cue \)|\1 SHARED |" CMakeLists.txt

%build
%cmake_insource
%make_build

%install
%makeinstall_std

%files
%_libdir/libcue.so.*
%doc README.md ChangeLog LICENSE

%files -n libcue-devel
%_includedir/libcue/
%_includedir/libcue.h
%_libdir/libcue.so
%_pkgconfigdir/libcue.pc

%changelog
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

