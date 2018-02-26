Name: json-c
Version: 0.9
Release: alt2

Summary: JSON implementation in C
License: MIT
Group: System/Libraries
Url: http://oss.metaparadigm.com/json-c/

Source: %name-%version-%release.tar

%description
JSON-C implements a reference counting object model that allows you to
easily construct JSON objects in C, output them as JSON formatted
strings and parse JSON formatted strings back into the C representation
of JSON objects.

%package -n libjson
Summary: JSON shared library
Group: System/Libraries

%package -n libjson-devel
Summary: header files for libjson
Group: Development/C
Requires: libjson = %version-%release

%description -n libjson
JSON-C implements a reference counting object model that allows you to
easily construct JSON objects in C, output them as JSON formatted
strings and parse JSON formatted strings back into the C representation
of JSON objects.

This package contains shared JSON-C library

%description -n libjson-devel
JSON-C implements a reference counting object model that allows you to
easily construct JSON objects in C, output them as JSON formatted
strings and parse JSON formatted strings back into the C representation
of JSON objects.

This package contains development part of JSON-C

%prep
%setup

%build
%autoreconf
%configure
%make all check

%install
%makeinstall

%files -n libjson
%_libdir/libjson*.so.*

%files -n libjson-devel
%_libdir/libjson*.so
%_includedir/json
%_pkgconfigdir/json.pc

%changelog
* Tue Nov 30 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9-alt2
- updated to svn rev.59

* Tue Aug  4 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9-alt1
- 0.9 released
