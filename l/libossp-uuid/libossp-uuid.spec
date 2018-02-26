Name: libossp-uuid
Version: 1.5.1
Release: alt1.2
Summary: Universally Unique Identifier library
License: MIT
Group: System/Libraries
Url: http://www.ossp.org/pkg/lib/uuid/
Packager: Michael Bochkaryov <misha@altlinux.ru>

Source: uuid-%version.tar.bz2
Patch: ossp-uuid.patch

# Automatically added by buildreq on Thu Mar 04 2010 (-bb)
BuildRequires: gcc-c++ gcc-fortran glibc-devel-static postgresql-devel termutils

BuildRequires: %_bindir/libtool

%description
OSSP uuid is a ISO-C:1999 application programming interface (API)
and corresponding command line interface (CLI) for the generation
of DCE 1.1, ISO/IEC 11578:1996 and RFC 4122 compliant Universally
Unique Identifier (UUID). It supports DCE 1.1 variant UUIDs of version
1 (time and node based), version 3 (name based, MD5), version 4
(random number based) and version 5 (name based, SHA-1). Additional
API bindings are provided for the languages ISO-C++:1998, Perl:5 and
PHP:4/5. Optional backward compatibility exists for the ISO-C DCE-1.1
and Perl Data::UUID APIs.

%package devel
Summary: Development support for Universally Unique Identifier library
Group: Development/C
Requires: %_pkgconfigdir
Requires: %name = %version-%release

%description devel
Development headers and libraries for OSSP uuid.

%package dce
Summary: DCE support for Universally Unique Identifier library
Group: Development/C
Requires: %name = %version-%release

%description dce
DCE OSSP uuid library.

%package dce-devel
Summary: DCE development support for Universally Unique Identifier library
Group: Development/C
Requires: %name-dce = %version-%release
Requires: %name-devel = %version-%release

%description dce-devel
DCE development headers and libraries for OSSP uuid.

%prep
%setup -q -n uuid-%version
%patch0 -p1

%build
# Build the library.
export LIB_NAME=libossp-uuid.la
export DCE_NAME=libossp-uuid_dce.la
export CXX_NAME=libossp-uuid++.la
export PHP_NAME=$RPM_SOURCE_DIR/php/modules/ossp-uuid.so
%configure \
    --disable-static \
    --without-perl \
    --without-php \
    --with-dce \
    --without-cxx \
    --without-pgsql

sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make

%install


%makeinstall_std
rm -f %buildroot%_libdir/*.la %buildroot%_libdir/*.a
chmod 755 %buildroot%_libdir/*.so.*.*.*


%check


%files
%doc AUTHORS ChangeLog HISTORY NEWS PORTING README SEEALSO THANKS TODO USERS
%_bindir/uuid
%_libdir/libossp-uuid.so.*
%_man1dir/*

%files devel
%_bindir/uuid-config
%_includedir/uuid.h
%_libdir/libossp-uuid.so
%_pkgconfigdir/ossp-uuid.pc
%_man3dir/ossp-uuid.3*

%files dce
%_libdir/libossp-uuid_dce.so.*

%files dce-devel
%_includedir/uuid_dce.h
%_libdir/libossp-uuid_dce.so

%changelog
* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1-alt1.2
- Removed bad RPATH

* Mon Nov 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1-alt1.1
- Rebuilt for soname set-versions

* Thu Mar 04 2010 Michael Bochkaryov <misha@altlinux.ru> 1.5.1-alt1
- Package renamed to libossp-uuid
- Ported to ALT Linux

* Tue Oct 7 2008 Devrim GUNDUZ <devrim@commandprompt.com> 1.5.1-4
- Initial build for yum.pgsqlrpms.org, based on EPEL spec
