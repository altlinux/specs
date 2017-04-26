Name: libucdn
Version: 0.0
Release: alt1

Summary: UCDN - Unicode Database and Normalization

Url: https://github.com/grigorig/ucdn
License: ISC, PYTHON-LICENSE
Group: Development/C

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: %url.git
Source: %name-%version.tar

BuildRequires: rpm-macros-cmake cmake
# TODO: libcheck-devel

%description
UCDN is a Unicode support library. Currently, it provides access
to basic character properties contained in the Unicode Character
Database and low-level normalization functions (pairwise canonical
composition/decomposition and compatibility decomposition). More
functionality might be provided in the future, such as additional
properties, string normalization and encoding conversion.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
Development files for the %name library.


%prep
%setup
%__subst "s|DESTINATION lib|DESTINATION %_lib|g" CMakeLists.txt

%build
%cmake_insource -DBUILD_SHARED_LIBS=true
%make_build

%install
%makeinstall_std

# TODO: use missed unittest
%check
LD_LIBRARY_PATH=$(pwd) ./ucdn-test 00FE

%files
%doc README
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/ucdn.h


%changelog
* Tue Apr 25 2017 Vitaly Lipatov <lav@altlinux.ru> 0.0-alt1
- initial build for ALT Linux Sisyphus
