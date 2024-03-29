%define _unpackaged_files_terminate_build 1
Name: perl-Specio
Version: 0.48
Release: alt1

Summary: Type constraints and coercions for Perl
Group: Development/Perl
License: Artistic-2

Url: %CPAN Specio
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl(List/MoreUtils.pm) perl(Try/Tiny.pm) perl(Moose/Role.pm) perl(parent.pm) perl(MooseX/Clone.pm) perl(Eval/Closure.pm) perl-devel perl(List/AllUtils.pm) perl(Sub/Name.pm) perl(Devel/PartialDump.pm) perl(Test/Fatal.pm) perl(Throwable/Error.pm) perl(Params/Util.pm) perl(Lingua/EN/Inflect.pm) perl(MooseX/SemiAffordanceAccessor.pm) perl(Moose.pm) perl(namespace/autoclean.pm) perl(Class/Load.pm) perl(MooseX/Params/Validate.pm) perl(Devel/StackTrace.pm) perl(Test/Requires.pm) perl(Test/Needs.pm)

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc TODO.md README.md Changes CONTRIBUTING.md
%perl_vendor_privlib/Specio*
%perl_vendor_privlib/Test/Specio*
%doc Changes README* TODO*

%changelog
* Wed Jun 15 2022 Igor Vlasenko <viy@altlinux.org> 0.48-alt1
- new version

* Mon May 16 2022 Alexandr Antonov <aas@altlinux.org> 0.47.fix-alt4
- pack Test:Specio

* Sat Aug 21 2021 Vitaly Lipatov <lav@altlinux.ru> 0.47.fix-alt3
- apply upstreamed patch reverts hack about old (2014) Moose tests

* Wed Aug 18 2021 Vitaly Lipatov <lav@altlinux.ru> 0.47-alt2
- don't pack Test:Spacio, drop require to Test::More (see #31417)

* Mon Feb 01 2021 Igor Vlasenko <viy@altlinux.ru> 0.47-alt1
- new version

* Wed Mar 25 2020 Igor Vlasenko <viy@altlinux.ru> 0.46-alt1
- new version

* Wed Nov 27 2019 Igor Vlasenko <viy@altlinux.ru> 0.45-alt1
- new version

* Thu Aug 15 2019 Igor Vlasenko <viy@altlinux.ru> 0.44-alt1
- new version

* Tue Oct 30 2018 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1
- automated CPAN update

* Sat Nov 25 2017 Igor Vlasenko <viy@altlinux.ru> 0.42-alt1
- automated CPAN update

* Sun Oct 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1
- automated CPAN update

* Wed May 10 2017 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1
- automated CPAN update

* Fri Feb 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.35-alt1
- automated CPAN update

* Sun Jan 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.32-alt1
- automated CPAN update

* Fri Nov 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1
- automated CPAN update

* Sun Sep 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- automated CPAN update

* Fri Jul 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- automated CPAN update

* Sun Jun 05 2016 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- automated CPAN update

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- automated CPAN update

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- automated CPAN update

* Thu Sep 05 2013 Vladimir Lettiev <crux@altlinux.ru> 0.08-alt1
- initial build for ALTLinux

