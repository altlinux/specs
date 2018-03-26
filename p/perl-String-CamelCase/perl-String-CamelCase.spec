%define _unpackaged_files_terminate_build 1
%define dist String-CamelCase
Name: perl-%dist
Version: 0.04
Release: alt1

Summary: CamelCase, de-camelcase
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/H/HI/HIO/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Nov 15 2011
BuildRequires: perl-Test-Pod perl-Test-Pod-Coverage

%description
CamelCase, de-camelcase

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/String

%changelog
* Mon Mar 26 2018 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- automated CPAN update

* Tue Sep 26 2017 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- automated CPAN update

* Tue Nov 15 2011 Alexey Tourbin <at@altlinux.ru> 0.02-alt1
- initial revision
