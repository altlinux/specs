Name: kyotocabinet
Version: 1.2.76
Release: alt1
Summary: library of routines for managing a database

Group: Databases
License: GPLv3
Url: http://fallabs.com/kyotocabinet/

Source: %name-%version.tar

BuildRequires: gcc-c++ zlib-devel

%description
Kyoto Cabinet is a library of routines for managing a database. The
database is a simple data file containing records, each is a pair of
a key and a value. Every key and value is serial bytes with variable
length. Both binary data and character string can be used as a key and
a value. Each key must be unique within a database. There is neither
concept of data tables nor data types. Records are organized in hash
table or B+ tree.
Kyoto Cabinet runs very fast. For example, elapsed time to store one
million records is 0.9 seconds for hash database, and 1.1 seconds for
B+ tree database. Moreover, the size of database is very small. For
example, overhead for a record is 16 bytes for hash database, and 4
bytes for B+ tree database. Furthermore, scalability of Kyoto Cabinet
is great. The database size can be up to 8EB (9.22e18 bytes).

%package utils
Summary: Command line tools for managing kyotocabinet databases
Group: Databases
Requires: lib%name = %version-%release

%description utils
This package contains command line tools for managing kyotocabinet
databases.

%package -n lib%name
Summary: kyotocabinet library
Group: System/Libraries
%description -n lib%name
%summary

%package -n lib%name-devel
Summary: development files for %name
Group: Development/C++
Requires: lib%name = %version-%release
%description -n lib%name-devel
%summary

%package doc
Summary: development documentation for %name
Group: Development/Documentation
Requires: lib%name = %version-%release
BuildArch: noarch
%description doc
%summary

%prep
%setup -q

%build
%configure
%make_build

%check
%make check

%install
%makeinstall_std
mv %buildroot%_defaultdocdir/%name %buildroot%_defaultdocdir/%name-%version
rm %buildroot%_libdir/lib%name.a

%files utils
%_bindir/kc*
%_man1dir/kc*

%files -n lib%name
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_includedir/kc*
%_libdir/lib%name.so
%_libdir/pkgconfig/%name.pc

%files doc
%_defaultdocdir/%name-%version

%changelog
* Wed Jul 04 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.76-alt1
- New version 1.2.76

* Wed Sep 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.70-alt1
- New version 1.2.70

* Mon Jul 11 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.67-alt1
- New version 1.2.67

* Wed Jun 15 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.62-alt1
- New version 1.2.62 (ALT #25756)

* Sat Mar 05 2011 Vladimir Lettiev <crux@altlinux.ru> 1.2.48-alt1
- New version 1.2.48

* Thu Mar 03 2011 Vladimir Lettiev <crux@altlinux.ru> 1.2.47-alt1
- New version 1.2.47

* Sun Feb 27 2011 Vladimir Lettiev <crux@altlinux.ru> 1.2.46-alt1
- New version 1.2.46

* Fri Feb 18 2011 Vladimir Lettiev <crux@altlinux.ru> 1.2.44-alt1
- initial build

