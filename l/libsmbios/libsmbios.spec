%define git 4fec2ad

Name: libsmbios
Version: 2.3.3
Release: alt1.0.g%git
License: GPLv2+ or OSL 2.1
Summary: Libsmbios C/C++ shared libraries
Group: System/Libraries
Source: http://linux.dell.com/libsmbios/download/libsmbios/libsmbios-%version/libsmbios-%version.tar.bz2
Url: http://linux.dell.com/libsmbios/main

BuildRequires: strace libxml2-devel gcc-c++ gettext doxygen valgrind cppunit-devel hardlink pkgconfig python-devel

# libsmbios only ever makes sense on intel compatible arches
# no DMI tables on ppc, s390, etc.
ExclusiveArch: x86_64 %ix86

%description
Libsmbios is a library and utilities that can be used by client programs to get
information from standard BIOS tables, such as the SMBIOS table.

This package provides the C-based libsmbios library, with a C interface.

This package also has a C++-based library, with a C++ interface. It is not
actively maintained, but provided for backwards compatibility. New programs
should use the libsmbios C interface.

%package -n smbios-utils
Summary: Binary utilities that use libsmbios
Group: System/Configuration/Hardware

%description -n smbios-utils
Get BIOS information, such as System product name, product id, service tag and
asset tag. Set service and asset tags on Dell machines. Manipulate wireless
cards/bluetooth on Dell laptops. Set BIOS password on select Dell systems.
Update BIOS on select Dell systems. Set LCD brightness on select Dell laptops.

%package -n python-module-smbios
Summary: Python interface to Libsmbios C library
Group: System/Configuration/Hardware
BuildArch: noarch

%description -n python-module-smbios
This package provides a Python interface to libsmbios

%package devel
Summary: Development headers and archives
Group: Development/C++
Requires: %name = %version-%release

%description devel
Libsmbios is a library and utilities that can be used by client programs to get
information from standard BIOS tables, such as the SMBIOS table.

This package contains the headers and .a files necessary to compile new client
programs against libsmbios.


%prep
%setup
find . -type d -exec chmod -f 755 {} \;
find doc src -type f -exec chmod -f 644 {} \;
chmod 755 src/cppunit/*.sh
chmod 755 src/pyunit/*.{sh,py}

%build
%autoreconf
%configure --enable-libsmbios_cxx
%make_build

%check
make check

%install
%makeinstall_std

#Install headers
install -d %buildroot%_includedir
cp -a src/include/*  %buildroot%_includedir/
cp -a out/public-include/*  %buildroot%_includedir/

#instal man
install -pD -m644 doc/smbios-sys-info.4 %buildroot%_man4dir/smbios-sys-info.4

#Remove unused files
rm -rf %buildroot%_libdir/*.a

%find_lang %name

%files
%doc COPYING* README.md src/bin/getopts_LICENSE.txt src/include/smbios/config/boost_LICENSE_1_0_txt
%_libdir/libsmbios*.so.*

%files devel
%_includedir/*
%_libdir/libsmbios*.so
%_pkgconfigdir/*

%files -n smbios-utils -f %name.lang
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/logging.conf
%_sbindir/*
%_datadir/smbios-utils
%_man4dir/*

%files -n python-module-smbios
%python_sitelibdir_noarch/*

%changelog
* Wed Nov 22 2017 L.A. Kostis <lakostis@altlinux.ru> 2.3.3-alt1.0.g4fec2ad
- Updated to 2.3.3-g4fec2ad.

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.28-alt1.2
- Fixed build

* Fri Jul 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.28-alt1.1
- Fixed build

* Tue Jan 03 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.2.28-alt1
- Build for ALT

