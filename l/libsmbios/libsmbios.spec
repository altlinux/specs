%define git %nil

Name: libsmbios
Version: 2.4.1
Release: alt2
License: GPLv2+ or OSL 2.1
Summary: Libsmbios C/C++ shared libraries
Group: System/Libraries
Source: %name-%version.tar
Patch: %name-2.4.1-alt-man.patch
Url: https://github.com/dell/libsmbios

BuildRequires(pre): rpm-build-python3
BuildRequires: strace libxml2-devel gettext doxygen valgrind cppunit-devel hardlink pkgconfig python3-devel help2man

# libsmbios only ever makes sense on intel compatible arches
# no DMI tables on ppc, s390, etc.
ExclusiveArch: x86_64 %ix86

# filter out bogus requirements
# due mess with python/python3 code
%add_python_req_skip libsmbios_c
%add_python3_req_skip cli

%description
Libsmbios is a library and utilities that can be used by client programs to get
information from standard BIOS tables, such as the SMBIOS table.

This package provides the C-based libsmbios library, with a C interface.

%package -n smbios-utils
Summary: Binary utilities that use libsmbios
Group: System/Configuration/Hardware
Requires: python3-module-smbios

%description -n smbios-utils
Get BIOS information, such as System product name, product id, service tag and
asset tag. Set service and asset tags on Dell machines. Manipulate wireless
cards/bluetooth on Dell laptops. Set BIOS password on select Dell systems.
Update BIOS on select Dell systems. Set LCD brightness on select Dell laptops.

%package -n python3-module-smbios
Summary: Python interface to Libsmbios C library
Group: System/Configuration/Hardware
Provides: python-module-smbios
Obsoletes: python-module-smbios
BuildArch: noarch

%description -n python3-module-smbios
This package provides a Python interface to libsmbios

%package devel
Summary: Development headers and archives
Group: Development/C
Requires: %name = %version-%release

%description devel
Libsmbios is a library and utilities that can be used by client programs to get
information from standard BIOS tables, such as the SMBIOS table.

This package contains the headers and .a files necessary to compile new client
programs against libsmbios.


%prep
%setup
%patch -p2
find . -type d -exec chmod -f 755 {} \;
find doc src -type f -exec chmod -f 644 {} \;
chmod 755 src/cppunit/*.sh
chmod 755 src/pyunit/*.{sh,py}

%build
%autoreconf
%configure
sed -i 's,^pyexecdir = .*,pyexecdir = $${prefix}%python3_sitelibdir_noarch,' Makefile
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
%doc COPYING* README.md src/bin/getopts_LICENSE.txt src/include/smbios_c/config/boost_LICENSE_1_0_txt
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
%_man1dir/*
%_man4dir/*
%exclude %_datadir/smbios-utils/__pycache__/*-1.pyc

%files -n python3-module-smbios
%python3_sitelibdir_noarch/*

%changelog
* Wed Mar 28 2018 L.A. Kostis <lakostis@altlinux.ru> 2.4.1-alt2
- Skip python req for -utils package.

* Tue Mar 27 2018 L.A. Kostis <lakostis@altlinux.ru> 2.4.1-alt1
- Updated to 2.4.1.
- Build with python3.
- Remove c++ library as discontinued by upstream.

* Wed Nov 22 2017 L.A. Kostis <lakostis@altlinux.ru> 2.3.3-alt1.0.g4fec2ad
- Updated to 2.3.3-g4fec2ad.

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.28-alt1.2
- Fixed build

* Fri Jul 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.28-alt1.1
- Fixed build

* Tue Jan 03 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.2.28-alt1
- Build for ALT

