%define _unpackaged_files_terminate_build 1
BuildRequires: perl(Test/Fatal.pm) perl(CPAN/Meta/Requirements.pm) perl(CPAN/Meta/Check.pm)
BuildRequires: perl(Test/Warnings.pm)
%define dist Getopt-Long-Descriptive
Name: perl-%dist
Version: 0.111
Release: alt1

Summary: Getopt::Long, but simpler and more powerful
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/R/RJ/RJBS/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Oct 25 2011
BuildRequires: perl-Params-Validate perl-Sub-Exporter perl-devel perl(Capture/Tiny.pm)

%description
Getopt::Long::Descriptive is yet another Getopt library.  It's built atop
Getopt::Long, and gets a lot of its features, but tries to avoid making you
think about its huge array of options.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Getopt

%changelog
* Thu Jan 12 2023 Igor Vlasenko <viy@altlinux.org> 0.111-alt1
- automated CPAN update

* Mon Nov 01 2021 Igor Vlasenko <viy@altlinux.org> 0.110-alt1
- automated CPAN update

* Wed Mar 24 2021 Igor Vlasenko <viy@altlinux.org> 0.109-alt1
- automated CPAN update

* Mon Mar 15 2021 Igor Vlasenko <viy@altlinux.org> 0.107-alt1
- automated CPAN update

* Tue Mar 03 2020 Igor Vlasenko <viy@altlinux.ru> 0.105-alt1
- automated CPAN update

* Mon Apr 29 2019 Igor Vlasenko <viy@altlinux.ru> 0.104-alt1
- automated CPAN update

* Wed Aug 08 2018 Igor Vlasenko <viy@altlinux.ru> 0.103-alt1
- automated CPAN update

* Thu Feb 22 2018 Igor Vlasenko <viy@altlinux.ru> 0.102-alt1
- automated CPAN update

* Thu Feb 01 2018 Igor Vlasenko <viy@altlinux.ru> 0.101-alt1
- automated CPAN update

* Mon Jul 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.100-alt1
- automated CPAN update

* Mon Jan 26 2015 Igor Vlasenko <viy@altlinux.ru> 0.099-alt1
- automated CPAN update

* Tue Nov 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.098-alt1
- automated CPAN update

* Thu Mar 06 2014 Igor Vlasenko <viy@altlinux.ru> 0.097-alt1
- automated CPAN update

* Sat Oct 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.096-alt1
- automated CPAN update

* Wed Oct 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.095-alt1
- automated CPAN update

* Mon Sep 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.094-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.093-alt1
- automated CPAN update

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.092-alt1
- automated CPAN update

* Mon Apr 16 2012 Vladimir Lettiev <crux@altlinux.ru> 0.091-alt1
- 0.090 -> 0.091

* Tue Oct 25 2011 Alexey Tourbin <at@altlinux.ru> 0.090-alt1
- 0.087 -> 0.090

* Wed Dec 29 2010 Alexey Tourbin <at@altlinux.ru> 0.087-alt1
- 0.085 -> 0.087

* Fri Apr 09 2010 Alexey Tourbin <at@altlinux.ru> 0.085-alt1
- initial revision, for perl-DBIx-Class
