%define _unpackaged_files_terminate_build 1
%define sname XML-SemanticDiff

Name: perl-XML-SemanticDiff
Version: 1.0007
Release: alt2
Summary: Perl extension for comparing XML documents
License: GPL+ or Artistic
Group: Development/Perl
Url: https://metacpan.org/release/XML-SemanticDiff
Source: %sname-%version.tar
BuildArch: noarch

BuildRequires: perl(XML/Parser.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(warnings.pm)
BuildRequires: perl(Digest/MD5.pm)
BuildRequires: perl(Encode.pm)
BuildRequires: perl(File/Spec.pm)
BuildRequires: perl(IO/Handle.pm)
BuildRequires: perl(IPC/Open3.pm)
BuildRequires: perl(Module/Build.pm)
BuildRequires: perl(Test.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Test/TrailingSpace.pm)

%description
XML::SemanticDiff provides a way to compare the contents and structure of two
XML documents. By default, it returns a list of hashrefs where each hashref
describes a single difference between the two docs.

%prep
%setup -q -n %sname-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendorlib/XML*
%doc Changes LICENSE META.json META.yml  README eg

%changelog
* Wed Apr 10 2019 Igor Vlasenko <viy@altlinux.ru> 1.0007-alt2
- bumped release to override autoimports

* Mon Apr 08 2019 Alexandr Antonov <aas@altlinux.org> 1.0007-alt1
- initial build for ALT

* Thu Oct 04 2018 Igor Vlasenko <viy@altlinux.ru> 1.0007-alt1_2
- update by mgaimport

* Mon Aug 27 2018 Igor Vlasenko <viy@altlinux.ru> 1.0007-alt1_1
- update by mgaimport

* Fri Oct 13 2017 Igor Vlasenko <viy@altlinux.ru> 1.0006-alt1_2
- update by mgaimport

* Mon Sep 25 2017 Igor Vlasenko <viy@altlinux.ru> 1.0005-alt1_1
- update by mgaimport

* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 1.0004-alt2_5
- update by mgaimport

* Sun Feb 21 2016 Igor Vlasenko <viy@altlinux.ru> 1.0004-alt2_4
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.0004-alt2_3
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.0004-alt2_2
- update by mgaimport

* Tue Sep 02 2014 Cronbuild Service <cronbuild@altlinux.org> 1.0004-alt2_1
- rebuild to get rid of unmets

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.0004-alt1_1
- update by mgaimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.0000-alt1_2
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 1.0000-alt1_1
- converted for ALT Linux by srpmconvert tools
