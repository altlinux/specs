%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Encode.pm) perl(Encode/CN.pm) perl(Encode/JP.pm) perl(Encode/KR.pm) perl(Encode/TW.pm) perl(Exporter.pm) perl(List/Util.pm) perl(Module/Build.pm) perl(PPI/Document.pm) perl(PPI/Dumper.pm) perl(PPIx/Regexp.pm) perl(Pod/Usage.pm) perl(Scalar/Util.pm) perl(Test/More.pm) perl(Test/Without/Module.pm) perl(base.pm) perl(constant.pm) perl(strict.pm) perl(warnings.pm) perl(charnames.pm) perl(Readonly.pm)
# END SourceDeps(oneline)
%define module_name PPIx-QuoteLike
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.020
Release: alt1
Summary: Parse Perl string literals and string-literal-like things.
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/W/WY/WYANT/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
This Perl class parses Perl string literals and things that are
reasonably like string literals. Its real reason for being is to find
interpolated variables for Perl::Critic policies and
similar code.
%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSES/Artistic Changes README CONTRIBUTING
%perl_vendor_privlib/P*

%changelog
* Fri Mar 25 2022 Igor Vlasenko <viy@altlinux.org> 0.020-alt1
- automated CPAN update

* Wed Nov 17 2021 Igor Vlasenko <viy@altlinux.org> 0.019-alt1
- automated CPAN update

* Sun Oct 24 2021 Igor Vlasenko <viy@altlinux.org> 0.018-alt1
- automated CPAN update

* Wed Apr 21 2021 Igor Vlasenko <viy@altlinux.org> 0.017-alt1
- automated CPAN update

* Wed Mar 31 2021 Igor Vlasenko <viy@altlinux.org> 0.016-alt1
- automated CPAN update

* Wed Feb 10 2021 Igor Vlasenko <viy@altlinux.ru> 0.015-alt1
- automated CPAN update

* Fri Jan 15 2021 Igor Vlasenko <viy@altlinux.ru> 0.014-alt1
- automated CPAN update

* Sat Oct 24 2020 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1
- automated CPAN update

* Tue Sep 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.012-alt1
- automated CPAN update

* Tue Apr 14 2020 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1
- automated CPAN update

* Sat Mar 14 2020 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1
- automated CPAN update

* Tue Mar 03 2020 Igor Vlasenko <viy@altlinux.ru> 0.009-alt1
- automated CPAN update

* Thu Aug 22 2019 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1
- automated CPAN update

* Sat Jun 01 2019 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1
- automated CPAN update

* Thu Jul 12 2018 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1
- automated CPAN update

* Sun Jun 03 2018 Igor Vlasenko <viy@altlinux.ru> 0.005-alt2
- to Sisyphus as perl-Perl-Critic dep

* Sun Jul 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1
- initial import by package builder

