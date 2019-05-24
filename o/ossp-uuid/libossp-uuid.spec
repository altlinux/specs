%def_with perl
%def_with cxx
%def_without php
Name: ossp-uuid
Version: 1.6.2
Release: alt2
Summary: Universally Unique Identifier library
License: MIT
Group: System/Libraries
Url: http://www.ossp.org/pkg/lib/uuid/

%define libversion %(echo %version | sed 's,\\.[0-9]*$,,;s,\\.,,')
%define libname lib%name%libversion
%define libdevel lib%{name}-devel
%define libdcename lib%{name}-dce%libversion
%define libdcedevel lib%{name}-dce-devel
%define libcxxname lib%{name}++%libversion
%define libcxxdevel lib%{name}++-devel
%define phpname php7-%{name}

Source: uuid-%version.tar.bz2
Patch0:         uuid-1.6.1-ossp.patch

Patch1:         uuid-1.6.1-mkdir.patch
Patch2:         uuid-1.6.2-php54.patch

# rhbz#829532
Patch3:         uuid-1.6.2-hwaddr.patch

# do not strip binaries
Patch4:         uuid-1.6.2-nostrip.patch
Patch5: uuid-1.6.2-manfix.patch
Patch6: uuid-aarch64.patch


# Automatically added by buildreq on Thu Mar 04 2010 (-bb)
BuildRequires: gcc-c++ gcc-fortran glibc-devel-static postgresql-devel termutils chrpath

BuildRequires: %_bindir/libtool
%if_with perl
BuildRequires: perl-devel
%endif
%if_with cxx
BuildRequires: gcc-c++
%endif
%if_with php
BuildRequires: rpm-build-php7
%endif

Conflicts: libossp-uuid < 1.5.1-alt3

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

%package -n %libname
Summary: Universally Unique Identifier library
Group: System/Libraries
Requires: %_pkgconfigdir
Requires: %libname = %EVR

%description -n %libname
OSSP uuid shared library.

%package -n %libdevel
Summary: Development support for Universally Unique Identifier library
Group: Development/C
Requires: %_pkgconfigdir
Requires: %libname = %EVR

%description -n %libdevel
Development headers and libraries for OSSP uuid.

%package -n %libdcename
Summary: DCE support for Universally Unique Identifier library
Group: System/Libraries
Requires: %libname = %EVR

%description -n %libdcename
DCE OSSP uuid library.

%package -n %libdcedevel
Summary: DCE development support for Universally Unique Identifier library
Group: Development/C
Requires: %libdcename = %EVR
Requires: lib%name-devel = %EVR

%description -n %libdcedevel
DCE development headers and libraries for OSSP uuid.

%if_with perl
%package -n perl-OSSP-uuid
Summary: perl bindings for Universally Unique Identifier library
Group: Development/C
Requires: %libname = %EVR

%description -n perl-OSSP-uuid
perl bindings for OSSP uuid.
%endif

%if_with cxx
%package -n %libcxxname
Group: System/Libraries
Summary:        C++ support for Universally Unique Identifier library
Requires:       %libname = %EVR

%description -n %libcxxname
C++ libraries for OSSP uuid.

%package -n %libcxxdevel
Group: Development/C++
Summary:        C++ development support for Universally Unique Identifier library
Requires:       %libcxxname = %EVR

%description -n %libcxxdevel
C++ development headers and libraries for OSSP uuid.
%endif

%if_with php
%package -n %phpname
Group: Development/Other
Summary:        PHP development support for Universally Unique Identifier library
Requires:       %libname = %EVR

%description -n %phpname
PHP extension for OSSP uuid.
%endif

%prep
%setup -q -n uuid-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1 -b .php54
%patch3 -p1 -b .hwaddr
%patch4 -p1 -b .nostrip
%patch5 -p1 -b .manfix
%patch6 -p1 -b .aarch64

%build
# Build the library.
export LIB_NAME=libossp-uuid.la
export DCE_NAME=libossp-uuid_dce.la
export CXX_NAME=libossp-uuid++.la
export PHP_NAME=$RPM_SOURCE_DIR/php/modules/ossp-uuid.so
export PGSQL_NAME=$(pwd)/pgsql/libossp-uuid.so
%configure \
    --disable-static \
    %{subst_with perl} \
    %{subst_with cxx} \
    %{subst_with php} \
    --with-dce \
    --without-pgsql

sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make

%install


%makeinstall_std
rm -f %buildroot%_libdir/*.la %buildroot%_libdir/*.a
chmod 755 %buildroot%_libdir/*.so.*.*.*

%if_with perl
mkdir -p %buildroot%perl_vendor_archlib
mv %buildroot%_libdir/perl/*/* %buildroot%perl_vendor_archlib/
chrpath -d %buildroot%perl_vendor_archlib/auto/OSSP/uuid/uuid.so ||:
%endif

mv %buildroot%_bindir/{uuid,%name}
ln -s %name %buildroot%_bindir/uuid

mv %buildroot%_man3dir/{uuid++.3,%{name}++.3}

%check
# TODO: killing rpath with sed -ri '...' libtool above breaks make check
# better to kill rpath with chrpath -d later
#make check

%files
%doc AUTHORS ChangeLog HISTORY NEWS PORTING README SEEALSO THANKS TODO USERS
%_bindir/%name
%_bindir/uuid
%_man1dir/*

%files -n %libname
%_libdir/libossp-uuid.so.%{libversion}*

%files -n %libdevel
%_bindir/uuid-config
%_includedir/uuid.h
%_libdir/libossp-uuid.so
%_pkgconfigdir/ossp-uuid.pc
%_man3dir/ossp-uuid.3*

%files -n %libdcename
%_libdir/libossp-uuid_dce.so.%{libversion}*

%files -n %libdcedevel
%_includedir/uuid_dce.h
%_libdir/libossp-uuid_dce.so

%if_with perl
%files -n perl-OSSP-uuid
%perl_vendor_archlib/OSSP
%perl_vendor_archlib/auto/OSSP
%endif

%if_with cxx
%files -n %libcxxname
%_libdir/libossp-uuid++.so.%{libversion}*

%files -n %libcxxdevel
%_includedir/uuid++.hh
%_libdir/libossp-uuid++.so
%_man3dir/ossp-uuid++.3*
%endif

%if_with php
%files -n %phpname
todo_fill_me
%endif


%changelog
* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt2
- added disabled php support

* Thu May 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1
- new version
- added c++ support
- packaged according to shared libs policy

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt2.1
- rebuild with new perl 5.28.1

* Tue Oct 16 2018 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt2
- NMU: built with perl

* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1-alt1.2
- Removed bad RPATH

* Mon Nov 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1-alt1.1
- Rebuilt for soname set-versions

* Thu Mar 04 2010 Michael Bochkaryov <misha@altlinux.ru> 1.5.1-alt1
- Package renamed to libossp-uuid
- Ported to ALT Linux

* Tue Oct 7 2008 Devrim GUNDUZ <devrim@commandprompt.com> 1.5.1-4
- Initial build for yum.pgsqlrpms.org, based on EPEL spec
