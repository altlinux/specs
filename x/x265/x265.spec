Name: x265
Version: 1.4
Release: alt1

Summary: H.265/HEVC encoder
License: GPL
Group: Video
Url: http://x265.org

Requires: libx265 = %version-%release

Source: %name-%version-%release.tar

BuildRequires: cmake gcc-c++ yasm

%description
H.265/HEVC encoder

%package -n libx265
Summary: H.265/HEVC encoder library
Group: System/Libraries

%package -n libx265-devel
Summary: Development files of H.265/HEVC encoder library
Group: Development/C
Requires: libx265 = %version-%release

%description -n libx265
H.265/HEVC encoder library

%description -n libx265-devel
Development files of H.265/HEVC encoder library

%prep
%setup
sed -i	-e '/X265_VERSION / s,unknown,%version,' \
	-e '/X265_LATEST_TAG / s,0\.0,%version,' \
	source/cmake/version.cmake

%build
%add_optflags %optflags_shared
cmake -DCMAKE_CXX_FLAGS='%optflags' -DCMAKE_INSTALL_PREFIX=%prefix -DLIB_INSTALL_DIR=%_lib source
%make_build

%install
%makeinstall_std

%ifnarch x86_64
%set_verify_elf_method textrel=relaxed
%endif

%files
%_bindir/x265

%files -n libx265
%_libdir/libx265.so.*

%files -n libx265-devel
%_libdir/libx265.so
%_includedir/x265.h
%_includedir/x265_config.h
%_pkgconfigdir/*

%changelog
* Tue Dec 09 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4-alt1
- 1.4 release
