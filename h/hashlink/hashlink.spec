%define _unpackaged_files_terminate_build 1

Name: hashlink
Version: 1.11
Release: alt3

Summary: HashLink is a virtual machine for Haxe
License: MIT
Group: Development/Other

Url: https://hashlink.haxe.org/
Source: %name-%version.tar

ExcludeArch: armh

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake libGLU-devel libSDL2-devel libdb4-devel
BuildRequires: libpng-devel libssl-devel libturbojpeg-devel libuv-devel libvorbis-devel zlib-devel

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
%cmake_insource -D BUILD_TESTING=OFF
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
%_libdir/sqlite.hdll
%_libdir/ui.hdll
%_libdir/uv.hdll

%files devel
%_libdir/libhl.so
%_includedir/hl.h
%_includedir/hlc.h
%_includedir/hlc_main.c

%changelog
* Mon Aug 07 2023 Vitaly Lipatov <lav@altlinux.ru> 1.11-alt3
- NMU: cleanup BR, disable build on armh (JIT does not support ARM processors)

* Mon May 18 2020 Denis Smirnov <mithraen@altlinux.ru> 1.11-alt2
- add /usr/include/hlc_main.c for HL/C support

* Mon May 18 2020 Denis Smirnov <mithraen@altlinux.ru> 1.11-alt1
- first build for Sisyphus

