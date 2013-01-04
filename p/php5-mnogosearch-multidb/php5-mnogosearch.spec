# Spec file to build PHP5 mnoGoSearch extension
#
# Note: Git repository for this package is mnogosearch.git,
#       this spec file is located in the one of php/* branches.
#

# mnoGoSearch database backends - must be the same as in the mnoGoSearch package
%def_with	mysql
%def_with	pgsql
%def_with	sqlite3
%def_without	sqlite
%def_with	unixODBC

%define		php5_extension	mnogosearch
%define 	real_name	mnogosearch
%define		real_version	3.3.12



%if_with mysql
%define conflicts_mysql php5-%php5_extension-mysql
%define subpackage_mysql mysql
%else 
%define conflicts_mysql %nil
%define subpackage_mysql %nil
%endif
%if_with pgsql
%define conflicts_pgsql php5-%php5_extension-pgsql
%define subpackage_pgsql pgsql
%else 
%define conflicts_pgsql %nil
%define subpackage_pgsql %nil
%endif
%if_with sqlite3
%define conflicts_sqlite3 php5-%php5_extension-sqlite3
%define subpackage_sqlite3 sqlite3
%else 
%define conflicts_sqlite3 %nil
%define subpackage_sqlite3 %nil
%endif
%if_with unixODBC
%define conflicts_odbc php5-%php5_extension-odbc
%define subpackage_odbc odbc
%else 
%define conflicts_odbc %nil
%define subpackage_odbc %nil
%endif


Name:	 	php5-%php5_extension-multidb
Version:	%php5_version
Release:	%php5_release.1

%define common_summary_for PHP5 mnogosearch extension for
%define common_desc_for mnoGoSearch is a full-featured SQL based web search engine.\
\
This package contains PHP frontend to mnogosearch for use with\
mnoGoSearch 


Summary:	%common_summary_for multi-database backend

License:	%gpl2plus
Group:		System/Servers
URL:		http://www.mnogosearch.org/

Packager:	Nikolay A. Fetisov <naf@altlinux.ru>

Source0:	%real_name-%real_version.tar
Source1:	php-%php5_extension.ini
Source2:	php-%php5_extension-params.sh
Patch1:		%real_name-3.3.8-alt-headers_location.patch

BuildRequires(pre): rpm-build-licenses rpm-build-php5
BuildRequires: php5-devel = %php5_version
BuildRequires: libmnogosearch-devel = %real_version

Conflicts: %conflicts_mysql %conflicts_pgsql %conflicts_sqlite3 %conflicts_odbc

%description
%common_desc_for multiple database backend package.

%if_with mysql
%package -n php5-%php5_extension-mysql
Summary: %common_summary_for MySQL database backend
Group: System/Servers
Conflicts: php5-%php5_extension-multidb %conflicts_pgsql %conflicts_sqlite3 %conflicts_odbc

%description -n php5-%php5_extension-mysql
%common_desc_for MySQL database backend package.
%endif


%if_with pgsql
%package -n php5-%php5_extension-pgsql
Summary: %common_summary_for PostgreSQL database backend
Group: System/Servers
Conflicts: php5-%php5_extension-multidb %conflicts_mysql %conflicts_sqlite3 %conflicts_odbc

%description -n php5-%php5_extension-pgsql
%common_desc_for PostgreSQL database backend package.
%endif


%if_with sqlite3
%package -n php5-%php5_extension-sqlite3
Summary: %common_summary_for SQLite3 database backend
Group: System/Servers
Conflicts: php5-%php5_extension-multidb %conflicts_mysql %conflicts_pgsql %conflicts_odbc

%description -n php5-%php5_extension-sqlite3
%common_desc_for SQLite3 database backend package.
%endif

%if_with unixODBC
%package -n php5-%php5_extension-odbc
Summary: %common_summary_for ODBC database backend
Group: System/Servers
Conflicts: php5-%php5_extension-multidb %conflicts_mysql %conflicts_pgsql %conflicts_sqlite3

%description -n php5-%php5_extension-odbc
%common_desc_for ODBC database backend package.
%endif


%prep
%setup -n %real_name-%real_version
%patch1 -p0

%build

# Make module for given backend
# Usage: make_backend <backend>
make_backend() {
    local backend=$1
    mkdir $backend
    cp -- config.m4  CREDITS  index.php  Makefile.in php_mnogo.c  php_mnogo.h  README $backend/
    pushd $backend
    # Filter backend-specific libraries:
    subst "s#\$MNOGOSEARCH_BINDIR/udm-config --libs#echo '-lmnogosearch-$backend -lmnogocharset'#" config.m4

    phpize

    BUILD_HAVE=`echo %php5_extension | tr '[:lower:]-' '[:upper:]_'`
    %add_optflags -fPIC -L%_libdir
    export LDFLAGS=-lphp-%_php5_version
    %configure \
        --with-%php5_extension=%_usr \
        --with-libdir=%_lib \
        %nil

    %php5_make

    popd
}

for i in multidb %subpackage_mysql %subpackage_pgsql %subpackage_sqlite3 %subpackage_odbc;do
    make_backend $i
done

%install
# Install module for given backend
# Usage: make_backend <backend>
install_backend() {
    local backend=$1
    pushd $backend
    %php5_make_install
    mv -- %buildroot%php5_extdir/%php5_extension.so %buildroot%php5_extdir/%php5_extension-$backend.so
    install -D -m 644 -- %SOURCE1 %buildroot/%php5_extconf/%php5_extension-$backend/config
    install -D -m 644 -- %SOURCE2 %buildroot/%php5_extconf/%php5_extension-$backend/params
    sed -e "s/%php5_extension/%php5_extension-$backend/" -i %buildroot/%php5_extconf/%php5_extension-$backend/config
    sed -e "s/%php5_extension/%php5_extension-$backend/" -i %buildroot/%php5_extconf/%php5_extension-$backend/params
    popd
}

for i in multidb %subpackage_mysql %subpackage_pgsql %subpackage_sqlite3 %subpackage_odbc; do
    install_backend $i
done


%define	php5_extension	mnogosearch-multidb
%files
%doc README CREDITS

%php5_extconf/%php5_extension
%php5_extdir/%{php5_extension}*

%post
%php5_extension_postin

%preun
%php5_extension_preun

%if_with mysql
%define	php5_extension	mnogosearch-mysql
%files -n php5-%php5_extension
%doc README CREDITS

%php5_extconf/%php5_extension
%php5_extdir/%{php5_extension}*

%post -n php5-%php5_extension
%php5_extension_postin

%preun -n php5-%php5_extension
%php5_extension_preun
%endif


%if_with pgsql
%define	php5_extension	mnogosearch-pgsql
%files -n php5-%php5_extension
%doc README CREDITS

%php5_extconf/%php5_extension
%php5_extdir/%{php5_extension}*

%post -n php5-%php5_extension
%php5_extension_postin

%preun -n php5-%php5_extension
%php5_extension_preun
%endif


%if_with sqlite3
%define	php5_extension	mnogosearch-sqlite3
%files -n php5-%php5_extension
%doc README CREDITS

%php5_extconf/%php5_extension
%php5_extdir/%{php5_extension}*

%post -n php5-%php5_extension
%php5_extension_postin

%preun -n php5-%php5_extension
%php5_extension_preun
%endif


%if_with unixODBC
%define	php5_extension	mnogosearch-odbc
%files -n php5-%php5_extension
%doc README CREDITS

%php5_extconf/%php5_extension
%php5_extdir/%{php5_extension}*

%post -n php5-%php5_extension
%php5_extension_postin

%preun -n php5-%php5_extension
%php5_extension_preun
%endif

%changelog
* Fri Jan 04 2013 Nikolay A. Fetisov <naf@altlinux.ru> 5.3.18.20121017-alt1.1
- Rebuild with php5-5.3.18.20121017-alt1.1

* Wed Nov 14 2012 Anton Farygin <rider@altlinux.ru> 5.3.18.20121017-alt1
- Rebuild with php5-5.3.18.20121017-alt1

* Tue Oct 02 2012 Anton Farygin <rider@altlinux.ru> 5.3.17.20120913-alt1
- Rebuild with php5-devel-5.3.17.20120913-alt1

* Sun Aug 26 2012 Nikolay A. Fetisov <naf@altlinux.ru> 5.3.10.20120202-alt1
- New version
- Build extension for every mnoGoSearch databases backends

* Mon Aug 24 2009 Nikolay A. Fetisov <naf@altlinux.ru> 5.2.11.20090722-alt1
- Initial build
