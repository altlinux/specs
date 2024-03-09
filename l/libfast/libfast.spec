%define        _unpackaged_files_terminate_build 1
%define        cname Fast
%define        oname fast

Name:          lib%{oname}
Version:       2.1.1
Release:       alt1
Summary:       FAST corner detectors
License:       BSD-3-Clause
Group:         System/Libraries
Url:           https://github.com/edrosten/fast-C-src
Vcs:           https://github.com/edrosten/fast-C-src.git

Source:        %name-%version.tar
Patch:         %name-%EVR.patch
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++

%description
C source code for FAST corner detectors.

The files are valid C and C++ code, and have no special requirements for
compiling, and they do not depend on any libraries. Just compile them along with
the rest of your project.

To use the functions, #include "fast.h"

The corner detectors have the following prototype (where X is 9, 10, 11 or 12):

The image is passed in as a block of data and dimensions, and the list of
corners is returned as an array of xy structs, and an integer (numcorners)
with the number of corners returned.  The data can be deallocated with free().
Nonmaximal suppression is performed on the corners. Note that the stride
is the number of bytes between rows. If your image has no padding, then this
is the same as xsize.

The detection, scoring and nonmaximal suppression are available as individual
functions.  To see how to use the individual functions, see fast.c


%package       -n %name-devel
Summary:       FAST corner detectors library development files
Group:         Development/Other
Requires:      %name = %version-%release

Requires:      cmake

%description   -n %name-devel
FAST corner detectors library development files.

The files are valid C and C++ code, and have no special requirements for
compiling, and they do not depend on any libraries. Just compile them along with
the rest of your project.

To use the functions, #include "fast.h"

The corner detectors have the following prototype (where X is 9, 10, 11 or 12):

The image is passed in as a block of data and dimensions, and the list of
corners is returned as an array of xy structs, and an integer (numcorners)
with the number of corners returned.  The data can be deallocated with free().
Nonmaximal suppression is performed on the corners. Note that the stride
is the number of bytes between rows. If your image has no padding, then this
is the same as xsize.

The detection, scoring and nonmaximal suppression are available as individual
functions.  To see how to use the individual functions, see fast.c


%package       -n %name-devel-static
Summary:       FAST corner detectors library development static files
Group:         Development/Other
Requires:      %name = %version-%release

Requires:      %name-devel = %EVR

%description   -n %name-devel-static
FAST corner detectors library development static files.

The files are valid C and C++ code, and have no special requirements for
compiling, and they do not depend on any libraries. Just compile them along with
the rest of your project.

To use the functions, #include "fast.h"

The corner detectors have the following prototype (where X is 9, 10, 11 or 12):

The image is passed in as a block of data and dimensions, and the list of
corners is returned as an array of xy structs, and an integer (numcorners)
with the number of corners returned.  The data can be deallocated with free().
Nonmaximal suppression is performed on the corners. Note that the stride
is the number of bytes between rows. If your image has no padding, then this
is the same as xsize.

The detection, scoring and nonmaximal suppression are available as individual
functions.  To see how to use the individual functions, see fast.c


%prep
%setup
%autopatch -p1

%build
%cmake_insource
%cmake_build

%install
%cmakeinstall_std

%files
%doc README LICENSE CHANGES
%_libdir/lib%{oname}*.so.*

%files         -n %name-devel
%doc README LICENSE CHANGES
%_libdir/lib%{oname}*.so
%_includedir/%oname.h
%_cmakedir/%{cname}
%_datadir/cmake/Modules/%{oname}*.cmake

%files         -n %name-devel-static
%doc README LICENSE CHANGES
%_libdir/lib%{oname}*.a

%changelog
* Fri Mar 08 2024 Pavel Skrylev <majioa@altlinux.org> 2.1.1-alt1
- Initial build v2.1.1 for Sisyphus
