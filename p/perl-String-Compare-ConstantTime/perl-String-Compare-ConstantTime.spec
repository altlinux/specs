%define _unpackaged_files_terminate_build 1
%define module_name String-Compare-ConstantTime
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.312
Release: alt1
Summary: unknown
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/F/FR/FRACTAL/%{module_name}-%{version}.tar.gz

%description
%summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc COPYING README Changes
%perl_vendor_archlib/S*
%perl_vendor_autolib/*

%changelog
* Fri Feb 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.312-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.311-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.311-alt1.1
- rebuild with new perl 5.22.0

* Mon Oct 26 2015 Igor Vlasenko <viy@altlinux.ru> 0.311-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.310-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.300-alt2.1
- rebuild with new perl 5.20.1

* Wed Oct 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.300-alt2
- build for Sisyphus (required for perl update)

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 0.300-alt1.1
- rebuild with new perl

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.300-alt1
- initial import by package builder

