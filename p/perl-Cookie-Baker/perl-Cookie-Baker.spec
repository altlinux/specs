%define _unpackaged_files_terminate_build 1
%define module_name Cookie-Baker
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Cookie/Baker/XS.pm) perl(Exporter.pm) perl(Module/Build.pm) perl(Test/More.pm) perl(Test/Time.pm) perl(URI/Escape.pm) perl(base.pm) perl(Module/Build/Tiny.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.09
Release: alt1
Summary: Cookie string generator / parser
Group: Development/Perl
License: perl
URL: https://github.com/kazeburo/Cookie-Baker

Source0: http://www.cpan.org/authors/id/K/KA/KAZEBURO/%{module_name}-%{version}.tar.gz
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
%doc Changes README.md LICENSE
%perl_vendor_privlib/C*

%changelog
* Wed Mar 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- automated CPAN update

* Sun Sep 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- automated CPAN update

* Thu Dec 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2
- moved to Sisyphus as dependency

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- regenerated from template by package builder

* Mon Mar 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- regenerated from template by package builder

* Tue Oct 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- regenerated from template by package builder

* Mon Oct 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial import by package builder

