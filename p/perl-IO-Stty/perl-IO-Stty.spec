%define dist IO-Stty
Name: perl-%dist
Version: 0.03
Release: alt1

Summary: Change and print terminal line settings
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Fri Jan 21 2011
BuildRequires: perl-Module-Build perl-Test-Pod perl-Test-Pod-Coverage

%description
This is the PERL POSIX compliant stty.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install
rm %buildroot%_bindir/stty.pl

%files
%doc Changes README
%dir %perl_vendor_privlib/IO
%perl_vendor_privlib/IO/Stty.pm

%changelog
* Fri Jan 21 2011 Alexey Tourbin <at@altlinux.ru> 0.03-alt1
- 0.02 -> 0.03

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.02-alt2.1
- Rebuilt with rpm-build-perl-0.5.1.

* Wed Nov 06 2002 Stanislav Ievlev <inger@altlinux.ru> 0.02-alt2
- rebuild with new perl

* Tue Aug 21 2001 Grigory Milev <week@altlinux.ru> 0.02-alt1
- First build for Sisyphus
