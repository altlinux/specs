Summary: C library for parsing, writing and creating RSS files or streams
Name: libmrss
Version: 0.19.2
Release: alt1.1
License: LGPLv2
Group: System/Libraries
Source0: http://www.autistici.org/bakunin/libmrss/%name-%version.tar.gz
Url: http://www.autistici.org/bakunin/libmrss/

BuildRequires: libnxml-devel libcurl-devel

%description
mRSS is a C library for parsing, writing and creating RSS (0.91, 0.92,
1.0, 2.0) files or streams

%package devel
Summary: Header files for mRss library
Group: System/Libraries
Requires: %name = %version-%release

%description devel
Header files for mRss library.

%prep
%setup
%build
%autoreconf
%configure
make

%install
%makeinstall_std

%files
%_libdir/%{name}*.so.*
%doc AUTHORS ChangeLog NEWS README

%files devel
%_libdir/lib*.so
%_includedir/*
%_pkgconfigdir/*.pc

%changelog
* Sun Nov 14 2010 Denis Smirnov <mithraen@altlinux.ru> 0.19.2-alt1.1
- rebuild (with the help of girar-nmu utility)

* Fri Sep  3 2010 Terechkov Evgenii <evg@altlinux.org> 0.19.2-alt1
- Initial build for ALT Linux Sisyphus
