%define _unpackaged_files_terminate_build 1
Name: perl-Future
Version: 0.50
Release: alt1

Summary: represent an operation awaiting completion
Group: Development/Perl
License: perl

Url: %CPAN Future
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-devel perl(Module/Build.pm) perl(Test/Refcount.pm) perl(Test/Fatal.pm) perl(Test/Identity.pm) perl(Test2/V0.pm)

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Future*
%perl_vendor_privlib/Test/Future*
%doc Changes README

%changelog
* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 0.50-alt1
- new version

* Sat Oct 22 2022 Igor Vlasenko <viy@altlinux.org> 0.49-alt1
- new version

* Thu Jan 27 2022 Igor Vlasenko <viy@altlinux.org> 0.48-alt1
- new version

* Wed Jan 06 2021 Igor Vlasenko <viy@altlinux.ru> 0.47-alt1
- new version

* Sat Oct 24 2020 Igor Vlasenko <viy@altlinux.ru> 0.46-alt1
- new version

* Mon Apr 27 2020 Igor Vlasenko <viy@altlinux.ru> 0.45-alt1
- new version

* Wed Mar 25 2020 Igor Vlasenko <viy@altlinux.ru> 0.44-alt1
- new version

* Wed Jan 08 2020 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1
- new version

* Tue Nov 19 2019 Igor Vlasenko <viy@altlinux.ru> 0.42-alt1
- new version

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 0.41-alt1
- new version

* Tue May 21 2019 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1
- new version

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1
- automated CPAN update

* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1
- automated CPAN update

* Sun Oct 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.35-alt1
- automated CPAN update

* Fri Nov 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.34-alt1
- automated CPAN update

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.33-alt1
- automated CPAN update

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1
- automated CPAN update

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.29-alt1
- automated CPAN update

* Tue Jun 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- automated CPAN update

* Sat Dec 14 2013 Vladimir Lettiev <crux@altlinux.ru> 0.20-alt1
- initial build for ALTLinux

