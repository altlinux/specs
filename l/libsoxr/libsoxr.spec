%define realname soxr

Name: lib%realname
Version: 0.1.2
Release: alt4
Group: System/Libraries
Summary: The SoX Resampler library

License: LGPLv2+
Url: https://sourceforge.net/p/soxr/wiki/Home/
Source0: http://downloads.sourceforge.net/%name/%realname-%version-Source.tar.xz
Patch0: https://raw.githubusercontent.com/videolan/vlc/master/contrib/src/soxr/0003-config-use-stdint.h-and-stdbool.h.patch

# Automatically added by buildreq on Wed Apr 22 2015 (-bi)
# optimized out: cmake cmake-modules elfutils pkg-config python-base xz
BuildRequires: ccmake ctest

%description
The SoX Resampler library `libsoxr' performs one-dimensional sample-rate
conversion -- it may be used, for example, to resample PCM-encoded audio.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name%{?_isa} = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -n %realname-%version-Source
%patch -p1
%ifarch %e2k
# has up to SSE4.1 actually
sed -i 's,defined\([( ]\)__x86_64__\([ )]\),& || defined\1__e2k__\2,' src/{pffft.c,soxr.c}
%endif

%build
mkdir build && cd build
cmake	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DCMAKE_INSTALL_PREFIX=%prefix \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DLIB_INSTALL_DIR:PATH=%_libdir \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	../.
%make_build

%install
cd build
%makeinstall_std

# Remove docs and use the rpmbuild macro instead
rm -rf %buildroot%_docdir/*

%files
%doc LICENCE NEWS README
%_libdir/*.so.*

%files devel
%doc examples
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/soxr-lsr.pc
%_pkgconfigdir/soxr.pc

%changelog
* Wed Oct 31 2018 Michael Shigorin <mike@altlinux.org> 0.1.2-alt4
- Replace e2k arch name with %%e2k macro (grenka@)

* Tue Aug 22 2017 Michael Shigorin <mike@altlinux.org> 0.1.2-alt3
- E2K: re-enable SIMD (thanks MCST for hints)

* Tue Aug 22 2017 Michael Shigorin <mike@altlinux.org> 0.1.2-alt2
- added vlc patch to drop faulty village magic with types
  (helps e2k, should help aarch64)
- E2K: explicitly disable SIMD (FTBFS)

* Fri Sep 25 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1.2-alt1
- 0.1.2 released

* Wed Apr 22 2015 Motsyo Gennadi <drool@altlinux.ru> 0.1.1-alt1
- build for ALT Linux
