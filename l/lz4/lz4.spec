Name: lz4
Epoch: 1
Version: 1.7.5
Release: alt1
Summary: Fast LZ compression algorithm library and tools
License: GPLv2+ and BSD
Group: Archiving/Compression
Url: https://lz4.github.io/lz4/
# https://github.com/lz4/lz4
# git://git.altlinux.org/gears/l/lz4.git
Source: %name-%version-%release.tar
Requires: lib%name = %EVR
%def_disable static
%define BUILD_STATIC %{?_enable_static:yes}%{?_disable_static:no}

%description
LZ4 is a very fast lossless compression algorithm, providing compression
speed at 400 MB/s per core, scalable with multi-cores CPU.  It also
features an extremely fast decoder, with speed in multiple GB/s per
core, typically reaching RAM speed limits on multi-core systems.

%package -n lib%name
Summary: Fast LZ compression algorithm shared library
License: BSD
Group: System/Libraries

%description -n lib%name
LZ4 is a very fast lossless compression algorithm, providing compression
speed at 400 MB/s per core, scalable with multi-cores CPU.  It also
features an extremely fast decoder, with speed in multiple GB/s per
core, typically reaching RAM speed limits on multi-core systems.

This package contains lib%name shared library.

%package -n lib%name-devel
Summary: Fast LZ compression algorithm development files
License: BSD
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
LZ4 is a very fast lossless compression algorithm, providing compression
speed at 400 MB/s per core, scalable with multi-cores CPU.  It also
features an extremely fast decoder, with speed in multiple GB/s per
core, typically reaching RAM speed limits on multi-core systems.

This package contains development files required to build applications
using lib%name library.

%package -n lib%name-devel-static
Summary: Fast LZ compression algorithm static library
License: BSD
Group: Development/C
Requires: lib%name-devel = %EVR

%description -n lib%name-devel-static
LZ4 is a very fast lossless compression algorithm, providing compression
speed at 400 MB/s per core, scalable with multi-cores CPU.  It also
features an extremely fast decoder, with speed in multiple GB/s per
core, typically reaching RAM speed limits on multi-core systems.

This package contains lib%name static library required to build
statically linked applications using lib%name library.

%prep
%setup -n %name-%version-%release
# reenable recipe echoing
sed -i 's/^\([[:space:]]*\)@\$/\1\$/' */Makefile
# ensure that lz4.1 is recognized by file as a troff input
sed -i '1 i.\\"' programs/lz4.1
# skip recompilation attempts during check
sed -i '/ clean \$@ / s/^\([[:space:]]*\)\(.*\)/\1: SKIP: \2/' tests/Makefile
# export deprecated symbols
sed -i 's/^LZ4_DEPRECATED/LZ4LIB_API &/' lib/lz4.h lib/lz4hc.h

%build
export CFLAGS='%optflags -fvisibility=hidden'
%make_build all -C lib BUILD_STATIC=%BUILD_STATIC
%make_build all -C programs
%make_build all -C tests

%install
export CFLAGS=--EPERM # nothing should be compiled during install
%makeinstall_std BUILD_STATIC=%BUILD_STATIC PREFIX=%prefix LIBDIR=%_libdir

# Relocate shared libraries from %_libdir/ to /%_lib/ (ALT#30628).
mkdir -p %buildroot/%_lib
for f in %buildroot%_libdir/*.so; do
	t=$(readlink -v "$f")
	ln -snf ../../%_lib/"$t" "$f"
done
mv %buildroot%_libdir/*.so.* %buildroot/%_lib/

%set_verify_elf_method strict
%define _unpackaged_files_terminate_build 1

%check
export CFLAGS=--EPERM # nothing should be compiled during check
make test -C tests # these tests don't run in parallel

%files
%_bindir/*
%_man1dir/*
%doc LICENSE NEWS README.md

%files -n lib%name
/%_lib/*.so.*
%doc lib/LICENSE

%files -n lib%name-devel
%_includedir/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%changelog
* Mon Mar 06 2017 Dmitry V. Levin <ldv@altlinux.org> 1:1.7.5-alt1
- Initial revision.
