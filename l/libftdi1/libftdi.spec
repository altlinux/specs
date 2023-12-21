Summary:   Library to program and control the FTDI USB serial controllers
Name:      libftdi1
Version:   1.5
Release:   alt3.1
License:   LGPL for libftdi and GPLv2+linking exception for the C++ wrapper
Group:     System/Libraries
URL:       http://www.intra2net.com/en/developer/libftdi
Packager:  Evgeny Sinelnikov <sin@altlinux.ru>

Source:    %name-%version.tar
BuildRequires: libusb-devel, pkg-config, doxygen
BuildRequires: gcc-c++ boost-devel
BuildRequires: rpm-macros-cmake
BuildRequires: cmake swig
BuildRequires: python3-devel rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: libconfuse-devel


%define    namepp libftdipp1
%define    pyname python3-module-ftdi1

%define    soname libftdi1
%define    sonamepp libftdipp1

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

Patch:     %name-%version-alt.patch

%package   -n %namepp
Summary:   C++ interface for libftdi library
Group:     System/Libraries

%package   devel
Summary:   Header files and libraries for libftdi
Group:     Development/C
Requires:  %name = %version, libusb-devel

%package   -n ftdi-eeprom
Summary:   Tool for reading/erasing/flashing FTDI USB chip eeproms
Group:     Development/C

%package   -n %namepp-devel
Summary:   Header files and libraries for libftdipp
Group:     Development/C
Requires:  %name-devel = %version
Requires:  boost-devel

%package   devel-static
Summary:   Static libraries for libftdi
Group:     Development/C
Requires:  %name-devel = %version
Conflicts: libftdi-devel

%package   -n %namepp-devel-static
Summary:   Static libraries for libftdipp
Group:     Development/C
Requires:  %namepp-devel = %version

%package   -n %pyname
Summary:   Python bindings for libftdi
Group:     Development/Python
Requires:  %name = %version
AutoReqProv: yes,nopython

%package   docs
Summary:   Documentation files for libftdi
Group:     Development/C
BuildArch: noarch

%description 
Userspace library to program and control the FTDI
USB controllers, using libusb, including the popular
bitbang mode. This library talks to next FTDI chips:
FT232BM/245BM, FT2232C/D and FT232/245R.

%description -n %namepp
Full C++ wrapper for libftdi library

%description devel
Header files for userspace libftdi library

%description -n ftdi-eeprom
ftdi-eeprom is a small tool for creating and uploading the configuration
eeprom for the FTDI chip. This eeprom contains information such as vendor
and product ID, manufacturer and product strings, revision, etc.

%description -n %namepp-devel
Header files for full libftdi library C++ wrapper

%description devel-static
Static libraries for userspace libftdi library

%description -n %namepp-devel-static
Static libraries for full libftdi library C++ wrapper

%description -n %pyname
Python bindings for libftdi library

%description docs
Documentation files for userspace libftdi library

%prep
%setup
%patch -p1

%build
%cmake_insource \
    -D DOCUMENTATION=1 \
    -D PYTHON_BINDINGS=1 \
    -D FTDIPP=1 \
    -D FTDI_EEPROM=1 \
    -D EXAMPLES=1 \
    -D BUILD_TESTS=1
%make_build VERBOSE=1

%install
%makeinstall_std

# Install man pages
mkdir -p %buildroot%_mandir
cp -a doc/man/* %buildroot%_mandir/
mv %buildroot%_man3dir/size_and_time.3 %buildroot%_man3dir/ftdi_size_and_time.3
if test -f %buildroot%_man3dir/Libftdi.3; then
    mv %buildroot%_man3dir/Libftdi.3 %buildroot%_man3dir/libftdi.3
fi

%files
%_libdir/%soname.so.*

%files -n %namepp
%_libdir/%sonamepp.so.*

%files devel
%_bindir/%soname-config
%_libdir/%soname.so
%_libdir/pkgconfig/%soname.pc
%_includedir/%name/*.h
%_libdir/cmake/%name/*.cmake

%files -n ftdi-eeprom
%_bindir/ftdi_eeprom
%_docdir/%name/example.conf
%_man3dir/ftdi_eeprom*

%files -n %namepp-devel
%_libdir/%sonamepp.so
%_libdir/pkgconfig/%sonamepp.pc
%_includedir/%name/*.hpp

%files devel-static
%_libdir/%soname.a

%files -n %namepp-devel-static
%_libdir/%sonamepp.a

%files -n %pyname
%python3_sitelibdir/*.py*
%python3_sitelibdir/*.so
%python3_sitelibdir/*/ftdi1.*
%_datadir/libftdi/examples/*.py

%files docs
%doc doc/html
%_man3dir/*
%exclude %_man3dir/ftdi_eeprom*

%changelog
* Thu Dec 21 2023 Grigory Ustinov <grenka@altlinux.org> 1.5-alt3.1
- NMU: added build dependency on setuptools

* Thu Sep 16 2021 Ilya Mashkin <oddity@altlinux.ru> 1.5-alt3
- NMU: rebuild with new libconfuse
- Temporary disable LTO

* Mon Apr 05 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5-alt2
- fix broken libftdi1.pc file
- built python3 bindings

* Wed Mar 31 2021 Evgeny Sinelnikov <sin@altlinux.org> 1.5-alt1
- Update to latest release
- Implement tc[io]flush methods and deprecate broken purge_buffers methods

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.4-alt5
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 1.4-alt4
- NMU: remove %ubt from release

* Mon Oct 15 2018 Ivan A. Melnikov <iv@altlinux.org> 1.4-alt3%ubt
- Fix documentation build

* Tue Aug 15 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.4-alt2%ubt
- Fix non-identical noarch with Libftdi.3 man on x86_64 instead of libftdi.3

* Thu Aug 10 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.4-alt1%ubt
- Update to latest release
- Build with universal build tag (aka ubt macros)

* Sat May 21 2016 Evgeny Sinelnikov <sin@altlinux.ru> 1.3-alt1
- Update to latest release
- Include ftdi_eeprom subpackage

* Tue Mar 19 2013 Evgeny Sinelnikov <sin@altlinux.ru> 1.0-alt1
- Build new package libftdi1 with soname 2.0.0 using libusb1

* Thu Aug 30 2012 Evgeny Sinelnikov <sin@altlinux.ru> 0.20-alt1
- Update to last release 0.20

* Wed Aug 29 2012 Repocop Q. A. Robot <repocop@altlinux.org> 0.18-alt3.1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * vendor-tag for libftdipp-devel-static
  * vendor-tag for libftdipp-debuginfo
  * vendor-tag for libftdi
  * vendor-tag for libftdi-devel
  * vendor-tag for libftdipp
  * vendor-tag for libftdi-devel-static
  * vendor-tag for libftdipp-devel
  * vendor-tag for libftdi-docs
  * vendor-tag for libftdi-debuginfo
  * vendor-tag for python-module-ftdi
  * vendor-tag for python-module-ftdi-debuginfo

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.18-alt3.1
- Rebuild with Python-2.7

* Mon May 09 2011 Evgeny Sinelnikov <sin@altlinux.ru> 0.18-alt3
- Build documentation as noarch package
- Fix file conflict for deprecated.3.gz man page with libqwt-devel-5.2.0-alt7

* Mon May 02 2011 Evgeny Sinelnikov <sin@altlinux.ru> 0.18-alt2
- Build python-module-ftdi with libftdi python bindings

* Mon May 02 2011 Evgeny Sinelnikov <sin@altlinux.ru> 0.18-alt1
- Update to 0.18

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.17-alt3
- Rebuilt for debuginfo

* Tue May 11 2010 Evgeny Sinelnikov <sin@altlinux.ru> 0.17-alt2
- Build without rpm macros hack for cmake

* Sun May 02 2010 Evgeny Sinelnikov <sin@altlinux.ru> 0.17-alt1
- Update to 0.17
- Build with cmake

* Sun Jun 28 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.16-alt2
- Build with new scheme from original git
- Replace manpages to system directory man3

* Sun Jun 28 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.16-alt1
- Update to 0.16
- Rebuild with boost-1.39.0

* Thu Apr 16 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.15-alt2
- Rebuild with compat wrapper library for libusb-1.0

* Mon Jan 05 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.15-alt1
- Update to 0.15
- Add new libftdipp subpackages for C++ wrapper

* Fri Nov 21 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.14-alt1
- Update to 0.14

* Wed Mar 12 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.11-alt1
- Update to 0.11

* Mon Jul 02 2007 Evgeny Sinelnikov <sin@altlinux.ru> 0.10-alt1
- Update to 0.10

* Mon Jun 20 2005 Evgeny Sinelnikov <sin@altlinux.ru> 0.6-alt1
- Update to next version
+ Set library version on .so file again
+ Configurable serial line parameters
+ Improved filtering of status bytes - Fix small flow bug
+ Extended FT2232C support
+ Small improvement to the baudrate calculation code
+ Error handling cleanup

* Thu Sep 30 2004 Evgeny Sinelnikov <sin@altlinux.ru> 0.5-alt1
- Update to next version

* Mon Aug 09 2004 Evgeny Sinelnikov <sin@altlinux.ru> 0.4-alt5
- add ftdi_usb_reopen() function for testing

* Sat Aug 07 2004 Evgeny Sinelnikov <sin@altlinux.ru> 0.4-alt4
- add ignore status bytes with chunk sizes above than 64

* Mon Jul 26 2004 Evgeny Sinelnikov <sin@altlinux.ru> 0.4-alt3
- merge changes to upstream
+ some cosmetic changes

* Fri Jul 23 2004 Evgeny Sinelnikov <sin@altlinux.ru> 0.4-alt2
- add function to open device by description or serial

* Fri Jul 23 2004 Evgeny Sinelnikov <sin@altlinux.ru> 0.4-alt1
- initial release
+ add patch: ftdi_read_data() lose usb errors
             ftdi_write_data() lose usb errors

