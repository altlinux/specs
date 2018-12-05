Name: libolm
Version: 3.0.0
Release: alt1

Summary: An implementation of the Double Ratchet cryptographic ratchet

Group: Development/Other
License: Apache v2.0
Url: https://git.matrix.org/git/olm

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
%doc README.rst docs
%doc LICENSE
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/olm
%_libdir/cmake/Olm

%changelog
* Fri Nov 30 2018 Paul Wolneykien <manowar@altlinux.org> 3.0.0-alt1
- Initial release.
