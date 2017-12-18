%define _unpackaged_files_terminate_build 1
%define dist XML-LibXML-Simple
Name: perl-%dist
Version: 0.99
Release: alt1

Summary: XML::LibXML based XML::Simple clone
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/M/MA/MARKOV/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Nov 15 2011
BuildRequires: perl-File-Slurp perl-Test-Pod perl-XML-LibXML perl(File/Slurp/Tiny.pm)

%description
None.

%prep
%setup -q -n %{dist}-%{version}
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc ChangeLog README
%perl_vendor_privlib/XML

%changelog
* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.99-alt1
- automated CPAN update

* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 0.98-alt1
- automated CPAN update

* Wed Apr 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.97-alt1
- automated CPAN update

* Sat Mar 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.96-alt1
- automated CPAN update

* Thu Dec 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.95-alt1
- automated CPAN update

* Tue Jun 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.94-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.93-alt1
- automated CPAN update

* Tue Nov 15 2011 Alexey Tourbin <at@altlinux.ru> 0.91-alt1
- 0.13 -> 0.91

* Fri Mar 12 2010 Kirill Maslinsky <kirill@altlinux.org> 0.13-alt1
- initial build for ALT Linux Sisyphus
