%def_disable static

Name: libzrtpcpp
Version: 1.4.6
Release: alt1

Summary: ZRTP support for GNU RTP/RTCP stack

License: GPL
Group: System/Libraries
Url: http://www.gnu.org/software/ccrtp/

Source: %name-%version-%release.tar

BuildRequires: gcc-c++ libccrtp-devel >= 1.7.0 libstdc++-devel libgcrypt-devel

%description
This package provides a library that adds support to the GNU RTP stack 
for the zrtp protocol specification developed by Phil Zimmermen for 
zphone.  Using this package, together with GNU ccrtp (1.5.0 or later) 
provides a zrtp implimentation that can be directly embedded into client
and server applications, rather than the overhead penalty of using an 
external proxy such as zphone.  The first application to demonstrate 
this capability is the 0.8.2 release of the Twinkle softphone client.

%package devel
Summary: Header files for zrtpcpp library
Group: Development/Other
Requires: %name = %version-%release
Requires: libccrtp-devel >= 1.6.0

%package devel-static
Summary: Static libraries for %name
Group: Development/C
Requires: %name-devel = %version-%release

%description devel
Header files for zrtpcpp library.

%description devel-static
Common C++ devel static files

%prep
%setup

%build
%configure %{subst_enable static}
make

%install
%make_install DESTDIR=%buildroot install

%files
%doc AUTHORS COPYING README
%_libdir/lib*.so.*

%files devel
%_libdir/lib*.so
%_includedir/%name
%_pkgconfigdir/*.pc

%if_enabled static
%files devel-static
%_libddir/*.a
%endif

%changelog
* Wed Nov 10 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.6-alt1
- 1.4.6 released

* Fri May  8 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.3-alt1
- 1.4.3 released

* Sat Dec  6 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.0-alt2
- obsolete by filetriggers macros removed

* Sun Oct 26 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.0-alt1
- 1.3.0 released

* Sun Feb 24 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.0-alt1
- 1.0.0 released

* Sun Jan  7 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.0-alt0.1
- initial build
