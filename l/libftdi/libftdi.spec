Summary:   Library to program and control the FTDI USB serial controllers
Name:      libftdi
Version:   0.18
Release:   alt3.1
License: LGPL
Group:     System/Libraries
Vendor:    Intra2net AG
URL:       http://www.intra2net.com/opensource/ftdi/
Packager:  Evgeny Sinelnikov <sin@altlinux.ru>

Source:    %name-%version.tar
Requires:  libusb
BuildRequires: libusb-compat-devel, pkg-config, doxygen
BuildRequires: gcc-c++ boost-devel
BuildRequires: rpm-macros-cmake
BuildRequires: cmake swig
BuildRequires: python-devel rpm-build-python

Patch:     %name-%version-%release.patch

%package   -n libftdipp
Summary:   C++ interface for libftdi library
Group:     System/Libraries

%package   devel
Summary:   Header files and libraries for libftdi
Group:     Development/C
Requires:  libftdi = %version, libusb-devel

%package   -n libftdipp-devel
Summary:   Header files and libraries for libftdipp
Group:     Development/C
Requires:  libftdi-devel = %version
Requires:  boost-devel

%package   devel-static
Summary:   Static libraries for libftdi
Group:     Development/C
Requires:  libftdi-devel = %version

%package   -n libftdipp-devel-static
Summary:   Static libraries for libftdipp
Group:     Development/C
Requires:  libftdipp-devel = %version

%package   -n python-module-ftdi
Summary:   Python bindings for libftdi
Group:     Development/Python
Requires:  libftdi = %version

%package   docs
Summary:   Documentation files for libftdi
Group:     Development/C
BuildArch: noarch

%description 
Userspace library to program and control the FTDI
USB controllers, using libusb, including the popular
bitbang mode. This library talks to next FTDI chips:
FT232BM/245BM, FT2232C/D and FT232/245R.

%description -n libftdipp
Full C++ wrapper for libftdi library

%description devel
Header files for userspace libftdi library

%description -n libftdipp-devel
Header files for full libftdi library C++ wrapper

%description devel-static
Static libraries for userspace libftdi library

%description -n libftdipp-devel-static
Static libraries for full libftdi library C++ wrapper

%description -n python-module-ftdi
Python bindings for libftdi library

%description docs
Documentation files for userspace libftdi library

%prep
%setup
%patch -p1

%build
%cmake_insource
%make_build VERBOSE=1

%install
%makeinstall_std

# Install python bindings
mkdir -p %buildroot%python_sitelibdir
mv %buildroot%_prefix/site-packages/* %buildroot%python_sitelibdir/

# Install man pages
mkdir -p %buildroot%_mandir
cp -a doc/man/* %buildroot%_mandir/

# Fix confict between libqwt-devel-5.2.0-alt7 and libftdi-docs-0.18-alt2
# for /usr/share/man/man3/deprecated.3.gz
mv %buildroot%_man3dir/deprecated.3 %buildroot%_man3dir/ftdi_deprecated.3

%files
%_libdir/libftdi.so.*

%files -n libftdipp
%_libdir/libftdipp.so.*

%files devel
%_bindir/libftdi-config
%_libdir/lib*.so
%_libdir/pkgconfig/libftdi.pc
%dir %_includedir/%name
%_includedir/%name/*.h

%files -n libftdipp-devel
%_libdir/pkgconfig/libftdipp.pc
%_includedir/%name/*.hpp

%files devel-static
%_libdir/libftdi.a

%files -n libftdipp-devel-static
%_libdir/libftdipp.a

%files -n python-module-ftdi
%python_sitelibdir/*.py
%python_sitelibdir/*.so

%files docs
%doc doc/html
%_man3dir/*

%changelog
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

