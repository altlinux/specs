Name: libintelrdfpmath
Version: 2.0u3
Release: alt1
Summary: The Intel(R) Decimal Floating-Point Math Library
License: BSD-3-Clause
Group: Development/C
Url: https://www.netlib.org/misc/intel/
# VCS https://salsa.debian.org/debian/intelrdfpmath.git
Source: %name-%version.tar

## patches from Debian
Patch0001: debian-arches.patch
Patch0002: inject-buildflags.patch
Patch0003: abs-declaration.patch
Patch0004: wchar_t.patch
Patch0005: mongo-inteldfp-s390x.patch
Patch0006: disable-test-werror.patch
Patch0007: loongarch64.patch

%description
The library implements the functions defined for decimal floating-point
arithmetic operations in the IEEE Standard 754-2019 for Floating-Point
Arithmetic, which is a revision of the IEEE Standard 754-2019 for Floating-Point Arithmetic.
However, there were no changes in what is mandated for decimal floating-point arithmetic
in the IEEE Standard 754-2019, compared to the IEEE Standard 754-2019.

%package devel-static
Summary: The Intel(R) Decimal Floating-Point Math Library
Group: Development/C

%description devel-static
The library implements the functions defined for decimal floating-point
arithmetic operations in the IEEE Standard 754-2019 for Floating-Point
Arithmetic, which is a revision of the IEEE Standard 754-2019 for Floating-Point Arithmetic.
However, there were no changes in what is mandated for decimal floating-point arithmetic
in the IEEE Standard 754-2019, compared to the IEEE Standard 754-2019.

%prep
%setup
%autopatch -p1

%build

%ifarch %ix86
    _HOST_ARCH=x86
%else
    _HOST_ARCH=%_arch
%endif

export CC=gcc
for CALL_BY_REF in 0 1; do
    for GLOBAL_RND in 0 1; do
	for GLOBAL_FLAGS in 0 1; do
	    %make_build -C LIBRARY CC=${CC} CC_NAME_INDEX=4 CC_INDEX=4 _HOST_ARCH=${_HOST_ARCH} CALL_BY_REF=${CALL_BY_REF} GLOBAL_RND=${GLOBAL_RND} GLOBAL_FLAGS=${GLOBAL_FLAGS} UNCHANGED_BINARY_FLAGS=0
	    mv LIBRARY/libbid.a LIBRARY/libbidgcc${CALL_BY_REF}${GLOBAL_RND}${GLOBAL_FLAGS}.a
	    make -C LIBRARY CC_NAME_INDEX=4 CC_INDEX=4 _HOST_ARCH=${_HOST_ARCH} clean
	    %make_build -C LIBRARY CC=${CC} CC_NAME_INDEX=4 CC_INDEX=4 _HOST_ARCH=${_HOST_ARCH} CALL_BY_REF=${CALL_BY_REF} GLOBAL_RND=${GLOBAL_RND} GLOBAL_FLAGS=${GLOBAL_FLAGS} UNCHANGED_BINARY_FLAGS=1
	    mv LIBRARY/libbid.a LIBRARY/libbidgcc${CALL_BY_REF}${GLOBAL_RND}${GLOBAL_FLAGS}b.a
	    make -C LIBRARY CC_NAME_INDEX=4 CC_INDEX=4 _HOST_ARCH=${_HOST_ARCH} clean
	done
    done
done

%install
mkdir -p %buildroot%_libdir
cp -a LIBRARY/*.a %buildroot%_libdir

mkdir -p %buildroot%_includedir
cp -a LIBRARY/src/{bid_conf.h,bid_functions.h} %buildroot%_includedir

%files devel-static
%doc README eula.txt
%_includedir/*.h
%_libdir/*.a

%changelog
* Tue Sep 02 2025 Alexei Takaseev <taf@altlinux.org> 2.0u3-alt1
- Initial build for Sisyphus
