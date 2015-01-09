%define sover 0

Name: linenoise
Version: 20141007
Release: alt1
Summary: A small self-contained alternative to readline and libedit 
License: BSD
Group: System/Libraries
Url: https://github.com/antirez/linenoise
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/antirez/linenoise.git
Source: %name-%version.tar

%description
A minimal, zero-config, BSD licensed, readline replacement used in
Redis, MongoDB, and Android.

%package -n lib%name
Summary: A small self-contained alternative to readline and libedit
Group: System/Libraries

%description -n lib%name
A minimal, zero-config, BSD licensed, readline replacement used in
Redis, MongoDB, and Android.

%package -n lib%name-devel
Summary: Development files of lib%name
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
A minimal, zero-config, BSD licensed, readline replacement used in
Redis, MongoDB, and Android.

This package contains development files of lib%name.

%prep
%setup

%build
gcc %optflags %optflags_shared -c %name.c -o %name.o
gcc -shared *.o -Wl,-soname=lib%name.so.%sover \
	-o lib%name.so.%sover

%install
install -d %buildroot%_includedir
install -d %buildroot%_libdir

install -p -m644 *.h %buildroot%_includedir/

install -m644 lib%name.so.%sover %buildroot%_libdir/
ln -s lib%name.so.%sover %buildroot%_libdir/lib%name.so

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%doc example.c *.markdown
%_includedir/*
%_libdir/*.so

%changelog
* Fri Jan 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20141007-alt1
- Initial build for Sisyphus

