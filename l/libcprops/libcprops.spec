# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define oname		cprops

%define major		15
%define libname		lib%{oname}%{major}
%define develname	lib%{oname}-devel

%define dbms_major	0
%define mysqllib	libcp_dbms_mysql%{dbms_major}
%define pgreslib	libcp_dbms_postgres%{dbms_major}

%bcond_without	postgres
%bcond_without	mysql

Name:		lib%{oname}
Version:	0.1.12
Release:	alt1_14

Summary:	C Prototyping Tools
Group:		Development/C
License:	LGPLv2+
URL:		http://%{oname}.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{oname}/%{name}-%{version}.tar.bz2
Patch0:		libcprops-AC_DEFINE.patch
Patch1:		libcprops-format-string.patch

BuildRequires:	pkgconfig(openssl)
BuildRequires:	flex
BuildRequires:	bison
Source44: import.info

%description
The C Prototyping Tools library provides thread-safe linked list, priority
queue, hash table, hash list, AVL tree and trie implementations, as well
as a thread pool and a thread management framework, a TCP and an HTTP socket
API, and a DBMS abstraction layer.

%package -n %{libname}
Summary:	C Prototyping Tools
Group:		System/Libraries
Obsoletes:	%{_lib}libcprops0 < 0.1.12-3

%if %with mysql
%package -n %{mysqllib}
Summary:	MySQL (MariaDB) dbms driver for %{name}
Group:		System/Libraries
BuildRequires:	libmysqlclient-devel

%description -n %{mysqllib}
This package contains the MySQL (MariaDB) dbms driver for %{name}.
%endif

%if %with postgres
%package -n %{pgreslib}
Summary:	PostgreSQL dbms driver for %{name}
Group:		System/Libraries
BuildRequires:	postgresql-devel
Conflicts:	liblibcprops0 < 0.1.12-3

%description -n %{pgreslib}
This package contains the PostgreSQL dbms driver for %{name}.
%endif

%description -n %{libname}
The C Prototyping Tools library provides thread-safe linked list, priority
queue, hash table, hash list, AVL tree and trie implementations, as well
as a thread pool and a thread management framework, a TCP and an HTTP socket
API, and a DBMS abstraction layer.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{_lib}libcprops-devel < 0.1.12-3

%description -n %{develname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

# for autoreconf
mkdir -p m4

%build
autoreconf -vfi
%configure \
	--disable-static \
	--disable-cpsvc \
	--disable-cpsp \
	--enable-shared \
	--with-ssl=%{_prefix} \
	%{?with_postgres:--with-postgres-includes=%{_includedir}/pgsql} \
	%{?with_postgres:--with-postgres-libs=%{_libdir}} \
	%{?with_mysql:--with-mysql-includes=%{_includedir}/mysql} \
	%{?with_mysql:--with-mysql-libs=%{_libdir}}

sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|func_apped|func_append|' \
    -e 's|CC -shared|CC -shared -Wl,--as-needed|g' \
    -i libtool

%make

%install
%makeinstall_std

# we don't want these
find %{buildroot} -name "*.la" -delete

%files -n %{libname}
%doc README ChangeLog
%{_libdir}/%{name}.so.%{major}
%{_libdir}/%{name}.so.%{major}.*

%if %with mysql
%files -n %{mysqllib}
%{_libdir}/libcp_dbms_mysql.so.%{dbms_major}
%{_libdir}/libcp_dbms_mysql.so.%{dbms_major}.*
%endif

%if %with postgres
%files -n %{pgreslib}
%{_libdir}/libcp_dbms_postgres.so.%{dbms_major}
%{_libdir}/libcp_dbms_postgres.so.%{dbms_major}.*
%endif

%files -n %{develname}
%{_mandir}/man3/*
%{_includedir}/%{oname}/
%{_libdir}/*.so


%changelog
* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.1.12-alt1_14
- new version

