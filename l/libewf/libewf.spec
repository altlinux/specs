%def_disable python3

Name: libewf
Version: 20171104
Release: alt3

Summary: Library and tools to support the Expert Witness Compression Format

Url: http://code.google.com/p/libewf
Group: System/Libraries
License: BSD

# Source-url: https://googledrive.com/host/0B3fBvzttpiiSMTdoaVExWWNsRjg/libewf-20140406.tar.gz
Source: %name-%version.tar

BuildRequires: gcc-c++ libssl-devel libuuid-devel zlib-devel

BuildPreReq: libfuse-devel flex

%if_enabled python3
BuildRequires: python3-devel
%endif

%description
libewf is library for support of the Expert Witness Compression Format (EWF).
libewf allows you to read media information of EWF files in the SMART (EWF-S01)
format and the EnCase (EWF-E01) format. libewf allows to read files created by
EnCase 1 to 5, linen and FTK Imager.

Several tools for reading and writing EWF files are included in this package.

%package devel
Summary: Header files and libraries for developing applications which will use libewf
Group: Development/C
Requires: libewf = %version-%release

%description devel
Header files and libraries for developing applications which will use libewf.

%if_enabled python3
%package -n python3-module-pyewf
Summary: python3 bindings for libewf
Group: Development/Python3
Requires: libewf = %version-%release

%description -n python3-module-pyewf
libewf is library for support of the Expert Witness Compression Format (EWF).
libewf allows you to read media information of EWF files in the SMART (EWF-S01)
format and the EnCase (EWF-E01) format. libewf allows to read files created by
EnCase 1 to 5, linen and FTK Imager.

This package contains python3 bindings for libewf.
%endif

%prep
%setup

%build
%autoreconf
%configure \
	--disable-static \
	--disable-rpath \
	%{subst_enable python3} \
	--enable-wide-character-type
%make_build

%install
%makeinstall_std

find %buildroot -name '*.la' -delete

%files
%doc AUTHORS COPYING NEWS README
%_bindir/*
%_libdir/*.so.*
%_man1dir/*

%files devel
%doc AUTHORS COPYING NEWS README ChangeLog
%_libdir/*.so
%_includedir/%name/
%_includedir/%name.h
%_man3dir/*
%_pkgconfigdir/libewf.pc

%if_enabled python3
%files -n python3-module-pyewf
%python3_sitelibdir/*.so
%endif

%changelog
* Wed Dec 20 2023 Grigory Ustinov <grenka@altlinux.org> 20171104-alt3
- Add knob for building without python.

* Mon Sep 25 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 20171104-alt2
- NMU: fixed FTBFS with OpenSSL 3.

* Wed Sep 11 2019 Grigory Ustinov <grenka@altlinux.org> 20171104-alt1
- Build new version.
- Transfer to python3.

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 20140608-alt1.qa1.1
- NMU: Rebuild with new openssl 1.1.0.

* Thu Apr 27 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 20140608-alt1.qa1
- Fixed build with gcc >= 5.

* Tue Sep 02 2014 Vitaly Lipatov <lav@altlinux.ru> 20140608-alt1
- new version 20140608 (with rpmrb script)

* Tue Apr 15 2014 Michael Shigorin <mike@altlinux.org> 20140406-alt1
- NMU: 20140406

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 20130416-alt1
- new version 20130416 (with rpmrb script)

* Thu Aug 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20120813-alt1
- Version 20120813

* Wed Aug 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20080501-alt1.qa4
- Really fixed build with new glibc

* Wed Aug 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20080501-alt1.qa3
- Fixed build with new glibc

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 20080501-alt1.qa2
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 20080501-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libewf
  * postun_ldconfig for libewf
  * postclean-05-filetriggers for spec file

* Fri Nov 07 2008 Vitaly Lipatov <lav@altlinux.ru> 20080501-alt1
- new version 20080501

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 20070512-alt1
- initial build for ALT Linux Sisyphus
