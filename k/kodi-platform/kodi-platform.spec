Name: kodi-platform
Version: 17.0
Release: alt1

Summary: Kodi plugin development support
License: GPL
Group: Development/C++

Source: kodi-platform-%version.tar

BuildRequires: cmake gcc-c++ kodi-devel libcec-platform-devel tinyxml-devel

%package -n libkodiplatform
Summary: %summary
Group: System/Libraries

%package -n libkodiplatform-devel
Summary: %summary
Group: Development/C++

%description
%summary

%description -n libkodiplatform
%summary

%description -n libkodiplatform-devel
%summary

%prep
%setup

%build
cmake . -DCMAKE_INSTALL_PREFIX=%prefix
make

%install
%makeinstall_std

%files -n libkodiplatform
%_libdir/libkodiplatform.so.*

%files -n libkodiplatform-devel
%_libdir/libkodiplatform.so
%_libdir/kodiplatform
%_pkgconfigdir/kodiplatform.pc
%_includedir//kodi/util

%changelog
* Mon Feb 06 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 17.0-alt1
- updated for Krypton

* Wed Feb 24 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 16.0-alt1
- updated for Jarvis

* Wed Jul 29 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 15.0-alt1
- initial
