%define _unpackaged_files_terminate_build 1
%set_perl_req_method relaxed
%define module_name XS-Parse-Keyword
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/CBuilder.pm) perl(ExtUtils/CChecker.pm) perl(ExtUtils/ParseXS.pm) perl(Module/Build.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.31
Release: alt1
Summary: XS functions to assist in parsing keyword syntax
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/P/PE/PEVANS/%{module_name}-%{version}.tar.gz

%description
This module provides some XS functions to assist in writing syntax modules
that provide new perl-visible syntax, primarily for authors of keyword plugins
using the `PL_keyword_plugin' hook mechanism. It is unlikely to be of much
use to anyone else; and highly unlikely to be any use when writing perl code
using these. Unless you are writing a keyword plugin using XS, this module is
not for you.

This module is also currently experimental, and the design is still evolving
and subject to change. Later versions may break ABI compatibility, requiring
changes or at least a rebuild of any module that depends on it.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/X*
%perl_vendor_autolib/*

%changelog
* Thu Dec 29 2022 Igor Vlasenko <viy@altlinux.org> 0.31-alt1
- automated CPAN update

* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 0.30-alt1.1
- automated CPAN update

* Wed Dec 14 2022 Igor Vlasenko <viy@altlinux.org> 0.30-alt1
- automated CPAN update

* Fri Dec 02 2022 Igor Vlasenko <viy@altlinux.org> 0.27-alt1.1
- to Sisyphus as perl-Sub-HandlesVia dep

* Fri Nov 04 2022 Igor Vlasenko <viy@altlinux.org> 0.27-alt1
- updated by package builder

* Tue Oct 25 2022 Igor Vlasenko <viy@altlinux.org> 0.26-alt1
- updated by package builder

* Fri Jul 29 2022 Igor Vlasenko <viy@altlinux.org> 0.25-alt1
- updated by package builder

* Mon Jun 27 2022 Igor Vlasenko <viy@altlinux.org> 0.24-alt1
- updated by package builder

* Fri May 20 2022 Igor Vlasenko <viy@altlinux.org> 0.23-alt1
- updated by package builder

* Wed Feb 23 2022 Igor Vlasenko <viy@altlinux.org> 0.22-alt1
- updated by package builder

* Wed Oct 13 2021 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- updated by package builder

* Sat Oct 09 2021 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- updated by package builder

* Wed Sep 29 2021 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- updated by package builder

* Sun Sep 26 2021 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- updated by package builder

* Thu Sep 23 2021 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- updated by package builder

* Mon Sep 13 2021 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- updated by package builder

* Wed Sep 01 2021 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- updated by package builder

* Fri Aug 13 2021 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- updated by package builder

* Sun Jul 18 2021 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- updated by package builder

* Thu Jul 01 2021 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- updated by package builder

* Wed Jun 16 2021 Igor Vlasenko <viy@altlinux.org> 0.06-alt2
- rebuild with perl 5.34.0

* Wed Jun 02 2021 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- updated by package builder

* Wed May 26 2021 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- updated by package builder

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- updated by package builder

* Mon Apr 26 2021 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- updated by package builder

* Thu Apr 15 2021 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial import by package builder

