%define dist POE-Component-IKC
Name: perl-%dist
Version: 0.2302
Release: alt1

Summary: Inter-Kernel Communication for POE
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Nov 20 2011
BuildRequires: perl-FreezeThaw perl-POE perl-Test-Pod perl-Test-Pod-Coverage

%description
POE::Component::IKC provides inter-kernel communication functionality
for POE based applications.

This a first draft if Inter-Kernel Communication for POE. It is intended
as a point of reference for discusion of issues involved.

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
* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 0.2302-alt1
- 0.2200 -> 0.2302

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.2200-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Jul 16 2010 Igor Vlasenko <viy@altlinux.ru> 0.2200-alt1
- automated CPAN update

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 0.2001-alt1.1
- NMU for unknown reason

* Tue Jul 29 2008 Michael Bochkaryov <misha@altlinux.ru> 0.2001-alt1
- first build for ALT Linux Sisyphus
