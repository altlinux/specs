%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators perl(Test/Needs.pm)
# END SourceDeps(oneline)
Name:           perl-MooseX-StrictConstructor 
Version:        0.21
Release:        alt1
# see lib/MooseX/StrictConstructor.pm
License:        Artistic 2.0
Group:          Development/Perl
Summary:        Make your object constructors blow up on unknown attributes 
Source0:         http://www.cpan.org/authors/id/D/DR/DROLSKY/MooseX-StrictConstructor-%{version}.tar.gz
Url:            http://search.cpan.org/dist/MooseX-StrictConstructor
BuildArch:      noarch
BuildRequires:  perl(B.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Moose.pm)
BuildRequires:  perl(Moose/Exporter.pm)
BuildRequires:  perl(Moose/Role.pm)
BuildRequires:  perl(Moose/Util/MetaRole.pm)
BuildRequires:  perl(Test/Fatal.pm)
BuildRequires:  perl(Test/Moose.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(namespace/autoclean.pm)


Source44: import.info

%description
Simply loading this module makes your constructors "strict". If your
constructor is called with an attribute init argument that your class does
not declare, then it calls "Carp::confess()". This is a great way to catch
small typos.

%prep
%setup -q -n MooseX-StrictConstructor-%{version}

# avoid rpmlint wrong-script-interpreter warning
sed -i '1s~#!.*perl~#!%{__perl}~' t/*.t

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'

# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes t/ CONTRIBUTING.md README.md
%{perl_vendor_privlib}/*

%changelog
* Tue Feb 14 2017 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- automated CPAN update

* Sat Apr 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.19-alt3_5.1
- rebuild to restore role requires

* Sat Jan 04 2014 Igor Vlasenko <viy@altlinux.ru> 0.19-alt3_5
- Sisyphus build

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.19-alt2_5
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.19-alt2_4
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.19-alt2_3
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.19-alt2_1
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1_1
- fc import

