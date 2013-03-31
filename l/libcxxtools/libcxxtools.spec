Name: libcxxtools
Version: 2.1.1
Release: alt1

Summary: Set of reusable C++ components
License: LGPL
Group: Development/C++
Url: http://www.tntnet.org/

Source: %name-%version-%release.tar

BuildRequires: gcc-c++


%package devel
Summary: Set of reusable C++ components 
Group: Development/C++
Requires: %name = %version-%release

%description
%summary

%description devel
%summary
%prep
%setup

%build
%autoreconf
%configure --disable-static --with-atomictype=generic
%make_build

%install
%makeinstall_std

%files
%_libdir/libcxxtools*.so.*

%files devel
%doc AUTHORS COPYING
%_bindir/cxxtools-config
%_includedir/cxxtools
%_libdir/libcxxtools*.so

%changelog
* Wed Feb 13 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.1-alt1
- initial
