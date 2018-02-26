%define dist Want
Name: perl-%dist
Version: 0.18
Release: alt1.2

Summary: A generalisation of "wantarray"
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-devel perl-threads

%description
This module generalises the mechanism of the wantarray function,
allowing a function to determine in some detail how its return value
is going to be immediately used.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_archlib/Want*
%perl_vendor_autolib/Want

%changelog
* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.18-alt1.2
- rebuilt for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 0.18-alt1.1
- rebuilt with perl 5.12

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- automated CPAN update

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.09-alt2
- fix directory ownership violation
- disable man packaging

* Thu Sep 01 2005 Vitaly Lipatov <lav@altlinux.ru> 0.09-alt1
- first build for ALT Linux Sisyphus
