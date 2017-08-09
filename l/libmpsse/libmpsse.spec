Name:         libmpsse
Version:      20161223
Release:      alt2

Summary:      Open source library for SPI/I2C control via FTDI chips
Group:        System/Libraries
URL:          https://github.com/devttys0/libmpsse
License:      BSD

Source:       %name-%version.tar
Patch1:       %name-%version-alt-build.patch
BuildRequires: libftdi1-devel

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
%patch1 -p1

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
* Wed Aug 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 20161223-alt2
- Switched to libftdi1.

* Thu Dec 22 2016 Vladislav Zavjalov <slazav@altlinux.org> 20161223-alt1
- build for altlinux, latest github version
- built without python, with libftdi
