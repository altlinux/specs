%define _unpackaged_files_terminate_build 1
%define module_name XS-Parse-Sublike
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/CBuilder.pm) perl(Module/Build.pm) perl(Sub/Util.pm) perl(Test/Fatal.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.17
Release: alt1
Summary: XS functions to assist in parsing C<sub>-like syntax
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/P/PE/PEVANS/%{module_name}-%{version}.tar.gz

%description
This module provides some XS functions to assist in writing parsers for
`sub'-like syntax, primarily for authors of keyword plugins using the
`PL_keyword_plugin' hook mechanism. It is unlikely to be of much use to
anyone else; and highly unlikely to be any use when writing perl code using
these. Unless you are writing a keyword plugin using XS, this module is not
for you.

This module is also highly experimental, consisting currently of pieces of
code extracted and refactored from the Future::AsyncAwait manpage and the Object::Pad manpage.
It is hoped eventually this will be useful for other modules too.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_archlib/X*
%perl_vendor_autolib/*

%changelog
* Thu Mar 23 2023 Igor Vlasenko <viy@altlinux.org> 0.17-alt1
- automated CPAN update

* Fri Dec 02 2022 Igor Vlasenko <viy@altlinux.org> 0.16-alt1.1
- to Sisyphus as perl-Sub-HandlesVia dep

* Sat Dec 18 2021 Igor Vlasenko <viy@altlinux.org> 0.16-alt1
- updated by package builder

* Fri Oct 29 2021 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- updated by package builder

* Wed Sep 01 2021 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- updated by package builder

* Thu Jul 01 2021 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- updated by package builder

* Wed Jun 16 2021 Igor Vlasenko <viy@altlinux.org> 0.11-alt2
- rebuild with perl 5.34.0

* Tue Jan 19 2021 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- updated by package builder

* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.10-alt2
- rebuild with perl 5.30

* Mon Jun 22 2020 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- updated by package builder

* Fri Jun 19 2020 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- updated by package builder

* Sat Jun 13 2020 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- updated by package builder

* Fri Apr 03 2020 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- updated by package builder

* Sat Mar 28 2020 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- updated by package builder

* Thu Mar 19 2020 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- initial import by package builder

