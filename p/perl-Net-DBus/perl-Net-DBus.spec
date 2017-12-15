%define _unpackaged_files_terminate_build 1
%define dist Net-DBus
Name: perl-%dist
Version: 1.1.0
Release: alt1.1.1.1

Summary: Perl extension for the DBus message system
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/D/DA/DANBERR/Net-DBus-%{version}.tar.gz

# Automatically added by buildreq on Mon Oct 10 2011
BuildRequires: libdbus-devel perl-Test-Pod perl-Test-Pod-Coverage perl-XML-Twig

%description
Net::DBus provides a Perl API for the DBus message system. The DBus Perl
interface is currently operating against the 0.32 development version of
DBus, but should work with later versions too, providing the API changes
have not been too drastic.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

# workaround syntax check failures
%define __spec_autodep_custom_pre export PERL5OPT='-I%buildroot%perl_vendor_archlib -MNet::DBus'

%files
%doc AUTHORS Changes README* examples
%perl_vendor_archlib/Net
%perl_vendor_autolib/Net

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1.1
- rebuild with new perl 5.22.0

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt4.1
- rebuild with new perl 5.20.1

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 1.0.0-alt4
- built for perl 5.18

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 1.0.0-alt3
- rebuilt for perl-5.16

* Mon Oct 10 2011 Alexey Tourbin <at@altlinux.ru> 1.0.0-alt2
- rebuilt for perl-5.14

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1
- automated CPAN update

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 0.33.6-alt2.1
- rebuilt with perl 5.12

* Tue Jun 29 2010 Vladimir Lettiev <crux@altlinux.ru> 0.33.6-alt2
- fix deps

* Sun Sep 14 2008 Vladimir Lettiev <crux@altlinux.ru> 0.33.6-alt1
- Initial build for Sisyphus
