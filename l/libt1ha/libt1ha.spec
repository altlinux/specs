Name: libt1ha
Version: 2.0.1
Release: alt2

Summary: Fast Positive Hash
License: Zlib
Group: System/Libraries

URL: https://github.com/leo-yuriev/t1ha
Source: t1ha-%version.tar
Patch: t1ha-%version-%release.patch

%package devel
Summary: Fast Positive Hash
Group: Development/C

%description
t1ha provides a set of fast non-cryptographic hash functions.
%description devel
t1ha provides a set of fast non-cryptographic hash functions.

%prep
%setup -q -n t1ha-%version
%patch -p1

%build
# build libt1ha_pic.a
make libt1ha.a CFLAGS_LIB='%optflags -O3 -DNDEBUG -g0 -ffunction-sections -fpic'
mv libt1ha{,_pic}.a

# check that object files can be linked without undefined symbols
gcc -shared *.o -Wl,--no-undefined
rm *.o

# build libt1ha.a without -fpic
make libt1ha.a CFLAGS_LIB='%optflags -O3 -DNDEBUG -g0 -ffunction-sections'

%check
make check CFLAGS_LIB='%optflags -O3 -DNDEBUG' CFLAGS_TEST='%optflags'

%install
mkdir -p %buildroot%_includedir %buildroot%_libdir
install -m644 t1ha.h %buildroot%_includedir
install -m644 libt1ha{,_pic}.a %buildroot%_libdir

%files devel
%doc README.md
%_includedir/t1ha.h
%_libdir/libt1ha*.a

%changelog
* Fri Mar 30 2018 Alexey Tourbin <at@altlinux.ru> 2.0.1-alt2
- t1ha.h: push hidden visibility for all symbols in libt1ha{,_pic}.a

* Thu Mar 29 2018 Alexey Tourbin <at@altlinux.ru> 2.0.1-alt1
- initial revision
- built libt1ha{,_pic}.a, libt1ha.so barred
