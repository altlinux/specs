%define api_ver 1

%def_enable man

Name: liblqr
Version: 0.4.3
Release: alt1

Summary: LiquidRescale library
Group: System/Libraries
License: LGPL-3.0
Url: https://liblqr.wikidot.com/

Vcs: https://github.com/carlobaldassi/liblqr.git

Source: https://github.com/carlobaldassi/liblqr/archive/v%version/%name-%version.tar.gz
#Source: http://liblqr.wikidot.com/local--files/en:download-page/%name-%api_ver-%version.tar.bz2

BuildRequires: gcc-c++ glib2-devel
%{?_enable_man:BuildRequires: xsltproc docbook-dtds docbook-style-xsl}

%description
The LiquidRescale (lqr) library provides a C/C++ API for
performing non-uniform resizing of images by the seam-carving
technique.

%package devel
Summary: LiquidRescale library development kit
Group: System/Libraries
License: LGPL-3.0
Requires: %name = %EVR

%description devel
The libqr-devel package contains the header files
needed to develop applications with liblqr.

%prep
%setup -n %name-%version

%build
%autoreconf
%configure \
    %{?_enable_man:--enable-install-man}
%nil
%make_build

%install
%makeinstall_std

%files
%_libdir/%name-%api_ver.so.*
%doc README ChangeLog NEWS

%files devel
%_libdir/%name-%api_ver.so
%_includedir/lqr-%api_ver/
%_pkgconfigdir/lqr-%api_ver.pc
%{?_enable_man:%_man3dir/*}

%changelog
* Sun Sep 01 2024 Yuri N. Sedunov <aris@altlinux.org> 0.4.3-alt1
- 0.4.3

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
