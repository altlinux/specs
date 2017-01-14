%define _unpackaged_files_terminate_build 1
%define dist Lingua-EN-Inflect
Name: perl-%dist
Version: 1.901
Release: alt1

Summary: Convert singular to plural, select "a" or "an"
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/D/DC/DCONWAY/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Sep 26 2012
BuildRequires: perl-devel

%description
The exportable subroutines of Lingua::EN::Inflect provide plural
inflections, "a"/"an" selection for English words, and manipulation
of numbers as words.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Lingua

%changelog
* Sat Jan 14 2017 Igor Vlasenko <viy@altlinux.ru> 1.901-alt1
- automated CPAN update

* Fri Jul 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.900-alt1
- automated CPAN update

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 1.899-alt1
- automated CPAN update

* Wed Sep 26 2012 Alexey Tourbin <at@altlinux.ru> 1.895-alt1
- 1.893 -> 1.895

* Sun Apr 24 2011 Alexey Tourbin <at@altlinux.ru> 1.893-alt1
- 1.891 -> 1.893

* Mon Apr 26 2010 Alexey Tourbin <at@altlinux.ru> 1.891-alt1
- 1.89 -> 1.891

* Thu Jul 14 2005 Alexey Tourbin <at@altlinux.ru> 1.89-alt1
- initial revision
