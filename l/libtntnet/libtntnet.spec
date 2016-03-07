Name: libtntnet
Version: 2.2.1
Release: alt1

Summary: Web application server for web applications written in C++
License: LGPL
Group: System/Libraries
Url: http://www.tntnet.org/

Source: %name-%version-%release.tar

BuildRequires: gcc-c++ libcxxtools-devel libssl-devel zlib-devel zip

%package devel
Summary: Web application server for web applications written in C++
Group: Development/C++
Requires: %name = %version-%release

%package -n tntnet
Summary: Web application server for web applications written in C++
Group: Networking/WWW
Requires: %name = %version-%release

%description
Web application server for web applications written in C++
This package contains tntnet shared library.

%description devel
Web application server for web applications written in C++
This package contains development part of tntnet.

%description -n tntnet
Web application server for web applications written in C++
This package contains sample web server written with tntnet.

%prep
%setup

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%_libdir/libtnt*.so.*

%dir %_libdir/tntnet
%_libdir/tntnet/*.so*

%files devel
%_bindir/tntnet-config
%_bindir/ecppc
%_bindir/ecppl
%_bindir/ecppll

%_libdir/libtntnet*.so

%_includedir/tnt

%_man1dir/tntnet-config.1*
%_man1dir/ecppc.1*
%_man1dir/ecppl.1*
%_man1dir/ecppll.1*
%_man7dir/ecpp.7*

%files -n tntnet
%doc AUTHORS COPYING README

%dir %_sysconfdir/tntnet
%config(noreplace) %_sysconfdir/tntnet/tntnet.xml

%_bindir/tntnet

%_man7dir/tntnet.xml.7*
%_man7dir/tntnet.properties.7*
%_man8dir/tntnet.8*

%changelog
* Mon Mar 07 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.1-alt1
- 2.2.1 released

* Wed Jun 17 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.1-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Wed Feb 13 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1-alt1
- initial
