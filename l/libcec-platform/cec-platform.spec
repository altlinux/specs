Name: libcec-platform
Version: 1.0.10
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
%_includedir/platform
%_libdir/platform
%_libdir/libplatform.a
%_pkgconfigdir/platform.pc

%changelog
* Thu Jul 23 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.10-alt1
- 1.0.10
