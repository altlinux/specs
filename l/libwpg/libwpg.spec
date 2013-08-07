%define major 0.2
Name: libwpg
Version: %major.2
Release: alt3

Summary: Library for importing and converting Corel WordPerfect(tm) Graphics images

Group: System/Libraries
License: LGPL
Url: http://libwpg.sf.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/libwpg/%name-%version.tar

Provides: libwpg2 = %version-%release
Obsoletes: libwpg2

# Automatically added by buildreq on Sat Jan 21 2012
# optimized out: libstdc++-devel pkg-config
BuildRequires: doxygen gcc-c++ glibc-devel libwpd9-devel

%description
libwpg is a library for reading and converting WPG images

%package tools
Requires: %name = %version-%release
Summary: Tools to convert WPG images into other formats
Group: Office

%description tools
Tools to convert WPG images into other formats.
Currently supported: raw svg

%package devel
Requires: %name = %version-%release
Requires: libwpd9-devel >= 0.9.0
Summary: Files for developing with libwpg
Group: Development/C
Provides: libwpg2-devel = %version-%release
Obsoletes: libwpg2-devel

%description devel
Includes and definitions for developing with libwpg.

%package docs
Requires: %name = %version-%release
BuildRequires: doxygen
Summary: Documentation of libwpg API
Group: Documentation
BuildArch: noarch

%description docs
Documentation of libwpg API for developing with libwpg

%prep
%setup

%build
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' configure
%configure --disable-static

%make_build

%install
%makeinstall_std

rm -rf %buildroot%_libdir/libwpg*.la
#rm -rf %buildroot $RPM_BUILD_DIR/file.list.%name

%files
%_libdir/libwpg*.so.*
%doc ChangeLog README AUTHORS

%files tools
%_bindir/wpg2*

%files devel
%_libdir/libwpg*.so
%_pkgconfigdir/libwpg*.pc
%_includedir/libwpg-%major/

%files docs
%doc %_docdir/%name/

%changelog
* Wed Aug 07 2013 Vitaly Lipatov <lav@altlinux.ru> 0.2.2-alt3
- add provides/obsoletes for libwpg2-devel

* Tue Aug 06 2013 Vitaly Lipatov <lav@altlinux.ru> 0.2.2-alt2
- add provides/obsoletes for libwpg2

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 0.2.2-alt1
- new version 0.2.2 (with rpmrb script)

* Tue Apr 23 2013 Repocop Q. A. Robot <repocop@altlinux.org> 0.1.3-alt2.qa3
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * arch-dep-package-consists-of-usr-share for libwpg-docs
  * postclean-03-private-rpm-macros for the spec file

* Tue Apr 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt2.qa2
- Removed bad RPATH

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt2.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Sat Nov 08 2008 Vitaly Lipatov <lav@altlinux.ru> 0.1.3-alt2
- fix docs packing

* Wed Nov 05 2008 Vitaly Lipatov <lav@altlinux.ru> 0.1.3-alt1
- new version 0.1.3 (with rpmrb script)

* Sat Nov 03 2007 Vitaly Lipatov <lav@altlinux.ru> 0.1.0-alt1
- initial build for ALT Linux Sisyphus

* Fri Apr 20 2007 Fridrich Strba <fridrich.strba@bluewin.ch>
- Add documentation packaging
- Make doc and stream optional

* Tue Jan 27 2004 Fridrich Strba <fridrich.strba@bluewin.ch>
- Create rpm spec according to the rpm spec of libwpD
- of Rui M. Seabra
