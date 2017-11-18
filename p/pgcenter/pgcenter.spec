# SPEC file for Apache pgcenter
#

Name:     pgcenter
Version:  0.4.0
Release:  alt1

Summary: top-like PostgreSQL statistics viewer

Group:    System/Servers
License:  %bsdstyle
URL:      https://github.com/lesovsky/pgcenter
Packager: Nikolay Fetisov <naf@altlinux.ru>

Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses


# Automatically added by buildreq on Sat Feb 06 2016
# optimized out: libpq-devel libsasl2-3 libtinfo-devel
BuildRequires: libncurses-devel postgresql-devel

%description
Pgcenter is the PostgreSQL administration console with top-like
monitoring.

PostgreSQL provides various statistics which includes information
about tables, indexes, functions and other database objects and
their usage. Moreover, statistics has detailed information about
connections, current queries and database operations (INSERT/
DELETE/UPDATE). But most of this statistics are provided as
permanently incremented counters. The pgcenter provides
convenient interface to this statistics and allow viewing
statistics changes in time interval, eg. per second.

%prep
%setup  -n %name-%version
%patch0 -p1

%build
%make

%install
%make_install install DESTDIR=%buildroot

mkdir -p -- %buildroot%_man1dir
cp share/doc/%name.1  %buildroot%_man1dir

%files
%doc README.md COPYRIGHT share/doc/Changelog

%_bindir/*
%_man1dir/*
%_datadir/%{name}*

%changelog
* Sat Nov 18 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.4.0-alt1
- New version

* Sat Oct 01 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.3.0-alt1
- New version

* Sat Feb 06 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.2.0-alt1
- Initial build for ALT Linux Sisyphus

