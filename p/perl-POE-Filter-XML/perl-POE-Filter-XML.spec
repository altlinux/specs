%define dist POE-Filter-XML
Name: perl-%dist
Version: 1.102960
Release: alt1

Summary: XML parsing for the POE framework
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# cannot be detected automatically
Requires: perl-MooseX-InsideOut

# Automatically added by buildreq on Sun Nov 20 2011
BuildRequires: perl-MooseX-Declare perl-MooseX-InsideOut perl-MooseX-NonMoose perl-POE perl-XML-LibXML perl-devel

%description
POE::Filter::XML provides POE with a completely encapsulated XML parsing
strategy for POE::Wheels that will be dealing with XML streams.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/POE

%changelog
* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 1.102960-alt1
- 0.38 -> 1.102960

* Mon Nov 15 2010 Alexey Shabalin <shaba@altlinux.ru> 0.38-alt1
- 0.38
- drop %%perl_vendor_man3dir

* Wed Dec 03 2008 Alexey Shabalin <shaba@altlinux.ru> 0.33-alt1
- initial build for ALT Linux Sisyphus
