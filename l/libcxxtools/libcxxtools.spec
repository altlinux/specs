Name: libcxxtools
Version: 2.2.1
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
%configure --disable-static \
%ifnarch %ix86 x86_64
	--with-atomictype=pthread \
%endif
	#
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
%_pkgconfigdir/*.pc

%changelog
* Mon Mar 07 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.1-alt1
- 2.2.1 released

* Wed Jun 17 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.1.1-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Wed Feb 13 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.1-alt1
- initial
