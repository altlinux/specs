%define _unpackaged_files_terminate_build 1
Epoch: 1
%define module_name FindBin-libs
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Cwd.pm) perl(File/Spec.pm) perl(File/Spec/Functions.pm) perl(File/Temp.pm) perl(FindBin.pm) perl(List/Util.pm) perl(Module/Build.pm) perl(Symbol.pm) perl(Test/More.pm) perl(lib.pm) perl(strict.pm) perl(File/Copy/Recursive/Reduced.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 3.0.1
Release: alt1
Summary: FindBin::libs - locate and a 'use lib' or export 
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/L/LE/LEMBARK/%{module_name}-v%{version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -q -n %{module_name}-v%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README example CHANGES
%perl_vendor_privlib/F*

%changelog
* Fri Mar 25 2022 Igor Vlasenko <viy@altlinux.org> 1:3.0.1-alt1
- automated CPAN update

* Fri Dec 25 2020 Igor Vlasenko <viy@altlinux.ru> 1:2.200-alt1.1
- automated CPAN update

* Thu Feb 01 2018 Igor Vlasenko <viy@altlinux.ru> 2.1502-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 2.15-alt1
- automated CPAN update

* Mon Jan 19 2015 Igor Vlasenko <viy@altlinux.ru> 2.12-alt1
- automated CPAN update

* Tue Sep 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.11-alt1
- automated CPAN update

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 2.09-alt1
- automated CPAN update

* Mon May 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.9-alt1
- automated CPAN update

* Wed Oct 16 2013 Igor Vlasenko <viy@altlinux.ru> 1.8-alt2
- build for Sisyphus (required for perl update)

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1
- initial import by package builder

