%define _unpackaged_files_terminate_build 1
%define module_name String-Tagged
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Module/Build.pm) perl(Test/Identity.pm) perl(Test/More.pm) perl(Test2/V0.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators
BuildRequires: perl(experimental.pm)

Name: perl-%module_name
Version: 0.20
Release: alt1
Summary: string buffers with value tags on extents
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/P/PE/PEVANS/%{module_name}-%{version}.tar.gz
BuildArch: noarch

# was due to experimental.pm not installed
Patch: String-Tagged-0.17-alt-perl534.patch

%description
%summary

%prep
%setup -q -n %{module_name}-%{version}
#patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README examples
%perl_vendor_privlib/S*

%changelog
* Sat Feb 18 2023 Igor Vlasenko <viy@altlinux.org> 0.20-alt1
- automated CPAN update

* Thu Feb 09 2023 Igor Vlasenko <viy@altlinux.org> 0.19-alt1
- automated CPAN update

* Thu Dec 01 2022 Igor Vlasenko <viy@altlinux.org> 0.18-alt1.1
- to Sisyphus as perl-Sub-HandlesVia dep

* Sun May 01 2022 Igor Vlasenko <viy@altlinux.org> 0.18-alt1
- updated by package builder

* Sun Dec 05 2021 Igor Vlasenko <viy@altlinux.ru> 0.17-alt2
- added BR: perl-experimental

* Tue Nov 23 2021 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- updated by package builder

* Sat Apr 13 2019 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- updated by package builder

* Thu Oct 26 2017 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- regenerated from template by package builder

* Mon May 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- regenerated from template by package builder

* Mon Mar 20 2017 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- regenerated from template by package builder

* Mon Nov 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- regenerated from template by package builder

* Mon Nov 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- regenerated from template by package builder

* Mon Sep 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- regenerated from template by package builder

* Fri Sep 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- regenerated from template by package builder

* Tue Sep 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- initial import by package builder

