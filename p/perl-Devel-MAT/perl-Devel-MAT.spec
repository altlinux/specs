%define module_name Devel-MAT
%set_perl_req_method relaxed
%define _without_test 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Commandable/Invocation.pm) perl(Devel/MAT/Dumper.pm) perl(ExtUtils/CBuilder.pm) perl(Feature/Compat/Try.pm) perl(File/ShareDir.pm) perl(File/Spec.pm) perl(Heap.pm) perl(List/Util.pm) perl(List/UtilsBy.pm) perl(Module/Build.pm) perl(Module/Pluggable.pm) perl(String/Tagged.pm) perl(String/Tagged/Terminal.pm) perl(Struct/Dumb.pm) perl(Syntax/Keyword/Match.pm) perl(Term/ReadLine.pm) perl(Test/Identity.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.49
Release: alt1.1
Summary: Perl Memory Analysis Tool
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/P/PE/PEVANS/%{module_name}-%{version}.tar.gz

%description
From summary: %summary

%package scripts
Summary: %module_name scripts
Group: Development/Perl
Requires: %name = %{?epoch:%epoch:}%version-%release

%description scripts
scripts for %module_name

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build --install_path bindoc=%_man1dir

%install
%perl_vendor_install

%files
%doc LICENSE Changes README doc
%perl_vendor_archlib/D*
%perl_vendor_autolib/*

%files scripts
%_man1dir/*
%_bindir/*

%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 0.49-alt1.1
- to Sisyphus as perl-Sub-HandlesVia dep

* Tue Oct 04 2022 Igor Vlasenko <viy@altlinux.org> 0.49-alt1
- updated by package builder

* Wed Aug 31 2022 Igor Vlasenko <viy@altlinux.org> 0.48-alt1
- updated by package builder

* Mon Apr 04 2022 Igor Vlasenko <viy@altlinux.org> 0.47-alt1
- updated by package builder

* Fri Apr 01 2022 Igor Vlasenko <viy@altlinux.org> 0.46-alt1
- updated by package builder

* Tue Mar 01 2022 Igor Vlasenko <viy@altlinux.org> 0.45-alt1
- updated by package builder

* Wed Jun 16 2021 Igor Vlasenko <viy@altlinux.org> 0.44-alt2
- rebuild with perl 5.34.0

* Tue Mar 30 2021 Igor Vlasenko <viy@altlinux.ru> 0.44-alt1
- updated by package builder

* Wed Oct 07 2020 Cronbuild Service <cronbuild@altlinux.org> 0.43-alt2
- rebuild to get rid of unmets

* Wed Apr 29 2020 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1
- updated by package builder

* Fri Mar 22 2019 Igor Vlasenko <viy@altlinux.ru> 0.42-alt1
- updated by package builder

* Fri Feb 01 2019 Cronbuild Service <cronbuild@altlinux.org> 0.41-alt1.1
- rebuild with perl 5.28.1

* Wed Jan 16 2019 Igor Vlasenko <viy@altlinux.ru> 0.41-alt1
- regenerated from template by package builder

* Wed Sep 12 2018 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1
- regenerated from template by package builder

* Sat Aug 11 2018 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1
- regenerated from template by package builder

* Tue Aug 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1
- regenerated from template by package builder

* Wed Jul 25 2018 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1
- regenerated from template by package builder

* Fri Jul 20 2018 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1
- regenerated from template by package builder

* Sat Jul 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.35-alt1
- regenerated from template by package builder

* Wed Apr 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.34-alt1
- regenerated from template by package builder

* Wed Dec 20 2017 Igor Vlasenko <viy@altlinux.ru> 0.32-alt1
- regenerated from template by package builder

* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.31-alt2
- rebuild with perl 5.26

* Sat Nov 25 2017 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1
- regenerated from template by package builder

* Fri Oct 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1
- regenerated from template by package builder

* Sun Feb 12 2017 Cronbuild Service <cronbuild@altlinux.org> 0.24-alt2
- rebuild to get rid of unmets

* Sat Nov 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- regenerated from template by package builder

* Sun Mar 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- regenerated from template by package builder

* Mon Nov 30 2015 Igor Vlasenko <viy@altlinux.ru> 0.21-alt2
- rebuild with perl 522

* Tue Nov 03 2015 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- regenerated from template by package builder

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- initial import by package builder

