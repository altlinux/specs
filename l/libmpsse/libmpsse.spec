Name:         libmpsse
Version:      1.3.2
Release:      alt3

Summary:      Open source library for SPI/I2C control via FTDI chips
Group:        System/Libraries
#URL:          https://github.com/devttys0/libmpsse
URL:          https://github.com/l29ah/libmpsse
License:      BSD

Packager:     Vladislav Zavjalov <slazav@altlinux.org>

Source:       %name-%version.tar
BuildRequires: libftdi1-devel swig python-devel
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

%install
%makeinstall_std -C src

%files
%_libdir/*.so
%python_sitelibdir/*.so
%python_sitelibdir/*.py*
%exclude %_libdir/*.a

%files devel
%_includedir/*

%changelog
* Sun Dec 01 2019 Vladislav Zavjalov <slazav@altlinux.org> 1.3.2-alt3
- change python->python2 in configure.ac (fix Altlinux build)

* Mon Jul 23 2018 Vladislav Zavjalov <slazav@altlinux.org> 1.3.2-alt2
- fix Repocop warnings:
  altlinux-python-obsolete-buildreq-python-dev
  library-pkgnames-static

* Sun Jul 22 2018 Vladislav Zavjalov <slazav@altlinux.org> 1.3.2-alt1
- v.1.3.2, switch to new upstream (devttys0@github -> l29ah@github)
- turn on python bindings

* Wed Aug 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 20161223-alt2
- Switched to libftdi1.

* Thu Dec 22 2016 Vladislav Zavjalov <slazav@altlinux.org> 20161223-alt1
- build for altlinux, latest github version
- built without python, with libftdi
