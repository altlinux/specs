## SPEC file for innotop

Name: innotop
Version: 1.11.4
Release: alt1

Summary: a 'top' clone for MySQL with special attention paid to InnoDB

License: %perl_license
Group: Databases
URL: http://code.google.com/p/innotop
# http://sourceforge.net/projects/innotop/files/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildArch: noarch

AutoReqProv: perl, yes
BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Oct 14 2012
# optimized out: perl-DBI perl-Encode perl-Pod-Escapes perl-Pod-Simple perl-podlators
BuildRequires: perl-DBD-mysql perl-Pod-Parser perl-Term-ReadKey perl-devel perl-unicore


Requires: perl-DBD-mysql

%description
innotop is a MySQL and InnoDB transaction/status monitor. It can display
queries, InnoDB transactions, lock waits, deadlocks, foreign key errors,
open tables, replication status, buffer information, row operations,
logs, I/O operations, load graph, and more.  You can monitor many
servers at once with innotop.

%prep
%setup
%patch0 -p1

mv -f -- COPYING COPYING.GPL.orig
ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/COPYING) COPYING

%build
%perl_vendor_build

# Generating man page
/usr/bin/pod2man innotop > innotop.1

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
* Tue Feb 14 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.11.4-alt1
- New version

* Tue Sep 13 2016 Nikolay A. Fetisov <naf@altlinux.ru> 1.11.1-alt1
- New version
- Fix work on Perl 5.22.2

* Sat Aug 10 2013 Nikolay A. Fetisov <naf@altlinux.ru> 1.9.1-alt1
- New version

* Mon Oct 22 2012 Nikolay A. Fetisov <naf@altlinux.ru> 1.9.0-alt2
- Add missing requires on DBD::mysql

* Sun Oct 14 2012 Nikolay A. Fetisov <naf@altlinux.ru> 1.9.0-alt1
- New version

* Sun Nov 28 2010 Nikolay A. Fetisov <naf@altlinux.ru> 1.8.0-alt1
- New version

* Wed May 26 2010 Nikolay A. Fetisov <naf@altlinux.ru> 1.7.2-alt1
- Initial build for ALT Linux Sisyphus
