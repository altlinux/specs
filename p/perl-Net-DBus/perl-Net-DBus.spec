%define dist Net-DBus
Name: perl-%dist
Version: 1.0.0
Release: alt2

Summary: Perl extension for the DBus message system
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

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
%doc AUTHORS CHANGES README examples
%perl_vendor_archlib/Net
%perl_vendor_autolib/Net

%changelog
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
