Name: bml
Version: 0.8.0
Release: alt1.git20140910
Summary: buzzmachine loader (bml) for Buzztrax
License: LGPLv2.1
Group: Sound
Url: http://buzztrax.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Buzztrax/bml.git
Source: %name-%version.tar

BuildPreReq: gcc-c++

%description
The libbml is a library that loads buzz machines from the windows music
composer Jeskola Buzz, so that Linux/Unix applications can use them. It
can load the original 32bit dll on x86-32bit linux and open source buzz
machines on any platform.

%package -n lib%name
Summary: buzzmachine loader (bml) for Buzztrax
Group: System/Libraries

%description -n lib%name
The libbml is a library that loads buzz machines from the windows music
composer Jeskola Buzz, so that Linux/Unix applications can use them. It
can load the original 32bit dll on x86-32bit linux and open source buzz
machines on any platform.

%package -n lib%name-devel
Summary: Development files of buzzmachine loader (bml) for Buzztrax
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
The libbml is a library that loads buzz machines from the windows music
composer Jeskola Buzz, so that Linux/Unix applications can use them. It
can load the original 32bit dll on x86-32bit linux and open source buzz
machines on any platform.

This package contains development files of lib%name.

%prep
%setup

%build
./autogen.sh \
	--debug \
	--prefix=%prefix \
	--noconfigure
%configure \
	--enable-static=no \
	--enable-debug \
	--enable-dllwrapper
%make_build

%install
%makeinstall_std

rm -f %buildroot%_libdir/%name/*.la

%files -n lib%name
%doc AUTHORS ChangeLog NEWS *.md TODO
%_libdir/*.so.*
%_libdir/%name
%ifnarch x86_64
%_libdir/win32/*.dll
%endif

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%changelog
* Sun Sep 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1.git20140910
- Initial build for Sisyphus

