Name: pgmodeler
Version: 1.0.6
Release: alt1

Summary: PostgreSQL Database Modeler

License: GPLv3
Group: Databases
Url: http://pgmodeler.com.br/

# Source-git: https://github.com/pgmodeler/pgmodeler.git
Source: %name-%version.tar

Patch1: pgmodeler-fix-build-with-libxml2.patch

BuildRequires(pre): rpm-macros-qt5
BuildRequires: gcc-c++ libpq-devel libxml2-devel libXext-devel postgresql-devel
BuildRequires: qt6-base-devel qt6-svg-devel


%description
pgModeler - PostgreSQL Database Modeler - is an open source data modeling tool designed for PostgreSQL.
No more DDL commands written by hand let pgModeler do the job for you! This software reunites the concepts
of entity-relationship diagrams and the features that PostgreSQL implements as extensions of SQL standards.

%prep
%setup
%patch1 -p1

%build
%qmake_qt6 pgmodeler.pro \
    PREFIX=%prefix \
    PRIVATELIBDIR=%_libdir/%name \
    PLUGINSDIR=%_libdir/%name/plugins
# bug with rpath there
#    PRIVATEBINDIR=%_libdir/%name/bin \

%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot

%files
%doc README.md CHANGELOG.md RELEASENOTES.md
%_bindir/%name
%_bindir/%name-cli
%_bindir/%name-ch
%_bindir/%name-se
%_datadir/%name/
%_libdir/%name/

%changelog
* Mon Dec 25 2023 Vitaly Lipatov <lav@altlinux.ru> 1.0.6-alt1
- new version 1.0.6 (with rpmrb script)
- switch to Qt6

* Fri Feb 14 2020 Vitaly Lipatov <lav@altlinux.ru> 0.9.2-alt1
- new version 0.9.2 (with rpmrb script)
- use _libdir

* Sat Jun 30 2018 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt1
- new version 0.9.1 (with rpmrb script)

* Tue Jan 03 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.0-alt1
- new version 0.9.0 (with rpmrb script)

* Tue Aug 16 2016 Vitaly Lipatov <lav@altlinux.ru> 0.8.2-alt1
- build 0.8.2 release
- PostgreSQL version agnostic build

* Sun Dec 06 2015 Vitaly Lipatov <lav@altlinux.ru> 0.8.2-alt0beta
- initial build for ALT Linux Sisyphus

