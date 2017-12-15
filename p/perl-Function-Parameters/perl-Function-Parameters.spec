%define _unpackaged_files_terminate_build 1
%define module_name Function-Parameters
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Dir/Self.pm) perl(ExtUtils/MakeMaker.pm) perl(Moo.pm) perl(Moose.pm) perl(Moose/Util/TypeConstraints.pm) perl(MooseX/Types.pm) perl(MooseX/Types/Moose.pm) perl(Test/Deep.pm) perl(Test/Fatal.pm) perl(Test/More.pm) perl(XSLoader.pm) perl(aliased.pm) perl(attributes.pm) perl(constant.pm) perl(overload.pm) perl(strict.pm) perl(utf8.pm) perl(warnings.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 2.001003
Release: alt1.1
Summary: subroutine definitions with parameter lists
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/M/MA/MAUKE/%{module_name}-%{version}.tar.gz

%description
This module extends Perl with keywords that let you define functions with
parameter lists. It uses Perl's keyword plugin
API, so it works reliably and doesn't require a source filter.


%prep
%setup -q -n %{module_name}-%{version}
sed -i -e "s,^'ok'$,1;," lib/Function/Parameters.pm lib/Function/Parameters/*.pm

# TODO
rm t/unicode*.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/F*
%perl_vendor_autolib/*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.001003-alt1.1
- rebuild with new perl 5.26.1

* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 2.001003-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 2.001001-alt1
- automated CPAN update

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.000006-alt1
- automated CPAN update

* Mon Apr 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.000003-alt1
- automated CPAN update

* Sat Mar 25 2017 Igor Vlasenko <viy@altlinux.ru> 1.0706-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.0705-alt1.1
- rebuild with new perl 5.24.1

* Mon Jun 13 2016 Igor Vlasenko <viy@altlinux.ru> 1.0705-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.0704-alt1
- automated CPAN update

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 1.0703-alt1
- automated CPAN update

* Mon Dec 28 2015 Igor Vlasenko <viy@altlinux.ru> 1.0702-alt1
- automated CPAN update

* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.0701-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.0605-alt1.1
- rebuild with new perl 5.22.0

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 1.0605-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.0603-alt1.1
- rebuild with new perl 5.20.1

* Tue Nov 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.0603-alt1
- automated CPAN update

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.0602-alt1
- automated CPAN update

* Mon Oct 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.0503-alt1
- automated CPAN update

* Tue Sep 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.0402-alt1
- automated CPAN update

* Wed Dec 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.0401-alt2
- uploaded to Sisyphus as Scalar-Does dependency

* Thu Oct 10 2013 Igor Vlasenko <viy@altlinux.ru> 1.0401-alt1
- regenerated from template by package builder

* Thu Oct 03 2013 Igor Vlasenko <viy@altlinux.ru> 1.0301-alt1
- initial import by package builder

