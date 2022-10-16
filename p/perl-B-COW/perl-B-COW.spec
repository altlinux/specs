%define _unpackaged_files_terminate_build 1
%define module_name B-COW
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Devel/Peek.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.005
Release: alt1
Summary: B::COW additional B helpers to check COW status
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/A/AT/ATOOMIC/%{module_name}-%{version}.tar.gz

%description
B::COW provides some naive additional B helpers to check the COW status of one SvPV.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes examples
%perl_vendor_archlib/B*
%perl_vendor_autolib/*

%changelog
* Sun Oct 16 2022 Igor Vlasenko <viy@altlinux.org> 0.005-alt1
- automated CPAN update

* Mon Apr 27 2020 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1
- automated CPAN update

* Wed Apr 22 2020 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1
- automated CPAN update

* Mon Feb 24 2020 Igor Vlasenko <viy@altlinux.ru> 0.002-alt2
- to Sisyphus as perl-CDB_File dep

* Thu Feb 13 2020 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1
- updated by package builder

* Wed Jan 30 2019 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1
- initial import by package builder

