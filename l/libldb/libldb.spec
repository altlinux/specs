Name: libldb
Version: 1.1.4
Release: alt1
Summary: A schema-less, ldap like, API and database
License: LGPLv3+
Group: System/Libraries
Url: http://ldb.samba.org/

Source: http://samba.org/ftp/ldb/%name-%version.tar
Source2: lib.tar
Source3: buildtools.tar

BuildRequires: python-devel python-module-tdb libpytalloc-devel python-module-tevent
BuildRequires: libtalloc-devel libtdb-devel libtevent-devel libpopt-devel libldap-devel xsltproc docbook-style-xsl docbook-dtds

%description
An extensible library that implements and LDAP like API to access remote LDAP
servers, or use local tdb databases.

%package devel
Group: Development/C
Summary: Developer tools for the LDB library
Requires: %name = %version-%release

%description devel
Header files needed to develop programs that link against the LDB library.

%package -n ldb-tools
Group: Development/Tools
Summary: Tools to manage LDB files

%description -n ldb-tools
Tools to manage LDB files

%package -n python-module-pyldb
Group: Development/Python
Summary: Python bindings for the LDB library
Requires: %name = %version-%release

%description -n python-module-pyldb
Python bindings for the LDB library

%package -n python-module-pyldb-devel
Group: Development/Python
Summary: Development files for the Python bindings for the LDB library
Requires: python-module-pyldb = %version-%release

%description -n python-module-pyldb-devel
Development files for the Python bindings for the LDB library

%prep
%setup -q -a2 -a3

%build
%undefine _configure_gettext
%configure	\
		--prefix=%_usr \
		--disable-rpath \
		--disable-rpath-install \
		--bundled-libraries=NONE \
		--builtin-libraries=tdb_compat,ccan,replace \
		--with-modulesdir=%_libdir/ldb/modules \
		--with-privatelibdir=%_libdir/ldb
%make

%install
%makeinstall_std

rm -f %buildroot%_libdir/*.a

%files
%_libdir/libldb.so.*
%dir %_libdir/ldb
%dir %_libdir/ldb/modules
%dir %_libdir/ldb/modules/ldb
%_libdir/ldb/modules/ldb/*.so

%files devel
%_includedir/*.h
%_libdir/*.so
%_pkgconfigdir/ldb.pc
%_man3dir/*

%exclude %_includedir/pyldb.h
%exclude %_libdir/libpyldb-util.so

%files -n ldb-tools
%_bindir/*
%_man1dir/*
%_libdir/ldb/libldb-cmdline.so

%files -n python-module-pyldb
%python_sitelibdir/ldb.so
%_libdir/libpyldb-util.so.1*

%files -n python-module-pyldb-devel
%_includedir/pyldb.h
%_libdir/libpyldb-util.so
%_pkgconfigdir/pyldb-util.pc

%changelog
* Tue Feb 14 2012 Alexey Shabalin <shaba@altlinux.ru> 1.1.4-alt1
- 1.1.4

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt2.1
- Rebuild with Python-2.7

* Thu Jul 28 2011 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt2
- rebuild with new libtevent

* Wed May 11 2011 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Thu Apr 14 2011 Alexey Shabalin <shaba@altlinux.ru> 1.0.2-alt1
- 1.0.2
- package python bindings

* Fri Aug 13 2010 Alexey Shabalin <shaba@altlinux.ru> 0.9.10-alt1
- initial build for ALT Linux Sisyphus
