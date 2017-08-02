%define _unpackaged_files_terminate_build 1
%define dist Devel-PartialDump
Name: perl-%dist
Version: 0.20
Release: alt1

Summary: Partial dumping of data structures, optimized for argument printing
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/E/ET/ETHER/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Nov 20 2011
BuildRequires: perl-Moose perl-Test-Warn perl-Test-use-ok perl-namespace-clean perl(Module/Build/Tiny.pm) perl(Class/Tiny.pm) perl(Test/Warnings.pm)

%description
This module is a data dumper optimized for logging of arbitrary parameters.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Devel

%changelog
* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- automated CPAN update

* Thu Mar 06 2014 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- automated CPAN update

* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 0.15-alt1
- initial revision
