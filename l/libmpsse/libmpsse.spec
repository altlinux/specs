Name:         libmpsse
Version:      20161223
Release:      alt1

Summary:      Open source library for SPI/I2C control via FTDI chips
Group:        System/Libraries
URL:          https://github.com/devttys0/libmpsse
License:      BSD

Packager:     Vladislav Zavjalov <slazav@altlinux.org>

Source:       %name-%version.tar
BuildRequires: libftdi-devel
Requires:      libftdi

%description
Open source library for SPI/I2C control via FTDI chips

%package devel
Summary: Development files for %name.
Group:   System/Libraries
Requires: %name = %version-%release

%description devel
Open source library for SPI/I2C control via FTDI chips, development files.

%prep
%setup -q

%build
cd src
%configure --disable-python
%make_install
mkdir -p %buildroot/%_libdir/ %buildroot/%_includedir/
install -m644 libmpsse.so %buildroot/%_libdir/
install -m644 libmpsse.a  %buildroot/%_libdir/
install -m644 mpsse.h     %buildroot/%_includedir/

%files
%_libdir/*.so

%files devel
%_includedir/*
%_libdir/*.a

%changelog
* Thu Dec 22 2016 Vladislav Zavjalov <slazav@altlinux.org> 20161223-alt1
- build for altlinux, latest github version
- built without python, with libftdi
