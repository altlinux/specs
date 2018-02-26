Name: fi_lib
Version: 1.2
Release: alt4
Summary: A fast interval library
License: LGPL v2.0 or later
Group: Sciences/Mathematics
Url: http://www2.math.uni-wuppertal.de/~xsc/software/filib.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar.gz

BuildPreReq: gcc-c++

%description
The main features of the library, called fi_lib  (fast interval library)
are:

* Fast table look-up algorithms are used for the basic functions like
  arctan, exp or log
* All elementary function routines are supplied with reliable relative
  error bounds of high quality. The error estimates cover rounding
  errors, errors introduced by not exactly representable constants as
  well as approximation errors (best approximations with reliable error
  bounds).
* All error estimates are reliable worst-case estimates, which have been
  derived using interval methods.
* We only insist in a faithful computer arithmetic. The routines do not
  manipulate the rounding mode of basic operations (setting the rounding
  mode may be rather expensive).
* No higher precision internal data format is used. All computations are
  done using the IEEE-double format (64 bit).
* A C++ interface for easier use is also supplied with the library.
* To get good portability all programs are written in ANSI-C.

%package -n lib%name
Summary: Shared libraries of fi_lib, a fast interval library
Group: System/Libraries

%description -n lib%name
The main features of the library, called fi_lib  (fast interval library)
are:

* Fast table look-up algorithms are used for the basic functions like
  arctan, exp or log
* All elementary function routines are supplied with reliable relative
  error bounds of high quality. The error estimates cover rounding
  errors, errors introduced by not exactly representable constants as
  well as approximation errors (best approximations with reliable error
  bounds).
* All error estimates are reliable worst-case estimates, which have been
  derived using interval methods.
* We only insist in a faithful computer arithmetic. The routines do not
  manipulate the rounding mode of basic operations (setting the rounding
  mode may be rather expensive).
* No higher precision internal data format is used. All computations are
  done using the IEEE-double format (64 bit).
* A C++ interface for easier use is also supplied with the library.
* To get good portability all programs are written in ANSI-C.

This package contains shared libraries of fi_lib.

%package -n lib%name-devel
Summary: Development files of fi_lib, a fast interval library
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
The main features of the library, called fi_lib  (fast interval library)
are:

* Fast table look-up algorithms are used for the basic functions like
  arctan, exp or log
* All elementary function routines are supplied with reliable relative
  error bounds of high quality. The error estimates cover rounding
  errors, errors introduced by not exactly representable constants as
  well as approximation errors (best approximations with reliable error
  bounds).
* All error estimates are reliable worst-case estimates, which have been
  derived using interval methods.
* We only insist in a faithful computer arithmetic. The routines do not
  manipulate the rounding mode of basic operations (setting the rounding
  mode may be rather expensive).
* No higher precision internal data format is used. All computations are
  done using the IEEE-double format (64 bit).
* A C++ interface for easier use is also supplied with the library.
* To get good portability all programs are written in ANSI-C.

This package contains development files of fi_lib.

%package examples
Summary: Examples for fi_lib, a fast interval library
Group: Sciences/Mathematics
Requires: lib%name = %version-%release

%description examples
The main features of the library, called fi_lib  (fast interval library)
are:

* Fast table look-up algorithms are used for the basic functions like
  arctan, exp or log
* All elementary function routines are supplied with reliable relative
  error bounds of high quality. The error estimates cover rounding
  errors, errors introduced by not exactly representable constants as
  well as approximation errors (best approximations with reliable error
  bounds).
* All error estimates are reliable worst-case estimates, which have been
  derived using interval methods.
* We only insist in a faithful computer arithmetic. The routines do not
  manipulate the rounding mode of basic operations (setting the rounding
  mode may be rather expensive).
* No higher precision internal data format is used. All computations are
  done using the IEEE-double format (64 bit).
* A C++ interface for easier use is also supplied with the library.
* To get good portability all programs are written in ANSI-C.

This package contains examples for fi_lib.

%prep
%setup

%build
%make_build all

%install
%makeinstall_std LIBDIR=%_libdir

%check
export LD_LIBRARY_PATH=$PWD
echo 1|test/fi_test

%files -n lib%name
%doc README
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%files examples
%doc example/*.c example/*.hpp
%_bindir/*

%changelog
* Wed Mar 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt4
- Added -g into compiler flags

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt3
- Rebuilt for debuginfo

* Tue Oct 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2
- Rebuilt for soname set-versions

* Fri Sep 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1
- Initial build for Sisyphus

