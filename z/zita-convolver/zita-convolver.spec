%global libmajor 3

Summary: Convolution engine library
Name: zita-convolver
Version: 3.1.0
Release: alt1
License: GPLv3+
Group: System/Libraries
Url: http://kokkinizita.linuxaudio.org/
Packager: Anton Midyukov <antohami@altlinux.org>

Source: http://kokkinizita.linuxaudio.org/linuxaudio/downloads/%name-%version.tar.bz2

BuildRequires: gcc-c++ libfftw3-devel

%description
%name is a fast, partitioned convolution engine library.

%package devel
Summary: Fast, partitioned convolution engine library
Group: Development/Other
Requires: %name = %version-%release

%description devel
%name is a fast, partitioned convolution engine library. This package
contains libraries and header files for developing applications that use
%name.

%prep
%setup

# No need to call ldconfig during packaging
%__subst '\|ldconfig|d' libs/Makefile

%build
%make_build -C libs

%install
%makeinstall_std -C libs PREFIX=%prefix LIBDIR=%_lib
# create .so.x link
ln -s lib%name.so.%version %buildroot%_libdir/lib%name.so.%libmajor

%files
%doc AUTHORS COPYING
%_libdir/lib%name.so.*

%files devel
%_includedir/%name.h
%_libdir/lib%name.so

%changelog
* Thu May 18 2017 Anton Midyukov <antohami@altlinux.org> 3.1.0-alt1
- Initial build for ALT Linux Sisyphus.
