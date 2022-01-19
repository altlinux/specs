Name: SDL2_ttf
Version: 2.0.18
Release: alt1.2

Summary: Simple DirectMedia Layer - Sample TrueType Font Library
License: zlib
Group: System/Libraries

Url: http://www.libsdl.org/projects/SDL_ttf/
Packager: Nazarov Denis <nenderus@altlinux.org>

# http://www.libsdl.org/projects/SDL_ttf/release/%name-%version.tar.gz
Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: libICE-devel
BuildRequires: libSDL2-devel
BuildRequires: python3

%description
This library allows you to use TrueType fonts to render text in SDL
applications.

%package -n lib%name
Summary: Simple DirectMedia Layer - Sample TrueType Font Library
Group: System/Libraries

%description -n lib%name
This library allows you to use TrueType fonts to render text in SDL
applications.

%package -n lib%name-devel
Summary: Libraries, includes and more to develop SDL applications.
Group: Development/C

%description -n lib%name-devel
This library allows you to use TrueType fonts to render text in SDL
applications.

%prep
%setup
%ifarch %e2k
# HarfBuzz is written in C++ and pretends not to use
# the C++ runtime, but it relies on non-portable hacks.
# (1) dynamic -lstdc++
#sed -i 's/LINKER = $(LINK)/LINKER = $(CXXLINK)/' Makefile.am
# (2) static -lsupc++, worse
#sed -i 's/$(TTF_LIBS) @MATHLIB@/& -lsupc++/' Makefile.am
# (3) only include what's missing
cat >> "$(echo external/harfbuzz-*/src/hb-common.cc)" << "EOF"
extern "C" __attribute__((visibility("hidden")))
void __cxa_vec_ctor(void *a, size_t n, size_t size,
		void (*c)(void*), void (*d)(void*)) {
	size_t i = 0;
	if (c) while (n--) c((char*)a + size * i++);
}
extern "C" __attribute__((visibility("hidden")))
void __cxa_vec_dtor(void *a, size_t n, size_t size,
		void (*d)(void*)) {
	if (d) while (n--) d((char*)a + size * n);
}
EOF
%endif

%build
./autogen.sh
%configure --disable-static
%make_build

%install
%makeinstall_std
%__rm -rf %buildroot%_libdir/lib%name.la

%files -n lib%name
%doc CHANGES.txt COPYING.txt README.txt
%_libdir/lib%name-2.0.so.*

%files -n lib%name-devel
%dir %_includedir/SDL2
%_includedir/SDL2/SDL_ttf.h
%_pkgconfigdir/%name.pc
%_libdir/lib%name.so

%changelog
* Wed Jan 19 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.0.18-alt1.2
- Better fix for Elbrus

* Tue Jan 18 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.0.18-alt1.1
- Fixed build for Elbrus

* Tue Jan 11 2022 Nazarov Denis <nenderus@altlinux.org> 2.0.18-alt1
- Version 2.0.18

* Wed Feb 10 2021 Nazarov Denis <nenderus@altlinux.org> 2.0.15-alt1
- Version 2.0.15

* Thu Jul 14 2016 Nazarov Denis <nenderus@altlinux.org> 2.0.14-alt1
- Version 2.0.14

* Mon Jan 25 2016 Nazarov Denis <nenderus@altlinux.org> 2.0.13-alt1
- Version 2.0.13 

* Wed Feb 05 2014 Nazarov Denis <nenderus@altlinux.org> 2.0.12-alt0.M70T.1
- Build for branch t7

* Fri Nov 01 2013 Nazarov Denis <nenderus@altlinux.org> 2.0.12-alt1
- Initial build for ALT Linux
