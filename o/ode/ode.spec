%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: ode
Version: 0.16.5
Release: alt1
Summary: The Open Dynamics Engine (ODE)
License: LGPLv2.1+
Group: Graphics
Url: http://www.ode.org/

# https://bitbucket.org/odedevs/ode.git
Source: %name-%version.tar
# http://www.ode.org/ode-latest-userguide.pdf
Source1: ode-latest-userguide.pdf
# http://www.ode.org/joints.pdf
Source2: joints.pdf

BuildRequires: gcc-c++ libX11-devel libICE-devel libGL-devel libGLU-devel
BuildRequires: libSM-devel libgmp-devel

%description
ODE is an open source, high performance library for simulating rigid
body dynamics. It is fully featured, stable, mature and platform
independent with an easy to use C/C++ API. It has advanced joint types
and integrated collision detection with friction. ODE is useful for
simulating vehicles, objects in virtual reality environments and virtual
creatures. It is currently used in many computer games, 3D authoring
tools and simulation tools.

%package -n lib%name
Summary: Shared libraries of The Open Dynamics Engine (ODE)
Group: System/Libraries

%description -n lib%name
ODE is an open source, high performance library for simulating rigid
body dynamics. It is fully featured, stable, mature and platform
independent with an easy to use C/C++ API. It has advanced joint types
and integrated collision detection with friction. ODE is useful for
simulating vehicles, objects in virtual reality environments and virtual
creatures. It is currently used in many computer games, 3D authoring
tools and simulation tools.

This package contains shared libraries of ODE.

%package -n lib%name-devel
Summary: Development files of The Open Dynamics Engine (ODE)
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
ODE is an open source, high performance library for simulating rigid
body dynamics. It is fully featured, stable, mature and platform
independent with an easy to use C/C++ API. It has advanced joint types
and integrated collision detection with friction. ODE is useful for
simulating vehicles, objects in virtual reality environments and virtual
creatures. It is currently used in many computer games, 3D authoring
tools and simulation tools.

This package contains development files of ODE.

%package -n lib%name-devel-doc
Summary: Documentation for The Open Dynamics Engine (ODE)
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
ODE is an open source, high performance library for simulating rigid
body dynamics. It is fully featured, stable, mature and platform
independent with an easy to use C/C++ API. It has advanced joint types
and integrated collision detection with friction. ODE is useful for
simulating vehicles, objects in virtual reality environments and virtual
creatures. It is currently used in many computer games, 3D authoring
tools and simulation tools.

This package contains development documentation for ODE.

%package demos
Summary: Demos of The Open Dynamics Engine (ODE)
Group: Graphics
Requires: lib%name = %EVR

%description demos
ODE is an open source, high performance library for simulating rigid
body dynamics. It is fully featured, stable, mature and platform
independent with an easy to use C/C++ API. It has advanced joint types
and integrated collision detection with friction. ODE is useful for
simulating vehicles, objects in virtual reality environments and virtual
creatures. It is currently used in many computer games, 3D authoring
tools and simulation tools.

This package contains demos of ODE.

%prep
%setup
# the code is a trashfire with a whitelist of 64-bit architectures
# there are a dozen ways to detect pointer size portably!
# there is a whitelist that selects a portable way using <stdint.h>
sed -i 's/defined(__aarch64__)/1/' include/ode/odeconfig.h

touch libccd/NEWS libccd/AUTHORS libccd/ChangeLog

%build
%add_optflags -D_FILE_OFFSET_BITS=64

./bootstrap
#autoreconf
%add_optflags -fno-strict-aliasing
%ifarch %e2k
# -std=c++03 by default as of lcc 1.23.12
%add_optflags -std=c++11
%endif
%configure \
	--enable-shared \
	--disable-static \
	--enable-double-precision \
	--disable-asserts \
	--disable-threading-intf \
	--enable-builtin-threading-impl \
	--enable-ou \
	--with-drawstuff=X11 \
	--with-x \
	--enable-libccd \
	--with-cylinder-cylinder=libccd \
	--with-capsule-cylinder=libccd \
	--with-convex-box=libccd \
	--with-convex-capsule=libccd \
	--with-convex-cylinder=libccd \
	%nil

%make_build -C ou/src/ou
%make_build

%install
%makeinstall_std

# demos
install -d %buildroot%_libdir/%name
cp -fR drawstuff %buildroot%_libdir/%name/

pushd %buildroot%_libdir/%name
rm -f $(find ./ -name 'Makefile.*') \
	$(find ./ -name '*.o') \
	$(find ./ -name '*.a') \
	$(find ./ -name '*.lo') \
	$(find ./ -name '*.la')
popd

# docs
install -d %buildroot%_docdir/lib%name-devel
install -p -m644 %SOURCE1 %SOURCE2 \
	%buildroot%_docdir/lib%name-devel

%files -n lib%name
%doc CHANGELOG.txt LICENSE* README.md
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_bindir/*
%_pkgconfigdir/*

%files -n lib%name-devel-doc
%_docdir/lib%name-devel/*

%files demos
%_libdir/%name/

%changelog
* Thu Apr 25 2024 Andrey Cherepanov <cas@altlinux.org> 0.16.5-alt1
- New version.

* Wed Sep 27 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 0.16.2-alt3
- LoongArch patch removed.
- Build fix that should work for any architectures.

* Mon Sep 25 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.16.2-alt2
- NMU: fixed FTBFS on LoongArch.

* Tue Mar 01 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 0.16.2-alt1
- Updated to upstream version 0.16.2.

* Wed Jun 19 2019 Michael Shigorin <mike@altlinux.org> 0.13.1-alt3.hg20140702
- E2K: explicit -std=c++11

* Wed May 23 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.13.1-alt2.hg20140702
- Fixed build with new toolchain.

* Mon Jul 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.1-alt1.hg20140702
- Version 0.13.1

* Thu Jun 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13-alt1.svn20140203
- Version 0.13

* Fri Nov 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12-alt3.svn20130810
- New snapshot

* Fri Jul 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12-alt3.svn20130306
- New snapshot

* Tue Apr 09 2013 Dmitry V. Levin <ldv@altlinux.org> 0.12-alt3.svn20130203
- Fixed build (removed useless attempts to link with -lmp).

* Wed Feb 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12-alt2.svn20130203
- New snapshot

* Mon May 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12-alt2.svn20120225
- Fixed build

* Thu Mar 01 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12-alt1.svn20120225
- Version 0.12

* Fri Dec 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.1-alt1.svn20111207
- New snapshot

* Thu May 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.1-alt1.svn20110420
- New snapshot

* Fri Feb 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.1-alt1.svn20101006.1
- Rebuilt for debuginfo

* Wed Oct 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.1-alt1.svn20101006
- New snapshot

* Thu Jul 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.1-alt1.20100626
- New snapshot

* Thu Jan 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.1-alt1
- Initial build for Sisyphus

