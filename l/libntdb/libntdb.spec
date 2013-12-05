Name: libntdb
Version: 1.0
Release: alt1
Summary: A not-so trivial database
License: LGPLv3+
Group: System/Libraries
Url: http://tdb.samba.org/

Source: http://samba.org/ftp/tdb/%name-%version.tar
Source2: lib.tar
Source3: buildtools.tar

BuildRequires: python-devel
BuildRequires: xsltproc docbook-style-xsl docbook-dtds

%description
This is a simple database API.
If you have previously used the tdb library from Samba, much of
this will seem familiar, but there are some API changes which a
compiler will warn you about if you simply replace 'tdb' with
'ntdb' in your code!  The on-disk format for ntdb is
incompatible with tdb.

%package devel
Group: Development/C
Summary: Developer tools for the NTDB library
Requires: %name = %version-%release

%description devel
This is a simple database API.
If you have previously used the tdb library from Samba, much of
this will seem familiar, but there are some API changes which a
compiler will warn you about if you simply replace 'tdb' with
'ntdb' in your code!  The on-disk format for ntdb is
incompatible with tdb.

These are the development files.

%package -n ntdb-utils
Group: Development/Tools
Summary: A not-so trivial database utils
Requires: %name = %version-%release

%description -n ntdb-utils
This is a simple database API.
If you have previously used the tdb library from Samba, much of
this will seem familiar, but there are some API changes which a
compiler will warn you about if you simply replace 'tdb' with
'ntdb' in your code!  The on-disk format for ntdb is
incompatible with tdb.

This package contains some utils for managing ntdb databases

%package -n python-module-ntdb
Group: Development/Python
Summary: Python bindings for the NTDB library
Requires: %name = %version-%release

%description -n python-module-ntdb
Python bindings for the NTDB library

%prep
%setup -q -a2 -a3

%build
%undefine _configure_gettext
%configure	\
		--disable-rpath \
		--disable-rpath-install

%make_build

%install
%makeinstall_std

rm -f %buildroot%_libdir/*.a

%files
%_libdir/lib*.so.*

%files devel
%_includedir/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc
%_man3dir/*

%files -n ntdb-utils
%_bindir/*
%_man8dir/*

%files -n python-module-ntdb
%python_sitelibdir/ntdb.so

%changelog
* Wed Dec 04 2013 Alexey Shabalin <shaba@altlinux.ru> 1.0-alt1
- initial build for ALT Linux Sisyphus
