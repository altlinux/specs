Name: libiniparser
Version: 3.1
Release: alt2

Group: Development/C
Summary: Simple C library for parsing "INI-style" files
License: MIT
Url: http://ndevilla.free.fr/iniparser/
Source: %name-%version.tar

%description
iniParser is an ANSI C library to parse "INI-style" files,
often used to hold application configuration information.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains the header files, development library and
development documentation for %name.

%prep
%setup

%build
%make_build CFLAGS='%optflags %optflags_shared' libiniparser.so

%install
%define docdir %_docdir/%name-%version
mkdir -p %buildroot{%_libdir,%_includedir,%docdir}
install -pm644 libiniparser.so.0 %buildroot%_libdir/
ln -s libiniparser.so.0 %buildroot%_libdir/libiniparser.so
install -pm644 src/*.h  %buildroot%_includedir/
install -pm644 LICENSE html/* %buildroot%docdir/

%files
%_libdir/*.so.0
%dir %docdir
%docdir/LICENSE

%files devel
%_libdir/*.so
%_includedir/*
%dir %docdir
%docdir/*.*

%changelog
* Thu Apr 26 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 3.1-alt2
- great spec cleanup thanks to ldv@

* Wed Apr 25 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 3.1-alt1
- initial build

