%define lname libcjson

Name: cjson
Version: 1.7.16
Release: alt0.1

Summary: Ultralightweight JSON parser in ANSI C 

License: MIT
Group: Development/C
Url: https://github.com/DaveGamble/cJSON

Packager: Pavel Vainerman <pv@altlinux.ru>

# Source-url: https://github.com/DaveGamble/cJSON/archive/v%{version}.tar.gz
Source: %name-%version.tar

# Automatically added by buildreq on Fri Jul 07 2023
# optimized out: cmake-modules libgpg-error libsasl2-3 python-modules python2-base python3 python3-base python3-dev python3-module-paste sh4 tzdata
BuildRequires: cmake gcc ctest

Requires: %lname = %version-%release

%description
Ultralightweight JSON parser in ANSI C 

%package -n %lname
Group: Development/C
Summary: Ultralightweight JSON parser in ANSI C

%description -n %lname
Ultralightweight JSON parser in ANSI C 

%package -n %lname-devel
Group: Development/C
Summary: Libraries needed to develop for cjson
Requires: %lname = %version-%release
Obsoletes: %name-devel

%description -n %lname-devel
Libraries needed to develop for cjson

%prep
%setup 

%build
%cmake -DBUILD_SHARED_LIBS=ON -DCMAKE_SKIP_RPATH:BOOL=ON -DENABLE_CJSON_TEST=ON
%cmake_build

%install
%cmake_install

%check
cd %_cmake__builddir
export LD_LIBRARY_PATH=$PWD
ctest -V

%files -n %lname
%_libdir/*.so.*

%files -n %lname-devel
%_includedir/%name/*.h
%_libdir/*.so
%_libdir/cmake/cJSON/*
%_libdir/pkgconfig/*.pc

%changelog
* Fri Jul 07 2023 Pavel Vainerman <pv@altlinux.ru> 1.7.16-alt0.1
- new version (1.7.16) with rpmgs script
