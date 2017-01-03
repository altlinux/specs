Name: pgmodeler
Version: 0.9.0
Release: alt1

Summary: PostgreSQL Database Modeler

License: GPLv3
Group: Databases
Url: http://pgmodeler.com.br/

# Source-git: https://github.com/pgmodeler/pgmodeler.git
Source: %name-%version.tar

BuildRequires: gcc-c++ qt5-base-devel qt5-svg-devel libpq-devel libxml2-devel libXext-devel postgresql-devel

BuildPreReq: rpm-macros-qt5

%description
pgModeler - PostgreSQL Database Modeler - is an open source data modeling tool designed for PostgreSQL.
No more DDL commands written by hand let pgModeler do the job for you! This software reunites the concepts
of entity-relationship diagrams and the features that PostgreSQL implements as extensions of SQL standards.

%prep
%setup

%build
%qmake_qt5 PREFIX=%prefix pgmodeler.pro
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot 

%files
%doc README.md CHANGELOG.md RELEASENOTES.md
%_bindir/*
%_datadir/%name/
%_libexecdir/%name/

%changelog
* Tue Jan 03 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.0-alt1
- new version 0.9.0 (with rpmrb script)

* Tue Aug 16 2016 Vitaly Lipatov <lav@altlinux.ru> 0.8.2-alt1
- build 0.8.2 release
- PostgreSQL version agnostic build

* Sun Dec 06 2015 Vitaly Lipatov <lav@altlinux.ru> 0.8.2-alt0beta
- initial build for ALT Linux Sisyphus

