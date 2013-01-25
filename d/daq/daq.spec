Name: daq
Version: 2.0.0
Release: alt1
Summary: Data Acquisition Library
License: GPLv2
Group: System/Libraries
Provides: daq
Source: daq-%version.tar
URL: http://www.snort.org/

BuildRequires: autoconf, automake, flex, libpcap-devel

%description
Data Acquisition library for Snort.

%package -n lib%name
Summary: The shared library for Snort Data Acquisition.
Group: System/Libraries
Provides: %name-lib = %version
Obsoletes: %name-lib < %version

%package -n lib%name-devel
Summary: Header files for lib%name
Summary(ru_RU.UTF-8): Заголовочные файлы для lib%name
Group: Development/C
Requires: lib%name = %version-%release bc
Provides: %name-devel = %version
Obsoletes: %name-devel < %version

%description -n lib%name
This package contains lib%name shared library of functions for 
Snort Data Acquisition.


%description -n lib%name-devel
This package contains lib%name develomment library of functions for 
Snort Data Acquisition.

This package is required for development of applications that
utilize lib%name.


%prep
%setup -q

%build
%configure
%make

%install
make install DESTDIR=%buildroot

%files -n lib%name
%_bindir/daq-modules-config
%_libdir/daq/*.so
%_libdir/lib*.so.*

%files -n lib%name-devel
%_includedir/*.h
%_libdir/*.so

%changelog
* Wed Jan 09 2013 Timur Aitov <timonbl4@altlinux.org> 2.0.0-alt1
- new version

* Tue Sep 25 2012 Anton Farygin <rider@altlinux.ru> 1.1.1-alt1
- first build for Sisyphus
