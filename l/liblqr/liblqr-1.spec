%define api_ver 1

Name: liblqr
Version: 0.4.2
Release: alt1

Summary: LiquidRescale library
Group: System/Libraries
License: GPLv3
Url: http://liquidrescale.wikidot.com/

Source: http://liblqr.wikidot.com/local--files/en:download-page/%name-%api_ver-%version.tar.bz2

BuildRequires: gcc-c++ glib2-devel

%description
The LiquidRescale (lqr) library provides a C/C++ API for
performing non-uniform resizing of images by the seam-carving
technique.

%package devel
Summary: LiquidRescale library  development kit
Group: System/Libraries
License: GPLv3
Requires: %name = %version-%release

%description devel
The libqr-devel package contains the header files
needed to develop applications with liblqr

%prep
%setup -n %name-%api_ver-%version

%build
%configure
%make_build

%install
%makeinstall_std

%files
%_libdir/%name-%api_ver.so.*
%doc README ChangeLog

%files devel
%_libdir/%name-%api_ver.so
%_includedir/lqr-%api_ver/
%_libdir/pkgconfig/lqr-%api_ver.pc
%doc docs/liblqr_manual.docbook

%changelog
* Tue Oct 29 2013 Yuri N. Sedunov <aris@altlinux.org> 0.4.2-alt1
- 0.4.2

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt2.1_2
- initial import by fcimport

* Wed Mar 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt2.1
- Rebuilt for debuginfo

* Wed Nov 10 2010 Victor Forsiuk <force@altlinux.org> 0.4.1-alt2
- Rebuilt for soname set-versions.

* Wed Jul 08 2009 Victor Forsyuk <force@altlinux.org> 0.4.1-alt1
- 0.4.1

* Tue Dec 16 2008 Victor Forsyuk <force@altlinux.org> 0.2.1-alt2
- Remove obsolete ldconfig calls.

* Thu Nov 06 2008 Victor Forsyuk <force@altlinux.org> 0.2.1-alt1
- 0.2.1

* Wed Apr 02 2008 Victor Forsyuk <force@altlinux.org> 0.1.0-alt1
- Initial build.
