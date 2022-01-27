%define _unpackaged_files_terminate_build 1
%define dist MooseX-Types-JSON
Name: perl-%dist
Version: 1.01
Release: alt1

Summary: JSON datatype for Moose
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/P/PL/PLICEASE/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Apr 13 2010
BuildRequires: perl-Class-C3-XS perl-JSON-XS perl-MooseX-Types perl-Test-Pod perl-JSON

%description
%summary.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README author.yml examples
%perl_vendor_privlib/MooseX*

%changelog
* Thu Jan 27 2022 Igor Vlasenko <viy@altlinux.org> 1.01-alt1
- automated CPAN update

* Sat Apr 09 2016 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1.1
- rebuild to restore role requires

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1
- automated CPAN update

* Mon Jan 06 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- automated CPAN update

* Tue Apr 13 2010 Alexey Tourbin <at@altlinux.ru> 0.02-alt1
- initial revision
