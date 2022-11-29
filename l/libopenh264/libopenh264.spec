%define oname openh264
%def_enable check
%ifarch %ix86 x86_64
%def_with meson
%else
%def_without meson
%endif

%def_disable static

Name: libopenh264
Version: 2.3.1
Release: alt1

Summary: H.264 codec library
License: BSD-2-Clause
Group: System/Libraries
Url: http://www.openh264.org/

Vcs: https://github.com/cisco/openh264.git
# Source-url: https://github.com/cisco/openh264/archive/v%version/%oname-%version.tar.gz
Source: %name-%version.tar

%ifarch %ix86
%add_optflags -msse2 -mfpmath=sse
%set_verify_elf_method textrel=relaxed
%endif

%if_with meson
BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
%endif
BuildRequires: gcc-c++ nasm

%{?_enable_check:BuildRequires: libgtest-devel}

%description
OpenH264 is a codec library which supports H.264 encoding and decoding.
It is suitable for use in real time applications such as WebRTC.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package devel-static
Summary: Static H.264 codec library
Group: Development/C++
Requires: %name-devel = %EVR

%description devel-static
This package provides %name static library.

%prep
%setup
# setup build options
%add_optflags %optflags_shared
%ifarch %ix86
%add_optflags -msse2 -mfpmath=sse
sed -i 's|^USE_ASM[[:space:]][[:space:]]*=.*|USE_ASM = No|' Makefile
sed -i 's|^HAVE_AVX2[[:space:]][[:space:]]*:=.*|HAVE_AVX2 := No|' build/arch.mk
%endif
sed -i -e 's|^CFLAGS_OPT=.*$|CFLAGS_OPT=%{optflags} %(getconf LFS_CFLAGS)|' Makefile
#sed -i -e '/^CFLAGS_OPT=/i LDFLAGS={ldflags}' Makefile
sed -i -e 's|^PREFIX=.*$|PREFIX=%{_prefix}|' Makefile
sed -i -e 's|^LIBDIR_NAME=.*$|LIBDIR_NAME=%{_lib}|' Makefile
sed -i -e 's|^SHAREDLIB_DIR=.*$|SHAREDLIB_DIR=%{_libdir}|' Makefile

%build
%if_with meson
%meson
%meson_build
%else
%make_build
%endif

%install
%if_with meson
%meson_install
%else
%makeinstall_std
%endif

%if_disabled static
%{?_without_meson:rm -v %buildroot%_libdir/%name.a}
%endif

%check
%if_with meson
%__meson_test
%endif

%files
%_libdir/%name.so.*
%doc LICENSE README.md RELEASES

%files devel
%_includedir/wels/
%_libdir/%name.so
%_pkgconfigdir/%oname.pc

%if_enabled static
%files devel-static
%_libdir/%name.a
%endif

%changelog
* Wed Sep 21 2022 Yuri N. Sedunov <aris@altlinux.org> 2.3.1-alt1
- 2.3.1 (bumped soname)

* Mon Aug 01 2022 Yuri N. Sedunov <aris@altlinux.org> 2.3.0-alt1
- 2.3.0
- used meson for %%ix86 and x86_64 builds
- fixed License tag

* Tue May 03 2022 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- 2.2.0

* Sun Aug 29 2021 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt3
- disable devel-static subpackage (contains __gnu_lto_slim)

* Sun Jul 04 2021 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt2
- cleanup spec, drop ExclusiveArch
- switch build to makefile (thanks, zerg@!), fix build (ALT bug 38832)

* Wed Jun 03 2020 Yuri N. Sedunov <aris@altlinux.org> 2.1.1-alt1
- 2.1.1

* Thu Apr 02 2020 Yuri N. Sedunov <aris@altlinux.org> 2.1.0-alt1
- 2.1.0

* Fri Oct 04 2019 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- updated to v2.0.0-7-g0e377291

* Wed May 01 2019 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- first build for Sisyphus

