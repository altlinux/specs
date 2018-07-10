Name: psqlodbc
Version: 10.03.0000
Release: alt1

Summary: The official PostgreSQL ODBC Driver
License: LGPL
Group: Databases

Url: http://www.postgresql.org
Source: http://ftp.postgresql.org/pub/odbc/versions/src/%name-%version.tar.gz

BuildRequires: libunixODBC-devel
BuildRequires: postgresql-devel

%description
The official PostgreSQL ODBC Driver

%package -n lib%name
Group: Databases
Summary: The official PostgreSQL ODBC Driver
Provides: %name

%description -n lib%name
The official PostgreSQL ODBC Driver

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%files -n lib%name
%_libdir/%{name}*
%doc docs/*

%changelog
* Tue Jul 10 2018 Michael Shigorin <mike@altlinux.org> 10.03.0000-alt1
- initial release (based on mageia package)

