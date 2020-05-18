%define _unpackaged_files_terminate_build 1

Name: hashlink
Version: 1.11
Release: alt1

Summary:HashLink is a virtual machine for Haxe
License: MIT
Group: Development/Other

Url: https://hashlink.haxe.org/
Source: %name-%version.tar

BuildPreReq: cmake rpm-macros-cmake

# Automatically added by buildreq on Mon May 18 2020
# optimized out: cmake-modules glibc-kernheaders-generic glibc-kernheaders-x86 libglvnd-devel libogg-devel libsasl2-3 pkg-config python-modules python2-base python3 python3-base python3-dev sh4 zlib-devel
BuildRequires: cmake libGLU-devel libSDL2-devel libdb4-devel libpng-devel libssl-devel libturbojpeg-devel libuv-devel libvorbis-devel python3-module-mpl_toolkits python3-module-yieldfrom zlib-devel-static

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

%changelog
* Mon May 18 2020 Denis Smirnov <mithraen@altlinux.ru> 1.11-alt1
- first build for Sisyphus

