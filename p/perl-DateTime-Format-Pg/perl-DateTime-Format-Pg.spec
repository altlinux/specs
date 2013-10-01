# BEGIN SourceDeps(oneline):
BuildRequires: perl(CPAN/Meta.pm) perl(CPAN/Meta/Prereqs.pm) perl(DateTime.pm) perl(DateTime/Duration.pm) perl(DateTime/Format/Builder.pm) perl(DateTime/TimeZone.pm) perl(DateTime/TimeZone/Floating.pm) perl(DateTime/TimeZone/UTC.pm) perl(Module/Build.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define module_version 0.16009
%define module_name DateTime-Format-Pg
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.16009
Release: alt1
Summary: Parse and format PostgreSQL dates and times
Group: Development/Perl
License: perl
URL: https://github.com/lestrrat/DateTime-Format-Pg

Source0: http://cpan.org.ua/authors/id/D/DM/DMAKI/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE Changes README.md
%perl_vendor_privlib/D*

%changelog
* Tue Oct 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.16009-alt1
- regenerated from template by package builder

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.16008-alt1_4
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.16008-alt1_3
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.16008-alt1_2
- update to new release by fcimport

* Wed Jan 09 2013 Igor Vlasenko <viy@altlinux.ru> 0.16008-alt1_1
- update to new release by fcimport

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.16007-alt2_4
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.16007-alt1_4
- update to new release by fcimport

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.16007-alt1_2
- fc import

