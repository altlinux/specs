%define _unpackaged_files_terminate_build 1

Name: hashlink
Version: 1.14
Release: alt1

Summary: HashLink is a virtual machine for Haxe
License: MIT
Group: Development/Other

Url: https://hashlink.haxe.org/

# Source-url: https://github.com/HaxeFoundation/hashlink/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

ExcludeArch: armh
ExcludeArch: ppc64le aarch64

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: libSDL2-devel libGLU-devel libopenal-devel
BuildRequires: libmbedtls-compat-devel
BuildRequires: libpng-devel libjpeg-devel libvorbis-devel
BuildRequires: libuv-devel zlib-devel

%add_optflags -Wno-incompatible-pointer-types -Wno-int-conversion

# for sdl.hdll and gl* symbols
%set_verify_elf_method unresolved=relaxed

%package devel
Summary: %summary
Group: %group

%description
%summary

%description devel
%summary

%prep
%setup

%build
%cmake_insource -D BUILD_TESTING=OFF \
 -DCMAKE_C_FLAGS="%optflags"
%make_build MAKE=/usr/bin/make # VERBOSE=1 

%install
%makeinstall_std MAKE=/usr/bin/make
install -m644 src/hlc_main.c %buildroot%_includedir/hlc_main.c

%find_lang %name
%files -f %name.lang
%doc LICENSE README.md
#%doc AUTHORS ChangeLog NEWS README THANKS TODO contrib/ manual/
%_bindir/hl
%_libdir/libhl.so.1
%_libdir/libhl.so.1.*
%_libdir/fmt.hdll
%_libdir/sdl.hdll
%_libdir/openal.hdll
%_libdir/ssl.hdll
%_libdir/sqlite.hdll
%_libdir/ui.hdll
%_libdir/uv.hdll

%files devel
%_libdir/libhl.so
%_includedir/hl.h
%_includedir/hlc.h
%_includedir/hlc_main.c

%changelog
* Sun Feb 02 2025 Vitaly Lipatov <lav@altlinux.ru> 1.14-alt1
- new version 1.14 (with rpmrb script)
- build from tarball
- ExcludeArch: ppc64le aarch64

* Mon Aug 07 2023 Vitaly Lipatov <lav@altlinux.ru> 1.11-alt3
- NMU: cleanup BR, disable build on armh (JIT does not support ARM processors)

* Mon May 18 2020 Denis Smirnov <mithraen@altlinux.ru> 1.11-alt2
- add /usr/include/hlc_main.c for HL/C support

* Mon May 18 2020 Denis Smirnov <mithraen@altlinux.ru> 1.11-alt1
- first build for Sisyphus

