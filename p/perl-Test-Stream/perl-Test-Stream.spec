%define _unpackaged_files_terminate_build 1
%define module_version 1.302027
%define module_name Test-Stream
%filter_from_requires /^perl.Sub.Util.pm/d
# BEGIN SourceDeps(oneline):
BuildRequires: perl(B.pm) perl(Carp.pm) perl(Config.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(File/Temp.pm) perl(List/Util.pm) perl(PerlIO.pm) perl(Scalar/Util.pm) perl(Storable.pm) perl(Test/Harness.pm) perl(Unicode/GCString.pm) perl(base.pm) perl(overload.pm) perl(threads.pm) perl(threads/shared.pm) perl(utf8.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.302027
Release: alt1
Summary: Comming soon
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source: http://www.cpan.org/authors/id/E/EX/EXODIST/Test-Stream-%{version}.tar.gz
BuildArch: noarch

%description
From summary: %summary

%prep
%setup -n %{module_name}-%{module_version}
# TODO fix
rm -f t/modules/Table.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE README Changes
%perl_vendor_privlib/T*

%changelog
* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.302027-alt1
- automated CPAN update

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.302026-alt1
- automated CPAN update

* Mon Nov 02 2015 Igor Vlasenko <viy@altlinux.ru> 1.302021-alt1
- automated CPAN update

* Thu Oct 29 2015 Igor Vlasenko <viy@altlinux.ru> 1.302018-alt1
- automated CPAN update

* Sun Oct 18 2015 Igor Vlasenko <viy@altlinux.ru> 1.302017-alt1
- automated CPAN update

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 1.302016-alt1
- regenerated from template by package builder

* Mon Jan 05 2015 Igor Vlasenko <viy@altlinux.ru> 0.000003-alt1
- regenerated from template by package builder

* Thu Sep 04 2014 Igor Vlasenko <viy@altlinux.ru> 0.000002-alt1
- initial import by package builder

