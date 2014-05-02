Name: libleveldb
Version: 1.17
Release: alt1

Summary: A fast and lightweight key/value database library by Google

License: BSD
Group: Development/Databases
Url: http://code.google.com/p/leveldb/

Packager: Alexei Takaseev <taf@altlinux.ru>

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

# Automatically added by buildreq on Tue Apr 16 2013
# optimized out: libstdc++-devel
BuildRequires: gcc-c++ libsnappy-devel

%description
LevelDB is a fast key-value storage library written at Google that provides an
ordered mapping from string keys to string values.

%package devel
Summary: The development files for %name
Group: Development/Databases
Requires: %name = %version-%release

%description devel
Additional header files for development with %name.

%prep
%setup
%patch0 -p1

%build
%autoreconf
%configure --disable-static --with-pic
%make_build

%install
make install DESTDIR=%buildroot

%files
%doc doc/ AUTHORS LICENSE README
%_libdir/%name.so.*

%files devel
%_includedir/leveldb/
%_libdir/%name.so
%_libdir/pkgconfig/*

%changelog
* Fri May 02 2014 Alexei Takaseev <taf@altlinux.org> 1.17-alt1
- 1.17

* Tue Mar 04 2014 Alexei Takaseev <taf@altlinux.org> 1.16-alt1
- 1.16

* Tue Apr 16 2013 Alexei Takaseev <taf@altlinux.org> 1.9.0-alt1
- Initial build for Sisyphus
