%define module_name String-Compare-ConstantTime
%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(XSLoader.pm) perl(base.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.312
Release: alt2.1
Summary: Timing side-channel protected string compare
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/F/FR/FRACTAL/%{module_name}-%{version}.tar.gz

%description
This module provides one function, `equals' (not exported by default).

You should pass this function two strings of the same length. Just like perl's `eq', it will return true if they are string-wise identical and false otherwise. However, comparing any two differing strings of the same length will take a fixed amount of time. If the lengths of the strings are different, `equals' will return false right away.
%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README COPYING Changes
%perl_vendor_archlib/S*
%perl_vendor_autolib/*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.312-alt2.1
- rebuild with new perl 5.26.1

* Sat Oct 28 2017 Igor Vlasenko <viy@altlinux.ru> 0.312-alt2
- updated summary

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

