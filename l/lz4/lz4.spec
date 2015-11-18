%define sover 1
%def_enable static

Name: lz4
Version: r131
Release: alt1
Summary: Extremely Fast Compression algorithm
License: BSD
Group: Archiving/Compression
Url: http://www.lz4.org

# https://github.com/Cyan4973/lz4
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

%package -n lib%name-devel-static
Summary: Development files of LZ4
Group: Development/C
Requires: lib%name-devel = %EVR

%description -n lib%name-devel-static
LZ4 is a very fast lossless compression algorithm, providing compression
speed at 400 MB/s per core, scalable with multi-cores CPU. It also
features an extremely fast decoder, with speed in multiple GB/s per
core, typically reaching RAM speed limits on multi-core systems.

A high compression derivative, called LZ4_HC, is also provided. It
trades CPU time for compression ratio.

This package contains static library files of LZ4.

%prep
%setup

%build
%make_build_ext lib
%make_build_ext

%install
%ifarch x86_64
LIB_SUFFIX=64
%endif
%makeinstall_std LIBDIR=%_libdir PREFIX=%_prefix

# Relocate shared libraries from %_libdir/ to /lib/.
mkdir -p %buildroot/%_lib
for f in %buildroot%_libdir/*.so; do
	t=$(readlink "$f") || continue
	ln -snf ../../%_lib/"$t" "$f"
done
mv %buildroot%_libdir/*.so.* %buildroot/%_lib/

%files
%doc NEWS README.md
%_bindir/*
%_man1dir/*

%files -n lib%name
/%_lib/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%else
%exclude %_libdir/*.a
%endif

%changelog
* Wed Nov 18 2015 Alexey Shabalin <shaba@altlinux.ru> r131-alt1
- r131

* Tue Jan 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r127-alt1.svn20141224
- New snapshot
- Moved libraries from %_libdir into /%_lib (ALT #30628)

* Mon Jul 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r119-alt1.svn20140702
- New snapshot

* Wed Jun 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r117-alt1.svn20140422
- Initial build for Sisyphus

