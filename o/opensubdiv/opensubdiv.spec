%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define soname 3.4.4

Name: opensubdiv
Version: %soname
Release: alt2
Summary: An Open-Source subdivision surface library
Group: Development/Other
License: Apache-2.0
URL: https://graphics.pixar.com/opensubdiv/

# https://github.com/PixarAnimationStudios/OpenSubdiv.git
Source: %name-%version.tar

Patch1: opensubdiv-alt-no-static-libraries.patch
Patch2: opensubdiv-alt-tutorials-install.patch

# https://github.com/PixarAnimationStudios/OpenSubdiv/pull/1234
Patch3: opensubdiv-upstream-tbb-support.patch

BuildRequires: cmake gcc-c++
BuildRequires: tbb-devel
BuildRequires: libgomp-devel
# examples
BuildRequires: libglfw3-devel libXrandr-devel libXxf86vm-devel libXcursor-devel libXinerama-devel libXi-devel

%description
OpenSubdiv is a set of open source libraries that implement
high performance subdivision surface (subdiv) evaluation
on massively parallel CPU and GPU architectures.
This codepath is optimized for drawing deforming subdivs
with static topology at interactive framerates.
The resulting limit surface matches Pixar's Renderman to numerical precision.

OpenSubdiv is covered by the Apache license,
and is free to use for commercial or non-commercial use.
This is the same code that Pixar uses internally for animated film production.
Our intent is to encourage high performance accurate subdiv drawing
by giving away the "good stuff".

Feel free to use it and let us know what you think.

%package -n lib%name%soname
Summary: An Open-Source subdivision surface library
Group: System/Libraries

%description -n lib%name%soname
OpenSubdiv is a set of open source libraries that implement
high performance subdivision surface (subdiv) evaluation
on massively parallel CPU and GPU architectures.
This codepath is optimized for drawing deforming subdivs
with static topology at interactive framerates.
The resulting limit surface matches Pixar's Renderman to numerical precision.

OpenSubdiv is covered by the Apache license,
and is free to use for commercial or non-commercial use.
This is the same code that Pixar uses internally for animated film production.
Our intent is to encourage high performance accurate subdiv drawing
by giving away the "good stuff".

Feel free to use it and let us know what you think.

%package devel
Summary: An Open-Source subdivision surface library
Group: Development/C++
Requires: %name = %EVR
Requires: lib%name%soname = %EVR

%description devel
OpenSubdiv is a set of open source libraries that implement
high performance subdivision surface (subdiv) evaluation
on massively parallel CPU and GPU architectures.
This codepath is optimized for drawing deforming subdivs
with static topology at interactive framerates.
The resulting limit surface matches Pixar's Renderman to numerical precision.

OpenSubdiv is covered by the Apache license,
and is free to use for commercial or non-commercial use.
This is the same code that Pixar uses internally for animated film production.
Our intent is to encourage high performance accurate subdiv drawing
by giving away the "good stuff".

Feel free to use it and let us know what you think.

This package contains development files for OpenSubdiv.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%add_optflags -D_FILE_OFFSET_BITS=64

%cmake \
	-DPYTHON_EXECUTABLE=%_bindir/python3 \
	-DCMAKE_LIBDIR_BASE=%_lib \
	-DCMAKE_TUTORIAL_BASE=%_lib/%name \
	%nil

%cmake_build

%install
%cmake_install

%files
%_bindir/*
%dir %_libdir/%name
%_libdir/%name/tutorials

%files -n lib%name%soname
%doc LICENSE.txt
%doc NOTICE.txt README.md
%_libdir/*.so.%{soname}

%files devel
%_libdir/*.so
%_includedir/*

%changelog
* Thu Jan 27 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 3.4.4-alt2
- Rebuilt with new TBB.

* Fri Jun 04 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 3.4.4-alt1
- Initial build for ALT.
