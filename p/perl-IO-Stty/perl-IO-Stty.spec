%define _unpackaged_files_terminate_build 1
%define dist IO-Stty
Name: perl-%dist
Version: 0.04
Release: alt1

Summary: Change and print terminal line settings
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/T/TO/TODDR/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Fri Jan 21 2011
BuildRequires: perl-Module-Build perl-Test-Pod perl-Test-Pod-Coverage

%description
This is the PERL POSIX compliant stty.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%dir %perl_vendor_privlib/IO
%perl_vendor_privlib/IO/Stty.pm

%changelog
* Mon Feb 24 2020 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- automated CPAN update

* Fri Jan 21 2011 Alexey Tourbin <at@altlinux.ru> 0.03-alt1
- 0.02 -> 0.03

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.02-alt2.1
- Rebuilt with rpm-build-perl-0.5.1.

* Wed Nov 06 2002 Stanislav Ievlev <inger@altlinux.ru> 0.02-alt2
- rebuild with new perl

* Tue Aug 21 2001 Grigory Milev <week@altlinux.ru> 0.02-alt1
- First build for Sisyphus
