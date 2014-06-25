Name: lz4
Version: r117
Release: alt1.svn20140422
Summary: Extremely Fast Compression algorithm
License: BSD
Group: Archiving/Compression
Url: https://code.google.com/p/lz4/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://lz4.googlecode.com/svn/trunk/
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-make

Requires: lib%name = %EVR

%description
LZ4 is a very fast lossless compression algorithm, providing compression
speed at 400 MB/s per core, scalable with multi-cores CPU. It also
features an extremely fast decoder, with speed in multiple GB/s per
core, typically reaching RAM speed limits on multi-core systems.

A high compression derivative, called LZ4_HC, is also provided. It
trades CPU time for compression ratio.

%package -n lib%name
Summary: Shared libraries of LZ4
Group: System/Libraries

%description -n lib%name
LZ4 is a very fast lossless compression algorithm, providing compression
speed at 400 MB/s per core, scalable with multi-cores CPU. It also
features an extremely fast decoder, with speed in multiple GB/s per
core, typically reaching RAM speed limits on multi-core systems.

A high compression derivative, called LZ4_HC, is also provided. It
trades CPU time for compression ratio.

This package contains shared libraries of LZ4.

%package -n lib%name-devel
Summary: Development files of LZ4
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
LZ4 is a very fast lossless compression algorithm, providing compression
speed at 400 MB/s per core, scalable with multi-cores CPU. It also
features an extremely fast decoder, with speed in multiple GB/s per
core, typically reaching RAM speed limits on multi-core systems.

A high compression derivative, called LZ4_HC, is also provided. It
trades CPU time for compression ratio.

This package contains development files of LZ4.

%prep
%setup

%build
%make_build_ext

%install
%ifarch x86_64
LIB_SUFFIX=64
%endif
%makeinstall_std LIB_SUFFIX=$LIB_SUFFIX

%files
%doc NEWS README.md
%_bindir/*
%_man1dir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Wed Jun 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r117-alt1.svn20140422
- Initial build for Sisyphus

