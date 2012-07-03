Name: libwpg
Version: 0.1.3
Release: alt2.qa2
Packager: Vitaly Lipatov <lav@altlinux.ru>

Summary: Library for importing and converting Corel WordPerfect(tm) Graphics images

Group: System/Libraries
License: LGPL
Url: http://libwpg.sf.net/

Source: http://prdownloads.sf.net/libwpg/%name-%version.tar.bz2

# Automatically added by buildreq on Sat Nov 03 2007
BuildRequires: doxygen gcc-c++ libwpd-devel

%description
libwpg is a library for reading and converting WPG images

%package tools
Requires: libwpg
Summary: Tools to convert WPG images into other formats
Group: Office

%description tools
Tools to convert WPG images into other formats.
Currently supported: raw svg

%package devel
Requires: libwpg
Requires: libwpd-devel >= 0.8.0
Summary: Files for developing with libwpg
Group: Development/C

%description devel
Includes and definitions for developing with libwpg.

%package docs
Requires: libwpg
BuildRequires: doxygen
Summary: Documentation of libwpg API
Group: Documentation

%description docs
Documentation of libwpg API for developing with libwpg

%prep
%setup

%build
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' configure
%configure

%make_build

%install
%makeinstall_std

%__rm -rf %buildroot%_libdir/libwpg*.la
#%__rm -rf %buildroot $RPM_BUILD_DIR/file.list.%name

%files
%_libdir/libwpg*.so.*
%doc ChangeLog README COPYING AUTHORS

%files tools
%_bindir/wpg2*

%files devel
%_libdir/libwpg*.so
%_pkgconfigdir/libwpg*.pc
%_includedir/libwpg-0.1/

%files docs
%doc %_docdir/%name/

%changelog
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
