Name: libass
Version: 0.9.13
Release: alt1
Summary: Portable library for SSA/ASS subtitles rendering

Group: System/Libraries
License: BSD
Url: http://code.google.com/p/libass/
Source: %name-%version-%release.tar

BuildRequires: libpng-devel libenca-devel fontconfig-devel libfreetype-devel
BuildRequires: gcc-c++

%description
libass is portable library for SSA/ASS subtitles rendering.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
This package contains the headers and libraries for libass development.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall

%files
#%doc AUTHORS COPYING NEWS README ChangeLog
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*

%changelog
* Tue Aug 30 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.13-alt1
- 0.9.13 release

* Sun Jun 12 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.12-alt1
0.9.12 release

* Sun Nov 07 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.11-alt2
- rebuilt with set-versioned rpm

* Wed Aug 18 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.11-alt1
- 0.9.11 release

* Wed Mar 03 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.9-alt1
- 0.9.9 release

* Sun Dec 27 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.8-alt2
- unwanted free() in ass_read_memory fixed

* Sat Nov 14 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.8-alt1
- 0.9.8 release 

* Sat Nov 14 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.7-alt1
- 0.9.7 release 

* Thu Aug 14 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.9.5-alt1
- Initial build for ALT Linux.

