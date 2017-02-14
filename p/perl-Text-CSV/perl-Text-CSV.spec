%define _unpackaged_files_terminate_build 1
%define module Text-CSV

Name: perl-%module
Version: 1.91
Release: alt1

Summary: Text::CSV - comma-separated values manipulation routines
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source0: http://www.cpan.org/authors/id/I/IS/ISHIGAKI/%{module}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Fri Feb 11 2011
BuildRequires: perl-Test-Pod perl-Text-CSV_XS perl(charnames.pm)

%description
Text::CSV provides facilities for the composition and decomposition of
comma-separated values. An instance of the Text::CSV class can combine
fields into a CSV string and parse a CSV string into fields.

%prep
%setup -q -n %{module}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README.md
%perl_vendor_privlib/Text

%changelog
* Tue Feb 14 2017 Igor Vlasenko <viy@altlinux.ru> 1.91-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 1.33-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.32-alt1
- automated CPAN update

* Fri Feb 11 2011 Victor Forsiuk <force@altlinux.org> 1.21-alt1
- 1.21

* Tue Nov 16 2010 Victor Forsiuk <force@altlinux.org> 1.20-alt1
- 1.20

* Tue Jun 22 2010 Victor Forsiuk <force@altlinux.org> 1.18-alt1
- 1.18

* Thu Apr 08 2010 Victor Forsiuk <force@altlinux.org> 1.17-alt1
- 1.17

* Fri Feb 12 2010 Victor Forsiuk <force@altlinux.org> 1.16-alt1
- 1.16

* Mon Nov 30 2009 Victor Forsyuk <force@altlinux.org> 1.15-alt1
- 1.15

* Tue Dec 30 2008 Victor Forsyuk <force@altlinux.org> 1.10-alt1
- 1.10

* Fri Jul 27 2007 Victor Forsyuk <force@altlinux.org> 0.01-alt2
- Spec cleanups.

* Tue May 02 2006 Igor Zubkov <icesik@altlinux.ru> 0.01-alt1
- first build for ALT Linux Sisyphus
