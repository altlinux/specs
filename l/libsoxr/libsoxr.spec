%define realname soxr
%def_enable check
%def_enable CR32S

Name: lib%realname
Version: 0.1.3
Release: alt1

Summary: The SoX Resampler library
Group: System/Libraries
License: LGPLv2+
Url: https://sourceforge.net/p/soxr/wiki/Home/

Vcs: https://github.com/chirlu/soxr.git
#Source: http://downloads.sourceforge.net/%realname/%realname-%version-Source.tar.xz
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake ctest

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
%setup -n %name-%version
%patch -p1
%ifarch %e2k
# has up to SSE4.1 actually
sed -i 's,defined\([( ]\)__x86_64__\([ )]\),& || defined\1__e2k__\2,' src/{pffft.c,soxr.c}
%endif

%build
%cmake	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DCMAKE_INSTALL_PREFIX=%prefix \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DLIB_INSTALL_DIR:PATH=%_libdir \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	%{?_disable_CR32S:-DWITH_CR32S=FALSE}
%nil
%cmake_build

%install
%cmake_install

# Remove docs and use the rpmbuild macro instead
rm -rf %buildroot%_docdir/*

%check
%cmake_build -t test

%files
%_libdir/*.so.*
%doc LICENCE NEWS README

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/soxr-lsr.pc
%_pkgconfigdir/soxr.pc
%doc examples

%changelog
* Thu Mar 30 2023 Yuri N. Sedunov <aris@altlinux.org> 0.1.3-alt1
- 0.1.3
- switched to upstream git
- removed obsolete VLC patch
- fixed Source, added Vcs tags
- ported to cmake macros, updated BR, enabled %%check

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
