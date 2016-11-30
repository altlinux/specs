Serial: 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(DateTime.pm) perl(ExtUtils/MakeMaker.pm) perl(Test/More.pm) perl(strict.pm) perl(version.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define module_version 1.2.0
%define module_name DateTime-Format-RFC3339
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.2.0
Release: alt2
Summary: Parse and format RFC3339 datetime strings
Group: Development/Perl
License: unrestricted
URL: http://search.cpan.org/dist/DateTime-Format-RFC3339/

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/I/IK/IKEGAMI/%{module_name}-v%{module_version}.tar.gz
BuildArch: noarch

%description
This module understands the RFC3339 date/time format, an ISO 8601 profile,
defined at http://tools.ietf.org/html/rfc3339.

It can be used to parse these formats in order to create the appropriate
objects.
%prep
%setup -q -n %{module_name}-v%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes LICENSE.txt README.txt
%perl_vendor_privlib/D*

%changelog
* Wed Nov 30 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.2.0-alt2
- regenerated from template by package builder

* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> v1.2.0-alt1_2
- update by mgaimport

* Sat May 14 2016 Igor Vlasenko <viy@altlinux.ru> v1.2.0-alt1_1
- update by mgaimport

* Sun Feb 21 2016 Igor Vlasenko <viy@altlinux.ru> v1.0.5-alt2_7
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> v1.0.5-alt2_6
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> v1.0.5-alt2_4
- update by mgaimport

* Tue Sep 02 2014 Cronbuild Service <cronbuild@altlinux.org> v1.0.5-alt2_3
- rebuild to get rid of unmets

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> v1.0.5-alt1_3
- mga update

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> v1.0.5-alt1_2
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> v1.0.5-alt1_1
- converted for ALT Linux by srpmconvert tools

