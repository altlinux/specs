Name: zstd
Version: 1.5.4
Release: alt2
Summary: Zstd compression library and tools
License: BSD-3-Clause
Group: Archiving/Compression
Url: https://facebook.github.io/zstd/
# https://github.com/facebook/zstd
# git://git.altlinux.org/gears/z/zstd.git
Source: %name-%version-%release.tar
Requires: lib%name = %EVR
%def_enable pzstd
%{?!_disable_pzstd:BuildRequires: gcc-c++}
%{?!_disable_pzstd:%{?!_without_check:%{?!_disable_check:BuildRequires: libgtest-devel}}}

# needed for cli-tests
%{?!_without_check:%{?!_disable_check:BuildRequires: python3 less}}

%description
Zstd, short for Zstandard, is a fast lossless compression algorithm,
targeting real-time compression scenarios at zlib-level compression ratio.

%package -n pzstd
Summary: Parallel Zstandard tool
Group: %group
Requires: %name = %EVR

%description -n pzstd
Parallel Zstandard is a Pigz-like tool for Zstandard.

It provides Zstandard format compatible compression and decompression
that is able to utilize multiple cores.  It breaks the input up into
equal sized chunks and compresses each chunk independently into a
Zstandard frame.  It then concatenates the frames together to produce
the final compressed output.  Pzstandard will write a 12 byte header for
each frame that is a skippable frame in the Zstandard format, which
tells PZstandard the size of the next compressed frame.

PZstandard supports parallel decompression of files compressed with
PZstandard.  When decompressing files compressed with Zstandard,
PZstandard does IO in one thread, and decompression in another.

%package -n lib%name
Summary: Zstd compression shared library
Group: System/Libraries

%description -n lib%name
Zstd, short for Zstandard, is a fast lossless compression algorithm,
targeting real-time compression scenarios at zlib-level compression ratio.

This package contains lib%name shared library.

%package -n lib%name-devel
Summary: Zstd compression development files
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
Zstd, short for Zstandard, is a fast lossless compression algorithm,
targeting real-time compression scenarios at zlib-level compression ratio.

This package contains development files required to build applications
using lib%name library.

%prep
%setup -n %name-%version-%release
%ifarch %e2k
# fine tuning for architecture and compiler
%add_optflags -D__inline='__inline __attribute__((always_inline))'
%add_optflags -DMEM_FORCE_MEMORY_ACCESS=2 -DXXH_FORCE_MEMORY_ACCESS=2 -DXXH_FORCE_ALIGN_CHECK=0
%endif
# reenable recipe echoing
sed -i 's/^\([[:space:]]*\)@\$/\1\$/' Makefile */Makefile
# some cli-tests fail because HAVE_ZLIB=0
rm tests/cli-tests/compression/{basic,gzip-compat}.sh
%ifarch i586 armh
# fail on 32-bit targets (not enough memory?)
rm tests/cli-tests/compression/window-resize.sh*
%endif
%define make_params PREFIX=%prefix LIBDIR=%_libdir GZFILES= ZSTD_LEGACY_SUPPORT=0 HAVE_ZLIB=0

%build
export CFLAGS="%optflags $(getconf LFS_CFLAGS)"
export CXXFLAGS="$CFLAGS"
# profile-guided optimization (PGO) build
# HASH_DIR is specified to use the same for tests
%make_build HASH_DIR=zstd_build -C programs zstd-pgo %make_params
# the rest is built without PGO
%make_build -C lib all %make_params
%{?!_disable_pzstd:%make_build -C contrib/pzstd %make_params}

%install
export CC=false CXX=false # nothing should be compiled or linked during install
for dir in lib programs; do
	%makeinstall_std -C $dir %make_params
done
%{?!_disable_pzstd:%makeinstall_std -C contrib/pzstd %make_params}

# Relocate shared library from %_libdir/ to /%_lib/
mkdir -p %buildroot/%_lib
for f in %buildroot%_libdir/*.so; do
        t=$(readlink -v "$f")
	ln -rsnf %buildroot/%_lib/"$t" "$f"
done
mv %buildroot%_libdir/*.so.* %buildroot/%_lib/

if grep -Frsl /usr/local %buildroot; then
	printf >&2 '%%s leaked into %%s\n' /usr/local %buildroot
	exit 1
fi

%set_verify_elf_method strict
%define _unpackaged_files_terminate_build 1

%check
export CFLAGS="%optflags $(getconf LFS_CFLAGS)"
export CXXFLAGS="$CFLAGS"
%make_build HASH_DIR=zstd_build -k -C tests test %make_params
%{?!_disable_pzstd:%make_build -k -C contrib/pzstd tests GTEST_INC= GTEST_LIB=}
%{?!_disable_pzstd:LD_LIBRARY_PATH=%buildroot/%_lib make -C contrib/pzstd check}

%files
%_bindir/*
%exclude %_bindir/pzstd
%_man1dir/*
%doc CHANGELOG README.md

%files -n pzstd
%_bindir/pzstd

%files -n lib%name
/%_lib/*.so.*
%doc LICENSE

%files -n lib%name-devel
%_includedir/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Mon Feb 13 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.5.4-alt2
- Only a few cli-tests are excluded, instead of all.
- Switched to PGO build.
- Tweaks for Elbrus build.

* Fri Feb 10 2023 Dmitry V. Levin <ldv@altlinux.org> 1.5.4-alt1
- 1.5.2 -> 1.5.4.

* Fri Apr 08 2022 Dmitry V. Levin <ldv@altlinux.org> 1.5.2-alt1
- 1.5.0 -> 1.5.2 (closes: #41356, #42239).

* Thu Jul 01 2021 Dmitry V. Levin <ldv@altlinux.org> 1.5.0-alt2
- Removed zstdgrep.1 and zstdless.1 manpages that are already packaged
  in gzip-utils along with scripts themselves.

* Fri May 14 2021 Dmitry V. Levin <ldv@altlinux.org> 1.5.0-alt1
- 1.4.9 -> 1.5.0.

* Tue Mar 02 2021 Dmitry V. Levin <ldv@altlinux.org> 1.4.9-alt1
- 1.4.8 -> 1.4.9.

* Sat Dec 19 2020 Dmitry V. Levin <ldv@altlinux.org> 1.4.8-alt1
- 1.4.5 -> 1.4.8.

* Tue Jun 23 2020 Dmitry V. Levin <ldv@altlinux.org> 1.4.5-alt2
- Fixed /usr/local leaking into installed files.

* Fri May 22 2020 Dmitry V. Levin <ldv@altlinux.org> 1.4.5-alt1
- 1.4.4 -> 1.4.5.

* Mon Nov 04 2019 Dmitry V. Levin <ldv@altlinux.org> 1.4.4-alt1
- 1.4.3 -> 1.4.4.

* Mon Aug 19 2019 Dmitry V. Levin <ldv@altlinux.org> 1.4.3-alt1
- 1.4.2 -> 1.4.3.

* Thu Jul 25 2019 Dmitry V. Levin <ldv@altlinux.org> 1.4.2-alt1
- 1.3.8 -> 1.4.2.

* Thu Dec 27 2018 Dmitry V. Levin <ldv@altlinux.org> 1.3.8-alt1
- 1.3.7 -> 1.3.8.

* Wed Oct 17 2018 Dmitry V. Levin <ldv@altlinux.org> 1.3.7-alt1
- 1.3.5 -> 1.3.7.

* Wed Jul 11 2018 Dmitry V. Levin <ldv@altlinux.org> 1.3.5-alt1
- 1.3.4 -> 1.3.5.

* Mon Mar 26 2018 Dmitry V. Levin <ldv@altlinux.org> 1.3.4-alt1
- 1.3.3 -> 1.3.4.

* Thu Dec 21 2017 Dmitry V. Levin <ldv@altlinux.org> 1.3.3-alt1
- 1.3.2 -> 1.3.3.

* Sun Oct 29 2017 Dmitry V. Levin <ldv@altlinux.org> 1.3.2-alt1
- 1.3.0 -> 1.3.2.

* Tue Jul 18 2017 Dmitry V. Levin <ldv@altlinux.org> 1.3.0-alt1
- 1.2.0 -> 1.3.0.

* Thu May 25 2017 Dmitry V. Levin <ldv@altlinux.org> 1.2.0-alt1
- 1.1.4 -> 1.2.0.

* Tue Mar 28 2017 Dmitry V. Levin <ldv@altlinux.org> 1.1.4-alt2
- Moved pzstd to separate subpackage.

* Tue Mar 21 2017 Dmitry V. Levin <ldv@altlinux.org> 1.1.4-alt1
- v1.1.3-322-gebf2 == v1.1.4.
- Relocated shared library from %_libdir/ to /%_lib/.

* Fri Mar 17 2017 Dmitry V. Levin <ldv@altlinux.org> 1.1.3.0.322.ebf2-alt1
- v1.1.3-322-gebf2.
