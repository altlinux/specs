Name: libcec-platform
Version: 2.1.0.1
Release: alt1

Summary: Platform support library used by libCEC and binary add-ons for Kodi
License: GPL
Group: Development/C++

Source: %name-%version.tar
BuildRequires: cmake gcc-c++

%description
%summary

%package devel
Summary: %summary
Group: Development/C++

%description devel
%summary

%prep
%setup

%build
cmake . -DCMAKE_INSTALL_PREFIX=%prefix
make

%install
%makeinstall_std

%files devel
%_includedir/p8-platform
%_libdir/p8-platform
%_libdir/libp8-platform.a
%_pkgconfigdir/p8-platform.pc

%changelog
* Mon Feb 06 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.0.1-alt1
- 2.1.0.1

* Thu Jul 23 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.10-alt1
- 1.0.10
