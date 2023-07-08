%define _unpackaged_files_terminate_build 1
%define module_name IPC-System-Options
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Capture/Tiny.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(IO/Handle.pm) perl(IPC/Open3.pm) perl(IPC/Run.pm) perl(Log/Any/IfLOG.pm) perl(Pod/Coverage/TrustPod.pm) perl(Proc/ChildError.pm) perl(String/ShellQuote.pm) perl(Test/More.pm) perl(Test/Pod.pm) perl(Test/Pod/Coverage.pm) perl(strict.pm) perl(warnings.pm) perl(Test/Exception.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.341
Release: alt1
Summary: Perl's system() and backtick/qx replacement/wrapper, with options
Group: Development/Perl
License: perl
URL: https://metacpan.org/release/IPC-System-Options

Source0: http://www.cpan.org/authors/id/P/PE/PERLANCAR/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
From summary: %summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/I*

%changelog
* Sat Jul 08 2023 Igor Vlasenko <viy@altlinux.org> 0.341-alt1
- automated CPAN update

* Wed Feb 10 2021 Igor Vlasenko <viy@altlinux.ru> 0.340-alt1
- automated CPAN update

* Tue Sep 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.338-alt1
- automated CPAN update

* Tue Jun 09 2020 Igor Vlasenko <viy@altlinux.ru> 0.337-alt1
- automated CPAN update

* Mon Apr 27 2020 Igor Vlasenko <viy@altlinux.ru> 0.336-alt1
- automated CPAN update

* Sat Mar 14 2020 Igor Vlasenko <viy@altlinux.ru> 0.334-alt1
- automated CPAN update

* Wed Feb 12 2020 Igor Vlasenko <viy@altlinux.ru> 0.333-alt1
- automated CPAN update

* Wed Sep 11 2019 Igor Vlasenko <viy@altlinux.ru> 0.332-alt1
- automated CPAN update

* Mon Jan 21 2019 Igor Vlasenko <viy@altlinux.ru> 0.331-alt1
- automated CPAN update

* Tue Sep 26 2017 Igor Vlasenko <viy@altlinux.ru> 0.330-alt1
- automated CPAN update

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1
- automated CPAN update

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1
- automated CPAN update

* Wed Oct 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.29-alt1
- automated CPAN update

* Thu Jul 28 2016 Igor Vlasenko <viy@altlinux.ru> 0.27-alt2
- to Sisyphus

* Thu Jun 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1
- regenerated from template by package builder

* Fri Feb 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- regenerated from template by package builder

* Wed Oct 14 2015 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- regenerated from template by package builder

* Fri Apr 17 2015 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- regenerated from template by package builder

* Tue Feb 10 2015 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- regenerated from template by package builder

* Mon Jan 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- regenerated from template by package builder

* Mon Jan 12 2015 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- initial import by package builder

