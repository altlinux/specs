%define libname libopenhmd

Name:    openhmd
Version: 0.3.0
Release: alt1

Summary: Free and Open Source API and drivers for immersive technology
License: BSL-1.0
Group:   System/Configuration/Hardware
Url:     https://github.com/OpenHMD/OpenHMD

Source: %name-%version.tar
# License text based on the comment on top of src/ext_deps/nxjson.c
Source1: LICENSE.miniz
# License text extracted from the comment at the bottom of src/ext_deps/miniz.c
Source2: LICENSE.nxjson

BuildRequires(pre): rpm-macros-meson
BuildRequires: cmake doxygen gcc meson
BuildRequires: libhidapi-devel libSDL2-devel libGLEW-devel

# Vendored under src/ext_deps/miniz.c and included via a header wrapper
# License: Unlicense
Provides: bundled(miniz) = 1.15
# Vendored under src/ext_deps/nxjson.{c,h} and modified
# License: MIT
Provides: bundled(nxjson) = 20180520

%description
OpenHMD aims to provide a Free and Open Source API and drivers for immersive
technology, such as head mounted displays with built in head tracking.


%package -n %libname
Summary: Development headers and libraries for %name
Group:   System/Libraries

%description -n %libname
OpenHMD aims to provide a Free and Open Source API and drivers for immersive
technology, such as head mounted displays with built in head tracking.

%package -n %libname-devel
Summary: Development headers and libraries for %name
Group:   Development/C
Requires: %libname = %EVR

%description -n %libname-devel
This package contains development headers and libraries for %name.

%package doc
Summary: Developer documentation for %name
Group: Development/Documentation
BuildArch: noarch

%description doc
This package contains developer documentation for %name.

%package examples
Summary: Examples for %name
Group: Development/Documentation

%description examples
This package contains examples making use of %name.

%prep
%setup

# Copy license texts for bundled dependencies
cp -p %SOURCE1 %SOURCE2 .

%build
%meson -Dexamples=simple,opengl
%meson_build

# Build documentation
doxygen

%install
%meson_install

%check
%meson_test

%files -n %libname
%doc README.md LICENSE LICENSE.miniz LICENSE.nxjson
%_libdir/%libname.so.0*

%files -n %libname-devel
%_includedir/%name
%_libdir/%libname.so
%_libdir/pkgconfig/%name.pc

%files doc
%doc html LICENSE

%files examples
%_bindir/openhmd_simple_example
%_bindir/openhmd_opengl_example

%changelog
* Tue Jan 14 2025 Sergey Palcheh <minergenon@altlinux.org> 0.3.0-alt1
- initial build for ALT Sisyphus

