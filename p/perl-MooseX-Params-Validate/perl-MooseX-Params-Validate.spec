%define _unpackaged_files_terminate_build 1
%define dist MooseX-Params-Validate
Name: perl-%dist
Version: 0.21
Release: alt1.1

Summary: an extension of Params::Validate for using Moose's types
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/D/DR/DROLSKY/MooseX-Params-Validate-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Oct 26 2011
BuildRequires: perl-Devel-Caller perl-Moose perl-Params-Validate perl-Test-Fatal

%description
This module fills a gap in Moose by adding method parameter validation
to Moose.  This is just one of many developing options, it should not
be considered the "official" one by any means though.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README.md
%perl_vendor_privlib/MooseX

%changelog
* Sat Apr 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1.1
- rebuild to restore role requires

* Fri Oct 16 2015 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- automated CPAN update

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- automated CPAN update

* Wed Oct 26 2011 Alexey Tourbin <at@altlinux.ru> 0.16-alt1
- 0.14 -> 0.16

* Tue Apr 13 2010 Alexey Tourbin <at@altlinux.ru> 0.14-alt1
- initial revision
