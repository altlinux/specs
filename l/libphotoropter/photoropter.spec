Name: libphotoropter
Version: 0.1.0
Release: alt1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Photoropter Lens Correction library
License: MIT/X11
Group: Graphics

Url: http://photoropter.berlios.de/
Source: http://download.berlios.de/photoropter/phtr-%version.tar.gz

# Automatically added by buildreq on Mon Mar 15 2010
BuildRequires: boost-program_options-devel cmake doxygen gcc-c++ graphviz libgomp-devel

# Build without demo application that needs VXL

%description
Photoropter is a C++ library to correct a series of flaws commonly found in
images taken with digital cameras. Comparable in purpose to existing projects
like PTLens and LensFun.

%package devel
Summary: Development tools for programs which will use the %name library
Group: Development/C
Requires: %name = %version-%release

%description devel
Development tools for programs which will use the %name library.

%prep
%setup -n photoropter-%version

%build
# Need to fix 32-bit only thinking of author ;)
subst 's/DESTINATION lib/DESTINATION %_lib/g' CMakeLists.txt

%cmake
pushd BUILD
%make_build VERBOSE=1
popd

%install
pushd BUILD
%makeinstall_std
popd

%files
%_libdir/*.so.*
%exclude %_libdir/*.a

%files devel
%_includedir/*
%_libdir/*.so

%changelog
* Mon Mar 15 2010 Victor Forsiuk <force@altlinux.org> 0.1.0-alt1
- Initial build.
