%define sover 7
%define libkvazaar libkvazaar%sover
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
Name: kvazaar
Version: 2.2.0
Release: alt1
Summary: Kvazaar is an award-winning academic open-source video encoder for (HEVC/H.265)
Url: https://github.com/ultravideo/kvazaar
Group: Video
License: BSD-3-Clause
Source: %name-%version.tar

BuildRequires: automake autoconf libtool m4 yasm gcc gcc-c++ 

%package -n %libkvazaar
Summary: The shared library for %name
Group: System/Libraries

%package -n lib%name-devel
Summary: Header files for lib%name
Group: Development/C

%description
Kvazaar is an award-winning academic open-source video encoder for the state-of-the-art 
High Efficiency Video Coding (HEVC/H.265) standard developed since 2012. 

Kvazaar is being developed in C and optimized in SSE/AVX intrinsics under the BSD-3-Clause license since v2.1. 
The development is being coordinated by Ultra Video Group and the implementation work is carried out on GitHub. 

%description -n %libkvazaar
This package contains lib%name shared library

%description -n lib%name-devel
This package contains lib%name header files

%prep
%setup

%build
export ASFLAGS=1
%autoreconf
%configure --enable-static=no

%make_build 

%install
%makeinstall

%files 
%_bindir/kvazaar
%doc %_defaultdocdir/%name/CREDITS
%doc %_defaultdocdir/%name/LICENSE*
%doc %_defaultdocdir/%name/README.md
%_man1dir/kvazaar.1.xz

%files -n %libkvazaar
%_libdir/libkvazaar.so.%sover.*
%_libdir/libkvazaar.so.%sover

%files -n lib%name-devel
%_libdir/pkgconfig/kvazaar.pc
%_libdir/libkvazaar.so
%_includedir/kvazaar.h

%changelog
* Tue Jan 09 2024 Oleg Proskurin <proskur@altlinux.org> 2.2.0-alt1
- Initial build