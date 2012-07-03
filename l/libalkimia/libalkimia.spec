
Name:    libalkimia
Version: 4.3.2
Release: alt1

Summary: Financial library
License: LGPLv2+
Group:	 System/Libraries
URL:     http://community.kde.org/Alkimia/libalkimia

Source: 137323-%name-%version.tar.bz2

BuildRequires(pre): kde4libs-devel
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: libgmp_cxx-devel

%description
libalkimia is a library with common classes and functionality used by
finance applications for the KDE SC. Currently it supports a common
class to represent monetary values with arbitrary precision.

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
Requires: %name = %version-%release
%description devel
Headers and other files for develop with %name.

%prep
%setup -q

%build
%K4build -Wno-dev

%install
%K4install
%K4find_lang --with-kde %name

%files
%_K4libdir/%name.so.*

%files devel
%dir %_K4includedir/alkimia
%_K4includedir/alkimia/*
%_K4lib/devel/%name.so
%_pkgconfigdir/%name.pc
%_K4apps/cmake/modules/FindLibAlkimia.cmake

%changelog
* Thu Feb 09 2012 Andrey Cherepanov <cas@altlinux.org> 4.3.2-alt1
- New version 4.3.2

* Tue Sep 06 2011 Andrey Cherepanov <cas@altlinux.org> 4.3.1-alt1
- Initial build in Sisyphus

