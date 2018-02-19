%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Test/More.pm) perl(XSLoader.pm) perl(base.pm) perl(overload.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define module_name Email-Address-XS
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.02
Release: alt1
Summary: Parse and format RFC 2822 email addresses and groups
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/P/PA/PALI/%{module_name}-%{version}.tar.gz

%description
This module implements RFC 2822
parser and formatter of email addresses and groups. It parses an input
string from email headers which contain a list of email addresses or
a groups of email addresses (like From, To, Cc, Bcc, Reply-To, Sender,
...). Also it can generate a string value for those headers from a
list of email addresses objects.

Parser and formatter functionality is implemented in XS and uses
shared code from Dovecot IMAP server.

It is a drop-in replacement for the Email::Address module
which has several security issues. E.g. issue CVE-2015-7686 (Algorithmic complexity vulnerability),
which allows remote attackers to cause denial of service, is still
present in Email::Address version 1.908.

Email::Address::XS module was created to finally fix CVE-2015-7686.

Existing applications that use Email::Address module could be easily
switched to Email::Address::XS module. In most cases only changing
`use Email::Address' to `use Email::Address::XS' and replacing every
`Email::Address' occurrence with `Email::Address::XS' is sufficient.

So unlike Email::Address, this module does not use
regular expressions for parsing but instead native XS implementation
parses input string sequentially according to RFC 2822 grammar.

Additionally it has support also for named groups and so can be use
instead of the Email::Address::List module.
%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_archlib/E*
%perl_vendor_autolib/*

%changelog
* Mon Feb 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1
- automated CPAN update

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1.1
- rebuild with new perl 5.26.1

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1
- automated CPAN update

* Sun Oct 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.00-alt2
- to Sisyphus

* Sun Feb 26 2017 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1
- initial import by package builder

