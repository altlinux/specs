Name: libjson
Version: 0.10
Release: alt3

Summary: JSON implementation in C
License: MIT
Group: System/Libraries
Url: https://github.com/json-c/json-c/wiki

Source: %name-%version-%release.tar
# git://github.com/json-c/json-c.git

%description
JSON-C implements a reference counting object model that allows you to
easily construct JSON objects in C, output them as JSON formatted
strings and parse JSON formatted strings back into the C representation
of JSON objects.

%package devel
Summary: header files for libjson
Group: Development/C
Requires: libjson = %version-%release

%description devel
JSON-C implements a reference counting object model that allows you to
easily construct JSON objects in C, output them as JSON formatted
strings and parse JSON formatted strings back into the C representation
of JSON objects.

This package contains development part of JSON-C

%prep
%setup

%build
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
%_includedir/json
%_pkgconfigdir/json.pc

%changelog
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
