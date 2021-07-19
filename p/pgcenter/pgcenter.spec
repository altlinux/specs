# SPEC file for pgcenter
#

%global import_path github.com/lesovsky/pgcenter

Name:     pgcenter
Version:  0.9.2
Release:  alt1

Summary: top-like PostgreSQL statistics viewer

Group:    System/Servers
License:  %bsdstyle
URL:      https://github.com/lesovsky/pgcenter
Packager: Nikolay Fetisov <naf@altlinux.org>

Source0: %name-%version.tar
Source1: vendor.tar
Patch0:  %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-build-golang

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

tar xf %SOURCE1

%build
export GO111MODULE=auto
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build cmd

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

mv -- $BUILDDIR/bin/cmd $BUILDDIR/bin/%name

%golang_install


%files
%doc README.md COPYRIGHT doc/

%_bindir/*

%changelog
* Mon Jul 19 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.9.2-alt1
- New version

* Mon Jun 28 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.9.1-alt1
- New version (Closes: 36340, 38080)

* Sat Nov 18 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.4.0-alt1
- New version

* Sat Oct 01 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.3.0-alt1
- New version

* Sat Feb 06 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.2.0-alt1
- Initial build for ALT Linux Sisyphus

