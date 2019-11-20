Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(MooseX/AttributeHelpers.pm) perl(MooseX/Role/Strict.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-MooseX-ClassAttribute
Summary:        Declare class attributes Moose-style
Version:        0.29
Release:        alt1_10
License:        Artistic 2.0
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/MooseX-ClassAttribute-%{version}.tar.gz
URL:            https://metacpan.org/release/MooseX-ClassAttribute
BuildArch:      noarch

BuildRequires:  rpm-build-perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Moose.pm)
BuildRequires:  perl(Moose/Exporter.pm)
BuildRequires:  perl(Moose/Meta/Role/Attribute.pm)
BuildRequires:  perl(Moose/Role.pm)
BuildRequires:  perl(Moose/Util.pm)
BuildRequires:  perl(Moose/Util/MetaRole.pm)
BuildRequires:  perl(MooseX/Role/Parameterized.pm)
BuildRequires:  perl(namespace/autoclean.pm)
BuildRequires:  perl(namespace/clean.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
BuildRequires:  perl(Test/Fatal.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Requires.pm)


Source44: import.info

%description
This module allows you to declare class attributes in exactly the same way as
object attributes, using class_has() instead of has().

You can use any feature of Moose's attribute declarations, including overriding
a parent's attributes, delegation (handles), and attribute metaclasses, and it
should just work. The one exception is the "required" flag, which is not
allowed for class attributes.

The accessor methods for class attribute may be called on the class directly,
or on objects of that class. Passing a class attribute to the constructor will
not set it.

%prep
%setup -q -n MooseX-ClassAttribute-%{version}

# silence rpmlint warnings
sed -i '1s,#!.*perl,#!%{__perl},' t/*.t

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build


%install
make pure_install DESTDIR=%{buildroot}
# %{_fixperms} %{buildroot}/*


%check
make test


%files
%doc Changes t/
%doc --no-dereference LICENSE
%{perl_vendor_privlib}/*


%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.29-alt1_10
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.29-alt1_6
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.29-alt1_4
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.29-alt1_3
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.29-alt1_2
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.29-alt1_1
- update to new release by fcimport

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.29-alt1
- automated CPAN update

* Sat Apr 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.27-alt2_7.1
- rebuild to restore role requires

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.27-alt2_7
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.27-alt2_6
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.27-alt2_4
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.27-alt2_3
- update to new release by fcimport

* Thu Mar 06 2014 Igor Vlasenko <viy@altlinux.ru> 0.27-alt2_2
- moved to Sisyphus as dependency

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1_2
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.26-alt2_7
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.26-alt2_6
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.26-alt2_4
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1_4
- fc import

