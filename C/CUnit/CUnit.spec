Name: CUnit
Version: 2.1.2
Release: alt1
Summary: A lightweight system for unit tests in C

Group: System/Libraries
License: LGPLv2+
Url: http://cunit.sourceforge.net/
Packager: Mykola Grechukh <gns@altlinux.ru>

Source: http://downloads.sourceforge.net/cunit/%name-%version.tar

BuildRequires: libncurses-devel

%description
CUnit is a lightweight system for writing, administering, and running unit
tests in C.  It provides C programmers a basic testing functionality with a
flexible variety of user interfaces.

CUnit is built as a static library which is linked with the user's testing
code. It uses a simple framework for building test structures, and provides
a rich set of assertions for testing common data types.  In addition,
several different interfaces are provided for running tests and reporting
results.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup
sed -i '/^CURSES_OBJECT_FILES_SHARED/ s,$, -l\$\(CURSES_LIB\),' CUnit/Sources/Makefile.am

%build
autoreconf -fisv
%configure \
	--enable-curses \
	--disable-static
%make_build

%install
%makeinstall_std

# move /usr/doc/CUnit
mv -f %buildroot%prefix/doc/%name docs
rm -rf docs/headers

%files
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%_libdir/*.so.*
%_datadir/%name
%_mandir/*/%{name}*

%files devel
%doc docs/*
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%changelog
* Mon Nov 14 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 2.1.2-alt1
- New version

* Thu Oct 28 2010 Mykola Grechukh <gns@altlinux.ru> 2.1.0-alt1
- initial build for ALT Linux Sisyphus

* Wed May 28 2008 Peter Hanecak <hany@hany.sk> 2.1.0-1
- initial spec
