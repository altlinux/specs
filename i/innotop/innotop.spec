## SPEC file for innotop

Name: innotop
Version: 1.8.0
Release: alt1

Summary: a 'top' clone for MySQL with special attention paid to InnoDB

License: %perl_license
Group: Databases
URL: http://code.google.com/p/innotop
# http://sourceforge.net/projects/innotop/files/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %name-%version.tar
BuildArch: noarch

AutoReqProv: perl, yes
BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Nov 28 2010
BuildRequires: perl-DBI perl-Pod-Parser perl-Term-ReadKey perl-Term-ReadLine-Gnu termutils

%description
innotop is a MySQL and InnoDB transaction/status monitor. It can display
queries, InnoDB transactions, lock waits, deadlocks, foreign key errors,
open tables, replication status, buffer information, row operations,
logs, I/O operations, load graph, and more.  You can monitor many
servers at once with innotop.

# ATT: non-standart test suite, run it directly
%def_without test

%prep
%setup

mv -f -- COPYING COPYING.GPL.orig
ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/COPYING) COPYING

%build
%perl_vendor_build

# Generating man page
/usr/bin/pod2man innotop > innotop.1

# Running tests
cd t
/usr/bin/perl ./InnoDBParser.t
cd ..

%install
%perl_vendor_install

# Installing man page
install -d %buildroot%_man1dir
install -m 644 %name.1 %buildroot%_man1dir/%name.1

%files
%doc Changelog
%doc --no-dereference COPYING

%_bindir/%name

%_man1dir/%name.*

%changelog
* Sun Nov 28 2010 Nikolay A. Fetisov <naf@altlinux.ru> 1.8.0-alt1
- New version

* Wed May 26 2010 Nikolay A. Fetisov <naf@altlinux.ru> 1.7.2-alt1
- Initial build for ALT Linux Sisyphus
