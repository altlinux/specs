Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Carp.pm) perl(Exporter.pm) perl(IO/Handle.pm) perl(IPC/Open3.pm) perl(Pod/Coverage/TrustPod.pm) perl(Pod/Wordlist.pm) perl(Test/CPAN/Changes.pm) perl(Test/EOL.pm) perl(Test/Mojibake.pm) perl(Test/NoTabs.pm) perl(Test/Pod.pm) perl(Test/Pod/Coverage.pm) perl(Test/Spelling.pm) perl(Test/Synopsis.pm) perl(Test/Version.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:          perl-URI-FromHash 
Version:       0.05
Release:       alt1_2
Summary:       Build a URI from a set of named parameters 
# see lib/URI/FromHash.pm
License:       GPL+ or Artistic

Url:           http://search.cpan.org/dist/URI-FromHash
Source0:        http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/URI-FromHash-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(Module/Build/Compat.pm)
BuildRequires: perl(Params/Validate.pm)
BuildRequires: perl(Test/Fatal.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(URI.pm)


Source44: import.info

%description
This module provides a simple one-subroutine "named parameters" style
interface for creating URIs. Underneath the hood it uses 'URI.pm', though
because of the simplified interface it may not support all possible options
for all types of URIs.

It was created for the common case where you simply want to have a simple
interface for creating syntactically correct URIs from known components
(like a path and query string). Doing this using the native 'URI.pm'
interface is rather tedious, requiring a number of method calls, which is
particularly ugly when done inside a templating system such as Mason or
TT2.


%prep
%setup -q -n URI-FromHash-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes
%doc LICENSE
%{perl_vendor_privlib}/URI*

%changelog
* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_2
- update to new release by fcimport

* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_1
- update to new release by fcimport

* Mon Oct 26 2015 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- automated CPAN update

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_7
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_5
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_4
- update to new release by fcimport

* Tue Dec 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_3
- Sisyphus build

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_3
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_2
- update to new release by fcimport

* Fri Jul 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_1
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1_15
- update to new release by fcimport

* Wed Dec 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1_14
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1_13
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1_11
- fc import

