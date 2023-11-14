%define _unpackaged_files_terminate_build 1
%define module_name MetaCPAN-Client
%define _without_test 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(HTTP/Tiny.pm) perl(IO/Socket/SSL.pm) perl(JSON/MaybeXS.pm) perl(JSON/PP.pm) perl(LWP/Protocol/https.pm) perl(Moo.pm) perl(Moo/Role.pm) perl(Net/SSLeay.pm) perl(Ref/Util.pm) perl(Safe/Isa.pm) perl(Test/Fatal.pm) perl(Test/More.pm) perl(Test/Needs.pm) perl(Type/Tiny.pm) perl(URI/Escape.pm)
#BuildRequires: perl(HTTP/Tiny/Mech.pm)
#BuildRequires: perl(WWW/Mechanize/Cached.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 2.031000
Release: alt1
Summary: A comprehensive, DWIM-featured client to the MetaCPAN API
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/M/MI/MICKEY/%{module_name}-%{version}.tar.gz
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
%doc README Changes examples
%perl_vendor_privlib/M*

%changelog
* Tue Nov 14 2023 Igor Vlasenko <viy@altlinux.org> 2.031000-alt1
- automated CPAN update

* Mon Aug 22 2022 Igor Vlasenko <viy@altlinux.org> 2.030000-alt1
- automated CPAN update

* Wed Feb 17 2021 Igor Vlasenko <viy@altlinux.ru> 2.029000-alt2
- to Sisyphus as Crypt-CBC dep

* Thu Dec 24 2020 Igor Vlasenko <viy@altlinux.ru> 2.029000-alt1
- updated by package builder

* Fri Aug 28 2020 Igor Vlasenko <viy@altlinux.ru> 2.028000-alt1
- updated by package builder

* Fri Mar 15 2019 Igor Vlasenko <viy@altlinux.ru> 2.026000-alt1
- updated by package builder

* Tue Apr 24 2018 Igor Vlasenko <viy@altlinux.ru> 2.025000-alt1
- regenerated from template by package builder

* Wed Apr 04 2018 Igor Vlasenko <viy@altlinux.ru> 2.023000-alt1
- regenerated from template by package builder

* Wed Dec 20 2017 Igor Vlasenko <viy@altlinux.ru> 2.021000-alt1
- regenerated from template by package builder

* Thu Sep 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.025000-alt1
- regenerated from template by package builder

* Sun Aug 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.022003-alt1
- regenerated from template by package builder

* Mon Jul 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.020000-alt1
- regenerated from template by package builder

* Wed Jul 06 2016 Igor Vlasenko <viy@altlinux.ru> 1.017000-alt1
- regenerated from template by package builder

* Thu Jun 09 2016 Igor Vlasenko <viy@altlinux.ru> 1.015000-alt1
- regenerated from template by package builder

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.014000-alt1
- regenerated from template by package builder

* Wed Oct 14 2015 Igor Vlasenko <viy@altlinux.ru> 1.013000-alt1
- regenerated from template by package builder

* Fri Apr 17 2015 Igor Vlasenko <viy@altlinux.ru> 1.012000-alt1
- regenerated from template by package builder

* Thu Feb 05 2015 Igor Vlasenko <viy@altlinux.ru> 1.011000-alt1
- regenerated from template by package builder

* Mon Jan 26 2015 Igor Vlasenko <viy@altlinux.ru> 1.010000-alt1
- regenerated from template by package builder

* Mon Jan 19 2015 Igor Vlasenko <viy@altlinux.ru> 1.009000-alt1
- regenerated from template by package builder

* Mon Jan 05 2015 Igor Vlasenko <viy@altlinux.ru> 1.008001-alt1
- regenerated from template by package builder

* Mon Nov 24 2014 Igor Vlasenko <viy@altlinux.ru> 1.008000-alt1
- regenerated from template by package builder

* Thu Oct 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.007001-alt1
- regenerated from template by package builder

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.006000-alt1
- regenerated from template by package builder

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.005000-alt1
- regenerated from template by package builder

* Tue May 13 2014 Igor Vlasenko <viy@altlinux.ru> 1.003000-alt1
- initial import by package builder

