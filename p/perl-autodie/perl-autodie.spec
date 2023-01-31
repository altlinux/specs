%define _unpackaged_files_terminate_build 1
%define dist autodie
Name: perl-%dist
Version: 2.36
Release: alt1

Summary: Replace functions with ones that succeed or die with lexical scope
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/T/TO/TODDR/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-BSD-Resource perl-DBM perl-Sub-Identify perl-Tie-RefHash perl-devel perl-Encode perl(IPC/System/Simple.pm)

%description
This distribution provides 'autodie', a lexical equivalent
of 'Fatal'.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README.md AUTHORS
%perl_vendor_privlib/Fatal*
%perl_vendor_privlib/autodie*

%changelog
* Tue Jan 31 2023 Igor Vlasenko <viy@altlinux.org> 2.36-alt1
- automated CPAN update

* Mon Jan 25 2021 Igor Vlasenko <viy@altlinux.ru> 2.34-alt1
- automated CPAN update

* Wed Jan 22 2020 Igor Vlasenko <viy@altlinux.ru> 2.32-alt1
- automated CPAN update

* Wed Jan 08 2020 Igor Vlasenko <viy@altlinux.ru> 2.30-alt1
- automated CPAN update

* Fri Oct 16 2015 Igor Vlasenko <viy@altlinux.ru> 2.29-alt1
- automated CPAN update

* Sat Jan 03 2015 Igor Vlasenko <viy@altlinux.ru> 2.26-alt1
- automated CPAN update

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 2.25-alt1
- automated CPAN update

* Sat Mar 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.23-alt1
- automated CPAN update

* Mon Sep 30 2013 Igor Vlasenko <viy@altlinux.ru> 2.22-alt1
- automated CPAN update

* Fri Sep 06 2013 Vladimir Lettiev <crux@altlinux.ru> 2.20-alt1
- 2.12 -> 2.20
- Encode required for t/utf8_open.t

* Sun Sep 30 2012 Vladimir Lettiev <crux@altlinux.ru> 2.12-alt1
- 2.11 -> 2.12

* Mon Apr 09 2012 Vladimir Lettiev <crux@altlinux.ru> 2.11-alt1
- 2.10 -> 2.11

* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 2.10-alt2
- disabled build dependency on perl-Module-Install

* Sun Sep 19 2010 Alexey Tourbin <at@altlinux.ru> 2.10-alt1
- initial revision
