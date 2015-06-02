Name: mtop
Version: 0.6.6
Release: alt2

Summary: Tool to monitor a MySQL database

License: GPL
Group: Monitoring
Url: http://mtop.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

# manually removed:  python3 ruby ruby-stdlibs
BuildArch: noarch
# Automatically added by buildreq on Tue Jun 02 2015
# optimized out: perl-DBI perl-Encode perl-Pod-Escapes perl-Pod-Simple python3-base
BuildRequires: libdb4-devel perl-Curses perl-DBD-mysql perl-devel perl-libnet perl-podlators

%description
mtop (MySQL top) monitors a MySQL database showing the queries
which are taking the most amount of time to complete. Features
include 'zooming' in on a process to show the complete query
and 'explaining' the query optimizer information.

%prep
%setup

%build
perl Makefile.PL PREFIX="%buildroot%prefix"
make

%install
%makeinstall
rm -f /usr/share/perl5/cpan2spec.pl

%files
%doc ChangeLog COPYING README*
%doc %_man1dir/mkill.1*
%doc %_man1dir/mtop.1*
%_bindir/mkill
%_bindir/mtop

%changelog
* Tue Jun 02 2015 Vitaly Lipatov <lav@altlinux.ru> 0.6.6-alt2
- cleanup spec, rebuild for ALT Linux Sisyphus

* Wed Nov 15 2006 Mikhail Pokidko <pma@altlinux.ru> 0.6.6-alt1
- Initial build

