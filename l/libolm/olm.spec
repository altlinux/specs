%define _unpackaged_files_terminate_build 1

Name: libolm
Version: 3.2.4
Release: alt1

Summary: An implementation of the Double Ratchet cryptographic ratchet

Group: Development/Other
License: Apache v2.0
Url: https://gitlab.matrix.org/matrix-org/olm.git

Source: %name-%version.tar

BuildRequires: cmake ctest gcc-c++

%description
An implementation of the Double Ratchet cryptographic ratchet described by
https://whispersystems.org/docs/specifications/doubleratchet/, written
in C and C++11 and exposed as a C API.

The specification of the Olm ratchet can be found in `<docs/olm.rst>`.

This library also includes an implementation of the Megolm cryptographic
ratchet, as specified in `<docs/megolm.rst>`.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
The %name-devel package contains C++ header files for developing
applications that use %name.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%check
%make_build test

%files
%doc README.md
%doc LICENSE
%_libdir/*.so.*

%files devel
%doc docs
%_libdir/*.so
%_includedir/olm
%_libdir/cmake/Olm
%_pkgconfigdir/olm.pc

%changelog
* Tue Sep 14 2021 Paul Wolneykien <manowar@altlinux.org> 3.2.4-alt1
- Updated to v3.2.4.

* Sun Feb 14 2021 Paul Wolneykien <manowar@altlinux.org> 3.2.1-alt1
- Fresh up to v3.2.1.

* Fri Jul 03 2020 Paul Wolneykien <manowar@altlinux.org> 3.1.5-alt1
- Fresh up to v3.1.5.

* Tue Mar 31 2020 Paul Wolneykien <manowar@altlinux.org> 3.1.4-alt1
- New upstream version 3.1.4.

* Fri Nov 30 2018 Paul Wolneykien <manowar@altlinux.org> 3.0.0-alt1
- Initial release.
