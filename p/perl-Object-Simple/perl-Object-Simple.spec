Epoch: 1
%define module_name Object-Simple
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(Scalar/Util.pm) perl(Test/More.pm) perl(base.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 3.19
Release: alt3
Summary: Provide new() and accessor creating abilities
Group: Development/Perl
License: perl
URL: http://github.com/yuki-kimoto/object-simple

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/K/KI/KIMOTO/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.md Changes
%perl_vendor_privlib/O*

%changelog
* Wed Jul 13 2022 Igor Vlasenko <viy@altlinux.org> 1:3.19-alt3
- to Sisyphus as perl-Sub-HandlesVia build dep

* Fri Jan 13 2017 Igor Vlasenko <viy@altlinux.ru> 1:3.19-alt2
- regenerated from template by package builder

* Sun Sep 18 2016 Igor Vlasenko <viy@altlinux.ru> 3.1801-alt1
- regenerated from template by package builder

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 3.16-alt1
- regenerated from template by package builder

* Thu Apr 07 2016 Igor Vlasenko <viy@altlinux.ru> 3.15-alt1
- regenerated from template by package builder

* Thu Apr 02 2015 Igor Vlasenko <viy@altlinux.ru> 3.14-alt1
- regenerated from template by package builder

* Mon Nov 17 2014 Igor Vlasenko <viy@altlinux.ru> 3.13-alt1
- regenerated from template by package builder

* Wed Feb 05 2014 Igor Vlasenko <viy@altlinux.ru> 3.10-alt1
- regenerated from template by package builder

* Mon Sep 16 2013 Igor Vlasenko <viy@altlinux.ru> 3.09-alt2
- regenerated from template by package builder

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 3.0501-alt1
- initial import by package builder

