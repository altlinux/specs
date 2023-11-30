%define dist DBIx-Safe

Name: perl-%dist
Version: 1.2.5
Release: alt4

Summary: Safe wrapper to DBI interface

License: Artistic
Group: Development/Perl
Url: %CPAN %dist

Packager: Mikhail Pokidko <pma@altlinux.org>

BuildArch: noarch
Source: %dist-%version.tar.gz

BuildRequires: perl-DBD-Pg perl-devel perl-Pod-Simple /usr/bin/pod2html

%description
The purpose of this module is to give controlled, limited access to an application,
rather than simply passing it a raw database handle through DBI. DBIx::Safe acts as
a wrapper to the database, by only allowing through the commands you tell it to. It
filters all things related to the database handle - methods and attributes.

The typical usage is for your application to create a database handle via a normal
DBI call to new(), then pass that to DBIx::Safe->new(), which will return you a
DBIx::Safe object. After specifying exactly what is and what is not allowed, you can
pass the object to the untrusted application. The object will act very similar to a
DBI database handle, and in most cases can be used interchangeably.

By default, nothing is allowed to run at all. There are many things you can control.
You can specify which SQL commands are allowed, by indicating the first word in the
SQL statement (e.g. 'SELECT'). You can specify which database methods are allowed to
run (e.g. 'ping'). You can specify a regular expression that allows matching SQL
statements to run (e.g. 'qr{SET TIMEZONE}'). You can specify a regular expression
that is NOT allowed to run (e.g. qr(UPDATE xxx}). Finally, you can indicate which
database attributes are allowed to be read and changed (e.g. 'PrintError'). For all
of the above, there are matching methods to remove them as well.

%prep
%setup -q -n %dist-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/*
%exclude %perl_vendor_archlib

%changelog
* Thu Nov 30 2023 Igor Vlasenko <viy@altlinux.org> 1.2.5-alt4
- added BR: /usr/bin/pod2html

* Mon Sep 10 2012 Vladimir Lettiev <crux@altlinux.ru> 1.2.5-alt3
- fixed build with perl-5.16
- spec cleanup

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.2.5-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Sep 04 2008 Mikhail Pokidko <pma@altlinux.org> 1.2.5-alt2
- sisyphus_check fixes

* Thu May 15 2008 Mikhail Pokidko <pma@altlinux.org> 1.2.5-alt1
- first build for ALT Linux Sisyphus

