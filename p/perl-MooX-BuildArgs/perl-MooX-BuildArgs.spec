%define module_name MooX-BuildArgs
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Class/Method/Modifiers.pm) perl(Data/MethodProxy.pm) perl(Module/Build/Tiny.pm) perl(Moo.pm) perl(Moo/Object.pm) perl(Moo/Role.pm) perl(Scalar/Util.pm) perl(Test2/V0.pm) perl(namespace/clean.pm) perl(strictures.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.08
Release: alt2
Summary: Save instantiation arguments for later use.
Group: Development/Perl
License: perl
URL: https://github.com/bluefeet/MooX-BuildArgs

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/B/BL/BLUEFEET/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
From summary: %summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.md Changes LICENSE
%perl_vendor_privlib/M*

%changelog
* Thu Apr 10 2025 Igor Vlasenko <viy@altlinux.org> 0.08-alt2
- to Sisyphus as MooX-Role-Parameterized dep

* Wed Apr 24 2019 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- updated by package builder

* Mon Mar 04 2019 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- updated by package builder

* Sun Feb 17 2019 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- updated by package builder

* Wed Nov 30 2016 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- regenerated from template by package builder

* Sat Apr 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1.1
- rebuild to restore role requires

* Fri Feb 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- regenerated from template by package builder

* Wed Nov 12 2014 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial import by package builder

