%define _name guile
%define api_ver 2.0
# guile-readline version
%define gl_ver 18
%def_disable static

Name: %{_name}20
Version: %api_ver.5
Release: alt2

Summary: A GNU implementation of Scheme (version 2.0)
Url: http://www.gnu.org/software/guile/
License: GPL
Group: Development/Scheme
Source: ftp://ftp.gnu.org/gnu/%_name/%_name-%version.tar.gz
Patch: %_name-2.0.5-up-gc.test.patch

Provides: /usr/bin/guile
Provides: %_name = %version-%release

Requires: lib%name = %version-%release

BuildRequires: /proc
BuildRequires: gcc-c++ libgmp-devel libltdl-devel libncurses-devel libreadline-devel
BuildRequires: libffi-devel libunistring-devel libgc-devel ccache
%{?_enable_static:BuildRequires: glibc-devel-static}

#%%add_findreq_skiplist %_datadir/%_name/%api_ver/scripts/*

%description
Guile is an implementation of the Scheme programming language, packaged
as a library that can be linked into applications to give them their own
extension language.  Guile supports other languages as well, giving
users of Guile-based applications a choice of languages.

This package provides interactive Guile shell.

%package devel
Summary: A GNU implementation of Scheme for application extensibility
Group: Development/Scheme
Requires: %name = %version-%release

%description devel
Guile is an implementation of the Scheme programming language, packaged
as a library that can be linked into applications to give them their own
extension language.  Guile supports other languages as well, giving
users of Guile-based applications a choice of languages.

Install this package if you are going to develop extendable programs.

%package -n lib%name
Summary: A Guile (version 2.0) libraries
Group: System/Libraries

%description -n lib%name
Guile is an implementation of the Scheme programming language, packaged
as a library that can be linked into applications to give them their own
extension language.  Guile supports other languages as well, giving
users of Guile-based applications a choice of languages.

This package provides shared Guile (version 2.0) libraries.

%package -n lib%name-devel
Summary: A Guile (version 2.0) development package
Group: Development/Scheme
Requires: lib%name = %version-%release

%description -n lib%name-devel
Guile is an implementation of the Scheme programming language, packaged
as a library that can be linked into applications to give them their own
extension language.  Guile supports other languages as well, giving
users of Guile-based applications a choice of languages.

This package provides development Guile (version 2.0) headers and libraries.

%package -n lib%name-devel-static
Summary: A GNU implementation of Scheme for application extensibility
Group: Development/Scheme
Requires: %name-devel = %version-%release

%description -n lib%name-devel-static
Guile is an implementation of the Scheme programming language, packaged
as a library that can be linked into applications to give them their own
extension language.  Guile supports other languages as well, giving
users of Guile-based applications a choice of languages.

Install this package if you need to statically link your program with guile.

%prep
%setup -q -n %_name-%version
%patch -p1

%build
%autoreconf
%configure --with-threads \
	%{subst_enable static}
%make_build

%install
%makeinstall_std

# alternatives
cat > %name.alternatives << _EOF_
%_bindir/%_name		%_bindir/%name		40
%_man1dir/%_name.1.gz	%_man1dir/%name.1.gz	%_bindir/%name
_EOF_

install -pD -m644 %name.alternatives %buildroot%_altdir/%name
mv %buildroot%_bindir/%_name %buildroot%_bindir/%name
mv %buildroot%_man1dir/%_name.1 %buildroot%_man1dir/%name.1

%check
%make check

%files
%_bindir/%name
%_man1dir/%name.1.*
%_altdir/%name

%if 0
%files devel
%_bindir/%_name-snarf
%exclude %_bindir/%_name-config
%exclude %_bindir/guild
%exclude %_bindir/%_name-tools
%_datadir/aclocal/%_name.m4
%_datadir/info/*.info*
%endif

%files -n lib%name
%_libdir/lib%_name-%api_ver.so.*
%_libdir/libguilereadline-v-%gl_ver.so.*
%_libdir/%_name/%api_ver/
%_datadir/%_name/%api_ver/

%files -n lib%name-devel
%_includedir/%_name/%api_ver/
%_libdir/lib%_name-%api_ver.so
%_libdir/libguilereadline-v-%gl_ver.so
%_libdir/pkgconfig/%_name-%api_ver.pc

%if_enabled static
%files -n lib%name-devel-static
%_libdir/lib%_name-%api_ver.a
%_libdir/libguilereadline-v-%gl_ver.a
%endif

#%files %_name-common
#%_libdir/%_name/
#%_includedir/%_name/
#%dir %_datadir/%_name

%changelog
* Fri Jun 01 2012 Yuri N. Sedunov <aris@altlinux.org> 2.0.5-alt2
- fixed test suite from upstream

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 2.0.5-alt1
- first build for Sisyphus

