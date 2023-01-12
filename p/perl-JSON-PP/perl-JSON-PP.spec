%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(charnames.pm)
# END SourceDeps(oneline)
Epoch: 1
%define dist JSON-PP
Name: perl-%dist
Version: 4.16
Release: alt1

Summary: JSON::XS compatible pure-Perl module
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/I/IS/ISHIGAKI/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Apr 28 2011
BuildRequires: perl-Math-BigInt perl-Tie-IxHash perl-devel perl(Encode.pm) perl(Pod/Man.pm)

%description
JSON::PP was inculded in JSON distribution (CPAN module).
It comes to be a perl core module in Perl 5.14.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/JSON
%_bindir/json_pp
%_man1dir/json_pp*

%changelog
* Thu Jan 12 2023 Igor Vlasenko <viy@altlinux.org> 1:4.16-alt1
- automated CPAN update

* Thu Dec 29 2022 Igor Vlasenko <viy@altlinux.org> 1:4.15-alt1
- automated CPAN update

* Wed Oct 12 2022 Igor Vlasenko <viy@altlinux.org> 1:4.12-alt1
- automated CPAN update

* Mon Aug 01 2022 Igor Vlasenko <viy@altlinux.org> 1:4.11-alt1
- automated CPAN update

* Mon Jun 27 2022 Igor Vlasenko <viy@altlinux.org> 1:4.10-alt1
- automated CPAN update

* Mon May 23 2022 Igor Vlasenko <viy@altlinux.org> 1:4.09-alt1
- automated CPAN update

* Mon Apr 11 2022 Igor Vlasenko <viy@altlinux.org> 1:4.08-alt1
- automated CPAN update

* Tue Dec 21 2021 Igor Vlasenko <viy@altlinux.org> 1:4.07-alt1
- automated CPAN update

* Mon Jan 25 2021 Igor Vlasenko <viy@altlinux.ru> 1:4.06-alt1
- automated CPAN update

* Thu Jul 23 2020 Igor Vlasenko <viy@altlinux.ru> 1:4.05-alt1
- automated CPAN update

* Sun Jul 07 2019 Igor Vlasenko <viy@altlinux.ru> 1:4.04-alt1
- automated CPAN update

* Wed Jun 19 2019 Igor Vlasenko <viy@altlinux.ru> 1:4.03-alt1
- automated CPAN update

* Mon Feb 25 2019 Igor Vlasenko <viy@altlinux.ru> 1:4.02-alt1
- automated CPAN update

* Fri Feb 22 2019 Igor Vlasenko <viy@altlinux.ru> 1:4.01-alt1
- automated CPAN update

* Fri Dec 07 2018 Igor Vlasenko <viy@altlinux.ru> 1:4.00-alt1
- automated CPAN update

* Tue Dec 26 2017 Igor Vlasenko <viy@altlinux.ru> 1:2.97001-alt1
- automated CPAN update

* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 1:2.97000-alt1
- automated CPAN update

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 1:2.94-alt1.1
- automated CPAN update

* Tue May 03 2016 Igor Vlasenko <viy@altlinux.ru> 2.27400-alt1
- automated CPAN update

* Mon Oct 20 2014 Igor Vlasenko <viy@altlinux.ru> 2.27300-alt1
- automated CPAN update

* Sat Oct 19 2013 Igor Vlasenko <viy@altlinux.ru> 2.27203-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 2.27202-alt1
- automated CPAN update

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 2.27200-alt1
- automated CPAN update

* Thu Apr 28 2011 Alexey Tourbin <at@altlinux.ru> 2.27105-alt1
- initial revision
