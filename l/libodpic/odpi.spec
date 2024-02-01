#define        _unpackaged_files_terminate_build 1
%define        pname odpi
%define        libname odpic

Name:          lib%libname
Version:       5.1.0
Release:       alt1
Group:         Development/C
Summary:       ODPI-C: Oracle Database Programming Interface for Drivers and Applications
License:       Apache-2.0 or UPL-1.0
Url:           https://oracle.github.io/odpi/
Vcs:           https://github.com/oracle/odpi.git

Source:        %name-%version.tar
Patch:         makefile.patch

%description
Oracle Database Programming Interface for C (ODPI-C) is an open source library
of C code that simplifies access to Oracle Database for applications written in
C or C++. It is a wrapper over Oracle Call Interface (OCI) that makes
applications and language interfaces easier to develop.

ODPI-C supports basic and advanced features of Oracle Database and Oracle
Client. See the homepage for a list.


%package       devel
Group:         Development/C
Summary:       C99 library implementation of AWS client-side authentication development files

%description   devel
Development headers, libraries, and code for %libname.

Oracle Database Programming Interface for C (ODPI-C) is an open source library
of C code that simplifies access to Oracle Database for applications written in
C or C++. It is a wrapper over Oracle Call Interface (OCI) that makes
applications and language interfaces easier to develop.

ODPI-C supports basic and advanced features of Oracle Database and Oracle
Client. See the homepage for a list.


%prep
%setup
%autopatch

%build
%make_build

%install
%makeinstall_std PREFIX=%_prefix INSTALL_LIB_DIR=%buildroot%_libdir

%check
%make test

%files
%doc README* LICENSE*
%_libdir/%name.so.*

%files         devel
%_libdir/%name.so
%_includedir/dpi.h
%_datadir/%pname/*

%changelog
* Wed Jan 31 2024 Pavel Skrylev <majioa@altlinux.org> 5.1.0-alt1
- Initial build for Sisyphus
