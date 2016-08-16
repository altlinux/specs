Name: opm-core
Version: 2.3
Release: alt2

Summary: Central module of the Open PostgreSQL Monitoring
License: BSD like
Group: Monitoring

Url: https://github.com/OPMDG/opm-core

Source: %name-%version.tar

BuildArchitectures: noarch

# manually removed:  rpm-build-mingw32 rpm-build-python3 ruby ruby-stdlibs
# Automatically added by buildreq on Sun Sep 14 2014 (-bi)
# optimized out: perl-Compress-Raw-Zlib perl-Digest-SHA perl-EV perl-Encode perl-IO-Socket-IP perl-Net-SSLeay perl-Pod-Escapes perl-Pod-Simple perl-Pod-Usage perl-URI perl-common-sense perl-devel python-base python3 python3-base
BuildRequires: perl-DBI perl-IO-Socket-SSL perl-podlators rpm-build-gir

BuildPreReq: postgresql-devel
BuildPreReq: perl-Mojolicious >= 4.50

Requires: perl-DBD-Pg perl-Locale-Maketext

# we need version in [4.5 4.9], but have no it in repo, install in with # curl get.mojolicio.us | sh
Requires: perl-Mojolicious >= 4.50
Requires: perl-Mojolicious-Plugin-I18N

%add_perl_lib_path %_datadir/opm-core/ui/lib

# FIXME: Can't locate OPM/I18N.pm in @INC at /usr/share/perl5/Mojo/Base.pm line 30.
%add_findreq_skiplist %_datadir/opm-core/ui/lib/OPM/I18N/en.pm
%add_findreq_skiplist %_datadir/opm-core/ui/lib/OPM/I18N/fr.pm

%description
Open PostgreSQL Monitoring central part.

%package postgresql
Summary: PostgreSQL extension for OPM
Group: Development/Python
#Requires: postgresql9.5-contrib
Requires: /usr/bin/pgbench

%description postgresql
PostgreSQL extension for Open PostgreSQL Monitoring central part.

%prep
%setup

%install
cd pg
# we need hack with PGXS only if build with Etersoft's PG where lib/postgresql is used
#makeinstall_std PGXS=%_libdir/pgsql/pgxs/src/makefiles/pgxs.mk
%makeinstall_std
cd -
mkdir -p %buildroot/%_datadir/%name/
cp -a ui %buildroot/%_datadir/%name/

# create conf in normal place
mkdir -p %buildroot%_sysconfdir/%name/
cp ui/opm.conf-dist %buildroot%_sysconfdir/%name/opm.conf
ln -s %_sysconfdir/%name/opm.conf %buildroot%_datadir/%name/ui/opm.conf


%files
%dir %_sysconfdir/%name/
%config(noreplace) %_sysconfdir/%name/opm.conf
%dir %_datadir/%name/
%_datadir/%name/ui/

%files postgresql
%_datadir/pgsql/extension/opm_core*

%changelog
* Tue Aug 16 2016 Vitaly Lipatov <lav@altlinux.ru> 2.3-alt2
- PostgreSQL version agnostic build

* Wed Mar 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3-alt1.1
- Rebuilt with PostgreSQL 9.4

* Sun Sep 14 2014 Vitaly Lipatov <lav@altlinux.ru> 2.3-alt1
- initial build for ALT Linux Sisyphus
