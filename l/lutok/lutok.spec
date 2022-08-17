%def_enable snapshot
%define _libexecdir %_prefix/libexec
%define pkgtestsdir %_libexecdir/lutok/tests
%define pkgdocdir %_defaultdocdir/%name-%version
%define sover 3

%def_with doxygen
%def_disable check

Name: lutok
Version: 0.4
Release: alt1

Summary: Lightweight C++ API library for Lua
License: BSD-3-Clause
Group: Development/Tools
Url: https://github.com/jmmv/lutok

%if_disabled snapshot
Source: https://github.com/jmmv/%name/archive/%name-%version/%name-%version.tar.gz
%else
Vcs: https://github.com/jmmv/lutok.git
Source: %name-%version.tar
%endif
Patch1: %name-0.4-alt-testdir.patch

%define lua_ver 5.3
Requires: lua%lua_ver

BuildRequires: gcc-c++
BuildRequires: libatf-c++-devel >= 0.20
BuildRequires: libatf-sh-devel
BuildRequires: liblua%lua_ver-devel >= %lua_ver
%{?_with_doxygen:BuildRequires: doxygen}
%{?_enable_check:BuildRequires: kuya}

%description
Lutok provides thin C++ wrappers around the Lua C API to ease the
interaction between C++ and Lua. These wrappers make intensive use of
RAII to prevent resource leakage, expose C++-friendly data types, report
errors by means of exceptions and ensure that the Lua stack is always
left untouched in the face of errors. The library also provides a small
subset of miscellaneous utility functions built on top of the wrappers.

Lutok focuses on providing a clean and safe C++ interface; the drawback
is that it is not suitable for performance-critical environments.  In
order to implement error-safe C++ wrappers on top of a Lua C binary
library, Lutok adds several layers or abstraction and error checking
that go against the original spirit of the Lua C API and thus degrade
performance.

%package -n lib%name
Summary: Shared Lutok library
Group: System/Libraries

%description -n lib%name
Lutok provides thin C++ wrappers around the Lua C API to ease the
interaction between C++ and Lua. These wrappers make intensive use of
RAII to prevent resource leakage, expose C++-friendly data types, report
errors by means of exceptions and ensure that the Lua stack is always
left untouched in the face of errors. The library also provides a small
subset of miscellaneous utility functions built on top of the wrappers.

Lutok focuses on providing a clean and safe C++ interface; the drawback
is that it is not suitable for performance-critical environments.  In
order to implement error-safe C++ wrappers on top of a Lua C binary
library, Lutok adds several layers or abstraction and error checking
that go against the original spirit of the Lua C API and thus degrade
performance.

%package -n lib%name-devel
Summary: Libraries and header files for Lutok development
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
Provides the libraries and header files to develop applications that
use the Lutok C++ API to Lua.

%package -n lib%name-devel-doc
Summary: API documentation of the Lutok library and example programs
Group: Development/Documentation
BuildArch: noarch
Conflicts: lib%name < %version

%description -n lib%name-devel-doc
Provides HTML documentation describing the API of the Lutok library
and a collection of sample source programs to demonstrate the use
of the library.

%package tests
Summary: Run-time tests of the Lutok library
Group: Development/Tools
Requires: lib%name = %EVR

%description tests
This package installs the run-time tests for the Lutok library.
To run this tests use the following command:
$ kyua test -k %pkgtestsdir/Kyuafile

%prep
%setup %{?_disable_snapshot:-n %name-%name-%version}
%patch1 -b .testsdir

%build
%autoreconf
%configure \
    --disable-static \
    %{subst_with doxygen} \
    --docdir=%pkgdocdir \
    --htmldir=%pkgdocdir/html
%nil
%make_build

%check
%make check

%install
%makeinstall_std

%files -n lib%name
%_libdir/lib%name.so.%{sover}*

%files -n lib%name-devel
%_includedir/%name
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc

%files -n lib%name-devel-doc
%pkgdocdir/

%files tests
%pkgtestsdir

%changelog
* Wed Aug 17 2022 Yuri N. Sedunov <aris@altlinux.org> 0.4-alt1
- first build for Sisyphus (0.4-15-g8f8eaef)


