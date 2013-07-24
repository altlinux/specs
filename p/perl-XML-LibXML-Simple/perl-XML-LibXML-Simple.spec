%define dist XML-LibXML-Simple
Name: perl-%dist
Version: 0.93
Release: alt1

Summary: XML::LibXML based XML::Simple clone
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/M/MA/MARKOV/XML-LibXML-Simple-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Nov 15 2011
BuildRequires: perl-File-Slurp perl-Test-Pod perl-XML-LibXML

%description
None.

%prep
%setup -q -n %dist-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc ChangeLog README
%perl_vendor_privlib/XML

%changelog
* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.93-alt1
- automated CPAN update

* Tue Nov 15 2011 Alexey Tourbin <at@altlinux.ru> 0.91-alt1
- 0.13 -> 0.91

* Fri Mar 12 2010 Kirill Maslinsky <kirill@altlinux.org> 0.13-alt1
- initial build for ALT Linux Sisyphus
