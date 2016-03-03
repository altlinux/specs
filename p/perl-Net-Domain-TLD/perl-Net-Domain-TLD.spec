%define _unpackaged_files_terminate_build 1
%define dist Net-Domain-TLD

Name: perl-%dist
Version: 1.74
Release: alt1

Summary: Gives ability to retrieve currently available TLD
License: Perl
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/A/AL/ALEXP/Net-Domain-TLD-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Apr 20 2011
BuildRequires: perl-devel

%description
The purpose of this module is to provide user with current list of available
top level domain names including new ICANN additions and ccTLDs

%prep
%setup -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Net/Domain

%changelog
* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.74-alt1
- automated CPAN update

* Wed Feb 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.73-alt1
- automated CPAN update

* Mon Mar 24 2014 Igor Vlasenko <viy@altlinux.ru> 1.72-alt1
- automated CPAN update

* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.70-alt1
- automated CPAN update

* Wed Apr 20 2011 Victor Forsiuk <force@altlinux.org> 1.69-alt1
- 1.69

* Fri Aug 11 2006 Alexey Tourbin <at@altlinux.ru> 1.65-alt1
- 1.5 -> 1.65

* Mon Aug 30 2004 Alexey Tourbin <at@altlinux.ru> 1.5-alt1
- initial revision (needed by perl-Email-Valid, which is needed by otrs)
