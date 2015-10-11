%define _unpackaged_files_terminate_build 1
%define module_version 1.07
%define module_name Hash-MostUtils
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(FindBin.pm) perl(Scalar/Util.pm) perl(Test/More.pm) perl(base.pm) perl(overload.pm) perl(provide.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.07
Release: alt1
Summary: Pairwise list manipulators
Group: Development/Perl
License: perl
URL: https://github.com/belden/perl-hash-mostutils

Source: http://www.cpan.org/authors/id/B/BE/BELDEN/Hash-MostUtils-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -n %module_name-%module_version
# TODO: broken
rm t/leach.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.pod LICENSE
%perl_vendor_privlib/H*

%changelog
* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1
- automated CPAN update

* Sun Oct 06 2013 Igor Vlasenko <viy@altlinux.ru> 1.05-alt2
- Sisyphus build. required by Test-Easy update

* Mon Sep 23 2013 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1
- initial import by package builder

