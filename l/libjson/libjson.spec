Name: libjson
Version: 0.12.1
Release: alt2

Summary: JSON implementation in C
License: MIT
Group: System/Libraries
Url: https://github.com/json-c/json-c/wiki

Source: %name-%version-%release.tar
# git://github.com/json-c/json-c.git
Provides: libjson-c = %EVR
Obsoletes: libjson-c < %EVR

%description
JSON-C implements a reference counting object model that allows you to
easily construct JSON objects in C, output them as JSON formatted
strings and parse JSON formatted strings back into the C representation
of JSON objects.

%package devel
Summary: header files for libjson
Group: Development/C
Requires: libjson = %EVR
Provides: libjson-c-devel = %EVR
Obsoletes: libjson-c-devel < %EVR

%description devel
JSON-C implements a reference counting object model that allows you to
easily construct JSON objects in C, output them as JSON formatted
strings and parse JSON formatted strings back into the C representation
of JSON objects.

This package contains development part of JSON-C

%prep
%setup

%build
%add_optflags -Wno-error=unused-but-set-variable
%autoreconf
%configure --disable-static
%make

%install
%makeinstall

%check
%make check

%files
%_libdir/libjson*.so.*

%files devel
%_libdir/libjson*.so
%_includedir/json-c
%_pkgconfigdir/json-c.pc

%changelog
* Thu May 04 2017 Andrey Cherepanov <cas@altlinux.org> 0.12.1-alt2
- Obsoletes libjson-c

* Tue May 02 2017 Andrey Cherepanov <cas@altlinux.org> 0.12.1-alt1
- New version

* Fri Sep 18 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.10-alt3
- Fixed FTBFS.

* Tue May 27 2014 Alexey Shabalin <shaba@altlinux.ru> 0.10-alt2
- rename source package from json-c to libjson

* Fri Dec 07 2012 Alexey Shabalin <shaba@altlinux.ru> 0.10-alt1
- 0.10

* Tue Nov 30 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9-alt2
- updated to svn rev.59

* Tue Aug  4 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9-alt1
- 0.9 released
