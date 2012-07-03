Name: hwloc
Version: 1.4
Release: alt1
Summary: Portable Hardware Locality (hwloc)
License: BSD
Group: Development/Tools
Url: http://www.open-mpi.org/projects/hwloc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: libxml2-devel libX11-devel libcairo-devel
BuildPreReq: libpci-devel libncurses-devel xml-utils

Requires: lib%name = %version-%release

%description
The Portable Hardware Locality (hwloc) software package provides a
portable abstraction (across OS, versions, architectures, ...) of the
hierarchical topology of modern architectures, including NUMA memory
nodes, sockets, shared caches, cores and simultaneous multithreading. It
also gathers various system attributes such as cache and memory
information as well as the locality of I/O devices such as network
interfaces, InfiniBand HCAs or GPUs. It primarily aims at helping
applications with gathering information about modern computing hardware
so as to exploit it accordingly and efficiently.

%package -n lib%name
Summary: Shared libraries of the Portable Hardware Locality (hwloc)
Group: System/Libraries

%description -n lib%name
The Portable Hardware Locality (hwloc) software package provides a
portable abstraction (across OS, versions, architectures, ...) of the
hierarchical topology of modern architectures, including NUMA memory
nodes, sockets, shared caches, cores and simultaneous multithreading. It
also gathers various system attributes such as cache and memory
information as well as the locality of I/O devices such as network
interfaces, InfiniBand HCAs or GPUs. It primarily aims at helping
applications with gathering information about modern computing hardware
so as to exploit it accordingly and efficiently.

This package contains shared libraries of hwloc.

%package -n lib%name-devel
Summary: Development files of the Portable Hardware Locality (hwloc)
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
The Portable Hardware Locality (hwloc) software package provides a
portable abstraction (across OS, versions, architectures, ...) of the
hierarchical topology of modern architectures, including NUMA memory
nodes, sockets, shared caches, cores and simultaneous multithreading. It
also gathers various system attributes such as cache and memory
information as well as the locality of I/O devices such as network
interfaces, InfiniBand HCAs or GPUs. It primarily aims at helping
applications with gathering information about modern computing hardware
so as to exploit it accordingly and efficiently.

This package contains development files of hwloc.

%package docs
Summary: Documentation for the Portable Hardware Locality (hwloc)
Group: Documentation
BuildArch: noarch

%description docs
The Portable Hardware Locality (hwloc) software package provides a
portable abstraction (across OS, versions, architectures, ...) of the
hierarchical topology of modern architectures, including NUMA memory
nodes, sockets, shared caches, cores and simultaneous multithreading. It
also gathers various system attributes such as cache and memory
information as well as the locality of I/O devices such as network
interfaces, InfiniBand HCAs or GPUs. It primarily aims at helping
applications with gathering information about modern computing hardware
so as to exploit it accordingly and efficiently.

This package contains documentation for hwloc.

%prep
%setup

%build
%autoreconf
%configure \
	--with-sysroot=%prefix \
	--with-x \
	--enable-doxygen \
	--disable-silent-rules

%make_build

%install
%makeinstall_std

%files
%doc AUTHORS COPYING NEWS README
%_bindir/*
%_datadir/%name
%_man1dir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
%_man3dir/*
%_man7dir/*

%files docs
%doc %_docdir/%name
%doc doc/doxygen-doc/html

%changelog
* Fri Feb 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1
- Version 1.4

* Wed Dec 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1
- Initial build for Sisyphus

