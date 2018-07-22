Name:         libmpsse
Version:      1.3.2
Release:      alt1

Summary:      Open source library for SPI/I2C control via FTDI chips
Group:        System/Libraries
#URL:          https://github.com/devttys0/libmpsse
URL:          https://github.com/l29ah/libmpsse
License:      BSD

Packager:     Vladislav Zavjalov <slazav@altlinux.org>

Source:       %name-%version.tar
BuildRequires: libftdi1-devel swig python-dev
Requires:      libftdi1

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
autoreconf
%configure
%make_build
%makeinstall_std

%files
%_libdir/*.so
%python_sitelibdir/*.so
%python_sitelibdir/*.py

%files devel
%_includedir/*
%_libdir/*.a

%changelog
* Sun Jul 22 2018 Vladislav Zavjalov <slazav@altlinux.org> 1.3.2-alt1
- v.1.3.2, switch to new upstream (devttys0@github -> l29ah@github)
- turn on python bindings

* Wed Aug 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 20161223-alt2
- Switched to libftdi1.

* Thu Dec 22 2016 Vladislav Zavjalov <slazav@altlinux.org> 20161223-alt1
- build for altlinux, latest github version
- built without python, with libftdi
