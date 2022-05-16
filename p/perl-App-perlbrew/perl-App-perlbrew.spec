%define _unpackaged_files_terminate_build 1
%define oname App-perlbrew
Name: perl-App-perlbrew
Version: 0.95
Release: alt1

Summary: Manage perl installations in your $HOME
Group: Development/Perl
License: mit

Url: %CPAN App-perlbrew
Source0: http://www.cpan.org/authors/id/G/GU/GUGOD/%{oname}-%{version}.tar.gz

Requires: perl-Devel-PatchPerl

BuildArch: noarch
BuildRequires: curl perl-CPAN-Perl-Releases perl-IO-All perl-Capture-Tiny perl-Test-Exception perl-devel perl-Devel-PatchPerl perl-Test-Spec perl-File-Path-Tiny perl-Path-Class perl-Test-Output perl-local-lib perl-Test-NoWarnings perl(Pod/Markdown.pm) perl(Module/Build/Tiny.pm) perl(File/Which.pm) perl(Test/TempDir/Tiny.pm)

%description
%summary

%prep
%setup -q -n %{oname}-%{version}

%build
export SHELL
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes CONTRIBUTING.md
%_bindir/perlbrew
%_man1dir/*
%perl_vendor_privlib/App/perlbrew*
%perl_vendor_privlib/App/Perlbrew*
%doc Changes README

%changelog
* Mon May 16 2022 Igor Vlasenko <viy@altlinux.org> 0.95-alt1
- automated CPAN update

* Sun Dec 05 2021 Igor Vlasenko <viy@altlinux.org> 0.94-alt1
- automated CPAN update

* Tue Nov 23 2021 Igor Vlasenko <viy@altlinux.org> 0.93-alt1
- automated CPAN update

* Wed Apr 21 2021 Igor Vlasenko <viy@altlinux.org> 0.92-alt1
- automated CPAN update

* Mon Feb 01 2021 Igor Vlasenko <viy@altlinux.ru> 0.91-alt1
- automated CPAN update

* Sat Oct 24 2020 Igor Vlasenko <viy@altlinux.ru> 0.89-alt1
- automated CPAN update

* Wed Feb 12 2020 Igor Vlasenko <viy@altlinux.ru> 0.88-alt1
- automated CPAN update

* Mon Oct 28 2019 Igor Vlasenko <viy@altlinux.ru> 0.87-alt1
- automated CPAN update

* Thu Jan 31 2019 Ivan A. Melnikov <iv@altlinux.org> 0.86-alt2
- fix rebuild on Sisyphus

* Wed Jan 30 2019 Igor Vlasenko <viy@altlinux.ru> 0.86-alt1
- automated CPAN update

* Sat Dec 22 2018 Igor Vlasenko <viy@altlinux.ru> 0.85-alt1
- automated CPAN update

* Tue Jun 26 2018 Igor Vlasenko <viy@altlinux.ru> 0.84-alt1
- automated CPAN update

* Wed Dec 20 2017 Igor Vlasenko <viy@altlinux.ru> 0.82-alt1
- automated CPAN update

* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.78-alt1
- automated CPAN update

* Fri Nov 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.77-alt1
- automated CPAN update

* Mon Mar 28 2016 Igor Vlasenko <viy@altlinux.ru> 0.75-alt1
- automated CPAN update

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.73-alt1
- automated CPAN update

* Thu Dec 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.72-alt1
- automated CPAN update

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.69-alt1
- automated CPAN update

* Fri Apr 04 2014 Vladimir Lettiev <crux@altlinux.ru> 0.67-alt1
- 0.66 -> 0.67

* Tue Sep 10 2013 Vladimir Lettiev <crux@altlinux.ru> 0.66-alt1
- 0.52 -> 0.66

* Wed Oct 10 2012 Vladimir Lettiev <crux@altlinux.ru> 0.52-alt1
- initial build for ALTLinux

