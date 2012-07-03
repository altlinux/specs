%define dist POE-Component-Generic
Name: perl-%dist
Version: 0.1401
Release: alt1

Summary: Generic non-blocking POE interface to any OO-module
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# avoid dependency on Net::SSH2
%add_findreq_skiplist */POE/Component/Generic/Net/SSH2.pm

# Automatically added by buildreq on Sun Nov 20 2011 (-bi)
BuildRequires: perl-IO-Stty perl-Net-SSH-Perl perl-Net-SSH2 perl-POE perl-Test-Pod perl-Test-Pod-Coverage

%description
POE::Component::Generic is a POE component that provides a non-blocking
wrapper around any object.  This allows you to build a POE component from
existing code with minimal effort.

%prep
%setup -q -n %dist-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README example
%perl_vendor_privlib/POE

%changelog
* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 0.1401-alt1
- 0.1205 -> 0.1401

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.1205-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.1205-alt1
- automated CPAN update

* Thu Nov 20 2008 Michael Bochkaryov <misha@altlinux.ru> 0.1100-alt2
- fix directory owndership violation

* Sun Jul 27 2008 Michael Bochkaryov <misha@altlinux.ru> 0.1100-alt1
- first build for ALT Linux Sisyphus
