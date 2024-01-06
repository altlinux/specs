%def_enable static

Name: astc-encoder
Version: 4.6.1
Release: alt1

Summary: ARM Adaptive Scalable Texture Compression (ASTC) Encoder
License: APL
Group: System/Libraries

Url: http://github.com/ARM-software/astc-encoder
Source: %name-%version.tar

ExcludeArch: armh %ix86

Provides: astcenc = %version-%release
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): cmake gcc-c++
%{?!_without_check:%{?!_without_test:%{?!_disable_check:%{?!_disable_test:BuildRequires: ctest}}}}

%description
ARM Adaptive Scalable Texture Compression (ASTC) Encoder,
astcenc, a command-line tool for compressing and decompressing
images using the ASTC texture compression standard.

%package devel
Summary: Development files for %name%{?!_enable_static (static)}
Group: Development/C
Requires: %name = %version-%release

%description devel
Development files for %name.

%prep
%setup
%ifarch %e2k
# lcc 1.26.21: -Wtype-limits, -Wreduced-alignment
sed -i '/-Werror/d' Source/cmake_core.cmake
%endif

%build
export LIB_SUFFIX=%_libsuff
%cmake_insource \
%ifarch aarch64
	-DISA_NEON=ON \
%endif
%ifarch x86_64
	-DISA_AVX2=ON \
	-DISA_SSE41=ON \
	-DISA_SSE2=ON \
%endif
%ifarch %e2k
	-DISA_AVX2=OFF \
	-DISA_SSE41=ON \
	-DISA_SSE2=ON \
%endif
%if_enabled check
%if_with test
	-DASTCENC_UNITTEST=ON \
%endif
%endif
	-DCMAKE_SKIP_RPATH=ON \
%if_disabled static
	-DBUILD_SHARED_LIBS=ON \
	-DASTCENC_SHAREDLIB=ON \
%endif
	-DNO_INVARIANCE=ON \
	-DCLI=ON
%make_build

# TODO: proper test run (currently no-op)
%check
%make test

%install
%makeinstall_std

# TODO: debian manpage?

%files
%_bindir/astcenc-*

# TODO:
# proper shared/static library subpackage(s) -- needs debian patchset for 4.6.0?

%if 0
%files devel
%_includedir/*.h
%if_enabled static
%_libdir/*.a
%else
%_libdir/*.so*
%endif
%endif

%changelog
* Sat Jan 06 2024 Michael Shigorin <mike@altlinux.org> 4.6.1-alt1
- initial release
  + loosely based on cooker spec with debian bits
  + exclude 32-bit arches due to ftbfs
