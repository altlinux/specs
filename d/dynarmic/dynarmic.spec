%define sover 6.7

Name: dynarmic
Version: 6.7.0
Release: alt5

Summary: A dynamic recompiler for ARM.
License: 0BSD
Group: System/Libraries

Url: https://github.com/merryhime/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: x86_64 aarch64

# https://github.com/merryhime/%name/archive/refs/tags/%version/%name-%version.tar.gz
Source: %name-%version.tar

Patch0: %name-mcl-alt.patch
Patch1: %name-inc-alt.patch
Patch2: %name-xbyak-7-tests-alt.patch

BuildRequires: /proc
BuildRequires: boost-devel
BuildRequires: catch-devel
BuildRequires: gcc-c++
BuildRequires: libmcl-devel
BuildRequires: liboaknut-devel
BuildRequires: librobin-map-devel
BuildRequires: libxbyak-devel
BuildRequires: libzydis-devel

%description
A dynamic recompiler for ARM.

%package -n lib%name%sover
Summary: A dynamic recompiler for ARM.
Group: System/Libraries

%description -n lib%name%sover
A dynamic recompiler for ARM.

%package -n lib%name-devel
Summary: Header files for lib%name
Group: Development/C++

%description -n lib%name-devel
Header files for lib%name

%prep
%setup
%autopatch -p1

%build
%add_optflags -DXBYAK_STRICT_CHECK_MEM_REG_SIZE=0
%cmake \
	-DBUILD_SHARED_LIBS:BOOL=TRUE \
	-DDYNARMIC_IGNORE_ASSERTS=TRUE \
	-DDYNARMIC_USE_PRECOMPILED_HEADERS:BOOL=FALSE
%cmake_build

%install
%cmake_install

%files -n lib%name%sover
%doc LICENSE.txt README.md
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_libdir/cmake/%name
%_libdir/lib%name.so
%_includedir/%name

%changelog
* Sun Jun 28 2026 Nazarov Denis <nenderus@altlinux.org> 6.7.0-alt5
- Fix build with xbyak >= 7 (removed tAVX512_4FMAPS, tAVX512_4VNNIW, tAVX512ER, tAVX512PF, tPREFETCHWT1)

* Thu Aug 21 2025 Nazarov Denis <nenderus@altlinux.org> 6.7.0-alt4
- Add optflag -DXBYAK_STRICT_CHECK_MEM_REG_SIZE=0

* Mon Aug 04 2025 Nazarov Denis <nenderus@altlinux.org> 6.7.0-alt3
- Add inc files

* Mon Aug 04 2025 Nazarov Denis <nenderus@altlinux.org> 6.7.0-alt2
- Add ignore asserts option (thx zerg@)

* Mon Mar 25 2024 Nazarov Denis <nenderus@altlinux.org> 6.7.0-alt1
- New version 6.7.0.

* Tue Feb 13 2024 Nazarov Denis <nenderus@altlinux.org> 6.6.3-alt1
- New version 6.6.3.

* Thu Jul 27 2023 Nazarov Denis <nenderus@altlinux.org> 6.5.0-alt1
- New version 6.5.0.

* Tue May 30 2023 Nazarov Denis <nenderus@altlinux.org> 6.4.8-alt1
- Initial build for ALT Linux
