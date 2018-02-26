Name: libewf
Version: 20080501
Release: alt1.qa2

Summary: Library and tools to support the Expert Witness Compression Format

Url: https://www.uitwisselplatform.nl/projects/libewf/
Group: System/Libraries
License: BSD

Packager: Vitaly Lipatov <lav@altlinux.ru>


Source: https://www.uitwisselplatform.nl/frs/download.php/529/%name-%version.tar.gz

# Automatically added by buildreq on Thu Jan 10 2008
BuildRequires: gcc-c++ libssl-devel libuuid-devel zlib-devel

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

%prep
%setup -q

%build
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS COPYING NEWS README
%_bindir/ewfacquire
%_bindir/ewfacquirestream
%_bindir/ewfexport
%_bindir/ewfinfo
%_bindir/ewfverify
%_libdir/*.so.*
%_man1dir/*

### Exclude expirimental files ###
%exclude %_bindir/ewfalter
%exclude %_pkgconfigdir/libewf.pc

%files devel
%doc AUTHORS COPYING NEWS README ChangeLog
%_libdir/*.so
%_includedir/%name/
%_includedir/%name.h
%_man3dir/*

%changelog
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

* Mon Jan 15 2007 Joachim Metz <forensics@hoffmannbv.nl> 20070115-1
- Added ewfacquirestream to package

* Fri Dec 29 2006 Joachim Metz <forensics@hoffmannbv.nl> 20061229-1
- Added exclusion of new expirimental addtitions

* Tue Dec 26 2006 Christophe Grenier <grenier@cgsecurity.org> 20061223-2
- Made small correction to the spec file, removed abundant Requires line

* Sat Dec 23 2006 Joachim Metz <forensics@hoffmannbv.nl> 20061223-1
- Made small corrections to the spec file input by Christophe Grenier
- Added --libdir to ./configure to correct for %%_libdir64

* Sat Dec 19 2006 Joachim Metz <forensics@hoffmannbv.nl> 20061219-1
- Made small corrections to the spec file input by Christophe Grenier
- The library source package no longer contains a release number

* Sat Dec 16 2006 Christophe Grenier <grenier@cgsecurity.org> 20061213-2
- Fixed the spec file

* Sat Dec 9 2006 Joachim Metz <forensics@hoffmannbv.nl> 20061213-1
- Initial version

