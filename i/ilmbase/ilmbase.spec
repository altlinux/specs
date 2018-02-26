%define _optlevel s
%define beta %nil
%define libsover 6
%define rname IlmBase

Name: ilmbase
Version: 1.0.1
Release: alt6

Group: System/Libraries
Summary: A high-dynamic-range image file library
License: Modified BSD
URL: http://www.openexr.org/

Requires: libhalf%libsover = %version-%release
Requires: libiex%libsover = %version-%release
Requires: libilmthread%libsover = %version-%release
Requires: libimath%libsover = %version-%release
Provides: %rname = %version-%release
Obsoletes: %rname < %version-%release

Source: %name-%version%beta.tar
Patch1: ilmbase-1.0.1-alt-fix-linking.patch

# Automatically added by buildreq on Wed Apr 20 2011 (-bi)
# optimized out: elfutils libGL-devel libstdc++-devel pkg-config
#BuildRequires: gcc-c++ glibc-devel libGLU-devel libstdc++-devel
BuildRequires: gcc-c++ glibc-devel libGLU-devel zlib-devel

%description
Half is a class that encapsulates our 16-bit floating-point format.

IlmThread is a thread abstraction library for use with OpenEXR
and other software packages.  It currently supports pthreads and
Windows threads.

Imath implements 2D and 3D vectors, 3x3 and 4x4 matrices, quaternions
and other useful 2D and 3D math functions.

Iex is an exception-handling library.

%package -n %name%libsover-common
Group: System/Configuration/Other
Summary: Common empty package for %name
%description -n %name%libsover-common
Common empty package for %name

%package -n libhalf%libsover
Group: System/Libraries
Summary: %rname library
Requires: %name%libsover-common = %version-%release
Conflicts: ilmbase <= 1.0.1-alt1
%description -n libhalf%libsover
Half is a class that encapsulates our 16-bit floating-point format.

%package -n libiex%libsover
Group: System/Libraries
Summary: %rname library
Requires: %name%libsover-common = %version-%release
Conflicts: ilmbase <= 1.0.1-alt1
%description -n libiex%libsover
Iex is an exception-handling library.

%package -n libilmthread%libsover
Group: System/Libraries
Summary: %rname library
Requires: %name%libsover-common = %version-%release
Conflicts: ilmbase <= 1.0.1-alt1
%description -n libilmthread%libsover
IlmThread is a thread abstraction library for use with OpenEXR
and other software packages.  It currently supports pthreads and
Windows threads.

%package -n libimath%libsover
Group: System/Libraries
Summary: %rname library
Requires: %name%libsover-common = %version-%release
Conflicts: ilmbase <= 1.0.1-alt1
%description -n libimath%libsover
Imath implements 2D and 3D vectors, 3x3 and 4x4 matrices, quaternions
and other useful 2D and 3D math functions.

%package devel
Summary: Headers for developing programs that will use %name
Group: Development/Other
Requires: %name%libsover-common = %version-%release
Conflicts: openexr-devel < 1.6
%description devel
This package contains the static libraries and header files needed for
developing applications with %name


%prep
%setup -q -n %name-%version
%patch1 -p1

#autoreconf
./bootstrap ||:


%build
%configure \
  --enable-shared \
  --disable-static \
  --enable-dependency-tracking \
  --enable-threading

%make_build


%install
%make DESTDIR=%buildroot install



%files -n %name%libsover-common

%files
%doc AUTHORS ChangeLog COPYING LICENSE NEWS README

%files -n libhalf%libsover
%_libdir/libHalf.so.*

%files -n libiex%libsover
%_libdir/libIex.so.*

%files -n libilmthread%libsover
%_libdir/libIlmThread.so.*

%files -n libimath%libsover
%_libdir/libImath.so.*

%files devel
%doc AUTHORS ChangeLog COPYING LICENSE NEWS README
%_includedir/OpenEXR
%_libdir/*.so
%_libdir/pkgconfig/*


%changelog
* Wed Apr 20 2011 Sergey V Turchin <zerg@altlinux.org> 1.0.1-alt6
- fix build requires

* Mon Oct 25 2010 Sergey V Turchin <zerg@altlinux.org> 1.0.1-alt5
- fix build requires

* Thu Jul 23 2009 Sergey V Turchin <zerg@altlinux.org> 1.0.1-alt4
- remove obsoleted macroses

* Fri Aug 22 2008 Sergey V Turchin <zerg at altlinux dot org> 1.0.1-alt3
- fix to package common subpackage

* Fri Aug 22 2008 Sergey V Turchin <zerg at altlinux dot org> 1.0.1-alt2
- split lib* subpackages

* Fri Feb 22 2008 Sergey V Turchin <zerg at altlinux dot org> 1.0.1-alt1
- initial specfile

