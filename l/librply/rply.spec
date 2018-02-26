%define _name rply

Name: lib%_name
Version: 1.01
Release: alt1

Summary: A library to read and write PLY files
Group: System/Libraries
License: MIT
Url: http://www.tecgraf.puc-rio.br/~diego/professional/%_name/

Source: http://www.tecgraf.puc-rio.br/~diego/professional/%_name/%_name-1.01.tar.gz
Patch: %_name-1.01-cmake_build.patch

BuildRequires: cmake >= 2.6.0 gcc-c++

%description
RPly is a library that lets applications read and write PLY files.
The PLY file format is widely used to store geometric information, such as 3D
models, but is general enough to be useful for other purposes.

RPly is easy to use, well documented, small, free, open-source, ANSI C,
efficient, and well tested. The highlights are:

* A callback mechanism that makes PLY file input straightforward;
* Support for the full range of numeric formats;
* Binary (big and little endian) and text modes are fully supported;
* Input and output are buffered for efficiency;
* Available under the MIT license for added freedom.

%prep
%setup -n %_name-%version
%patch -p1

%build
%cmake -DCMAKE_BUILD_TYPE:STRING="Release" \
	-DCMAKE_VERBOSE_MAKEFILE=ON

pushd BUILD
%make_build

%install
pushd BUILD
%make DESTDIR=%buildroot install

%files
%_libdir/*.so.*
%_bindir/*
%doc LICENSE manual/*

%package devel
Summary: Libraries and headers for rply
Group: Development/C
Requires: %name = %version-%release

%description devel
Rply Library Header Files and Link Libraries

%files devel
%_includedir/%_name/
%_libdir/*.so
%_datadir/%_name/

%changelog
* Mon Sep 05 2011 Yuri N. Sedunov <aris@altlinux.org> 1.01-alt1
- Adapted for Sisyphus

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Mar 21 2010 Mario Ceresa mrceresa@gmail.com rply 1.01-3
- Added CMake modules to detect the package

* Thu Mar 04 2010 Mario Ceresa mrceresa@gmail.com rply 1.01-2
- Fixed problems detected in https://bugzilla.redhat.com/show_bug.cgi?id=570258#c2

* Wed Mar 03 2010 Mario Ceresa mrceresa@gmail.com rply 1.01-1
- Initial RPM Release

