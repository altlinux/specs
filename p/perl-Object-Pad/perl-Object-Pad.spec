%set_perl_req_method relaxed
%define module_name Object-Pad
# bootstrap 
#BuildRequires: perl(Future/AsyncAwait.pm) perl(Devel/MAT/Dumper.pm)
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Data/Dump.pm) perl(ExtUtils/CBuilder.pm) perl(Module/Build.pm) perl(Moo.pm) perl(Syntax/Keyword/Dynamically.pm) perl(Test/Fatal.pm) perl(Test/More.pm) perl(Test/Refcount.pm) perl(XS/Parse/Keyword.pm) perl(XS/Parse/Keyword/Builder.pm) perl(XS/Parse/Sublike.pm) perl(XS/Parse/Sublike/Builder.pm) perl(experimental.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.71
Release: alt1.1
Summary: a simple syntax for lexical slot-based objects
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/P/PE/PEVANS/%{module_name}-%{version}.tar.gz

%description
WARNING This is a highly experimental proof-of-concept. Please don't
actually use this in production :)

This module provides a simple syntax for creating object classes, which uses
private variables that look like lexicals as object member attributes.

%prep
%setup -q -n %{module_name}-%{version}

rm -f "t/80dynamically+Object-Pad.t"
rm -f "t/81async-method+dynamically.t"

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README LICENSE Changes
%perl_vendor_archlib/O*
%perl_vendor_autolib/*

%changelog
* Wed Nov 30 2022 Igor Vlasenko <viy@altlinux.org> 0.71-alt1.1
- to Sisyphus as perl-Sub-HandlesVia dep

* Fri Nov 04 2022 Igor Vlasenko <viy@altlinux.org> 0.71-alt1
- updated by package builder

* Thu Oct 27 2022 Igor Vlasenko <viy@altlinux.org> 0.69-alt1
- updated by package builder

* Sat Aug 13 2022 Igor Vlasenko <viy@altlinux.org> 0.68-alt1
- updated by package builder

* Fri Jul 08 2022 Igor Vlasenko <viy@altlinux.org> 0.66-alt1
- updated by package builder

* Thu May 12 2022 Igor Vlasenko <viy@altlinux.org> 0.65-alt1
- updated by package builder

* Tue Apr 05 2022 Igor Vlasenko <viy@altlinux.org> 0.64-alt1
- updated by package builder

* Fri Mar 25 2022 Igor Vlasenko <viy@altlinux.org> 0.63-alt1
- updated by package builder

* Fri Feb 18 2022 Igor Vlasenko <viy@altlinux.org> 0.61-alt1
- updated by package builder

* Thu Feb 03 2022 Igor Vlasenko <viy@altlinux.org> 0.60-alt1
- updated by package builder

* Sun Dec 19 2021 Igor Vlasenko <viy@altlinux.org> 0.59-alt1
- updated by package builder

* Fri Nov 26 2021 Igor Vlasenko <viy@altlinux.org> 0.58-alt1
- updated by package builder

* Fri Nov 19 2021 Igor Vlasenko <viy@altlinux.ru> 0.57-alt1
- updated by package builder

* Wed Nov 17 2021 Igor Vlasenko <viy@altlinux.ru> 0.56-alt1
- updated by package builder

* Wed Sep 01 2021 Igor Vlasenko <viy@altlinux.ru> 0.52-alt1
- updated by package builder

* Fri Aug 13 2021 Igor Vlasenko <viy@altlinux.ru> 0.51-alt1
- updated by package builder

* Mon Aug 02 2021 Igor Vlasenko <viy@altlinux.ru> 0.47-alt1
- updated by package builder

* Wed Jul 28 2021 Igor Vlasenko <viy@altlinux.ru> 0.46-alt1
- updated by package builder

* Sun Jul 18 2021 Igor Vlasenko <viy@altlinux.ru> 0.45-alt1
- updated by package builder

* Wed Jun 16 2021 Igor Vlasenko <viy@altlinux.org> 0.39-alt2
- rebuild with perl 5.34.0

* Fri May 28 2021 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1
- updated by package builder

* Mon May 17 2021 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1
- updated by package builder

* Wed Apr 14 2021 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1
- updated by package builder

* Sun Feb 21 2021 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1
- updated by package builder

* Wed Dec 30 2020 Igor Vlasenko <viy@altlinux.ru> 0.35-alt1
- updated by package builder

* Fri Nov 06 2020 Igor Vlasenko <viy@altlinux.ru> 0.34-alt1
- updated by package builder

* Wed Oct 07 2020 Igor Vlasenko <viy@altlinux.ru> 0.33-alt1
- updated by package builder

* Wed Oct 07 2020 Cronbuild Service <cronbuild@altlinux.org> 0.32-alt2
- rebuild to get rid of unmets

* Fri Aug 28 2020 Igor Vlasenko <viy@altlinux.ru> 0.32-alt1
- updated by package builder

* Wed Jul 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1
- updated by package builder

* Sun Jun 28 2020 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1
- updated by package builder

* Wed Apr 29 2020 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- updated by package builder

* Tue Apr 14 2020 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- updated by package builder

* Mon Apr 06 2020 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- updated by package builder

* Wed Apr 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- updated by package builder

* Sun Mar 29 2020 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- updated by package builder

* Thu Mar 26 2020 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- updated by package builder

* Sat Mar 21 2020 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- updated by package builder

* Thu Mar 12 2020 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- updated by package builder

* Tue Nov 26 2019 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- updated by package builder

* Mon Nov 18 2019 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- updated by package builder

* Sun Oct 27 2019 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- updated by package builder

* Fri Oct 25 2019 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- updated by package builder

* Mon Oct 21 2019 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- updated by package builder

* Sun Oct 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- initial import by package builder

