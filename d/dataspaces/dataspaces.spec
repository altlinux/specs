%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

#set_autoconf_version 2.13
%define sover 0

Name: dataspaces
Version: 1.6.0
Release: alt1
Summary: An Extreme-Scale Data Management Framework
License: BSD
Group: Networking/Other
Url: http://dataspaces.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: %mpiimpl-devel

Requires: lib%name = %EVR

%description
DataSpaces is a programming system targeted at current large-scale
systems and designed to support dynamic interaction and coordination
patterns between scientific applications. DataSpaces essentially
provides a semantically specialized shared-space abstraction using a set
of staging nodes. This abstraction derives from the tuple-space model
and can be associatively accessed by the interacting applications of a
simulation workflow. DataSpaces also provides services including
distributed in-memory associative object store, scalable messaging, as
well as runtime mapping and scheduling of online data analysis
operations.

%package -n lib%name
Summary: Shared libraries of %name
Group: System/Libraries

%description -n lib%name
DataSpaces is a programming system targeted at current large-scale
systems and designed to support dynamic interaction and coordination
patterns between scientific applications. DataSpaces essentially
provides a semantically specialized shared-space abstraction using a set
of staging nodes. This abstraction derives from the tuple-space model
and can be associatively accessed by the interacting applications of a
simulation workflow. DataSpaces also provides services including
distributed in-memory associative object store, scalable messaging, as
well as runtime mapping and scheduling of online data analysis
operations.

This package contains shared libraries of %name.

%package -n lib%name-devel
Summary: Development files of %name
Group: Development/Other
Requires: lib%name = %EVR

%description -n lib%name-devel
DataSpaces is a programming system targeted at current large-scale
systems and designed to support dynamic interaction and coordination
patterns between scientific applications. DataSpaces essentially
provides a semantically specialized shared-space abstraction using a set
of staging nodes. This abstraction derives from the tuple-space model
and can be associatively accessed by the interacting applications of a
simulation workflow. DataSpaces also provides services including
distributed in-memory associative object store, scalable messaging, as
well as runtime mapping and scheduling of online data analysis
operations.

This package contains development files of %name.

%prep
%setup

%build
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"

%add_optflags %optflags_shared
%autoreconf
%configure \
	--enable-dimes \
	 CC=mpicc FC=mpif90
%make_build || %make_build

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath=%mpidir/lib -L%mpidir/lib"

%makeinstall_std

pushd %buildroot%_libdir
LIBS="-libverbs -lrdmacm"
for i in dscommon dart dspaces dspacesf; do
	mpif90 -shared -Wl,--whole-archive lib$i.a -Wl,--no-whole-archive \
		-o lib$i.so.%sover -Wl,-soname=lib$i.so.%sover -L. $LIBS
	ln -s lib$i.so.%sover lib$i.so
	LIBS="$LIBS -l$i"
done
popd

%files
%doc AUTHORS ChangeLog COPYING CREDITS KNOWN_BUGS NEWS README RELEASE_VERSIONS
%_bindir/*
%exclude %_bindir/test*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%doc examples
%_bindir/test*
%_includedir/*
%_libdir/*.so

%changelog
* Thu Jul 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt1
- Version 1.6.0

* Thu Mar 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1
- Initial build for Sisyphus

