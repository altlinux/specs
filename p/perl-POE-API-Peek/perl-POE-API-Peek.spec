%define dist POE-API-Peek
Name: perl-%dist
Version: 2.19
Release: alt1

Summary: Peek into the internals of a running POE environment
License: BSD
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Nov 20 2011
BuildRequires: perl-Devel-Size perl-POE perl-devel

%description
POE::API::Peek extends the POE::Kernel interface to provide clean access to
Kernel internals in a cross-version compatible manner.  Other calculated data
is also available.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes LICENSE README
%perl_vendor_privlib/POE

%changelog
* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 2.19-alt1
- 1.34 -> 2.19

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.34-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Jul 16 2010 Igor Vlasenko <viy@altlinux.ru> 1.34-alt1
- automated CPAN update

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 1.32-alt1.1
- NMU for unknown reason

* Tue Jul 29 2008 Michael Bochkaryov <misha@altlinux.ru> 1.32-alt1
- first build for ALT Linux Sisyphus
